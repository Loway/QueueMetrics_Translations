# CLAUDE.md

Guidance for working in this repository. Read the [README.md](README.md) for the
human-facing contributor workflow; this file is the operational guide for doing
translation work here.

## What this repo is

Localization label files for two Loway products, **QueueMetrics** and
**WombatDialer**. These labels are shown in each product's GUI. Each file holds
the labels for one language/country (locale).

- `queuemetrics_<locale>.md` — QueueMetrics labels (repo root).
- `WombatDialer/wombatdialer_<locale>.md` — WombatDialer labels.

Locales are `<ISO-639-1 language>_<ISO-3166 country>`, e.g. `fr_FR`, `pt_BR`,
`ka_GE`. They must be Java-compatible (see README "The Locale" section).

## Source of truth

**Loway authors the English text** and ships it in the `en_US` files:

- [queuemetrics_en_US.md](queuemetrics_en_US.md)
- [WombatDialer/wombatdialer_en_US.md](WombatDialer/wombatdialer_en_US.md)

Every other language is derived from English. When a label is missing or untranslated
in a language, QueueMetrics falls back to the English text — partial translations are
fine.

The **document structure** (headings, comments, ordering) is taken verbatim from
English. Do not modify it; it is regenerated from English anyway. Only translate
**values**.

## Terminology glossary

[glossary_en_US.md](glossary_en_US.md) is the **terminology master** for
QueueMetrics. It collects the telephony jargon, abbreviations and recurring UI
terms that appear (often hundreds of times) across the label files, so each term
is **decided once and translated consistently** everywhere.

- It is a **human-readable Markdown table**, not a `key=value` label file — it is
  *not* consumed by the `aitrans` tool.
- Columns are **Term | English meaning/context | Translation | Example label(s)**.
  The *Example label(s)* column points at one or two keys in `*_en_US.md` where
  the term occurs, for context. Keys are never translated.
- Section 0 lists **do-not-translate** terms (product names, protocols, file
  formats). Later sections cover telephony acronyms, KPI/metric acronyms, UI
  abbreviations, telephony domain words, and general UI terms.

To localize terminology for a language, copy the file to `glossary_<locale>.md`,
fill the **Translation** column once, and **reuse those exact choices** when
translating that language's label files. This is the source of truth for term
consistency; when a glossary entry conflicts with an ad-hoc choice, follow the
glossary.

When you are told that the Glossary file was updated, look at the git history of the English version, then apply the same change to each language. If the corresponding label does not exists, decide one.

## File format

Translatable entries live inside indented code blocks, one per line:

```
    key=value
```

- **Indent every entry line with 4 spaces**.
- The **key** (left of `=`) is preserved **exactly as-is, never altered**.
- Only the **value** (right of `=`) is translated.

### Three kinds of entries (see README)

- **Translated / human-reviewed** — `key=translation` (no `?`). The translation has
  been written or reviewed by a human.
- **👽 Alien / AI translation** — `key=?translation`. The `?` immediately after `=`
  marks it as machine-made or imported from a similar locale.
- **🔴 Missing** — a reference comment line followed by an empty, arrowed value line:

  ```
      # 🔴 key -> English text for reference
      ➡️ key=
  ```

  `👽` is used instead of `🔴` in the comment when an alien translation already exists.
  The `➡️` arrow and `# ...` comment are scan aids so untranslated items are easy to find.

## Translation rules

When given lines to translate, each input line looks like one of:

```
key=English text
```

Any leading/trailing whitespace are **cosmetic — ignore them**.

Output one translated line per input line:

- **Never alter the key.**
- Translate the value only.
- **Check the language's glossary first.** If `glossary_<locale>.md` exists, look up
  any glossary term that appears in the value (telephony jargon, abbreviation, or UI
  term) and reuse its agreed translation **exactly**, so terminology stays consistent
  with the rest of the pack. The glossary wins over an ad-hoc choice. If the term has
  an open row in the glossary's "Doubts & items needing review" section, follow the
  seeded choice and don't silently diverge.
- **Preserve placeholders, variables, HTML tags and punctuation patterns** — trailing
  colons, parentheses like `(sec.)`, `<font color='red'>...</font>`, format tokens, etc.
- **Keep abbreviations short when the original is abbreviated** (e.g.
  `Ephemeral Att.` → `Attr. éphémères`), especially for menu/header labels with limited
  space.
- Mark every AI-produced value as alien: the `=` becomes `=?`
  (i.e. `key=?translation`).

### Product-specific terms (from the en_US header)

- **WombatDialer** is a product name — leave it unaltered.
- **CSV** — leave unaltered.
- **AMO** = Assisted Manual Outbound.
- **Teams** refers to MS Teams — leave the name unaltered.

## Tasks

### Complete missing translations for a language

1. In the target language file, find untranslated items — lines whose value is empty
   (`key=` with nothing after the `=`; in practice `    ➡️ key=`).
2. Look up the same key in the corresponding English file (`*_en_US.md`) to get the
   source text. The reference text is also shown on the preceding `# ... -> English`
   comment line.
3. Translate it and fill the value **in place**: keep the `# ...` comment line and the
   `➡️` arrow as they are, and just insert the translation after the `=`, using `=?` to
   mark it as an AI translation:

   ```
       # 🔴 key -> English text for reference
       ➡️ key=?Translated text
   ```

### Create a glossary for a language

Produce `glossary_<locale>.md` from [glossary_en_US.md](glossary_en_US.md). The
goal is to fill the **Translation** column once, so terminology stays coherent
across the whole label pack.

**Always seed from the values already in use** — do not invent translations when
the language pack already has them:

1. Copy the structure of [glossary_en_US.md](glossary_en_US.md) (same sections,
   terms, **Example label(s)** and **Notes** columns).
2. For each term, look up its **Example label(s)** keys in the target language
   file (`queuemetrics_<locale>.md`) and read the value already used there. That
   existing value is the seed for the **Translation** column. Keys are matched
   exactly; the value is everything to the right of the `=` (ignore any `?`, `➡️`
   arrow or `# ...` comment).
3. Pre-fill the **Translation** column with what the pack actually uses.
   - When the pack **keeps the English term** (e.g. `SLA`, `AMO`, `PBX`), keep it
     and note "Kept in English" in **Notes**.
   - When the pack is **inconsistent** for a term (the same English word rendered
     differently across labels), pick one and flag the alternatives in **Notes**.
   - When no existing value is found, fill the best standard term for that
     language and mark it "Verify against pack" in **Notes**.
4. Add a header note stating the file was **seeded from existing labels** and
   still needs human review.
5. Collect every uncertain choice into a **"Doubts & items needing review"**
   section at the end of the file (see fr_FR for the layout). Whenever you have a
   doubt about a translation — the pack is inconsistent, keeps the English term,
   or you couldn't confirm a value from a label — add a row there with the term,
   the issue, the seeded choice, and the options to decide between. The inline
   **Notes** column flags it in place; this section is the consolidated to-do
   list. Resolve a row, then update the table above and delete the row.

Keep section 0 (do-not-translate terms) as-is for every language. This is a
**human-readable Markdown table**, not a `key=value` file — never run it through
the `aitrans` tool.

### Translate an ad-hoc list of lines

When asked to translate a set of lines (not necessarily tied to existing empty entries),
**append** the translated lines to the destination file. Each appended line is indented
with 4 spaces and uses `=?` to mark it as an AI translation.

## Generated / do-not-edit files

These are produced by tooling and/or gitignored — do not hand-edit:

- `aitrans` — compiled Elixir/Erlang translation tool (gitignored; `.tool-versions`
  pins `erlang 27.3`). Referenced as `Aitrans.rewrite_languages()`.
- `*.prompt`, `*.trans` — gitignored working files.
- [INDEX.md](INDEX.md) and [WombatDialer/INDEX.md](WombatDialer/INDEX.md) — generated
  completion-status tables.
- [NewLanguage/queuemetrics_xx_xx.md](NewLanguage/queuemetrics_xx_xx.md) — template for
  bootstrapping a new language (the `aitrans` tool consumes it).
