# OpenCode setup

TraceLesson supports two separate modes in OpenCode:

1. **Discoverable skill:** OpenCode can load `self-improvement` when the request matches or the user asks for it.
2. **Persistent instruction:** OpenCode includes the skill instructions in each session covered by the configuration.

Persistent instruction does not create a daemon, schedule, hook, or automatic file write.

## 1. Install the skill

```powershell
npx skills add wagmarsouza/trace-lesson@self-improvement -g -y
```

Confirm the actual installed `SKILL.md` path. Install locations vary by agent and Skills CLI version.

## 2. Add persistent instructions

Open `~/.config/opencode/opencode.json`. Preserve all existing fields and instruction entries. Add the installed `SKILL.md` path to the `instructions` array:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "instructions": [
    "C:/absolute/path/to/self-improvement/SKILL.md"
  ]
}
```

On Windows, forward slashes avoid JSON backslash escaping. Do not copy the example path literally.

Reload OpenCode:

```powershell
opencode reload
```

This mode keeps the coordinator instructions available. It still writes only when an active agent decides a verified, reusable lesson exists and file access is authorized.

## Optional project bridge

For projects whose host reads `AGENTS.md`, append this block once without replacing existing instructions:

```markdown
<!-- self-improvement:start -->
## Operational learning
Before substantive work, consult `.opencode/memory/self-improvement/INDEX.md` when it exists and load `self-improvement` when a relevant lesson may apply. After difficult investigations, verified corrections, or explicit memory requests, persist only useful, evidence-backed lessons. Reconfirm volatile facts. Routine work with no new lesson requires no memory entry.
<!-- self-improvement:end -->
```

The bridge improves predictability but does not guarantee a post-task event.

## Explicit use

Use natural language rather than assuming a slash command:

```text
Use the self-improvement skill for this task. Retrieve relevant lessons first, then record only verified new learning.
```

## Disable without deleting memory

1. Remove only the TraceLesson `SKILL.md` path from `instructions`.
2. Remove only the delimited bridge from `AGENTS.md`, if present.
3. Run `opencode reload`.

To uninstall discovery, remove the installed skill using the package manager that installed it. Keep `.opencode/memory/self-improvement/` unless the user explicitly asks to delete those records.

