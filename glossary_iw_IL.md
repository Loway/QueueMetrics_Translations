# Glossary — QueueMetrics (iw_IL)

> **This glossary was SEEDED FROM EXISTING LABELS** in queuemetrics_iw_IL.md and still requires human review for consistency and completeness.

This is the **terminology reference** for QueueMetrics in Hebrew (iw_IL). It collects the telephony
jargon, abbreviations and recurring UI terms that appear — often hundreds of
times — across [queuemetrics_iw_IL.md](queuemetrics_iw_IL.md).

## Why this file exists

Many labels reuse the same handful of domain terms (נציג, תור, זמן המתנה, SLA, זמן השהייה, ממוצע…). If each label is translated in isolation, the
same English word ends up rendered three different ways in one language. The
goal here is: **decide the translation of each term once, then reuse it
everywhere** so a whole language pack stays coherent.

## How to use it (per language)

1. Refer to this file when translating the main label files for consistency.
2. When translating the main label files, reuse exactly these choices.

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
| ACD | Automatic Call Distribution — the routing engine that assigns calls to agents | קבוצת ACD | `clage_agent_performance_acd_group` | Kept in English as ACD within the phrase |
| IVR | Interactive Voice Response — the automated voice menu | IVR | `aout_inforec` | Kept in English |
| DNIS | Dialed Number Identification Service — the number that was called | DNIS | `cld_asterisk_dnis` | Kept in English |
| DID | Direct Inward Dialing — a directly-reachable inbound number | DID/DNIS | `fp_dnis_edit` | Kept in English |
| CLID | Calling Line Identification — the caller's number / caller-ID | CLID | `carea_select_number_of_clid_digits_to_search` | Kept in English |
| PBX | Private Branch Exchange — the phone system QueueMetrics monitors | מרכזייה | `pgag_popup_cannot_send_message` | Translated |
| MOH | Music On Hold | מוזיקה בהמתנה | `cld_asterisk_mohdur` | Translated |
| AMO | Assisted Manual Outbound (Loway term) | AMO | `hdr_amo` | Kept in English |
| AGAW | Agent real-time monitoring module (QueueMetrics-specific term) | AGAW | `td_dbtest_wz_agawcleanup`, `edit_record_agawqueue_title` | Kept in English |

---

## 2. Metrics & KPI acronyms

| Term | English meaning / context | Translation | Example label(s) | Notes |
|------|---------------------------|-------------|------------------|-------|
| SLA | Service Level Agreement — % of calls answered within target time | SLA | `td_ancod_answered_calls_sla` | Kept in English |
| SPH | Sales per Hour | מכירות לשעה | `aout_index_sph` | Translated |
| CPH | Contacts per Hour | התקשרויות לשעה | `aout_cph` | Translated |
| QCPH | Qualified Contacts per Hour | התקשרויות לשעה מתוקננות | `aout_index_qcph` | Translated |
| DOW | Day Of Week | יום בשבוע | `cldst_ta_traffic_analysis_by_period_dow` | Translated |

---

## 3. Quality / training / system acronyms

| Term | English meaning / context | Translation | Example label(s) | Notes |
|------|---------------------------|-------------|------------------|-------|
| QA | Quality Assurance (grading / scorecards) | QA | `art_lblQAForm` | Kept in English |
| QC | Quality Control | תור | `ko_succ_q` | Partially extracted from context |
| CBT | Computer-Based Training | CBT | `hdr_cbt` | Kept in English |

---

## 4. Common UI abbreviations

Keep the translation **abbreviated** too — these sit in tight table headers and
menus. Match the source's truncation style (trailing `.`).

| Term | Full form | Translation | Example label(s) | Notes |
|------|-----------|-------------|------------------|-------|
| Avg. | Average | ממוצע | `aout_avg_sec` | Translated |
| Max. | Maximum | מקס. | `cldst_ta_ag_max` | Translated |
| Min. | Minimum | מין. | (paired with Max.) | Standard Hebrew abbreviation |
| Tot. | Total | סה"כ | (used in totals) | Standard Hebrew abbreviation |
| Num. | Number | מספר | `propedit_key_phone_maxsessions` | Translated |
| Dur. | Duration | משך | `clage_acd_duration` | Translated |
| Att. | Attempts | נסיונות | `hdr_attempts` | Translated |
| Ans. | Answered | נענו | `cldst_ans` | Translated |
| Unans. | Unanswered | לא נענו | `cldst_unans` | Translated |
| Conv. | Conversation | המרה | `aout_ftrconv` | Translated |
| Qualif. | Qualified | מיון | `td_calloutc_qualif` | Translated |
| Cont. | Contacts | קשר | `aout_contacts_n` | Translated |
| Bill. | Billable | חיוב | `aout_billable_s` | Translated |
| Succ. | Successful | מוצלחות | `ko_succ_q` | Translated (marked as alien in pack) |
| Short. | Short | קצר | (not yet in pack) | Standard Hebrew form |
| Ag. | Agent | נציג | `cldst_ta_ag_max` | Translated |
| Ext. | Extension | שלוחה | `art_localExtension` | Translated |
| Ref. | Reference | אסמכתא | `ccase_case_xref` | Translated (marked as alien in pack) |
| sec. | seconds | שניות | `rt3_duration` | Translated |

---

## 5. Telephony domain terms (full words)

The high-frequency vocabulary of the product. Pick one translation per term and
keep it consistent everywhere.

| Term | English meaning / context | Translation | Example label(s) | Notes |
|------|---------------------------|-------------|------------------|-------|
| Agent | Operator who handles calls | נציג | `td_agstatus_agent_is_currently_logged_off` | Translated |
| Queue | Call queue | תור | `td_ancod_answered_calls_agents_on_queue` | Translated |
| Caller | The person calling in | מתקשר | `td_cko_caller_abandon` | Translated |
| Call (answered) | Answered call | שיחה שנענתה | `td_ancod_answered_calls_details` | Translated |
| Unanswered / Lost call | Call that was not answered | שיחה שלא נענתה / שיחה אבודה | `td_ancod_unanswered_calls_details`, `aout_fcr_detail_lost` | Translated |
| Abandon(ed) | Caller hung up while waiting | נטישה | `td_cko_abandon` | Translated |
| Hangup | Call termination | ניתוק | `aout_ivr_hangups` | Translated |
| Wait time | Time spent queued before answer | זמן המתנה | `edit_record_agawqueue_avgwait` | Translated |
| Talk time | Time spent in conversation | זמן דיבור | `qap_details_talk` | Translated (marked as alien in pack) |
| Wrap-up | Post-call work time | זמן השהייה | `td_autoconf_wz_queuewrapup` | Translated |
| Pause | Agent paused / not taking calls | בהפסקה | `td_agawlogon_paused` | Translated |
| Session | An agent's logged-on period | הפעלה | `td_ancod_agent_sessions_detail` | Translated |
| Inbound / Outbound | Call direction | נכנס / יוצא | `aout_*` | Translated |
| Transfer | Passing a call to another party | העברה | `td_callstatus_html_transferred` | Translated |
| Spill | Overflow call routed onward | עודף | `td_aglev_spill` | Translated |
| Ringing | Phone is ringing | מצלצל | `evt_ringing` | Translated |
| Extension | Phone extension number | שלוחה | `art_localExtension` | Translated |
| Skill | Agent skill / competency tag | כישור | `cldst_skills_per_day` | Translated |
| Voicemail | Recorded message | דואר קולי | `td_cko_timeout_voicemail` | Translated |
| Recall | Scheduled call-back | תיזמון חיוג חוזר | `art_lblWbRecallPanel` | Translated |
| Supervisor | Agent overseer | אחראי משמרת | `edit_ac_supervisor` | Translated |
| Spy / Barge / Whisper | Live-call monitoring actions | עקוב / התפרץ / לחש | `rt3_actions_barge`, `rt3_actions_whisper` | Translated |
| Billable | Time/activity that is billed | חיוב | `aout_act_billable` | Translated |
| Outcome | Result/disposition of a call | תוצאה | `aout_call_res_by_outcome` | Translated |
| Disposition | Coded call result / rule | תוצאת שיחה | `cdp_clonedispositions` | Translated |
| Tag | Call tag / label | תגית | `aout_calltag` | Translated |
| Realtime | Live monitoring view | Realtime | (monitoring views) | Kept in English; standard in many apps |
| Wallboard | Large real-time status display | לוח מחוונים | `rt3_delete_current_wallboard_confirm` | Translated |
| Alarm | Threshold alert | התראה | `edit_record_agawqueue_title` | Translated |
| Threshold | Trigger value for alarms/SLA | סף | `custrep_skills_valhrd` | Translated |

---

## 6. General UI terms

Recurring application-chrome vocabulary. Worth fixing once for menu/button
consistency.

| Term | Context | Translation | Example label(s) | Notes |
|------|---------|-------------|------------------|-------|
| Report | Analysis output | דו"ח | `aout_agent_report`, report menus | Translated |
| Edit / Add / Delete / Create | CRUD actions on forms | עריכה / הוספה / מחיקה / יצירה | `rt3_menu_edit`, `rt3_add`, `edit_record_delete` | Translated |
| Export | Export to CSV/PDF/XLS | ייצוא | `home_sysadmin_import_export` | Translated |
| Configuration / Settings | Setup screens | תצורה | `keydesc_config` | Translated |
| Visibility | Access/visibility key | גלוי | (visibility-key labels) | Guess; verify against pack |
| Group | Agent / report grouping | קבוצה | `clage_agent_performance_acd_group` | Translated |
| Period | Time range of a report | תקופה | (period selectors) | Guess; verify against pack |
| Status | Current state | סטטוס | `hdr_agaw_status` | Translated |
| Details / Detail | Drill-down view | פרטים | `td_ancod_answered_calls_details` | Translated |
| Feature | Licensable capability | תכונה | `aout_call_res_by_feature` | Translated |
| Password / User / Code | Login & identity fields | סיסמה / משתמש / קוד | (auth fields) | Guess; verify against pack |

---

## 7. Doubts & items needing review

Per-language glossaries add rows here for any term whose translation is
uncertain or whose existing pack is inconsistent.

| Term | Issue | Seeded choice | Options to decide between |
|------|-------|---------------|---------------------------|
| QC | Extracted from context; unclear whether stands for "Quality Control" or another acronym | תור | Needs review against original English context |
| Min. | No example found in pack; using standard Hebrew abbreviation | מין. | Verify if should match Max. style differently |
| Tot. | No direct example in pack; using standard Hebrew abbreviation | סה"כ | Verify standard abbreviation for totals |
| Short. | No example found in pack for "Short.Q." | קצר | Verify if exists and how used in pack |
| Inbound / Outbound | Used as concepts but may vary by context | נכנס / יוצא | Check if consistent throughout pack |
| Realtime | Kept in English; check whether should be "זמן אמת" | Realtime | Keep English or translate to "זמן אמת"? |
| Visibility | No example found in pack | גלוי | Verify if term appears and how translated |
| Period | No direct example in pack | תקופה | Verify standard translation in context |
| Password / User / Code | No example found in pack | סיסמה / משתמש / קוד | Verify against actual auth-related labels |
| Talk time (qap_details_talk) | Marked as alien (?) in pack; verify human review | זמן דיבור | Confirm whether properly translated or needs adjustment |
| Succ. (ko_succ_q) | Marked as alien (?) in pack | מוצלחות | Verify correctness and context of abbreviation |
| Ref. (ccase_case_xref) | Marked as alien (?) in pack | אסמכתא | Verify if correct Hebrew term for "Reference #" |
