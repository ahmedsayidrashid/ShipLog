import json
import uuid
from pathlib import Path

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

DATA_DIR = Path(__file__).parent / "data"
IDEAS_FILE = DATA_DIR / "ideas.json"

CHECKED_PREFIX = "[x] "


def load_ideas():
    if not IDEAS_FILE.exists():
        return []
    with IDEAS_FILE.open(encoding="utf-8") as f:
        return json.load(f)


def save_ideas(ideas):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with IDEAS_FILE.open("w", encoding="utf-8") as f:
        json.dump(ideas, f, indent=2)


def new_idea(text):
    return {"id": uuid.uuid4().hex[:8], "text": text.strip(), "checked": False}


def format_for_textarea(ideas):
    lines = []
    for idea in ideas:
        line = idea["text"]
        if idea.get("checked"):
            line = CHECKED_PREFIX + line
        lines.append(line)
    return "\n".join(lines)


def parse_line(line):
    line = line.strip()
    if not line:
        return None
    checked = False
    if line.startswith(CHECKED_PREFIX):
        checked = True
        line = line[len(CHECKED_PREFIX) :].strip()
    elif line.startswith("[ ] "):
        line = line[4:].strip()
    return {"text": line, "checked": checked}


def parse_textarea(text, existing):
    parsed = []
    for line in text.splitlines():
        item = parse_line(line)
        if item:
            parsed.append(item)

    ideas = []
    for i, item in enumerate(parsed):
        if i < len(existing):
            idea = existing[i].copy()
            idea["text"] = item["text"]
            idea["checked"] = item["checked"]
        else:
            idea = new_idea(item["text"])
            idea["checked"] = item["checked"]
        ideas.append(idea)
    return ideas


def toggle_checked(ideas, idea_id):
    for idea in ideas:
        if idea["id"] == idea_id:
            idea["checked"] = not idea.get("checked", False)
            break
    return ideas


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        action = request.form.get("action")
        ideas = load_ideas()

        if action == "save":
            ideas = parse_textarea(
                request.form.get("ideas_text", ""), load_ideas()
            )
        elif action == "add":
            text = request.form.get("new_idea", "").strip()
            if text:
                ideas.append(new_idea(text))
        elif action == "remove":
            idea_id = request.form.get("idea_id")
            ideas = [i for i in ideas if i["id"] != idea_id]
        elif action == "toggle":
            idea_id = request.form.get("idea_id")
            ideas = toggle_checked(ideas, idea_id)

        save_ideas(ideas)
        return redirect(url_for("index"))

    ideas = load_ideas()
    return render_template(
        "index.html",
        ideas=ideas,
        textarea_text=format_for_textarea(ideas),
    )


if __name__ == "__main__":
    app.run(debug=True)
