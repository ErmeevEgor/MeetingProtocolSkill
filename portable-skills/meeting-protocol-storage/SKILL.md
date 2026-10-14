---
name: meeting-protocol-storage
description: Build a structured meeting protocol from a transcript and optional project context, using a bundled Confluence Storage Format XML template. Never invent unsupported facts; leave uncertain fields blank. A previous protocol may provide facts only when it is demonstrably from the same project/stage.
---

# Meeting Protocol — Transcript → Confluence Storage Format

Create a client-ready meeting protocol from the supplied transcript. The canonical output is a **Confluence Storage Format XML/XHTML fragment**, not DOCX.

## Canonical scenario

### Required input

- meeting transcript (`.md`, `.txt`, pasted text, or another readable text source).

### Optional input

- previous protocol from the same project/stage;
- project/context files that establish stable facts such as client name, project name, stage, participant roles or already-agreed terminology;
- a user correction or explicit instruction.

The bundled template in `templates/protocol-template.xml` is always available and is the default structural template.

### Primary output

Return:

`Протокол_<YYYY-MM-DD>_Confluence_Storage_Format.xml`

Do not create DOCX unless the user separately requests it.

## Required references

Before drafting, use:

- `references/source-priority.md`;
- `references/fact-extraction-rules.md`;
- `references/protocol-structure.md`;
- `references/confluence-storage-format.md`;
- `references/status-rules.md`.

## Core non-invention rule

Never fill a field just because the template contains it.

If a value is not supported by the current transcript, a reliable same-project context source, or an explicit user statement:

- leave the value cell empty (`<td><br /></td>`), or
- omit a data row when the entire row would be meaningless.

Do **not** write filler such as:

- `Не указан`;
- `Неизвестный`;
- `Предположительно`;
- invented job titles, organizations, dates, deadlines, systems or statuses.

An empty field is preferable to an unsupported fact.

## Source priority

Use sources in this order:

1. explicit corrections/instructions from the user for the current task;
2. the current meeting transcript;
3. project/context evidence supplied with the task;
4. a previous protocol only if it is clearly the same project and relevant stage/meeting series;
5. deterministic calendar conversion from an explicit relative date, but only when the meeting date makes it unambiguous.

The current transcript overrides older protocol facts when they conflict.

Do not use general web knowledge to fill protocol facts unless the user explicitly asks for external research or verification.

## Previous-protocol gate

Before reusing facts from a previous protocol, check whether it belongs to the same project/stage.

Positive indicators include several of the following:

- same client/project name;
- same stage or workstream;
- same systems/process terminology;
- overlapping participants;
- explicit reference in the transcript to that previous meeting/protocol;
- chronological continuity.

If project identity is mismatched or uncertain, use that protocol only as a **format/visual reference**, never as a factual source.

Do not carry a previous participant, role, decision, deadline or open issue into the new protocol merely because it existed before.

## Transcript processing

Ignore non-substantive speech such as greetings, audio checks, filler, jokes and transcription noise unless it changes project meaning.

Normalize spoken language into concise business language without changing meaning.

Preserve the distinction between:

- fact;
- proposal;
- accepted decision;
- open question;
- task/action;
- risk/problem/limitation.

Do not turn a proposal into a decision.

Do not turn a speaker's intention into a committed task unless the dialogue supports that commitment.

## Participant handling

Only include participant names that are actually present in the transcript/context.

Fill `Сторона` and `Должность` only when supported.

If a person is named but their organization/role is unclear, keep those cells empty.

Do not create rows for unnamed participants merely because transcript metadata says, for example, “6 participants”.

## Relative dates and times

A relative date may be converted to an absolute date only when deterministic.

Example: a meeting is explicitly dated Monday 05.10.2026 and the participants agree on “следующая встреча в пятницу”. It is safe to render 09.10.2026.

Do not calculate a date from vague phrases such as “в начале месяца”, “примерно через пару недель” or “как обычно”. Keep the wording as stated.

If different time references conflict, use the final explicit agreement and describe timezone when stated.

## Protocol sections

Render the protocol in the canonical order from `templates/protocol-template.xml`:

1. `Общая информация`;
2. `Участники`;
3. `Цель встречи и исходный контекст`;
4. `Ключевые итоги встречи`;
5. `Обсуждение по тематическим блокам`;
6. `Зафиксированное текущее состояние`;
7. `Принятые решения`;
8. `Открытые вопросы, риски и ограничения`;
9. `Задачи и следующие шаги`.

Do not add sections just to make the protocol longer.

A section may contain no data rows if the meeting produced no supported content for it. Prefer omitting empty data rows over inventing content.

## Thematic blocks

Group the transcript by business topic, not by chronological speaker turns.

For each block record:

- what was discussed;
- the actual conclusion;
- status according to `references/status-rules.md`.

Keep wording compact enough to scan in Confluence.

Use `<br /><br />` inside a table cell to separate multiple supported subpoints.

## Decisions

A row belongs in `Принятые решения` only when acceptance is explicit or clearly confirmed by the dialogue.

Examples of acceptance signals:

- “давайте так”;
- “согласовано”;
- “всё верно”;
- “окей, тогда делаем ...”;
- an explicit confirmation after a proposal.

Do not list unresolved proposals as decisions.

## Tasks and next steps

Create a task when an action is agreed or clearly undertaken.

- `Задача` — what will be done.
- `Ожидаемый результат` — concrete deliverable/outcome only if supported.
- `Срок` — exact date/time if explicit or deterministically derivable; otherwise blank.
- `Ответственный` — person/side only if supported; otherwise blank.

Do not invent a responsible party from “someone should”.

## Open questions, risks and limitations

Use this section for unresolved matters that require follow-up.

Recommended `Тип` values are descriptive, not a closed enum, for example:

- `Организационный вопрос`;
- `Проблема`;
- `Риск`;
- `Ограничение`;
- `Технический вопрос`;
- `Бизнес-процесс`.

Do not label an already-realized issue as a future risk.

## Confluence output rules

The output must be a Storage Format fragment.

- Do not wrap it in Markdown code fences.
- Do not emit `<html>`, `<head>` or `<body>`.
- Preserve valid XML/XHTML nesting.
- Escape `&`, `<`, `>` when they are text.
- Use `<br />`, not HTML-only `<br>`.
- Preserve the heading style from the bundled template.
- Tables use `class="wrapped"`.
- Do not insert JavaScript, CSS blocks or unsupported macros.

If the user supplies a previous same-project protocol with Confluence macros/layout and explicitly asks to preserve them, inherit compatible markup from that protocol. Otherwise use the bundled template.

## Mandatory quality pass

Before returning the file, verify:

1. every visible fact is supported by a source allowed by the priority rules;
2. no unsupported participant role/organization was added;
3. proposals are not presented as accepted decisions;
4. open issues are not silently treated as closed;
5. tasks have no invented responsible/deadline;
6. relative dates were converted only when deterministic;
7. headings and tables follow the canonical structure;
8. empty/unknown values are blank, not “Не указан/Неизвестный”;
9. XML special characters are escaped;
10. the fragment parses when wrapped in a temporary root element;
11. the final response names the generated XML file and briefly notes any deliberately blank fields that materially affect interpretation.

## Execution workflow

1. Read the current transcript completely.
2. Read optional project context and previous protocol if supplied.
3. Apply the previous-protocol gate before reusing any prior fact.
4. Build a factual meeting outline: metadata, participants, topics, decisions, open items and tasks.
5. Mark uncertain fields as blank rather than guessing.
6. Render the outline into the bundled Storage Format structure.
7. Run the mandatory quality pass and XML validation.
8. Return the XML file.
