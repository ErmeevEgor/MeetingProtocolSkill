# Fact extraction rules

## Extract

- explicit meeting metadata;
- named participants;
- stated goals/context;
- substantive discussion topics;
- decisions with acceptance evidence;
- unresolved questions/problems/risks;
- explicit tasks, commitments and next steps;
- dates/times only when explicit or deterministically derivable.

## Ignore unless materially relevant

- greetings;
- microphone/audio checks;
- jokes and side comments;
- filler words;
- duplicate restatements;
- transcription noise.

## Conservative normalization

Convert colloquial speech into business wording, but do not add meaning.

Bad:

> “Понедельник неудобен” → “Заказчик запретил встречи по понедельникам.”

Good:

> “Предложено не проводить регулярные встречи по понедельникам из-за загрузки в начале недели.”

## Unknown values

Leave cells blank. Never substitute `Не указан`, `Неизвестный` or guessed content.

## Participants

A named person may be included without side/role.

Do not infer a formal job title from the topic they discuss.

## Derived dates

Derive only deterministic dates. Record timezone when explicitly stated.
