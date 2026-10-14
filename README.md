# MeetingProtocolSkill

Portable skill for generating meeting minutes from a transcript in **Confluence Storage Format XML/XHTML**.

The skill is designed for project meetings where the main source is a transcript. A previous protocol from the same project/stage may be supplied as context. Unsupported fields are left blank instead of being invented.

## Repository contents

- `portable-skills/meeting-protocol-storage/SKILL.md` — main skill instructions.
- `portable-skills/meeting-protocol-storage/USER_GUIDE.md` — how to use the skill in a web LLM / ChatGPT.
- `portable-skills/meeting-protocol-storage/templates/protocol-template.xml` — embedded canonical Confluence Storage Format template.
- `portable-skills/meeting-protocol-storage/references/` — extraction, source-priority, status and XML rules.
- `portable-skills/meeting-protocol-storage/examples/` — example transcript and generated protocol.
- `portable-skills/meeting-protocol-storage/scripts/validate_storage.py` — local XML-fragment validator.
- `tests/test_storage.py` — minimal regression check for the bundled template and example.

## Quick use

Give the model:

1. the meeting transcript;
2. optionally the previous protocol **from the same project/stage**;
3. optionally project/context files that clarify stable facts such as client name, team and stage;
4. a link to this repository and the instruction to use `portable-skills/meeting-protocol-storage/SKILL.md`.

Expected primary output:

`Протокол_<YYYY-MM-DD>_Confluence_Storage_Format.xml`

The output is a Confluence Storage Format **fragment**, intended for insertion into the Confluence source editor. DOCX is not required.

## Local validation

```bash
python portable-skills/meeting-protocol-storage/scripts/validate_storage.py \
  portable-skills/meeting-protocol-storage/examples/output/Протокол_2026-10-05_Confluence_Storage_Format.xml
```

Run tests:

```bash
python -m unittest discover -s tests -v
```

## Version

Initial release: `0.1.0`.
