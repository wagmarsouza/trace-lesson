# Host contract and portability

The skill coordinates ordinary file operations. A compatible host needs:

- skill discovery or a way to include `SKILL.md` as instructions;
- read access to project instructions and the selected memory directory;
- write access only when the current task authorizes persistence;
- a way to inspect diffs or verify files after writing.

## Three layers

1. **Facts:** durable observations and preferences with scope, evidence, and revalidation conditions.
2. **Procedures:** reusable methods kept in the specialized skill that owns the task.
3. **Raw history:** searchable detail used when exact prior context is necessary.

The catalog or index should stay cheap to inspect. Load full entries only when they are relevant.

## Truth hierarchy

Apply information in this order:

1. current user instruction and authorization;
2. current project instructions;
3. verified live state;
4. relevant stored lesson;
5. unverified candidate or old history.

Stored memory never overrides a higher layer.

## No universal automatic activation

Different hosts discover and inject skills differently. A repository cannot force a host to load its instructions. Persistent loading must be configured in the host, and even then it does not create asynchronous work after a conversation ends.

