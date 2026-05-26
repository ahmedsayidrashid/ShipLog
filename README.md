# ShipLog

A privacy-first, local-storage personal branding and content execution dashboard built for developers and creators.

ShipLog helps you capture content ideas, track posting metrics, and improve your output over time—without handing your data to a third-party platform. Everything stays on your machine. The long-term vision connects a FastAPI backend and local database to an LLM for tailored feedback, niche trend discovery, and a gamified leaderboard for consistency with friends.

## Core features

### Local Data Ownership

Your content ideas, performance metrics, and preferences live in a local database (PostgreSQL or SQLite)—not on someone else's servers. You own the data, can export it, and can run ShipLog entirely offline for core workflows. No account or cloud sync required for the essentials.

### AI-Driven Iteration

ShipLog will connect to an LLM API to analyze your past video performance and stated content preferences, then suggest what to double down on, what to retire, and how to refine your next posts. Feedback is grounded in *your* history, not generic creator advice.

### Trend Scraping

A niche-specific trend aggregator will surface high-performing topics and formats in your space, so you can spot opportunities early and align ideas with what's working—without manually scrolling every platform.

### Gamified Consistency

A social leaderboard lets you and friends track posting streaks, hit consistency goals, and compete in a lightweight, motivating way—turning discipline into something you actually want to open each day.

## Tech stack

| Layer | Target | Current MVP |
|-------|--------|-------------|
| API | FastAPI | Flask |
| Storage | PostgreSQL / SQLite | `data/ideas.json` |
| AI | LLM API (performance-aware feedback) | — |
| Trends | Niche trend aggregator | — |
| Social | Gamified leaderboard | — |
| Frontend | API clients / dashboard (TBD) | Jinja + HTML |

**Target architecture:** FastAPI backend, local PostgreSQL or SQLite, LLM integration, trend-scraping service, leaderboard module.

**Current MVP:** Flask app with a single route, one Jinja template, and JSON file persistence for content ideas.

## Current MVP

What works today:

- **Content ideas** — add, edit, check off, and remove ideas from a simple web UI
- **Local JSON storage** — ideas saved to `data/ideas.json` on your machine (gitignored)
- **Single-page UI** — large textarea for bulk editing plus quick actions per idea

Relevant files:

- [`app.py`](app.py) — Flask routes and persistence helpers
- [`templates/index.html`](templates/index.html) — UI template

Not yet implemented: database layer, FastAPI, LLM feedback, trend scraping, leaderboard.

## Setup

Prerequisites: Python 3.10+

```bash
git clone <your-repo-url>
cd ShipLog

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -r requirements.txt
flask --app app run --debug
```

Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

On first save, ShipLog creates `data/ideas.json` locally. That file is not committed to git.

### Using the MVP

- **Add** — enter text in “New content idea” and click **Add**
- **Modify** — edit lines in the textarea, then **Save changes**
- **Check** — prefix a line with `[x] ` and save, or use **Check** / **Uncheck** in quick actions
- **Remove** — delete a line and save, or click **Remove** on an idea

## Roadmap

- Migrate storage from JSON to SQLite / PostgreSQL
- Replace Flask with FastAPI and a proper API surface
- LLM integration for performance-aware content feedback
- Niche-specific trend aggregator
- Gamified social leaderboard for consistency tracking
