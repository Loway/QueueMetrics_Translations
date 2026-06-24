# Glossary — QueueMetrics (pl_PL)

This is the **terminology master** for QueueMetrics in Polish. It collects the telephony
jargon, abbreviations and recurring UI terms that appear — often hundreds of
times — across [queuemetrics_pl_PL.md](queuemetrics_pl_PL.md).

> **NOTE:** This glossary was **seeded from existing labels** in the Polish pack and still needs human review. Verify translations against the pack and adjust inconsistencies.

## Why this file exists

Many labels reuse the same handful of domain terms (`agent`, `queue`, `wait
time`, `SLA`, `wrap-up`, `Avg.`…). If each label is translated in isolation, the
same English word ends up rendered three different ways in one language. The
goal here is: **decide the translation of each term once, then reuse it
everywhere** so a whole language pack stays coherent.

## How to use it (per language)

1. Copy this file to `glossary_<locale>.md` (e.g. `glossary_fr_FR.md`).
2. Fill the **Translation** column with the agreed term for that language.
3. When translating the main label files, reuse exactly these choices.

The **Example label(s)** column points at one or two keys in the en_US file
where the term occurs, so you can see it in context. Keys are never translated —
only values.

---

## 0. Do-not-translate terms

Leave these **unaltered** in every language (product names, protocols, file
formats, standards).

| Term | Note |
|------|------|
| QueueMetrics | Product name |
| WombatDialer | Product name |
| Teams | Refers to MS Teams — keep the name |
| CSV, JSON, XML, HTML, PDF, XLS | File formats |
| SIP, AMI, HTTP(S), SMTP, RPC, API, URL, VNC, SSO, ICE | Protocols / standards |

---

## 1. Telephony & call-center acronyms

| Term | English meaning / context | Translation | Example label(s) | Notes |
|------|---------------------------|-------------|------------------|-------|
| ACD | Automatic Call Distribution — the routing engine that assigns calls to agents | Grupa ACD | `clage_agent_performance_acd_group` | Seeded from pack |
| IVR | Interactive Voice Response — the automated voice menu | IVR | `aout_inforec` | Kept in English (marked as alien in pack) |
| DNIS | Dialed Number Identification Service — the number that was called | DNIS | `cld_asterisk_dnis` | Kept in English (marked as alien in pack) |
| DID | Direct Inward Dialing — a directly-reachable inbound number | Linie DID/DNIS | `fp_dnis_edit` (DID/DNIS Lines) | Seeded from pack |
| CLID | Calling Line Identification — the caller's number / caller-ID | CLID | `carea_select_number_of_clid_digits_to_search` | Seeded from pack |
| PBX | Private Branch Exchange — the phone system QueueMetrics monitors | PBX | `pgag_popup_cannot_send_message` | Kept in English (standard term) |
| MOH | Music On Hold | MOH | `cld_asterisk_mohdur` (MOH duration) | Kept in English (marked as alien in pack) |
| AMO | Assisted Manual Outbound (Loway term) | AMO | `hdr_amo` | Kept in English (product term, marked as alien in pack) |
| AGAW | Agent real-time monitoring module (QueueMetrics-specific term) | AGAW | `td_dbtest_wz_agawcleanup`, `edit_record_agawqueue_title` | Kept in English (product-specific term) |

---

## 2. Metrics & KPI acronyms

| Term | English meaning / context | Translation | Example label(s) | Notes |
|------|---------------------------|-------------|------------------|-------|
| SLA | Service Level Agreement — % of calls answered within target time | SLA | `td_ancod_answered_calls_sla` | Kept in English (standard metric) |
| SPH | Sales per Hour | Sprzedaż na godzinę (SPH) | `aout_index_sph` | Seeded from pack |
| CPH | Contacts per Hour | CPH | `aout_cph` | Kept in English (marked as alien in pack) |
| QCPH | Qualified Contacts per Hour | Rzeczowe kontakty na godzinę (RKNG) | `aout_index_qcph` | Seeded from pack with note: "RKNG" is the Polish acronym |
| DOW | Day Of Week | DOW | `cldst_ta_traffic_analysis_by_period_dow` | Kept in English; see Notes in Doubts section |

---

## 3. Quality / training / system acronyms

| Term | English meaning / context | Translation | Example label(s) | Notes |
|------|---------------------------|-------------|------------------|-------|
| QA | Quality Assurance (grading / scorecards) | Formularz QA | `art_lblQAForm` (QA Form) | Seeded from pack (marked as alien) |
| QC | Quality Control | Pomyślne.K. | `ko_succ_q` | Uncertain; see Doubts section |
| CBT | Computer-Based Training | CBT | `hdr_cbt` (CBTs) | Kept in English (marked as alien in pack) |
| Prompt | A prompt for an AI model to perform QA | Prompt | `edit_qa_prompt`, `edit_record_qa_aiprompt` | New AI term; kept in English — verify against pack |

---

## 4. Common UI abbreviations

Keep the translation **abbreviated** too — these sit in tight table headers and
menus. Match the source's truncation style (trailing `.`).

| Term | Full form | Translation | Example label(s) | Notes |
|------|-----------|-------------|------------------|-------|
| Avg. | Average | Śred. | `aout_avg_sec` | Seeded from pack |
| Max. | Maximum | Maks. | `aout_ivr_maxTime` (or `cldst_ta_ag_max` for "Max Ag.") | Seeded from pack |
| Min. | Minimum | Min. | `aout_ivr_minTime` | Seeded from pack |
| Tot. | Total | Całkowity czas | `aout_tot_sec` (Tot. Time) | Seeded from pack; "Całkowity czas" is longer, may need shortening |
| Num. | Number | Liczba | `carea_select_number_of_clid_digits_to_search` | Seeded from pack (as "Liczba") |
| Dur. | Duration | Dł. | `clage_acd_duration` | Seeded from pack |
| Att. | Attempts | Próby | `hdr_attempts` | Seeded from pack |
| Ans. | Answered | Odeb. | `cldst_ans` | Seeded from pack |
| Unans. | Unanswered | Nieodeb. | `cldst_unans` | Seeded from pack |
| Conv. | Conversation | Konw. cech | `aout_ftrconv` (Ftr. Conv.) | Seeded from pack (marked as alien) |
| Qualif. | Qualified | Rzeczowy | `td_calloutc_qualif` | Seeded from pack |
| Cont. | Contacts | Kontakt | `aout_contacts_n` | Seeded from pack |
| Bill. | Billable | Doliczony | `aout_billable_s` | Seeded from pack |
| Succ. | Successful | Pomyślne.K. | `ko_succ_q` (Succ.Q.) | Seeded from pack (marked as alien) |
| Short. | Short | Krótkie.K. | `ko_sho_q` (Short.Q.) | Seeded from pack (marked as alien) |
| Ag. | Agent | Ag. | `cldst_ta_ag_max` (Max Ag.) | Seeded from pack; "Max Ag." kept as-is |
| Ext. | Extension | Wewn. | `art_localExtension` | Seeded from pack (marked as alien) |
| Ref. | Reference | Nr ref. | `ccase_case_xref` (Ref. #) | Seeded from pack (marked as alien) |
| sec. | seconds | sek. | `rt3_duration` (Duration (sec.)) | Seeded from pack (marked as alien) |

---

## 5. Telephony domain terms (full words)

The high-frequency vocabulary of the product. Pick one translation per term and
keep it consistent everywhere.

| Term | English meaning / context | Translation | Example label(s) | Notes |
|------|---------------------------|-------------|------------------|-------|
| Agent | Operator who handles calls | Konsultant | `td_agstatus_agent_is_currently_logged_off` | Seeded from pack |
| Queue | Call queue | Kolejka | `td_ancod_answered_calls_agents_on_queue` | Seeded from pack |
| Caller | The person calling in | Rozmówca | `td_cko_caller_abandon` | Seeded from pack |
| Call (answered) | Answered call | Połączenia odebrane | `td_ancod_answered_calls_details` | Seeded from pack |
| Unanswered / Lost call | Call that was not answered | Połączenia nieodebrane | `td_ancod_unanswered_calls_details`, `aout_fcr_detail_lost` | Seeded from pack |
| Abandon(ed) | Caller hung up while waiting | Rozłączył | `td_cko_abandon` | Seeded from pack |
| Hangup | Call termination | Rozłączenia | `aout_ivr_hangups` | Seeded from pack (marked as alien) |
| Wait time | Time spent queued before answer | Średni czas oczekiwania | `edit_record_agawqueue_avgwait` | Seeded from pack (marked as alien) |
| Talk time | Time spent in conversation | Czas rozmowy | `qap_details_talk` | Seeded from pack (marked as alien) |
| Wrap-up | Post-call work time | Czas po rozmowie | `td_autoconf_wz_queuewrapup` | Seeded from pack |
| Pause | Agent paused / not taking calls | Spauzowany | `td_agawlogon_paused` | Seeded from pack |
| Session | An agent's logged-on period | Sesje konsultanta | `td_ancod_agent_sessions_detail` | Seeded from pack |
| Inbound / Outbound | Call direction | Outbound | `aout_*` (Outbound), `aout_inforec` | Kept in English for "Outbound"; see Doubts section |
| Transfer | Passing a call to another party | Transfer | `td_callstatus_html_transferred` | Seeded from pack |
| Spill | Overflow call routed onward | Przelew | `td_aglev_spill` | Seeded from pack |
| Ringing | Phone is ringing | Dzwonienie | `evt_ringing` | Seeded from pack (marked as alien) |
| Extension | Phone extension number | Wewn. | `art_localExtension` | Seeded from pack (marked as alien); abbreviation form |
| Skill | Agent skill / competency tag | Umiejętności | `cldst_skills_per_day` | Seeded from pack (marked as alien) |
| Voicemail | Recorded message | Poczta głosowa | `td_cko_timeout_voicemail` | Seeded from pack |
| Recall | Scheduled call-back | Harmonogram oddzwonień | `art_lblWbRecallPanel` (Recall Scheduler) | Seeded from pack (marked as alien) |
| Supervisor | Agent overseer | Przełożony | `edit_ac_supervisor` | Seeded from pack (marked as alien) |
| Spy / Barge / Whisper | Live-call monitoring actions | Wtrącenie / Szept | `rt3_actions_barge`, `rt3_actions_whisper` | Seeded from pack (both marked as alien) |
| Billable | Time/activity that is billed | Doliczone aktywności | `aout_act_billable` | Seeded from pack |
| Outcome | Result/disposition of a call | Wynik | `aout_call_res_by_outcome` | Seeded from pack |
| Disposition | Coded call result / rule | Reguły dyspozycji | `cdp_clonedispositions` | Seeded from pack (marked as alien) |
| Tag | Call tag / label | Tag | `aout_calltag` | Seeded from pack (marked as alien); kept in English |
| Realtime | Live monitoring view | W czasie rzeczywistym | `art_active_polling_error` | Seeded from pack (marked as alien) |
| Wallboard | Large real-time status display | Tablica | `rt3_delete_current_wallboard_confirm` | Seeded from pack (marked as alien) |
| Alarm | Threshold alert | Alarm | `edit_record_agawqueue_title` (AGAW alarms) | Seeded from pack (marked as alien); kept in English |
| Threshold | Trigger value for alarms/SLA | Próg | `custrep_skills_valhrd` | Seeded from pack (marked as alien) |

---

## 6. General UI terms

Recurring application-chrome vocabulary. Worth fixing once for menu/button
consistency.

| Term | Context | Translation | Example label(s) | Notes |
|------|---------|-------------|------------------|-------|
| Report | Analysis output | Raport | `aout_*`, report menus | Seeded from pack |
| Edit / Add / Delete / Create | CRUD actions on forms | Edytuj / Dodaj / Usuń / Utwórz | `*_edit`, `*_add`, `*_delete` | Seeded from pack (all marked as alien) |
| Export | Export to CSV/PDF/XLS | Eksport | export buttons | Seeded from pack (marked as alien) |
| Configuration / Settings | Setup screens | Ustawienia | `*configuration*`, `*settings*` | Seeded from pack (marked as alien) |
| Visibility | Access/visibility key | Widoczność / Klucz widoczności | visibility-key labels | Seeded from pack (both marked as alien) |
| Group | Agent / report grouping | Grupa | `clage_agent_performance_acd_group` | Seeded from pack (marked as alien) |
| Period | Time range of a report | Okres | period selectors | Verify against pack |
| Status | Current state | Status | `td_agstatus_*` | Seeded from pack (kept in English for UI) |
| Details / Detail | Drill-down view | Szczegóły | `td_ancod_answered_calls_details` | Seeded from pack |
| Feature | Licensable capability | Cecha | feature-key labels | Seeded from pack (marked as alien) |
| Password / User / Code | Login & identity fields | Hasło | `td_autoconf_wz_agentpwd` | Seeded from pack |

---

## 7. Doubts & items needing review

Per-language glossaries add rows here for any term whose translation is
uncertain or whose existing pack is inconsistent. Resolve each row, then
update the table above and delete the row.

| Term | Issue | Seeded choice | Options to decide between |
|------|-------|---------------|---------------------------|
| Tot. | Seeded value "Całkowity czas" is a full phrase, not an abbreviation. Pack inconsistency or deliberate choice? | Całkowity czas | Śred. tot. / Tot. / C.czas / other |
| DOW | Pack may keep English or translate. Verify current usage. | DOW | DOW / Dzień tygodnia / D.tyg. / other |
| QC | Pack has "Pomyślne.K." seeded, but this seems to conflate Quality Control with "Successful". Need clarification. | Pomyślne.K. | K.K. / Kontrola Jakości / Pomyślne.K. / other |
| Inbound | Pack mostly uses "Outbound" in English; treatment of "Inbound" unclear. | Outbound (English) | Przychodzący / Wychodzący / keep English / other |
| Period | No direct lookup found; placeholder term. | Okres | Okres / Przedział / Zakres czasowy / other |
| Status | Pack appears to keep "Status" in English for UI. Verify if this is intentional or fallback. | Status (English) | Status / Stan / Zdarzenie / other |
| Inbound / Outbound | Full term row: the pack uses "Outbound" in English; "Inbound" usage not confirmed. | Outbound (English) | Przychodzący / Wychodzący / keep both English / other |
| Tag | Seeded as kept-English "Tag"; verify if intentional or unmarked alien. | Tag (English) | Etykieta / Oznaczenie / Tag / other |
| Alarm | Seeded as kept-English "Alarm"; verify if intentional or unmarked alien. | Alarm (English) | Alarm / Ostrzeżenie / Sygnał / other |
| Disposition | Full term "Reguły dyspozycji" is lengthy for frequent use. May need shortening. | Reguły dyspozycji | Dyspozycja / Reguły / Kat. rozmowy / other |
| SPH | Seeded phrase includes English acronym. Verify if "SPH" should be standalone. | Sprzedaż na godzinę (SPH) | Sprzedaż/godz. / SPH / Sp.na godz. / other |
| QCPH | Polish acronym "RKNG" seeded; verify if this is standard and if "QCPH" appears elsewhere. | Rzeczowe kontakty na godzinę (RKNG) | QCPH / RKNG / Rzeczowe kontakty/godz. / other |
