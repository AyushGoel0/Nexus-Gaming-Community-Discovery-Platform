# Nexus Roadmap

This roadmap translates the project directions PDF into dependency-ordered
work for the repository as it exists today. The PDF makes Nexus the flagship
project: Weeks 1–22 build the Django, API, infrastructure, and deployed
backend; later weeks add ML, RAG, React, infrastructure as code, and system
design. Each stage below has an exit condition so later technologies are not
started before the product needs them.

## Current checkpoint

The repository is entering the PDF's Week 4 relationships phase after
completing the foundation and authentication work:

- project, apps, migrations, and local server work;
- custom user model and profile fields exist;
- game and genre models exist;
- admin management works;
- the catalogue, health endpoint, and baseline tests work;
- registration, login/logout, profile editing, and account tests work.
- GitHub Actions runs `manage.py check` and the test suite on every push and
  pull request.

The screenshots confirm the earlier checkpoint in Django admin and in the
catalogue. The public home, account, profile, and catalogue pages now share a
project-level layout and stylesheet. Communities and discussions do not exist
yet.

## Next implementation slice

Complete the Django MVP in this order:

1. **Core relationships:** user preferences, user-to-game relationships,
   `Community`, membership, ownership, and moderation roles.
2. **MVP pages:** useful home/discovery page, game detail page, community
   detail page, and protected access rules.
3. **Discovery:** game search, genre filters, and server-rendered pagination.
4. **Discussions and engagement:** posts, comments, reviews, likes, and
   bookmarks, with tests for permissions and edge cases.
5. **MVP gate:** a user can register, manage a profile, discover a game, and
   participate in a community.

Do not add DRF until the MVP gate passes. Do not add Redis, Celery, Docker,
PostgreSQL, React, ML, or RAG merely because they appear later in the PDF.
The current GitHub Actions workflow is limited to system checks and tests;
Docker image builds and deployment automation remain deferred until the
production backend stage.

## Product stages

| Stage | Scope | Exit condition |
| --- | --- | --- |
| 1. Django MVP | Accounts, profiles, games, genres, communities, posts, comments, reviews, likes, bookmarks | A user can discover games and participate in a community |
| 2. Backend API | DRF serializers, authentication, permissions, search, filters, pagination, throttling | Core flows are available as tested JSON APIs |
| 3. Production backend | PostgreSQL, testing, Redis, Celery, Docker, Linux, CI/CD, AWS | Nexus is deployable with background jobs and documented operations |
| 4. ML integration | NumPy, Pandas, statistics, scikit-learn, matching/recommendation model, Django integration | Recommendations are evaluated and exposed through Nexus |
| 5. RAG platform | Embeddings, pgvector, ingestion, retrieval, Celery, React UI | A separate Django RAG knowledge platform works end to end |
| 6. Full-stack and infrastructure | React integration, Terraform, Kubernetes, system design | The portfolio can explain and deploy the complete architecture |

## 52-week alignment from the PDF

- **Weeks 1–5:** Django foundation and the Nexus MVP.
- **Weeks 6–8:** DRF serializers, authentication, permissions, filtering,
  search, pagination, and throttling.
- **Weeks 9–11:** PostgreSQL query skills and a strong automated test suite.
- **Weeks 12–18:** Redis, Celery, Docker, Linux, and GitHub Actions.
- **Weeks 19–22:** AWS deployment and production hardening.
- **Weeks 23–31:** NumPy, Pandas, statistics, scikit-learn, and ML-powered
  game matching/recommendations integrated with Nexus.
- **Weeks 32–34:** Deep-learning and transformer experiments.
- **Weeks 35–40:** A separate Django RAG knowledge platform using embeddings,
  pgvector, retrieval, Celery, and Redis.
- **Weeks 41–44:** React and full-stack integration.
- **Weeks 45–48:** Terraform and Kubernetes fundamentals.
- **Weeks 49–52:** System design, portfolio documentation, and interview
  preparation.

## Working rules

- Learn a technology when the current product needs it; do not start all
  courses simultaneously.
- Write tests while building each feature, not only at the end of a phase.
- Use Git from day one and keep commits small and explainable.
- Prefer official documentation as a reference for Django, DRF, PostgreSQL,
  Redis, Celery, Docker, AWS, and Terraform.
- Keep React lightweight because the primary specialization is Django/backend,
  cloud/DevOps, and AI/ML.
- Treat the local SQLite database as disposable development data until a
  repeatable fixture or seed command is added.
- Keep the public README aligned with verified behavior; do not report a
  roadmap feature as complete until its code and tests exist.

## Documentation backlog

The current repository needs only [README.md](./README.md) and this roadmap.
No new Markdown file should be implemented now. Add feature-specific
documentation only when the related implementation is real:

- `docs/API.md` or OpenAPI output during the DRF stage;
- `docs/ARCHITECTURE.md` after communities, APIs, and infrastructure stabilize;
- `CONTRIBUTING.md` when collaboration begins;
- `SECURITY.md` before production deployment;
- `CHANGELOG.md` when versioned releases begin.

Avoid describing unimplemented functionality as completed and avoid empty
placeholder Markdown files. The next documentation update should accompany the
first real feature slice, especially authentication and profile behavior.
