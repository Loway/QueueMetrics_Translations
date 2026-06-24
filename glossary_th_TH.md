# Glossary — QueueMetrics (th_TH)

> **Note:** This glossary was **seeded from existing labels** in the Thai language pack and still needs human review. Some terms may be inconsistent or marked as uncertain in section 7 below.

This is the **terminology master** for QueueMetrics in Thai. It collects the telephony
jargon, abbreviations and recurring UI terms that appear — often hundreds of
times — across [queuemetrics_th_TH.md](queuemetrics_th_TH.md).

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
| ACD | Automatic Call Distribution — the routing engine that assigns calls to agents | ACD | `clage_agent_performance_acd_group` | Kept in English |
| IVR | Interactive Voice Response — the automated voice menu | ระบบตอบรับอัตโนมัติ (IVR) | `aout_inforec` | Kept English acronym with Thai explanation |
| DNIS | Dialed Number Identification Service — the number that was called | หมายเลข Call center | `cld_asterisk_dnis` | Kept in English |
| DID | Direct Inward Dialing — a directly-reachable inbound number | DID/DNIS | `fp_dnis_edit` | Kept in English |
| CLID | Calling Line Identification — the caller's number / caller-ID | CLID | `carea_select_number_of_clid_digits_to_search` | Kept in English |
| PBX | Private Branch Exchange — the phone system QueueMetrics monitors | PBX | `pgag_popup_cannot_send_message` | Kept in English |
| MOH | Music On Hold | เสียงพักสาย | `cld_asterisk_mohdur` | Verify against pack |
| AMO | Assisted Manual Outbound (Loway term) | AMO | `hdr_amo` | Kept in English |
| AGAW | Agent real-time monitoring module (QueueMetrics-specific term) | AGAW | `td_dbtest_wz_agawcleanup`, `edit_record_agawqueue_title` | Kept in English |

---

## 2. Metrics & KPI acronyms

| Term | English meaning / context | Translation | Example label(s) | Notes |
|------|---------------------------|-------------|------------------|-------|
| SLA | Service Level Agreement — % of calls answered within target time | SLA | `td_ancod_answered_calls_sla` | Kept in English |
| SPH | Sales per Hour | ยอดขายต่อชั่วโมง (SPH) | `aout_index_sph` | Kept English acronym with Thai explanation |
| CPH | Contacts per Hour | จำนวนการโทรต่อชั่วโมง | `aout_cph` | Verify against pack |
| QCPH | Qualified Contacts per Hour | Contacts ที่ยืนยันรายชั่วโมง | `aout_index_qcph` | Verify against pack |
| DOW | Day Of Week | รายวันของสัปดาห์ | `cldst_ta_traffic_analysis_by_period_dow` | Verify against pack |

---

## 3. Quality / training / system acronyms

| Term | English meaning / context | Translation | Example label(s) | Notes |
|------|---------------------------|-------------|------------------|-------|
| QA | Quality Assurance (grading / scorecards) | QA | `art_lblQAForm` | Kept in English |
| QC | Quality Control | Q | `ko_succ_q` | Verify against pack |
| CBT | Computer-Based Training | CBT | `hdr_cbt` | Kept in English |
| Prompt | A prompt for an AI model to perform QA | Prompt | `edit_qa_prompt`, `edit_record_qa_aiprompt` | New AI term; kept in English — verify against pack |

---

## 4. Common UI abbreviations

Keep the translation **abbreviated** too — these sit in tight table headers and
menus. Match the source's truncation style (trailing `.`).

| Term | Full form | Translation | Example label(s) | Notes |
|------|-----------|-------------|------------------|-------|
| Avg. | Average | เฉลี่ย | `aout_avg_sec` | Abbreviated form |
| Max. | Maximum | มากสุด | `cldst_ta_ag_max` | Verify against pack |
| Min. | Minimum | น้อยสุด | (paired with Max.) | Verify against pack |
| Tot. | Total | เวลาทั้งหมด | `aout_tot_sec` | Inconsistent: found "เวลาทั้งหมด" |
| Num. | Number | จำนวน | `propedit_key_phone_maxsessions` | Verify against pack |
| Dur. | Duration | ระยะเวลา | `clage_acd_duration` | Abbreviated form |
| Att. | Attempts | การกระจายสาย | `hdr_attempts` | Verify against pack |
| Ans. | Answered | รับสาย | `cldst_ans` | Abbreviated form |
| Unans. | Unanswered | สายที่ไม่ได้รับ | `cldst_unans` | Inconsistent: found "สายที่ไม่ได้รับ" |
| Conv. | Conversation | Ftr. Conv. | `aout_ftrconv` | Kept in English form |
| Qualif. | Qualified | Qualif. | `td_calloutc_qualif` | Kept in English form |
| Cont. | Contacts | หมายเลขติดต่อ | `aout_contacts_n` | Inconsistent: found "หมายเลขติดต่อ" |
| Bill. | Billable | billable | `aout_billable_s` | Kept in English |
| Succ. | Successful | Succ.Q. | `ko_succ_q` | Kept in English form |
| Short. | Short | สั้น Q | `ko_sho_q` | Inconsistent: found "สั้น Q" |
| Ag. | Agent | Agent | `cldst_ta_ag_max` | Kept in English |
| Ext. | Extension | (Ext.) | `art_localExtension` | Kept in English |
| Ref. | Reference | อ้างอิง | `ccase_case_xref` | Abbreviated form |
| sec. | seconds | วิ. | `rt3_duration` | Abbreviated form |

---

## 5. Telephony domain terms (full words)

The high-frequency vocabulary of the product. Pick one translation per term and
keep it consistent everywhere.

| Term | English meaning / context | Translation | Example label(s) | Notes |
|------|---------------------------|-------------|------------------|-------|
| Agent | Operator who handles calls | ตัวแทน | `td_agstatus_agent_is_currently_logged_off` | Inconsistent: found both "ตัวแทน" and "agent" |
| Queue | Call queue | คิว | `td_ancod_answered_calls_agents_on_queue` | Kept mostly in English as "queue" |
| Caller | The person calling in | ผู้โทร | `td_cko_caller_abandon` | Standard Thai term |
| Call (answered) | Answered call | สายที่รับ | `td_ancod_answered_calls_details` | Verify against pack |
| Unanswered / Lost call | Call that was not answered | สายที่ไม่ได้รับ | `td_ancod_unanswered_calls_details`, `aout_fcr_detail_lost` | Standard Thai term |
| Abandon(ed) | Caller hung up while waiting | ละทิ้ง | `td_cko_abandon` | Verify against pack |
| Hangup | Call termination | วางสาย | `aout_ivr_hangups` | Standard Thai term |
| Wait time | Time spent queued before answer | เวลารอสาย | `edit_record_agawqueue_avgwait` | Verify against pack |
| Talk time | Time spent in conversation | เวลาคุยสาย | `qap_details_talk` | Verify against pack |
| Wrap-up | Post-call work time | เวลาพักสาย | `td_autoconf_wz_queuewrapup` | Verify against pack |
| Pause | Agent paused / not taking calls | พักรับสาย | `td_agawlogon_paused` | Standard Thai term |
| Session | An agent's logged-on period | ช่วงเวลา (เซสชัน) | `td_ancod_agent_sessions_detail` | Verify against pack |
| Inbound / Outbound | Call direction | สายเรียกเข้า / สายโทรออก | `aout_*`, `td_qdir_inbound_calls` | Standard Thai terms |
| Transfer | Passing a call to another party | โอนสาย | `td_callstatus_html_transferred` | Standard Thai term |
| Spill | Overflow call routed onward | สำรอง | `td_aglev_spill` | Verify against pack |
| Ringing | Phone is ringing | Ringing | `evt_ringing` | Kept in English |
| Extension | Phone extension number | หมายเลขภายใน (Ext.) | `art_localExtension` | Keep with English abbr |
| Skill | Agent skill / competency tag | Skills | `cldst_skills_per_day` | Kept in English |
| Voicemail | Recorded message | ข้อความเสียง | `td_cko_timeout_voicemail` | Verify against pack |
| Recall | Scheduled call-back | โทรซ้ำ | `art_lblWbRecallPanel` | Standard Thai term |
| Supervisor | Agent overseer | Supervisor | `edit_ac_supervisor` | Kept in English |
| Spy / Barge / Whisper | Live-call monitoring actions | ประชุม 3 สาย / คุยกับ agent | `rt3_actions_barge`, `rt3_actions_whisper` | Mixed: some kept English |
| Billable | Time/activity that is billed | billable | `aout_act_billable` | Kept in English |
| Outcome | Result/disposition of a call | ผลลัพธ์ (outcome) | `aout_call_res_by_outcome` | Inconsistent: mixed Thai and English |
| Disposition | Coded call result / rule | Disposition Rules | `cdp_clonedispositions` | Kept in English |
| Tag | Call tag / label | Tag | `aout_calltag` | Kept in English |
| Realtime | Live monitoring view | realtime | `art_active_polling_error` | Kept in English |
| Wallboard | Large real-time status display | Wallboard | `rt3_delete_current_wallboard_confirm` | Kept in English |
| Alarm | Threshold alert | สัญญาณเตือน | `edit_record_agawqueue_title` | Verify against pack |
| Threshold | Trigger value for alarms/SLA | Threshold | `custrep_skills_valhrd` | Kept in English |

---

## 6. General UI terms

Recurring application-chrome vocabulary. Worth fixing once for menu/button
consistency.

| Term | Context | Translation | Example label(s) | Notes |
|------|---------|-------------|------------------|-------|
| Report | Analysis output | Report | `aout_*`, report menus | Kept in English |
| Edit / Add / Delete / Create | CRUD actions on forms | แก้ไข / เพิ่ม / ลบ / สร้าง | `*_edit`, `*_add`, `*_delete` | Mix of Thai and English |
| Export | Export to CSV/PDF/XLS | Export | export buttons | Kept in English |
| Configuration / Settings | Setup screens | การกำหนดค่า | `*configuration*`, `*settings*` | Thai term used |
| Visibility | Access/visibility key | Visibility | visibility-key labels | Verify against pack |
| Group | Agent / report grouping | กลุ่ม | `clage_agent_performance_acd_group` | Verify against pack |
| Period | Time range of a report | ระยะเวลา | period selectors | Verify against pack |
| Status | Current state | สถานะ | `td_agstatus_*` | Verify against pack |
| Details / Detail | Drill-down view | รายละเอียด | `td_ancod_answered_calls_details` | Standard Thai term |
| Feature | Licensable capability | Feature | feature-key labels | Kept in English |
| Password / User / Code | Login & identity fields | รหัสผ่าน / User / รหัส | `td_autoconf_wz_agentpwd` | Mixed translation |

---

## 7. Doubts & items needing review

| Term | Issue | Seeded choice | Options to decide between |
|------|-------|---------------|---------------------------|
| MOH | No value found in example; standard term needed | เสียงพักสาย | "เสียงพักสาย" vs. "เพลงรอ" vs. keep "MOH" |
| CPH | Inconsistent or partial translation in pack | จำนวนการโทรต่อชั่วโมง | "จำนวนการโทรต่อชั่วโมง" vs. "Contacts ต่อชั่วโมง" vs. keep "CPH" |
| QCPH | Inconsistent or partial translation in pack | Contacts ที่ยืนยันรายชั่วโมง | Keep as-is vs. simplify to "โอกาส ที่ยืนยัน/ชั่วโมง" |
| DOW | Incomplete translation found | รายวันของสัปดาห์ | "รายวันของสัปดาห์" vs. "วันในสัปดาห์" |
| QC | Uncertain abbreviation found | Q | "Q" vs. "QC" vs. "ควบคุมคุณภาพ" |
| Max./Min. | Found "มากสุด" but Min. not explicitly found | มากสุด / น้อยสุด | Verify both forms consistent |
| Tot. | Multiple renderings found (เวลาทั้งหมด) | เวลาทั้งหมด | "เวลาทั้งหมด" (verbose) vs. "รวม" (short) |
| Num. | No explicit value found | จำนวน | "จำนวน" vs. "หมายเลข" vs. "เลข" |
| Att. | Found "การกระจายสาย" which may not match Attempts | การกระจายสาย | Verify or choose "ความพยายาม" vs. "จำนวนครั้ง" |
| Unans. | Long form found; should abbreviate | สายที่ไม่ได้รับ | "สายที่ไม่ได้รับ" (verbose) vs. "ไม่รับ" (abbreviated) |
| Conv. | Kept English form in pack | Ftr. Conv. | Keep "Ftr. Conv." vs. "บทสนทนา" |
| Qualif. | Kept English form in pack | Qualif. | Keep "Qualif." vs. "คุณสมบัติ" |
| Cont. | Inconsistent form found | หมายเลขติดต่อ | "หมายเลขติดต่อ" (verbose) vs. "ติดต่อ" |
| Short. | Mixed form found | สั้น Q | Keep "สั้น Q" vs. "Short.Q" vs. standardize |
| Agent | Multiple renderings (ตัวแทน vs. agent) | ตัวแทน | Use "ตัวแทน" consistently vs. allow "agent" fallback |
| Queue | Mostly kept English | คิว | "คิว" (Thai) vs. allow "queue" fallback |
| Call (answered) | Incomplete verification | สายที่รับ | "สายที่รับ" vs. "สายตอบรับ" vs. "สายเข้า" |
| Wait time | Pack uses "เวลาการรอเฉลี่ย" | เวลารอสาย | "เวลารอสาย" vs. "เวลาการรอเฉลี่ย" (verbose) |
| Talk time | Pack uses "เวลาสนทนา" | เวลาคุยสาย | "เวลาคุยสาย" vs. "เวลาสนทนา" vs. "เวลาพูด" |
| Wrap-up | Pack uses "เวลาพักสาย" | เวลาพักสาย | Confirm standard vs. "เวลากิจกรรมหลังสาย" |
| Session | Found with Thai/English mix | ช่วงเวลา (เซสชัน) | Standardize to "เซสชัน" vs. "ช่วงเวลา" vs. "ช่วงการเข้าสู่ระบบ" |
| Ringing | Kept English in pack | Ringing | Keep "Ringing" vs. "เรียกเข้า" vs. "โทรเข้า" |
| Skill | Kept English in pack | Skills | Keep "Skills" vs. "ทักษะ" |
| Outcome | Mixed Thai/English found | ผลลัพธ์ (outcome) | "ผลลัพธ์" (Thai) vs. keep "outcome" |
| Disposition | Kept English in pack | Disposition Rules | Keep "Disposition" vs. "การจัดประเภท" |
| Tag | Kept English in pack | Tag | Keep "Tag" vs. "ป้ายกำกับ" vs. "มาร์กเกอร์" |
| Realtime | Kept English in pack | realtime | Keep "realtime" vs. "เรียลไทม์" vs. "สดใจ" |
| Wallboard | Kept English in pack | Wallboard | Keep "Wallboard" vs. "กระดานข้อมูล" |
| Alarm | Found "สัญญาณเตือน" | สัญญาณเตือน | Verify "สัญญาณเตือน" vs. "สัญญาณแจ้งเตือน" |
| Threshold | Kept English in pack | Threshold | Keep "Threshold" vs. "เกณฑ์" vs. "ระดับเตือน" |
| Report | Kept English in pack | Report | Keep "Report" vs. "รายงาน" |
| Export | Kept English in pack | Export | Keep "Export" vs. "ส่งออก" |
| Edit/Add/Delete | Mix of Thai and English | แก้ไข / เพิ่ม / ลบ | Verify consistent use across all labels |
| Password/User/Code | Mixed translations | รหัสผ่าน | Standardize User and Code terms |
