# Glossary — QueueMetrics (am_ET)

> **Note:** This glossary was **seeded from existing labels** in `queuemetrics_am_ET.md`. All translations require human review and verification before release.

This is the **terminology master** for QueueMetrics in Amharic. It collects the telephony
jargon, abbreviations and recurring UI terms that appear — often hundreds of
times — across [queuemetrics_am_ET.md](queuemetrics_am_ET.md).

## Why this file exists

Many labels reuse the same handful of domain terms (`agent`, `queue`, `wait
time`, `SLA`, `wrap-up`, `Avg.`…). If each label is translated in isolation, the
same English word ends up rendered three different ways in one language. The
goal here is: **decide the translation of each term once, then reuse it
everywhere** so a whole language pack stays coherent.

## How to use it (per language)

1. Verify the **Translation** column against the agreed Amharic terminology.
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
| ACD | Automatic Call Distribution — the routing engine that assigns calls to agents | ACD | `clage_agent_performance_acd_group` | Kept in English |
| IVR | Interactive Voice Response — the automated voice menu | IVR | `aout_inforec` | Kept in English |
| DNIS | Dialed Number Identification Service — the number that was called | DNIS | `cld_asterisk_dnis` | Kept in English |
| DID | Direct Inward Dialing — a directly-reachable inbound number | DID | `fp_dnis_edit` (DID/DNIS Lines) | Kept in English |
| CLID | Calling Line Identification — the caller's number / caller-ID | CLID | `carea_select_number_of_clid_digits_to_search` | Kept in English |
| PBX | Private Branch Exchange — the phone system QueueMetrics monitors | ፒቢኤክስ | `pgag_popup_cannot_send_message` | Translated |
| MOH | Music On Hold | MOH | `cld_asterisk_mohdur` (MOH duration) | Kept in English |
| AMO | Assisted Manual Outbound (Loway term) | AMO | `hdr_amo` | Kept in English |
| AGAW | Agent real-time monitoring module (QueueMetrics-specific term) | AGAW | `td_dbtest_wz_agawcleanup`, `edit_record_agawqueue_title` | Kept in English |

---

## 2. Metrics & KPI acronyms

| Term | English meaning / context | Translation | Example label(s) | Notes |
|------|---------------------------|-------------|------------------|-------|
| SLA | Service Level Agreement — % of calls answered within target time | ኤሳኤልኤ | `td_ancod_answered_calls_sla` | Translated |
| SPH | Sales per Hour | በሰዓት የሚደረጉ ሽያጮች (SPH) | `aout_index_sph` | Hybrid (English acronym + Amharic expansion) |
| CPH | Contacts per Hour | CPH | `aout_cph` | Kept in English |
| QCPH | Qualified Contacts per Hour | በሰዓት የሚደረጉ ብቁ ግንኙነቶች (QCPH) | `aout_index_qcph` | Hybrid (English acronym + Amharic expansion) |
| DOW | Day Of Week | DOW | `cldst_ta_traffic_analysis_by_period_dow` | Kept in English |

---

## 3. Quality / training / system acronyms

| Term | English meaning / context | Translation | Example label(s) | Notes |
|------|---------------------------|-------------|------------------|-------|
| QA | Quality Assurance (grading / scorecards) | QA | `art_lblQAForm` (QA Form) | Kept in English |
| QC | Quality Control | QC | `ko_succ_q` | Kept in English |
| CBT | Computer-Based Training | CBTs | `hdr_cbt` (CBTs) | Kept in English |

---

## 4. Common UI abbreviations

Keep the translation **abbreviated** too — these sit in tight table headers and
menus. Match the source's truncation style (trailing `.`).

| Term | Full form | Translation | Example label(s) | Notes |
|------|-----------|-------------|------------------|-------|
| Avg. | Average | አማካይ | `aout_avg_sec` | Translated |
| Max. | Maximum | ከፍተኛ | `cldst_ta_ag_max` | Translated |
| Min. | Minimum | ዝቅተኛ | (paired with Max.) | Verify against pack |
| Tot. | Total | ጠቅላላ | `aout_tot_sec` (Tot. Time) | Translated as ጠቅላላ ጊዜ in full form; abbreviate to ጠቅላላ |
| Num. | Number | ቁጥር | `propedit_key_phone_maxsessions` | Verify against pack |
| Dur. | Duration | ቆይታ | `clage_acd_duration` | Translated |
| Att. | Attempts | ሙከራዎች | `hdr_attempts` | Translated as ሙከራዎች (full form); abbreviate to Att. |
| Ans. | Answered | መልስ | `cldst_ans` | Translated |
| Unans. | Unanswered | ያልተመለሱ | `cldst_unans` | Translated |
| Conv. | Conversation | Conversation | `aout_ftrconv` (Ftr. Conv.) | Kept in English |
| Qualif. | Qualified |  ኳሊፍ | `td_calloutc_qualif` | Translated |
| Cont. | Contacts | ተገናኝ | `aout_contacts_n` | Translated |
| Bill. | Billable | ክፍያ | `aout_billable_s` | Translated |
| Succ. | Successful | ተሳክቷል | `ko_succ_q` (Succ.Q.) | Translated |
| Short. | Short | አጭር | `ko_sho_q` (Short.Q.) | Translated as አጭር.ጥ.; note inconsistency |
| Ag. | Agent | ወኪል | `cldst_ta_ag_max` (Max Ag.) | Translated |
| Ext. | Extension | Ext. | `art_localExtension` | Kept in English |
| Ref. | Reference | Ref. | `ccase_case_xref` (Ref. #) | Kept in English |
| sec. | seconds | ሰከንድ | `rt3_duration` (Duration (sec.)) | Translated as ሰከንድ in full; abbreviate to sec. |

---

## 5. Telephony domain terms (full words)

The high-frequency vocabulary of the product. Pick one translation per term and
keep it consistent everywhere.

| Term | English meaning / context | Translation | Example label(s) | Notes |
|------|---------------------------|-------------|------------------|-------|
| Agent | Operator who handles calls | ወኪል | `td_agstatus_agent_is_currently_logged_off` | Translated |
| Queue | Call queue | ወረፋ | `td_ancod_answered_calls_agents_on_queue` | Translated |
| Caller | The person calling in | ደዋይ | `td_cko_caller_abandon` | Translated |
| Call (answered) | Answered call | ጥሪ | `td_ancod_answered_calls_details` | Translated |
| Unanswered / Lost call | Call that was not answered | ያልተነሱ ስልኮች / የጠፉ ጥሪዎች | `td_ancod_unanswered_calls_details`, `aout_fcr_detail_lost` | Translated |
| Abandon(ed) | Caller hung up while waiting | መተው | `td_cko_abandon` | Translated |
| Hangup | Call termination | ስልኩን መዝጋት | `aout_ivr_hangups` | Translated |
| Wait time | Time spent queued before answer | አማካይ የጥበቃ ጊዜ | `edit_record_agawqueue_avgwait` | Translated |
| Talk time | Time spent in conversation | የንግግር ጊዜ | `qap_details_talk` | Translated |
| Wrap-up | Post-call work time | የማጠቃለያ ጊዜ | `td_autoconf_wz_queuewrapup` | Translated |
| Pause | Agent paused / not taking calls | ማቆም | `td_agawlogon_paused` | Translated |
| Session | An agent's logged-on period | ሥራ ክፍለ ጊዜ | `td_ancod_agent_sessions_detail` | Translated as ዝርዝር in example; verify exact term |
| Inbound / Outbound | Call direction | ወደ ውስጥ / ወደ ውጪ | `aout_*` (Outbound), `aout_inforec` | Verify against pack |
| Transfer | Passing a call to another party | ተላልፏል | `td_callstatus_html_transferred` | Translated |
| Spill | Overflow call routed onward | መፍሰስ | `td_aglev_spill` | Translated |
| Ringing | Phone is ringing | እየደወለ ነው | `evt_ringing` | Translated |
| Extension | Phone extension number | Ext. | `art_localExtension` | Kept in English |
| Skill | Agent skill / competency tag | ክህሎቶች | `cldst_skills_per_day` | Translated |
| Voicemail | Recorded message | ጊዜው ያለፈበት (የድምጽ መልእክት) | `td_cko_timeout_voicemail` | Translated |
| Recall | Scheduled call-back | የማስታዎሻ መርሐግብር | `art_lblWbRecallPanel` (Recall Scheduler) | Translated |
| Supervisor | Agent overseer | ተቆጣጣሪ | `edit_ac_supervisor` | Translated |
| Spy / Barge / Whisper | Live-call monitoring actions | ጣልቃ ግባ / ሹክሹክታ | `rt3_actions_barge`, `rt3_actions_whisper` | Translated |
| Billable | Time/activity that is billed | የሚከፈልባቸው | `aout_act_billable` | Translated |
| Outcome | Result/disposition of a call | ውጤት | `aout_call_res_by_outcome` | Translated |
| Disposition | Coded call result / rule | የአቀማመጥ | `cdp_clonedispositions` | Translated |
| Tag | Call tag / label | መለያ | `aout_calltag` | Translated |
| Realtime | Live monitoring view | Realtime | `art_active_polling_error` | Kept in English |
| Wallboard | Large real-time status display | የግድግዳ ሰሌዳ | `rt3_delete_current_wallboard_confirm` | Translated |
| Alarm | Threshold alert | ማንቂያ | `edit_record_agawqueue_title` (AGAW alarms) | Translated |
| Threshold | Trigger value for alarms/SLA | መጠነ ልክ | `custrep_skills_valhrd` | Translated |

---

## 6. General UI terms

Recurring application-chrome vocabulary. Worth fixing once for menu/button
consistency.

| Term | Context | Translation | Example label(s) | Notes |
|------|---------|-------------|------------------|-------|
| Report | Analysis output | ሪፖርት | `hdr_reports` | Translated |
| Edit / Add / Delete / Create | CRUD actions on forms | አርትዕ / ጨመር / ሰርዝ / ጣውቅ | `*_edit`, `*_add`, `*_delete` | Verify against pack for consistency |
| Export | Export to CSV/PDF/XLS | ላክ | `cld_btn_export_calls` | Translated |
| Configuration / Settings | Setup screens | ማዋቀር / ቅንብሮች | `td_synchronier_configuration`, `edit_record_agawqueue_asettings` | Translated |
| Visibility | Access/visibility key | የሚታይ ቁልፍ | visibility-key labels | Translated |
| Group | Agent / report grouping | ቡድን | `clage_agent_performance_acd_group` | Translated |
| Period | Time range of a report | ጊዜ | `edit_exports_period` | Translated |
| Status | Current state | ሁኔታ | `art_lblCallStatus` | Translated |
| Details / Detail | Drill-down view | ዝርዝር | `td_ancod_answered_calls_details` | Translated |
| Feature | Licensable capability | ባህሪ | `art_setFeatureCode` | Translated |
| Password / User / Code | Login & identity fields | ፓስወርድ / ተጠቃሚ / ኮድ | `td_autoconf_wz_agentpwd` | Verify against pack |

---

## 7. Doubts & items needing review

Per-language glossaries add rows here for any term whose translation is
uncertain or whose existing pack is inconsistent.

| Term | Issue | Seeded choice | Options to decide between |
|------|-------|---------------|---------------------------|
| Min. | No value found in pack for minimum abbreviation | ዝቅተኛ | Use full word ዝቅተኛ or abbreviate to Min. in tight spaces |
| Num. | No value found in pack for number abbreviation | ቁጥር | Use full word ቁጥር or shorten to Num. |
| Conv. | Pack keeps English "Conversation" (Ftr. Conv.) | Conversation | Verify whether to translate or keep English |
| Inbound / Outbound | Pack uses inconsistent patterns; needs verification | ወደ ውስጥ / ወደ ውጪ | Check all occurrences for consistency |
| Ext. | Pack keeps English abbreviation | Ext. | Verify whether Ext. is acceptable or needs Amharic term |
| Ref. | Pack keeps English abbreviation | Ref. | Verify whether Ref. is acceptable or needs Amharic term |
| Session | Example shows ዝርዝር (detail) but session may need separate term | ሥራ ክፍለ ጊዜ | Verify correct Amharic term for "session" |
| Edit / Add / Delete / Create | Multiple forms exist in pack; need consistency check | አርትዕ / ጨመር / ሰርዝ / ጣውቅ | Verify all CRUD action terms are consistent across pack |
| Password / User / Code | No specific examples found for all three | ፓስወርድ / ተጠቃሚ / ኮድ | Search pack for these terms and verify translations |
| Realtime | Pack keeps English term | Realtime | Verify whether to use Amharic equivalent or keep English |
| SPH / QCPH | Pack uses hybrid form (English acronym + Amharic explanation) | በሰዓት የሚደረጉ ሽያጮች (SPH) / በሰዓት የሚደረጉ ብቁ ግንኙነቶች (QCPH) | Clarify whether to use acronym alone or keep hybrid form |
| Tot. (abbreviation) | Full form is ጠቅላላ ጊዜ; abbreviation form needs verification | ጠቅላላ | Verify correct abbreviation for tight table headers |
| Att. (abbreviation) | Full form is ሙከራዎች; abbreviation form needs verification | Att. (may keep English) | Verify correct abbreviation for tight table headers |
| Short. (inconsistency) | Pack shows አጭር.ጥ. in one context | አጭር | Clarify intended abbreviation format |
| Ag. (abbreviation) | Full form is ወኪል; abbreviation in tight spaces | Ag. (may keep English) | Verify abbreviation strategy for agent |
