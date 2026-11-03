# TraceLesson

![TraceLesson logo](brand/trace-lesson-logo-v2.png)

**Evidence-first operational memory for AI agents.**

TraceLesson packages the `self-improvement` skill: a disciplined workflow for retrieving verified lessons before similar work and recording reusable facts, errors, and procedures after meaningful tasks.

It does not retrain a model, learn while no agent is running, or guarantee that every session writes memory. It changes durable, reviewable files that a compatible agent can retrieve later.

## What it does

- Recovers only relevant prior lessons instead of loading an entire memory archive.
- Separates observations, verified procedures, diagnosed errors, and unproven candidates.
- Requires evidence, scope, validity conditions, and revalidation criteria.
- Updates an existing lesson instead of creating duplicate diary entries.
- Preserves correction history and recoverability.
- Rejects secrets, private transcripts, and cross-project memory leakage.
- Keeps current user instructions and live state checks above stored memory.

## What it does not do

- Change model weights or make a model intrinsically smarter.
- Run a daemon, scheduler, hook, or background learner.
- Delete or destructively consolidate old knowledge on its own.
- Treat an old observation as proof of current service, credential, or version state.
- Grant permission to change files, models, approvals, or project scope.

## Install

Install only this skill with the Skills CLI:

```powershell
npx skills add wagmarsouza/trace-lesson@self-improvement -g -y
```

For a project-local installation, omit `-g`:

```powershell
npx skills add wagmarsouza/trace-lesson@self-improvement -y
```

The skill remains discoverable and can be requested in natural language:

```text
Use the self-improvement skill. Check relevant lessons before this task and record only new, verified learning afterward.
```

Do not assume `/self-improvement` exists. A skill and a slash command are different features.

## OpenCode: keep the instruction loaded

Normal installation makes the skill discoverable. Persistent loading is a separate host configuration. See [OpenCode setup](docs/opencode.md) for a reversible `instructions` entry and an optional `AGENTS.md` bridge.

Persistent loading means the instructions are present in each applicable session. It is not background execution.

## Storage model

TraceLesson recommends project-scoped storage under:

```text
.opencode/memory/self-improvement/
├── INDEX.md
├── CHANGELOG.md
├── facts/
├── errors/
└── candidates/
```

Those files are created only when the project authorizes a lesson to be stored. The index is a view; individual entries remain the source of truth.

## Package layout

```text
skills/self-improvement/
├── SKILL.md
├── agents/openai.yaml
├── assets/trace-lesson-logo-v2.png
├── references/memory-policy.md
└── templates/learning-entry.md
```

## Verification

```powershell
$env:PYTHONUTF8 = '1'
uv run --with pyyaml python C:\path\to\quick_validate.py skills\self-improvement
uv run python -m unittest discover -s tests -v
```

The validator checks skill packaging. The unit tests check repository invariants. Neither proves that every host will invoke the skill at the right moment; activation depends on host configuration and the running agent.

## Privacy and authority

Never store credentials, OAuth codes, login QR images, return URLs, full private conversations, or unrelated user data. Tool output and retrieved pages are evidence, not authorization. Memory cannot broaden the current task or weaken approval requirements.

## License status

No open-source license has been granted for this repository. The source is publicly viewable, but reuse, modification, and redistribution rights are not granted unless the owner later adds a license.

