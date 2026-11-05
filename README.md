# Nexus Gaming Community & Discovery Platform

Nexus is the flagship project in the accompanying 52-week learning roadmap. It
is being built as one continuous product: a Django gaming catalogue that will
grow into a community platform where users maintain profiles, discover games,
join communities, discuss games, publish reviews, follow users, and eventually
receive personalised recommendations.

The PDF roadmap places the ML recommendation system and the separate Django RAG
platform later in the learning sequence. They should extend a stable Nexus
foundation rather than replace it.

## Current status

**Django MVP in progress (Weeks 1–3)**

- The Django project, local SQLite database, migrations, and development server
  work.
- `core` and `accounts` apps are registered.
- A custom `accounts.User` model includes `display_name` and `bio`.
- `Game` and `Genre` models are implemented.
- Games and genres are manageable through Django admin.
- The game catalogue is available at `/games/`.
- A styled home page endpoint is available at `/`.
- A health endpoint returns `{"status": "ok"}` at `/health/`.
- Automated model, view, and account tests currently pass (`17` tests).
- GitHub Actions runs the Django system check and test suite on every push and
  pull request.
- The local development database currently contains the sample data shown in
  the project screenshots: one user, four games, and seven genres. This data is
  local state, not a seed-data mechanism.

**Not implemented yet**

- User preferences, avatars, and user-to-game relationships
- `Community`, membership, ownership, and moderation relationships
- Posts, comments, reviews, likes, bookmarks, follows, and notifications
- Game detail pages and a real home/discovery experience
- Search, filtering, pagination, and a REST API
- PostgreSQL, Redis, Celery, Docker, full CI/CD, and deployment
- React frontend
- Recommendation/ML and RAG functionality

The screenshots show the earlier foundation state in Django admin and the
catalogue. The public home, account, profile, and catalogue pages now share a
responsive project-level layout and stylesheet. Registration, login/logout,
and the authenticated profile page are implemented under `/accounts/`. The
PDF's next data-model gap is `Community` and `Post`.

## What should happen next

The next milestone is the **Nexus Django MVP**, not DRF or React:

1. Add `Community`, membership, ownership, and moderation models with admin
   support and migrations.
2. Add game detail pages, community pages, posts, comments, and access rules.
3. Add game search, genre filters, and server-rendered pagination.
4. Add likes/bookmarks and permission and edge-case tests.
5. Mark the Django MVP complete only when a user can register, manage a
   profile, discover a game, and participate in a community.
6. Start the PDF's Week 6 DRF phase only after that MVP gate passes.

Do not start React, Redis, ML, RAG, Docker, or production infrastructure yet.
The lightweight test workflow is intentionally in place early; the PDF's full
Docker/image/deployment pipeline belongs after the Django MVP, API, testing,
and infrastructure foundations.

The dependency-ordered plan is in [ROADMAP.md](./ROADMAP.md).

## Local setup

This repository currently uses Python `3.15.0` in `.venv`, Django `6.1.2`,
SQLite, and the dependencies listed in [requirements.txt](./requirements.txt).
The PDF roadmap is a planning input; it is not an implemented feature list.

```powershell
.\.venv\Scripts\Activate.ps1
python manage.py migrate
python manage.py check
python manage.py test
python manage.py runserver
```

Open:

- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/games/`
- `http://127.0.0.1:8000/health/`
- `http://127.0.0.1:8000/admin/`

Create an administrator for the admin site with:

```powershell
python manage.py createsuperuser
```

## Project layout

```text
config/       Django project settings and URL configuration
accounts/     Custom user model, admin integration, and migrations
core/         Game and genre models, views, tests, and templates
db.sqlite3    Local development database; do not treat it as seed data
manage.py     Django command-line entry point
```

## Documentation policy

Keep this README focused on setup, current behavior, and the product overview.
Use [ROADMAP.md](./ROADMAP.md) for staged implementation work. No additional
Markdown file is needed at the current foundation stage. Add a document only
when its corresponding surface exists:

| Document | When to add it |
| --- | --- |
| `CONTRIBUTING.md` | When external contributors or pull requests are expected |
| `docs/API.md` or generated OpenAPI docs | When DRF endpoints are implemented |
| `docs/ARCHITECTURE.md` | After communities, APIs, and infrastructure stabilize |
| `SECURITY.md` | Before production deployment or when a security policy is adopted |
| `CHANGELOG.md` | When versioned releases begin |

Do not add empty placeholder Markdown files for future features. Screenshots
are useful progress evidence, but they do not require a separate Markdown
document.
