# Glossary — QueueMetrics (ar_SA)

Arabic terminology master for QueueMetrics. Derived from
[glossary_en_US.md](glossary_en_US.md); see that file and
[CLAUDE.md](CLAUDE.md) for how the glossary is used.

> **Seeded from existing labels.** The **Translation** column was pre-filled with
> the terms **already in use** in [queuemetrics_ar_SA.md](queuemetrics_ar_SA.md)
> (the *Example label(s)* keys were looked up there), so this glossary matches the
> current pack. Review and lock each choice; where the existing pack was
> inconsistent or kept the English term, that is flagged in **Notes**.

---

## 0. Do-not-translate terms

Leave unaltered (product names, protocols, file formats): **QueueMetrics**,
**WombatDialer**, **Teams** (MS Teams), **CSV, JSON, XML, HTML, PDF, XLS**,
**SIP, AMI, HTTP(S), SMTP, RPC, API, URL, VNC, SSO, ICE**.

---

## 1. Telephony & call-center acronyms

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| ACD | Automatic Call Distribution | ACD | `clage_agent_performance_acd_group` | Kept in English |
| IVR | Interactive Voice Response | الرد الآلي | `aout_inforec` | |
| DNIS | Dialed Number Identification Service | الرقم المستخدم | `cld_asterisk_dnis` | |
| DID | Direct Inward Dialing | DID | `fp_dnis_edit` | Kept in English; label says "DID / خطوط DNIS" |
| CLID | Calling Line Identification | رقم المتصل | `carea_select_number_of_clid_digits_to_search` | |
| PBX | Private Branch Exchange | PBX | `pgag_popup_cannot_send_message` | Kept in English |
| MOH | Music On Hold | موسيقى الانتظار | `cld_asterisk_mohdur` | |
| AMO | Assisted Manual Outbound | AMO | `hdr_amo` | Kept (Loway term) |
| AGAW | Agent real-time monitoring module | AGAW | `edit_record_agawqueue_title` | Kept (QueueMetrics term) |

---

## 2. Metrics & KPI acronyms

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| SLA | Service Level Agreement | اتفاقية مستوى الخدمة | `td_ancod_answered_calls_sla` | |
| SPH | Sales per Hour | المبيعات في الساعة | `aout_index_sph` | |
| CPH | Contacts per Hour | عدد الاتصالات في الساعة | `aout_cph` | |
| QCPH | Qualified Contacts per Hour | المتصلين المؤهلين في الساعة | `aout_index_qcph` | |
| DOW | Day Of Week | تحليل حركة المعلومات | `cldst_ta_traffic_analysis_by_period_dow` | Full phrase used in context |

---

## 3. Quality / training / system acronyms

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| QA | Quality Assurance | نموذج ضمان الجودة | `art_lblQAForm` | |
| QC | Quality Control | ناجح.ق. | `ko_succ_q` | Abbreviated form from pack |
| CBT | Computer-Based Training | CBTs | `hdr_cbt` | Kept in English |

---

## 4. Common UI abbreviations

Keep the Arabic abbreviated too (tight headers/menus).

| Term | Full form | Translation | Example label(s) | Notes |
|------|-----------|-------------|------------------|-------|
| Avg. | Average | متوسط | `aout_avg_sec` | |
| Max. | Maximum | أقصى حد | `cldst_ta_ag_max` | |
| Min. | Minimum | أدنى حد | `cldst_ta_ag_min` | |
| Tot. | Total | إجمالي | `aout_tot_sec` | Full phrase used: *إجمالي الوقت (بالثانية)* |
| Num. | Number | رقم | `propedit_key_phone_maxsessions` | |
| Dur. | Duration | المدة | `clage_acd_duration` | |
| Att. | Attempts | محاولات | `hdr_attempts` | Full form used; consider *محاول.* in tight headers |
| Ans. | Answered | مستلمة | `cldst_ans` | |
| Unans. | Unanswered | فائتة | `cldst_unans` | |
| Conv. | Conversation | خاصية المحادثة | `aout_ftrconv` | Existing pack uses fuller phrase |
| Qualif. | Qualified | المؤهلات | `td_calloutc_qualif` | Full form used |
| Cont. | Contacts | سجل اتصال | `aout_contacts_n` | Full form used |
| Bill. | Billable | الفاتورة | `aout_billable_s` | |
| Succ. | Successful | ناجح.ق. | `ko_succ_q` | Abbreviated with period and context marker |
| Short. | Short | قصير.ق. | `ko_sho_q` | Abbreviated with period and context marker |
| Ag. | Agent | أقصى حد للوكلاء | `cldst_ta_ag_max` | Full phrase used in context |
| Ext. | Extension | الرقم الداخلي | `art_localExtension` | |
| Ref. | Reference | رقم المرجع | `ccase_case_xref` | Marked alien in pack |
| sec. | seconds | مدة (بالثانية) | `rt3_duration` | |

---

## 5. Telephony domain terms (full words)

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| Agent | Operator | وكيل | `td_agstatus_agent_is_currently_logged_off` | Pack shows "اتم تسجيل دخول" (logged off context) |
| Queue | Call queue | صف | `td_ancod_answered_calls_agents_on_queue` | |
| Caller | Person calling in | متصل | `td_cko_caller_abandon` | Pack shows "المتصل" (the caller) |
| Call (answered) | Answered call | المكالمات المجابة | `td_ancod_answered_calls_details` | |
| Unanswered / Lost | Not answered | المكالمات التي لم يرد عليها | `td_ancod_unanswered_calls_details`, `aout_fcr_detail_lost` | Pack also uses "مفقودة" (lost) — pick one |
| Abandon(ed) | Caller hung up while queued | تخلى | `td_cko_abandon` | |
| Hangup | Call termination | إغلاق الخط | `aout_ivr_hangups` | |
| Wait time | Queue time before answer | متوسط وقت الانتظار | `edit_record_agawqueue_avgwait` | Full phrase used |
| Talk time | Conversation time | وقت التحدث | `qap_details_talk` | Marked alien in pack |
| Wrap-up | Post-call work time | فترة استراحة | `td_autoconf_wz_queuewrapup` | |
| Pause | Agent not taking calls | متوقف مؤقتاً | `td_agawlogon_paused` | |
| Session | Logged-on period | جلسات عمل الوكيل | `td_ancod_agent_sessions_detail` | Full phrase used |
| Inbound / Outbound | Call direction | — | `aout_*` | Not confirmed — verify terminology in pack |
| Transfer | Pass call onward | تحويل | `td_callstatus_html_transferred` | |
| Spill | Overflow call | تسرب | `td_aglev_spill` | |
| Ringing | Phone ringing | رنين | `evt_ringing` | |
| Extension | Phone extension | الرقم الداخلي | `art_localExtension` | |
| Skill | Agent competency | المهارات | `cldst_skills_per_day` | |
| Voicemail | Recorded message | البريد الصوتي | `td_cko_timeout_voicemail` | |
| Recall | Scheduled call-back | استعادة الجدولة | `art_lblWbRecallPanel` | |
| Supervisor | Agent overseer | المشرف | `edit_ac_supervisor` | |
| Barge / Whisper / Spy | Live-call monitoring | تدخل / همس / — | `rt3_actions_barge`, `rt3_actions_whisper` | "Spy" not confirmed in pack |
| Billable | Billed time/activity | أنشطة مفوترة | `aout_act_billable` | |
| Outcome | Call result | نتائج المكالمة | `aout_call_res_by_outcome` | Full phrase used |
| Disposition | Coded result / rule | نسخ القواعد النهائية للمكالمة | `cdp_clonedispositions` | Full phrase in pack |
| Tag | Call tag | بطاقة | `aout_calltag` | |
| Realtime | Live view | ليس مضبوطاً على قيمة صحيحة | `art_active_polling_error` | Status message used; verify actual term |
| Wallboard | Real-time display | شاشة المراقبة | `rt3_delete_current_wallboard_confirm` | Full phrase used |
| Alarm | Threshold alert | تحذيرات AGAW | `edit_record_agawqueue_title` | |
| Threshold | Trigger value | عتبة | `custrep_skills_valhrd` | |

---

## 6. General UI terms

| Term | Context | Translation | Example label(s) | Notes |
|------|---------|-------------|------------------|-------|
| Report | Analysis output | تقرير | `aout_agent_report` | |
| Edit / Add / Delete / Create | CRUD actions | تعديل / إضافة / حذف / — | `rt3_edit`, `rt3_add`, `edit_record_delete` | "Create" not confirmed |
| Export | Export to file | تصدير | `cld_btn_export_calls` | |
| Configuration / Settings | Setup screens | اعدادات | `td_synchronier_configuration` | |
| Visibility | Access/visibility key | — | visibility-key labels | Not confirmed in pack — verify |
| Group | Grouping | مجموعة | `edit_ac_group` | |
| Period | Report time range | مدة | `edit_exports_period` | |
| Status | Current state | — | `td_agstatus_*` | Not confirmed — verify |
| Details / Detail | Drill-down view | تفاصيل | `td_ancod_answered_calls_details` | |
| Feature | Licensable capability | خاصية | `aout_feature` | |
| Password / User / Code | Login & identity | كود / مستخدم / — | `edit_ac_agent_code`, `td_autoconf_wz_users` | "Password" not confirmed |

---

## 7. Doubts & items needing review

Terms where the seeded value is uncertain or the existing pack is inconsistent.
Resolve each, then update the table above and remove the row here.

| Term | Issue | Seeded choice | Options to decide between |
|------|-------|---------------|---------------------------|
| IVR (Interactive Voice Response) | Possible alternate phrasing | الرد الآلي | الرد الآلي vs Serveur Vocal Interactif — verify standard Arabic tech term |
| Unanswered | Pack uses multiple forms | المكالمات التي لم يرد عليها | المكالمات التي لم يرد عليها vs مكالمات غير مجابة vs فائتة |
| Att. (Attempts) | Full form used, no abbreviation in pack | محاولات | Keep full form or shorten to محاول. for tight headers |
| Inbound / Outbound | Not confirmed from a pack label | — | Need to find explicit labels using these terms or provide standard forms |
| Status | Not confirmed from a pack label | — | Need to find how pack renders "current state" or "status" |
| Spy (monitoring action) | Not confirmed in pack | — | Need to verify if pack translates this or keeps English |
| Visibility (access level) | Not confirmed from a pack label | — | Need to find visibility-key labels in pack |
| Password | Not confirmed from a pack label | — | Need to find login/password field labels in pack |
| Realtime (live view) | No clear confirmation | — | Pack fragment suggests complex phrasing — need context from actual labels |
| DID acronym | Kept English in DID/DNIS line | DID | Consider translating to Arabic equivalent or standard term |
| Create (CRUD action) | Not confirmed | — | Need to find "Create" or equivalent action in pack |
