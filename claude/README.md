# Claude coach folder

Owner: Claude. Only Claude writes here; ChatGPT reads. ChatGPT writes only in `chatgpt/`. Rule: plan v3.3 section 0, "Two coaches, one repository".

- `tests/<track>/`: test records, `YYYY-MM-DD-<unit>-<name>.md`. Each holds the questions as asked, Om's answers verbatim, every prompt given, the marks and the correct answers.
- `reviews/`: Claude's second opinions on ChatGPT's records, only when Om asks. Five lines or fewer each.
- `outbox.md`: messages from Claude to ChatGPT, newest on top. ChatGPT replies in `chatgpt/outbox.md`.

Never here: edits to ChatGPT's files, re-scores of its tests, or a second verdict Om did not ask for.
