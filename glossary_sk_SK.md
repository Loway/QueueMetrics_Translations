# Glossary — QueueMetrics (sk_SK)

> **Note:** This glossary was **seeded from existing labels** in `queuemetrics_sk_SK.md`. It collects
> terminology decisions already in use and still needs human review for consistency and accuracy.
> Review section 7 (Doubts & items needing review) for flagged items. Once verified, this becomes
> the source of truth for term consistency across the Slovak label pack.

This is the **terminology master** for QueueMetrics. It collects the telephony
jargon, abbreviations and recurring UI terms that appear — often hundreds of
times — across [queuemetrics_sk_SK.md](queuemetrics_sk_SK.md).

## Why this file exists

Many labels reuse the same handful of domain terms (`agent`, `queue`, `wait
time`, `SLA`, `wrap-up`, `Avg.`…). If each label is translated in isolation, the
same English word ends up rendered three different ways in one language. The
goal here is: **decide the translation of each term once, then reuse it
everywhere** so a whole language pack stays coherent.

## How to use it

The **Translation** column contains agreed terms for Slovak. When translating
main label files, reuse exactly these choices to maintain consistency.

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
| ACD | Automatic Call Distribution — the routing engine that assigns calls to agents | Skupina ACD | `clage_agent_performance_acd_group` | |
| IVR | Interactive Voice Response — the automated voice menu | IVR | `aout_inforec` | Kept in English |
| DNIS | Dialed Number Identification Service — the number that was called | DNIS | `cld_asterisk_dnis` | Kept in English |
| DID | Direct Inward Dialing — a directly-reachable inbound number | DID | `fp_dnis_edit` (DID/DNIS Lines) | Kept in English (as DID/DNIS) |
| CLID | Calling Line Identification — the caller's number / caller-ID | CLID | `carea_select_number_of_clid_digits_to_search` | Kept in English |
| PBX | Private Branch Exchange — the phone system QueueMetrics monitors | PBX | `pgag_popup_cannot_send_message` | Kept in English |
| MOH | Music On Hold | MOH | `cld_asterisk_mohdur` (MOH duration) | Kept in English |
| AMO | Assisted Manual Outbound (Loway term) | AMO | `hdr_amo` | Kept in English |
| AGAW | Agent real-time monitoring module (QueueMetrics-specific term) | AGAW | `td_dbtest_wz_agawcleanup`, `edit_record_agawqueue_title` | Kept in English |

---

## 2. Metrics & KPI acronyms

| Term | English meaning / context | Translation | Example label(s) | Notes |
|------|---------------------------|-------------|------------------|-------|
| SLA | Service Level Agreement — % of calls answered within target time | SLA | `td_ancod_answered_calls_sla` | Kept in English |
| SPH | Sales per Hour | Predaj za hodinu | `aout_index_sph` | |
| CPH | Contacts per Hour | CPH | `aout_cph` | Kept in English |
| QCPH | Qualified Contacts per Hour | Podstatné kontakty za hodinu | `aout_index_qcph` | |
| DOW | Day Of Week | Deň | `cldst_ta_traffic_analysis_by_period_dow` | |

---

## 3. Quality / training / system acronyms

| Term | English meaning / context | Translation | Example label(s) | Notes |
|------|---------------------------|-------------|------------------|-------|
| QA | Quality Assurance (grading / scorecards) | QA Formulár | `art_lblQAForm` (QA Form) | Verify against pack |
| QC | Quality Control | Úsp.Q. | `ko_succ_q` | Verify against pack |
| CBT | Computer-Based Training | CBT | `hdr_cbt` (CBTs) | Kept in English |
| Prompt | A prompt for an AI model to perform QA | Prompt | `edit_qa_prompt`, `edit_record_qa_aiprompt` | New AI term; kept in English — verify against pack |

---

## 4. Common UI abbreviations

Keep the translation **abbreviated** too — these sit in tight table headers and
menus. Match the source's truncation style (trailing `.`).

| Term | Full form | Translation | Example label(s) | Notes |
|------|-----------|-------------|------------------|-------|
| Avg. | Average | Priemer | `aout_avg_sec` | |
| Max. | Maximum | Max priem. | `cldst_ta_ag_max` | Inconsistent: could be just "Max." |
| Min. | Minimum | Min. | (paired with Max.) | Standard abbreviation |
| Tot. | Total | Celkovo | `aout_tot_sec` (Tot. Time) | |
| Num. | Number | Číslo | `propedit_key_phone_maxsessions` | Verify against pack |
| Dur. | Duration | Trvanie | `clage_acd_duration` | |
| Att. | Attempts | Pokusy | `hdr_attempts` | |
| Ans. | Answered | Odpov. | `cldst_ans` | Abbreviated correctly |
| Unans. | Unanswered | Neodpov. | `cldst_unans` | Abbreviated correctly |
| Conv. | Conversation | Konv. | `aout_ftrconv` (Ftr. Conv.) | Seeded from pack value |
| Qualif. | Qualified | Kvalif. | `td_calloutc_qualif` | |
| Cont. | Contacts | Kontakt | `aout_contacts_n` | |
| Bill. | Billable | účtovanie | `aout_billable_s` | Inconsistent capitalization |
| Succ. | Successful | Úsp.Q. | `ko_succ_q` (Succ.Q.) | |
| Short. | Short | Krátke.Q. | `ko_sho_q` (Short.Q.) | |
| Ag. | Agent | Ag. | `cldst_ta_ag_max` (Max Ag.) | Verify against pack |
| Ext. | Extension | Linka. | `art_localExtension` | |
| Ref. | Reference | Odkaz # | `ccase_case_xref` (Ref. #) | Seeded as phrase |
| sec. | seconds | (sek.) | `rt3_duration` (Duration (sec.)) | Seeded with parentheses |

---

## 5. Telephony domain terms (full words)

The high-frequency vocabulary of the product. Pick one translation per term and
keep it consistent everywhere.

| Term | English meaning / context | Translation | Example label(s) | Notes |
|------|---------------------------|-------------|------------------|-------|
| Agent | Operator who handles calls | Agent | `td_agstatus_agent_is_currently_logged_off` | |
| Queue | Call queue | Fronta | `td_ancod_answered_calls_agents_on_queue` | |
| Caller | The person calling in | Volajúci | `td_cko_caller_abandon` | |
| Call (answered) | Answered call | Prevzaté hovory | `td_ancod_answered_calls_details` | Seeded from pack context |
| Unanswered / Lost call | Call that was not answered | Neprevzané hovory | `td_ancod_unanswered_calls_details`, `aout_fcr_detail_lost` | |
| Abandon(ed) | Caller hung up while waiting | Ukončil | `td_cko_abandon` | |
| Hangup | Call termination | Ukončenia | `aout_ivr_hangups` | |
| Wait time | Time spent queued before answer | Priemerný čas čakania | `edit_record_agawqueue_avgwait` | |
| Talk time | Time spent in conversation | Čas hovoru | `qap_details_talk` | |
| Wrap-up | Post-call work time | Wrap-up čas | `td_autoconf_wz_queuewrapup` | Kept in English (wrap-up) |
| Pause | Agent paused / not taking calls | V pauze | `td_agawlogon_paused` | |
| Session | An agent's logged-on period | Sedenie agenta | `td_ancod_agent_sessions_detail` | |
| Inbound / Outbound | Call direction | Outbound | `aout_*` (Outbound), `aout_inforec` | Kept in English for Outbound |
| Transfer | Passing a call to another party | Presmerované | `td_callstatus_html_transferred` | |
| Spill | Overflow call routed onward | Odchod | `td_aglev_spill` | |
| Ringing | Phone is ringing | Zvonenie | `evt_ringing` | |
| Extension | Phone extension number | Linka | `art_localExtension` | |
| Skill | Agent skill / competency tag | Zručnosti | `cldst_skills_per_day` | |
| Voicemail | Recorded message | hlasová pošta | `td_cko_timeout_voicemail` | |
| Recall | Scheduled call-back | Plánovač pripomenutí | `art_lblWbRecallPanel` (Recall Scheduler) | |
| Supervisor | Agent overseer | Supervízor | `edit_ac_supervisor` | |
| Spy / Barge / Whisper | Live-call monitoring actions | Vstúpiť do hovoru / Šepkať | `rt3_actions_barge`, `rt3_actions_whisper` | |
| Billable | Time/activity that is billed | Účtované činnosti | `aout_act_billable` | |
| Outcome | Result/disposition of a call | Výsledky hovoru | `aout_call_res_by_outcome` | |
| Disposition | Coded call result / rule | Výsledky hovoru | `cdp_clonedispositions` | Seeded from outcome context |
| Tag | Call tag / label | Štítok | `aout_calltag` | |
| Realtime | Live monitoring view | (implicitly "On-Line" or "Monitor") | `art_active_polling_error` | Verify against pack |
| Wallboard | Large real-time status display | Wallboard | `rt3_delete_current_wallboard_confirm` | Kept in English; verify against pack |
| Alarm | Threshold alert | Prah | `edit_record_agawqueue_title` (AGAW alarms) | Verify against pack |
| Threshold | Trigger value for alarms/SLA | Prahová hodnota | `custrep_skills_valhrd` | |

---

## 6. General UI terms

Recurring application-chrome vocabulary. Worth fixing once for menu/button
consistency.

| Term | Context | Translation | Example label(s) | Notes |
|------|---------|-------------|------------------|-------|
| Report | Analysis output | Report / Prehľad | `aout_*`, report menus | Verify consistency in pack |
| Edit / Add / Delete / Create | CRUD actions on forms | Upraviť / Pridať / Vymazať / Vytvoriť | `*_edit`, `*_add`, `*_delete` | |
| Export | Export to CSV/PDF/XLS | Export | export buttons | |
| Configuration / Settings | Setup screens | Konfigurácia | `*configuration*`, `*settings*` | |
| Visibility | Access/visibility key | Viditeľnosť / Kľúč viditeľnosti | visibility-key labels | |
| Group | Agent / report grouping | Skupina | `clage_agent_performance_acd_group` | |
| Period | Time range of a report | Časové obdobie / Perióda | period selectors | |
| Status | Current state | Stav | `td_agstatus_*` | |
| Details / Detail | Drill-down view | Detaily / Podrobnosti | `td_ancod_answered_calls_details` | |
| Feature | Licensable capability | Funkcia | feature-key labels | |
| Password / User / Code | Login & identity fields | Heslo / Užívateľ / Kód | `td_autoconf_wz_agentpwd` | |

---

## 7. Doubts & items needing review

Per-language glossaries add rows here for any term whose translation is
uncertain or whose existing pack is inconsistent.

| Term | Issue | Seeded choice | Options to decide between |
|------|-------|---------------|---------------------------|
| QC | Glossary term vs. pack abbreviation | Úsp.Q. | Should "Quality Control" be abbreviated as "QC" or reuse the packed value "Úsp.Q." (which seems to refer to "Successful")? |
| QA | Inconsistent use in pack | QA Formulár | QA appears as "QA Formulár" in one place; verify if standalone QA should use this or just "QA" |
| Max. | Possible abbreviation variance | Max priem. | Pack shows "Max priem." (Max average?) but may need simpler "Max." alone |
| Num. | No explicit match found | Číslo | Standard translation; verify it appears correctly in numerical contexts in pack |
| Ag. | No explicit abbreviation found | Ag. | Standard abbreviation; verify if pack uses shortened agent form |
| Realtime | Translation implied but not explicit | (implicitly "On-Line" or "Monitor") | Check if pack has explicit "Realtime" or if "Monitor On-Line" is the standard phrase |
| Wallboard | Appears to be kept English | Wallboard | Confirm if Slovak should keep "Wallboard" untranslated or use a standard term |
| Alarm | Uncertain context | Prah | Pack context suggests threshold/alarm; confirm correct term |
| Report | Inconsistency in pack | Report / Prehľad | Pack uses both "Report" and "Prehľad"; pick one or clarify usage patterns |
| Disposition | May overlap with Outcome | Výsledky hovoru | Confirm if "Disposition" should distinguish from "Outcome" or remain the same |
| Ftr. Conv. | Abbreviation context | Konv. | Seeded as "Ftr. Konv." from pack; verify correct form for abbreviation |
| Ref. # | Phrase translation | Odkaz # | Seeded as phrase "Odkaz #" from pack; verify if standalone "Ref." should be used |
| sec. | Parenthetical form | (sek.) | Seeded with parentheses from pack; verify if this is the standard abbreviation style |
| Inbound | Missing explicit translation | (see Outbound context) | Outbound kept English; should Inbound also be kept English or translated as "Príchodzí"? |
| Billable term | Inconsistent capitalization | účtovanie | Pack shows lowercase "účtovanie"; verify if this should be capitalized "Účtovanie" |
