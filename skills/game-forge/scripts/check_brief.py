#!/usr/bin/env python3
"""Checks a game brief (assets/GAME_BRIEF.md format) for gaps.

    python3 check_brief.py docs/GAME_BRIEF.md [--json]

Each question is a `### N.N Title` heading, tagged `required` or not, followed
by an optional `>` hint and the answer. An answer counts as missing if it is
empty or still contains `_TODO_`. `DECIDE` means the developer chooses (and
records the choice in docs/PLAN.md); `N/A` means it doesn't apply. Answers
still carrying `(inferred)` were pre-filled by the developer and await the
user's confirmation.

Exit status: 0 when every required question is answered by the user (not
just inferred), 1 otherwise, so it can gate the move from Initiate to Plan.
"""
import json
import re
import sys

HEADING = re.compile(r"^###\s+(\d+(?:\.\d+)*)\s+(.*?)\s*$")


def parse(text):
    questions, cur, section = [], None, ""
    for line in text.splitlines():
        if line.startswith("## "):
            section = line[3:].strip()
            continue
        m = HEADING.match(line)
        if m:
            title = m.group(2)
            required = "`required`" in title
            title = title.replace("`required`", "").strip()
            cur = {"id": m.group(1), "title": title, "section": section, "required": required, "lines": []}
            questions.append(cur)
            continue
        if cur is not None and not line.startswith(">") and line.strip() != "---":
            cur["lines"].append(line)
    for q in questions:
        answer = "\n".join(q.pop("lines")).strip()
        q["answer"] = answer
        upper = answer.upper()
        if not answer or "_TODO_" in answer:
            q["state"] = "missing"
        elif re.fullmatch(r"\W*DECIDE\W*", upper) or upper.startswith("DECIDE"):
            q["state"] = "decide"
        elif re.fullmatch(r"\W*N/?A\W*", upper):
            q["state"] = "n/a"
        elif re.search(r"\(inferred\b", answer, re.I):
            q["state"] = "inferred"
        else:
            q["state"] = "answered"
    return questions


def report(questions):
    req = [q for q in questions if q["required"]]
    missing_req = [q for q in req if q["state"] == "missing"]
    missing_opt = [q for q in questions if not q["required"] and q["state"] == "missing"]
    decide = [q for q in questions if q["state"] == "decide"]
    inferred = [q for q in questions if q["state"] == "inferred"]
    done = sum(1 for q in questions if q["state"] != "missing")
    lines = [f"Brief: {done}/{len(questions)} questions answered; "
             f"{len(req) - len(missing_req)}/{len(req)} required."]

    def block(title, items, note=""):
        if items:
            lines.append("")
            lines.append(f"{title} ({len(items)}){note}:")
            for q in items:
                lines.append(f"  {q['id']:>5}  {q['title']}  [{q['section']}]")

    unconfirmed = [q for q in inferred if q["required"]]
    block("MISSING REQUIRED", missing_req, " - ask about these before planning")
    block("Inferred, awaiting confirmation", inferred)
    block("Delegated (DECIDE): choose and log in docs/PLAN.md", decide)
    block("Unanswered optional", missing_opt, " - fill from defaults or ask if they'd change the plan")
    lines.append("")
    if missing_req:
        lines.append("NOT READY: required answers missing")
    elif unconfirmed:
        lines.append("NOT READY: %d required answers are still only inferred; ask the user to confirm them" % len(unconfirmed))
    else:
        lines.append("READY TO PLAN")
    return "\n".join(lines), not missing_req and not unconfirmed


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        sys.exit(2)
    with open(args[0], encoding="utf-8") as f:
        questions = parse(f.read())
    if not questions:
        print("No questions found: is this a GAME_BRIEF.md (### N.N headings)?")
        sys.exit(2)
    text, ready = report(questions)
    if "--json" in sys.argv:
        print(json.dumps({"ready": ready, "questions": questions}, indent=2))
    else:
        print(text)
    sys.exit(0 if ready else 1)


if __name__ == "__main__":
    main()
