# Glossary — QueueMetrics (en_US)

This is the **terminology master** for QueueMetrics. It collects the telephony
jargon, abbreviations and recurring UI terms that appear — often hundreds of
times — across [queuemetrics_en_US.md](queuemetrics_en_US.md).

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

| Term | English meaning / context | Translation | Example label(s) |
|------|---------------------------|-------------|------------------|
| ACD | Automatic Call Distribution — the routing engine that assigns calls to agents | | `clage_agent_performance_acd_group` |
| IVR | Interactive Voice Response — the automated voice menu | | `aout_inforec` |
| DNIS | Dialed Number Identification Service — the number that was called | | `cld_asterisk_dnis` |
| DID | Direct Inward Dialing — a directly-reachable inbound number | | `fp_dnis_edit` (DID/DNIS Lines) |
| CLID | Calling Line Identification — the caller's number / caller-ID | | `carea_select_number_of_clid_digits_to_search` |
| PBX | Private Branch Exchange — the phone system QueueMetrics monitors | | `pgag_popup_cannot_send_message` |
| MOH | Music On Hold | | `cld_asterisk_mohdur` (MOH duration) |
| AMO | Assisted Manual Outbound (Loway term) | | `hdr_amo` |
| AGAW | Agent real-time monitoring module (QueueMetrics-specific term) | | `td_dbtest_wz_agawcleanup`, `edit_record_agawqueue_title` |

---

## 2. Metrics & KPI acronyms

| Term | English meaning / context | Translation | Example label(s) |
|------|---------------------------|-------------|------------------|
| SLA | Service Level Agreement — % of calls answered within target time | | `td_ancod_answered_calls_sla` |
| SPH | Sales per Hour | | `aout_index_sph` |
| CPH | Contacts per Hour | | `aout_cph` |
| QCPH | Qualified Contacts per Hour | | `aout_index_qcph` |
| DOW | Day Of Week | | `cldst_ta_traffic_analysis_by_period_dow` |

---

## 3. Quality / training / system acronyms

| Term | English meaning / context | Translation | Example label(s) |
|------|---------------------------|-------------|------------------|
| QA | Quality Assurance (grading / scorecards) | | `art_lblQAForm` (QA Form) |
| QC | Quality Control | | `ko_succ_q` |
| CBT | Computer-Based Training | | `hdr_cbt` (CBTs) |
| Prompt | A prompt for an AI model to perform QA | | `edit_qa_prompt`, `edit_record_qa_aiprompt`

---

## 4. Common UI abbreviations

Keep the translation **abbreviated** too — these sit in tight table headers and
menus. Match the source's truncation style (trailing `.`).

| Term | Full form | Translation | Example label(s) |
|------|-----------|-------------|------------------|
| Avg. | Average | | `aout_avg_sec` |
| Max. | Maximum | | `cldst_ta_ag_max` |
| Min. | Minimum | | (paired with Max.) |
| Tot. | Total | | `aout_tot_sec` (Tot. Time) |
| Num. | Number | | `propedit_key_phone_maxsessions` |
| Dur. | Duration | | `clage_acd_duration` |
| Att. | Attempts | | `hdr_attempts` |
| Ans. | Answered | | `cldst_ans` |
| Unans. | Unanswered | | `cldst_unans` |
| Conv. | Conversation | | `aout_ftrconv` (Ftr. Conv.) |
| Qualif. | Qualified | | `td_calloutc_qualif` |
| Cont. | Contacts | | `aout_contacts_n` |
| Bill. | Billable | | `aout_billable_s` |
| Succ. | Successful | | `ko_succ_q` (Succ.Q.) |
| Short. | Short | | `ko_sho_q` (Short.Q.) |
| Ag. | Agent | | `cldst_ta_ag_max` (Max Ag.) |
| Ext. | Extension | | `art_localExtension` |
| Ref. | Reference | | `ccase_case_xref` (Ref. #) |
| sec. | seconds | | `rt3_duration` (Duration (sec.)) |

---

## 5. Telephony domain terms (full words)

The high-frequency vocabulary of the product. Pick one translation per term and
keep it consistent everywhere.

| Term | English meaning / context | Translation | Example label(s) |
|------|---------------------------|-------------|------------------|
| Agent | Operator who handles calls | | `td_agstatus_agent_is_currently_logged_off` |
| Queue | Call queue | | `td_ancod_answered_calls_agents_on_queue` |
| Caller | The person calling in | | `td_cko_caller_abandon` |
| Call (answered) | Answered call | | `td_ancod_answered_calls_details` |
| Unanswered / Lost call | Call that was not answered | | `td_ancod_unanswered_calls_details`, `aout_fcr_detail_lost` |
| Abandon(ed) | Caller hung up while waiting | | `td_cko_abandon` |
| Hangup | Call termination | | `aout_ivr_hangups` |
| Wait time | Time spent queued before answer | | `edit_record_agawqueue_avgwait` |
| Talk time | Time spent in conversation | | `qap_details_talk` |
| Wrap-up | Post-call work time | | `td_autoconf_wz_queuewrapup` |
| Pause | Agent paused / not taking calls | | `td_agawlogon_paused` |
| Session | An agent's logged-on period | | `td_ancod_agent_sessions_detail` |
| Inbound / Outbound | Call direction | | `aout_*` (Outbound), `aout_inforec` |
| Transfer | Passing a call to another party | | `td_callstatus_html_transferred` |
| Spill | Overflow call routed onward | | `td_aglev_spill` |
| Ringing | Phone is ringing | | `evt_ringing` |
| Extension | Phone extension number | | `art_localExtension` |
| Skill | Agent skill / competency tag | | `cldst_skills_per_day` |
| Voicemail | Recorded message | | `td_cko_timeout_voicemail` |
| Recall | Scheduled call-back | | `art_lblWbRecallPanel` (Recall Scheduler) |
| Supervisor | Agent overseer | | `edit_ac_supervisor` |
| Spy / Barge / Whisper | Live-call monitoring actions | | `rt3_actions_barge`, `rt3_actions_whisper` |
| Billable | Time/activity that is billed | | `aout_act_billable` |
| Outcome | Result/disposition of a call | | `aout_call_res_by_outcome` |
| Disposition | Coded call result / rule | | `cdp_clonedispositions` |
| Tag | Call tag / label | | `aout_calltag` |
| Realtime | Live monitoring view | | `art_active_polling_error` |
| Wallboard | Large real-time status display | | `rt3_delete_current_wallboard_confirm` |
| Alarm | Threshold alert | | `edit_record_agawqueue_title` (AGAW alarms) |
| Threshold | Trigger value for alarms/SLA | | `custrep_skills_valhrd` |

---

## 6. General UI terms

Recurring application-chrome vocabulary. Worth fixing once for menu/button
consistency.

| Term | Context | Translation | Example label(s) |
|------|---------|-------------|------------------|
| Report | Analysis output | | `aout_*`, report menus |
| Edit / Add / Delete / Create | CRUD actions on forms | | `*_edit`, `*_add`, `*_delete` |
| Export | Export to CSV/PDF/XLS | | export buttons |
| Configuration / Settings | Setup screens | | `*configuration*`, `*settings*` |
| Visibility | Access/visibility key | | visibility-key labels |
| Group | Agent / report grouping | | `clage_agent_performance_acd_group` |
| Period | Time range of a report | | period selectors |
| Status | Current state | | `td_agstatus_*` |
| Details / Detail | Drill-down view | | `td_ancod_answered_calls_details` |
| Feature | Licensable capability | | feature-key labels |
| Password / User / Code | Login & identity fields | | `td_autoconf_wz_agentpwd` |

---

## 7. Doubts & items needing review

Per-language glossaries add rows here for any term whose translation is
uncertain or whose existing pack is inconsistent (see fr_FR for an example).
Empty in this English master.

| Term | Issue | Seeded choice | Options to decide between |
|------|-------|---------------|---------------------------|
| | | | |
