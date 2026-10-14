# User guide — meeting-protocol-storage

## What the skill does

The skill converts a meeting transcript into a structured protocol in **Confluence Storage Format XML/XHTML** using a built-in template.

It is intentionally conservative: when the source does not establish a client attribute, participant role, deadline or responsible person, the corresponding field remains empty.

## Recommended input

Minimum:

- transcript of the meeting.

Better:

- transcript;
- previous protocol from the same project/stage;
- project context files if the transcript uses names/abbreviations without explanation.

A previous protocol from another project can still be supplied as a visual example, but the skill must not reuse its facts.

## Ready-to-use prompt

```text
Используй актуальный skill meeting-protocol-storage из репозитория:
<ССЫЛКА_НА_РЕПОЗИТОРИЙ>

Сформируй протокол по приложенной транскрипции встречи.

Если приложен предыдущий протокол, используй его факты только если он относится к тому же проекту/этапу. Иначе используй его только как пример оформления.

Не додумывай неизвестные данные. Если поле нельзя достоверно заполнить — оставь его пустым.

На выходе верни файл Confluence Storage Format XML, готовый для вставки через Source Editor. DOCX не нужен.
```

## Typical usage with a previous protocol

Attach:

1. `previous_protocol.xml` or an exported protocol;
2. `meeting_transcript.md`;
3. optional project files.

Then use the prompt above.

## Output

The primary file should be named similar to:

```text
Протокол_2026-10-05_Confluence_Storage_Format.xml
```

Paste its contents into the Confluence source editor / Storage Format editing surface available in your Confluence setup.

## Publishing this repository to GitHub

### Option A — GitHub web + command line

1. Create an empty repository, for example `MeetingProtocolSkill`.
2. Unpack this archive locally.
3. Open a terminal in the unpacked `MeetingProtocolSkill` directory.
4. Run:

```bash
git init
git add .
git commit -m "Initial release meeting protocol skill v0.1.0"
git branch -M main
git remote add origin https://github.com/<USER>/MeetingProtocolSkill.git
git push -u origin main
```

### Option B — existing local clone

Copy the repository contents into the clone, then:

```bash
git add .
git commit -m "Add meeting-protocol-storage skill v0.1.0"
git push
```

## Updating later

When the skill changes:

1. edit `SKILL.md` and related references/template;
2. increment the version in `release.json`;
3. run the XML validator/tests;
4. commit with a meaningful message;
5. push to GitHub.

Example:

```bash
python portable-skills/meeting-protocol-storage/scripts/validate_storage.py \
  portable-skills/meeting-protocol-storage/templates/protocol-template.xml
python -m unittest discover -s tests -v
git add .
git commit -m "Refine protocol extraction rules v0.1.1"
git push
```

## Important limitation

A repository link does not by itself guarantee that every LLM product automatically imports `SKILL.md`. The model must have access to the repository (web/GitHub connector) or the skill files must be attached/imported into the environment. The prompt should explicitly tell the model which `SKILL.md` to use.
