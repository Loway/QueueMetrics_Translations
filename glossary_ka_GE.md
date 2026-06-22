# Glossary — QueueMetrics (ka_GE)

This is the **terminology master** for QueueMetrics in Georgian. It collects the telephony
jargon, abbreviations and recurring UI terms that appear — often hundreds of
times — across [queuemetrics_ka_GE.md](queuemetrics_ka_GE.md).

> **NOTE:** This glossary was **seeded from existing labels** in the Georgian language pack and **still needs human review**. Verify all translations, especially terms marked "Verify against pack" or listed in Section 7.

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
| ACD | Automatic Call Distribution — the routing engine that assigns calls to agents | ავტომატური ზარის მიწოდება | `clage_agent_performance_acd_group` | |
| IVR | Interactive Voice Response — the automated voice menu | ინტერაქციული ავტომოპასუხე (IVR) | `aout_inforec` | Kept in English (IVR) as part of expanded form |
| DNIS | Dialed Number Identification Service — the number that was called | აკრეფილი ნომრის ამოსაცნობი მომსახურება (DNIS) | `cld_asterisk_dnis` | Kept in English (DNIS) as part of expanded form |
| DID | Direct Inward Dialing — a directly-reachable inbound number | DID/DNIS ხაზები | `fp_dnis_edit` (DID/DNIS Lines) | Kept in English (DID/DNIS) as part of label |
| CLID | Calling Line Identification — the caller's number / caller-ID | აბონენტის ნომერი | `carea_select_number_of_clid_digits_to_search` | |
| PBX | Private Branch Exchange — the phone system QueueMetrics monitors | PBX | `pgag_popup_cannot_send_message` | Kept in English |
| MOH | Music On Hold | ხმოვანი ლოდინის რეჟიმი | `cld_asterisk_mohdur` (MOH duration) | |
| AMO | Assisted Manual Outbound (Loway term) | AMO | `hdr_amo` | Kept in English |
| AGAW | Agent real-time monitoring module (QueueMetrics-specific term) | AGAW | `td_dbtest_wz_agawcleanup`, `edit_record_agawqueue_title` | Kept in English |

---

## 2. Metrics & KPI acronyms

| Term | English meaning / context | Translation | Example label(s) | Notes |
|------|---------------------------|-------------|------------------|-------|
| SLA | Service Level Agreement — % of calls answered within target time | SLA | `td_ancod_answered_calls_sla` | Kept in English |
| SPH | Sales per Hour | გაყიდვების რაოდენობა საათში | `aout_index_sph` | |
| CPH | Contacts per Hour | საათში ზარების რაოდენობა | `aout_cph` | |
| QCPH | Qualified Contacts per Hour | საათში დადასტურებული კონტაქტები | `aout_index_qcph` | |
| DOW | Day Of Week | კვირის დღეები | `cldst_ta_traffic_analysis_by_period_dow` | |

---

## 3. Quality / training / system acronyms

| Term | English meaning / context | Translation | Example label(s) | Notes |
|------|---------------------------|-------------|------------------|-------|
| QA | Quality Assurance (grading / scorecards) | ხარისხის შეფასება | `art_lblQAForm` (QA Form) | |
| QC | Quality Control | ხარისხის კონტროლი | `ko_succ_q` | |
| CBT | Computer-Based Training | ტრენინგი | `hdr_cbt` (CBTs) | |

---

## 4. Common UI abbreviations

Keep the translation **abbreviated** too — these sit in tight table headers and
menus. Match the source's truncation style (trailing `.`).

| Term | Full form | Translation | Example label(s) | Notes |
|------|-----------|-------------|------------------|-------|
| Avg. | Average | საშ. | `aout_avg_sec` | |
| Max. | Maximum | მაქ. | `cldst_ta_ag_max` | |
| Min. | Minimum | მინ. | (paired with Max.) | |
| Tot. | Total | სულ. | `aout_tot_sec` (Tot. Time) | |
| Num. | Number | რ. | `propedit_key_phone_maxsessions` | |
| Dur. | Duration | ხანგრძლივობა | `clage_acd_duration` | |
| Att. | Attempts | ცდ. | `hdr_attempts` | |
| Ans. | Answered | პასუხი | `cldst_ans` | |
| Unans. | Unanswered | პასუხგაუცემელი | `cldst_unans` | |
| Conv. | Conversation | საუბარი | `aout_ftrconv` (Ftr. Conv.) | |
| Qualif. | Qualified | დადასტურებული | `td_calloutc_qualif` | |
| Cont. | Contacts | კონტ. | `aout_contacts_n` | |
| Bill. | Billable | ანაზღაურებადი | `aout_billable_s` | |
| Succ. | Successful | წარმატებული | `ko_succ_q` (Succ.Q.) | Alien in pack (წარმატებული. Q.) |
| Short. | Short | მოკლე | `ko_sho_q` (Short.Q.) | Alien in pack (მოკლე. Q.) |
| Ag. | Agent | აგენტი | `cldst_ta_ag_max` (Max Ag.) | |
| Ext. | Extension | შიდა | `art_localExtension` | |
| Ref. | Reference | Ref. | `ccase_case_xref` (Ref. #) | Kept in English in pack |
| sec. | seconds | წ. | `rt3_duration` (Duration (sec.)) | |

---

## 5. Telephony domain terms (full words)

The high-frequency vocabulary of the product. Pick one translation per term and
keep it consistent everywhere.

| Term | English meaning / context | Translation | Example label(s) | Notes |
|------|---------------------------|-------------|------------------|-------|
| Agent | Operator who handles calls | აგენტი | `td_agstatus_agent_is_currently_logged_off` | |
| Queue | Call queue | რიგი | `td_ancod_answered_calls_agents_on_queue` | |
| Caller | The person calling in | აბონენტი | `td_cko_caller_abandon` | |
| Call (answered) | Answered call | პასუხგაცემული ზარი | `td_ancod_answered_calls_details` | |
| Unanswered / Lost call | Call that was not answered | პასუხგაუცემელი ზარი | `td_ancod_unanswered_calls_details`, `aout_fcr_detail_lost` | |
| Abandon(ed) | Caller hung up while waiting | შეწყვეტილი | `td_cko_abandon` | |
| Hangup | Call termination | გათიშვა | `aout_ivr_hangups` | |
| Wait time | Time spent queued before answer | დაყოვნების დრო | `edit_record_agawqueue_avgwait` | |
| Talk time | Time spent in conversation | საუბრის დრო | `qap_details_talk` | |
| Wrap-up | Post-call work time | დასრულების დრო | `td_autoconf_wz_queuewrapup` | |
| Pause | Agent paused / not taking calls | პაუზა | `td_agawlogon_paused` | |
| Session | An agent's logged-on period | სესია | `td_ancod_agent_sessions_detail` | |
| Inbound / Outbound | Call direction | შემომავალი / გამომავალი | `aout_*` (Outbound), `aout_inforec` | |
| Transfer | Passing a call to another party | გადაცემა | `td_callstatus_html_transferred` | |
| Spill | Overflow call routed onward | დამატებითი | `td_aglev_spill` | |
| Ringing | Phone is ringing | ზარი | `evt_ringing` | Verify against pack |
| Extension | Phone extension number | შიდა ნომერი | `art_localExtension` | |
| Skill | Agent skill / competency tag | უნარ-ჩვევა | `cldst_skills_per_day` | |
| Voicemail | Recorded message | ხმოვანი ფოსტა | `td_cko_timeout_voicemail` | |
| Recall | Scheduled call-back | განმეორებითი ზარის განრიგი | `art_lblWbRecallPanel` (Recall Scheduler) | |
| Supervisor | Agent overseer | ხელმძღვანელი | `edit_ac_supervisor` | |
| Spy / Barge / Whisper | Live-call monitoring actions | შემოჭრა / ჩურჩული | `rt3_actions_barge`, `rt3_actions_whisper` | Alien in pack |
| Billable | Time/activity that is billed | ანაზღაურებადი საქმიანობა | `aout_act_billable` | |
| Outcome | Result/disposition of a call | შედეგი | `aout_call_res_by_outcome` | |
| Disposition | Coded call result / rule | განთავსების წესი | `cdp_clonedispositions` | |
| Tag | Call tag / label | კატეგორია | `aout_calltag` | |
| Realtime | Live monitoring view | რეალური დრო | `art_active_polling_error` | Verify against pack |
| Wallboard | Large real-time status display | wallboard | `rt3_delete_current_wallboard_confirm` | Kept in English in pack |
| Alarm | Threshold alert | გაფრთხილება | `edit_record_agawqueue_title` (AGAW alarms) | |
| Threshold | Trigger value for alarms/SLA | ზღვრის მნიშვნელობა | `custrep_skills_valhrd` | |

---

## 6. General UI terms

Recurring application-chrome vocabulary. Worth fixing once for menu/button
consistency.

| Term | Context | Translation | Example label(s) | Notes |
|------|---------|-------------|------------------|-------|
| Report | Analysis output | ანგარიში | `aout_*`, report menus | |
| Edit / Add / Delete / Create | CRUD actions on forms | რედაქტირება / დამატება / წაშლა / შექმნა | `*_edit`, `*_add`, `*_delete` | |
| Export | Export to CSV/PDF/XLS | ექსპორტი | export buttons | |
| Configuration / Settings | Setup screens | კონფიგურაცია | `*configuration*`, `*settings*` | |
| Visibility | Access/visibility key | ხელმისაწვდომობა | visibility-key labels | Verify against pack |
| Group | Agent / report grouping | ჯგუფი | `clage_agent_performance_acd_group` | |
| Period | Time range of a report | პერიოდი | period selectors | |
| Status | Current state | მდგომარეობა | `td_agstatus_*` | |
| Details / Detail | Drill-down view | დეტალები | `td_ancod_answered_calls_details` | |
| Feature | Licensable capability | ფუნქცია | feature-key labels | |
| Password / User / Code | Login & identity fields | პაროლი / მომხმარებელი / კოდი | `td_autoconf_wz_agentpwd` | |

---

## 7. Doubts & items needing review

Per-language glossaries add rows here for any term whose translation is
uncertain or whose existing pack is inconsistent.

| Term | Issue | Seeded choice | Options to decide between |
|------|-------|---------------|---------------------------|
| Ringing | No pack reference found for this term concept | ზარი | ზარი / რეზინა / სიგნალი |
| Realtime | Reference uses full phrase in pack, not a standalone term | რეალური დრო | Verify if "რეალური დრო", "ტიპიური დრო", or other abbreviation is preferred |
| Visibility | Term used abstractly in spec; no direct pack label matches | ხელმისაწვდომობა | Verify this Georgian term against real pack usage |
| Ref. (abbreviation) | Pack keeps this as "Ref. #" in English | Ref. | Consider "Ref." in English or Georgian equivalent "მით." |
| Wallboard | Product feature term, pack keeps in English | wallboard | Decide if should keep English or translate to Georgian equivalent |
| IVR | Pack expands fully as "(IVR)" — verify abbreviation choice | IVR | Verify if abbreviation should stand alone or always include expansion |
| DNIS | Pack expands fully as "(DNIS)" — verify abbreviation choice | DNIS | Verify if abbreviation should stand alone or always include expansion |

