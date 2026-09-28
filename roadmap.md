# Hexagonal Task Tracker: Master Roadmap

A learning-driven project that grows a single, well-tested domain core through progressively more complex adapters: CLI, database, web API, background workers, and AI. Every stage plugs into the same ports, which is the point of the hexagonal design.

It is also an app I use day to day. Real friction from using it decides which feature comes next, and every new tool has to solve a problem the app actually has.

---

## Engineering Standards

These are requirements, not phases, but they are adopted in steps so setup never outpaces feature work.

| Standard | When | Notes |
|---|---|---|
| **Testing** | Now | pytest for all domain logic; adapters get integration tests. No stage is done without tests. |
| **Version control** | Now | Small commits at each working checkpoint, feature branches, merge to `main` when a piece is done. `.gitignore` covers `__pycache__/`, `.pytest_cache/`, `.venv/`. |
| **CI** | Now | GitHub Actions runs pytest and Ruff on every push. |
| **Type checking** | During Stage 1 | Add type hints as code is touched, then turn on mypy in CI once the domain is fully annotated. |
| **Decision records** | During Stage 1 | Move significant decisions from `doc.txt` into short ADRs in `/docs/adr` (for example, `time` vs. timezone-aware `datetime`, separate serialization module). |
| **Pull requests** | From Stage 3 | Solo PRs for larger features, mainly to practice writing PR descriptions. |
| **README** | End of Stage 1 | Setup, architecture, and links to ADRs. Updated every stage. |

---

## Track A: Application & Architecture Evolution

### Stage 1: The Domain Engine (Current)
* **Focus:** Domain modeling, hexagonal architecture, Python fundamentals.
* **Tech Stack:** Python, CLI adapter, JSON file adapter.
* **Goal:** A headless CLI application where all business rules live in the domain core and the CLI and storage interact only through ports.
* **Validation approach:** The domain validates itself with plain Python (property setters). Pydantic is not used in the domain; it enters in Stage 3 at the API boundary for parsing requests.
* **Definition of Done:**
  * [x] `Status` enum with validation on name, status, and due date
  * [x] `to_dict` / `from_dict` (classmethod) with parsing in a separate serialization module
  * [x] Tests for domain rules and serialization round trips
  * [ ] Tasks have unique IDs
  * [ ] Due dates are timezone-aware `datetime` values, serialized as ISO 8601
  * [ ] A `TaskRepository` port with a JSON adapter; the CLI never touches files directly
  * [ ] `from_dict` raises one consistent error type for invalid data
  * [ ] Tests updated and passing for all of the above

### Stage 2: The Persistence Layer
* **Focus:** Relational data modeling and swapping adapters.
* **Tech Stack:** SQLite, then PostgreSQL, SQLAlchemy, Alembic (migrations).
* **Goal:** Replace the JSON adapter with a database adapter without changing a single line of domain code.
* **Definition of Done:**
  * The same repository test suite (contract tests) passes against both the JSON and database adapters.
  * Schema changes are managed through migrations, never by hand.

### Stage 3a: The API Bridge
* **Focus:** RESTful API design and request validation.
* **Tech Stack:** FastAPI, Pydantic (request/response models).
* **Goal:** Expose the domain through web endpoints for a single user, secure enough to deploy.
* **Definition of Done:**
  * CRUD endpoints with correct status codes and pagination.
  * Domain errors map to 4xx responses, never 500s.
  * Pydantic handles parsing at the boundary; domain rules are not duplicated in Pydantic models.
  * All endpoints protected by a single API key read from an environment variable.
  * Auto-generated OpenAPI docs and API integration tests.
* **Milestone:** Deploy to Track B Phase 1 immediately after this stage.

### Stage 3b: Users and Authentication
* **Focus:** Authentication and multi-user data.
* **Tech Stack:** JWT or OAuth2.
* **Goal:** Replace the single API key with real user accounts.
* **Definition of Done:**
  * Users can register and log in.
  * Users can only read and change their own tasks, with tests proving it.

### Stage 4: Event-Driven Background Work
* **Focus:** Asynchronous processing and keeping the web layer responsive ("The Waiter & The Chef" pattern).
* **Tech Stack:** Redis (message broker), Celery (workers and scheduled jobs).
* **Goal:** Offload slow or scheduled work so API requests never block on it.
* **Concrete Use Cases:**
  * Due-date reminder emails.
  * Recurring tasks (for example, "every Monday"). The recurrence rule is modeled in the domain; scheduled jobs create the next occurrence.
  * Daily or weekly task digests.
  * Later: LLM calls from Stage 5.
* **Definition of Done:**
  * Reminders are sent by workers and retried on failure.
  * Retries never send duplicates, using idempotency keys or a record of what was already sent. Expect this to be the hardest part of the stage.

### Stage 5: The AI & RAG Pipeline
* **Focus:** Embeddings, vector search, and LLM integration.
* **Tech Stack:** PostgreSQL with `pgvector`, OpenAI/Claude API, Redis (semantic caching).
* **Goal:** Turn task data into a conversational knowledge base that can generate task workflows from natural language notes.
* **Definition of Done:**
  * Semantic search across a user's tasks and notes.
  * "Paste notes, get tasks" feature that proposes tasks the user confirms before saving.
  * LLM calls run through Celery workers, and responses are cached.

---

## Track B: Cloud Infrastructure

### Phase 1: The PaaS Control Group
* **Focus:** Containerization and managed deployment.
* **Tech Stack:** Docker, Docker Compose, Render (or Railway), managed PostgreSQL (Supabase/Neon).
* **Goal:** Get the containerized app live on the public internet without managing servers, isolating deployment mechanics as the only new variable.
* **Definition of Done:**
  * A public URL for the API.
  * CI automatically deploys the main branch after tests pass.
  * Secrets managed through environment variables, never committed.

### Phase 2: The "Hard Way" (IaaS)
* **Focus:** Linux administration, reverse proxies, and networking.
* **Tech Stack:** AWS EC2, Ubuntu, Nginx, Let's Encrypt (Certbot) for SSL.
* **Goal:** Learn what PaaS providers automate by hosting the same containers on a raw server, securely.
* **Definition of Done:**
  * HTTPS via Nginx, firewall locked down to required ports, SSH key-only access.
  * Basic logging and uptime monitoring in place.

### Phase 3: Infrastructure as Code (Optional)
* **Focus:** Automated, reproducible infrastructure.
* **Tech Stack:** Terraform, AWS.
* **Goal:** Provision the Phase 2 environment (VPC, subnets, compute, database) entirely from code.
* **Note:** *Not required for shipping the app, but valuable for DevOps/SRE roles.*

---

## Recommended Order

The tracks run in parallel, not one after the other:

1. Stage 1: Domain Engine
2. Stage 2: Persistence Layer
3. Stage 3a: API Bridge
4. **Phase 1: PaaS deployment** (first live version)
5. Stage 3b: Users and Authentication
6. Stage 4: Background Work
7. Phase 2: IaaS migration
8. Stage 5: AI & RAG Pipeline
9. Phase 3: Terraform (optional)

Each step should leave the project in a working, deployable, tested state. A finished earlier stage is worth more than an unfinished later one.

If a stage's tool doesn't solve a problem I've actually run into yet, push the stage back instead of forcing it in.
