# Glossary — QueueMetrics (ru_RU)

Russian terminology master for QueueMetrics. Derived from
[glossary_en_US.md](glossary_en_US.md); see that file and
[CLAUDE.md](CLAUDE.md) for how the glossary is used.

> **Seeded from existing labels.** The **Translation** column was pre-filled with
> the terms **already in use** in [queuemetrics_ru_RU.md](queuemetrics_ru_RU.md)
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
| ACD | Automatic Call Distribution | ACD | `clage_agent_performance_acd_group` | Kept as acronym |
| IVR | Interactive Voice Response | IVR | `aout_inforec` | Kept as acronym |
| DNIS | Dialed Number Identification Service | DNIS | `cld_asterisk_dnis` | Kept as acronym |
| DID | Direct Inward Dialing | DID | `fp_dnis_edit` | Kept as acronym |
| CLID | Calling Line Identification | Номер абонента | `carea_select_number_of_clid_digits_to_search` | |
| PBX | Private Branch Exchange | PBX | `pgag_popup_cannot_send_message` | Kept in English |
| MOH | Music On Hold | MOH | `cld_asterisk_mohdur` | Kept as acronym |
| AMO | Assisted Manual Outbound | AMO | `hdr_amo` | Kept (Loway term) |
| AGAW | Agent real-time monitoring module | AGAW | `td_dbtest_wz_agawcleanup` | Kept (QueueMetrics term) |

---

## 2. Metrics & KPI acronyms

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| SLA | Service Level Agreement | SLA | `td_ancod_answered_calls_sla` | Kept in English |
| SPH | Sales per Hour | SPH | `aout_index_sph` | Kept as acronym |
| CPH | Contacts per Hour | Вызовы в час (выз/ч) | `aout_cph` | Pack expands it |
| QCPH | Qualified Contacts per Hour | Подтверждённые контакты в час (Пк/ч) | `aout_index_qcph` | Pack expands it |
| DOW | Day Of Week | День недели | `cldst_ta_traffic_analysis_by_period_dow` | Verify against pack |

---

## 3. Quality / training / system acronyms

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| QA | Quality Assurance | QA | `art_lblQAForm` | Kept as acronym |
| QC | Quality Control | QC | `ko_succ_q` | Kept as acronym |
| CBT | Computer-Based Training | Тренинг | `hdr_cbt` | Kept in English |
| Prompt | A prompt for an AI model to perform QA | Промпт | `edit_qa_prompt`, `edit_record_qa_aiprompt` | New AI term — verify against pack |

---

## 4. Common UI abbreviations

Keep the Russian abbreviated too (tight headers/menus).

| Term | Full form | Translation | Example label(s) | Notes |
|------|-----------|-------------|------------------|-------|
| Avg. | Average | Средн. | `aout_avg_sec` | |
| Max. | Maximum | Макс. | `cldst_ta_ag_max` | |
| Min. | Minimum | Мин. | `aout_min_sec` | |
| Tot. | Total | Суммарное | `aout_tot_sec` | Pack uses full form *Суммарное время* |
| Num. | Number | Кол-во | `aout_fcr_n_calls` | |
| Dur. | Duration | Продолж. | `clage_acd_duration` | |
| Att. | Attempts | Попытки | `hdr_attempts` | Pack uses full form |
| Ans. | Answered | Отв. | `cldst_ans` | |
| Unans. | Unanswered | Неотв. | `cldst_unans` | |
| Conv. | Conversation | Особ. разг. | `aout_ftrconv` | |
| Qualif. | Qualified | Неполный | `td_calloutc_qualif` | Verify — seeded value seems to mean "incomplete" |
| Cont. | Contacts | Контакт | `aout_contacts_n` | |
| Bill. | Billable | Оплачиваемо | `aout_billable_s` | |
| Succ. | Successful | Успешные в очереди | `ko_succ_q` | Pack uses full phrase |
| Short. | Short | Короткие в очереди | `ko_sho_q` | Pack uses full phrase |
| Ag. | Agent | Агентов | `cldst_ta_ag_max` | Verify short form |
| Ext. | Extension | Внутр. | `art_localExtension` | |
| Ref. | Reference | № ссылки | `ccase_case_xref` | |
| sec. | seconds | Продолжительность | `rt3_duration` | Verify — seeded value seems broader |

---

## 5. Telephony domain terms (full words)

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| Agent | Operator | Агент | `td_agstatus_agent_is_currently_logged_off` | |
| Queue | Call queue | Очередь | `td_ancod_answered_calls_agents_on_queue` | |
| Caller | Person calling in | Абонент | `td_cko_caller_abandon` | |
| Call (answered) | Answered call | Отвеченные вызовы | `td_ancod_answered_calls_details` | |
| Unanswered / Lost | Not answered | Неотвеченные вызовы | `td_ancod_unanswered_calls_details` | |
| Abandon(ed) | Caller hung up while queued | Отказы | `td_cko_abandon` | |
| Hangup | Call termination | Разъединения | `aout_ivr_hangups` | |
| Wait time | Queue time before answer | Среднее время ожидания | `edit_record_agawqueue_avgwait` | |
| Talk time | Conversation time | Время разговора | `qap_details_talk` | Marked as alien (?) in pack |
| Wrap-up | Post-call work time | Время завершения | `td_autoconf_wz_queuewrapup` | |
| Pause | Agent not taking calls | Пауза | `td_agawlogon_paused` | |
| Session | Logged-on period | Сессии агента | `td_ancod_agent_sessions_detail` | |
| Inbound / Outbound | Call direction | Входящий / Исходящий | `aout_inforec` | Verify against pack |
| Transfer | Pass call onward | Переведенные | `td_callstatus_html_transferred` | |
| Spill | Overflow call | Дополнительный | `td_aglev_spill` | |
| Ringing | Phone ringing | Звонок | `evt_ringing` | |
| Extension | Phone extension | Внутренний номер | `art_localExtension` | |
| Skill | Agent competency | Квалификации | `cldst_skills_per_day` | |
| Voicemail | Recorded message | Голосовая почта | `td_cko_timeout_voicemail` | |
| Recall | Scheduled call-back | Повторный вызов расписания | `art_lblWbRecallPanel` | |
| Supervisor | Agent overseer | Супервайзер | `edit_ac_supervisor` | |
| Barge / Whisper / Spy | Live-call monitoring | Barge / Шепот / (Spy unconfirmed) | `rt3_actions_barge`, `rt3_actions_whisper` | Barge kept English; Whisper = Шепот |
| Billable | Billed time/activity | Оплачиваемая деятельность | `aout_act_billable` | |
| Outcome | Call result | Итоги звонков, по результатам | `aout_call_res_by_outcome` | |
| Disposition | Coded result / rule | Клонировать правила размещения | `cdp_clonedispositions` | Verify — seeded value refers to an action |
| Tag | Call tag | Тэг | `aout_calltag` | |
| Realtime | Live view | Real-time | `art_active_polling_error` | Kept English; verify |
| Wallboard | Real-time display | Табло | `rt3_delete_current_wallboard_confirm` | |
| Alarm | Threshold alert | Оповещения AGAW | `edit_record_agawqueue_title` | |
| Threshold | Trigger value | Пороговое значение | `custrep_skills_valhrd` | |

---

## 6. General UI terms

| Term | Context | Translation | Example label(s) | Notes |
|------|---------|-------------|------------------|-------|
| Report | Analysis output | Отчёт / Детализированный отчёт | `aout_agent_report` | |
| Edit / Add / Delete / Create | CRUD actions | Редактировать / Добавить / Удалить / Создать | `edit_amo_numbers_edit`, `td_imwiz_added_agent`, `edit_record_delete` | |
| Export | Export to file | Выгрузить | `cld_btn_export_calls` | |
| Configuration / Settings | Setup screens | Конфигурация | `td_synchronier_configuration` | |
| Visibility | Access/visibility key | Видимость | `edit_record_export_visibility` | |
| Group | Grouping | Группа | `clage_agent_performance_acd_group` | |
| Period | Report time range | Период времени | `custrep_time_period` | |
| Status | Current state | Состояние | `td_agstatus_agent_status_cannot_be_determined` | |
| Details / Detail | Drill-down view | Детали | `td_ancod_answered_calls_details` | |
| Feature | Licensable capability | Код | `aout_feature` | Verify — pack uses "Код" which may mean something else |
| Password / User / Code | Login & identity | Пароль / Пользователь / Код | `td_autoconf_wz_agentpwd`, `td_autoconf_wz_users`, `aout_feature` | |

---

## 7. Doubts & items needing review

Terms where the seeded value is uncertain or the existing pack is inconsistent.
Resolve each, then update the table above and remove the row here.

| Term | Issue | Seeded choice | Options to decide between |
|------|-------|---------------|---------------------------|
| CPH / QCPH | Pack expands acronyms instead of using short form | *Вызовы в час (выз/ч)* / *Подтверждённые контакты в час (Пк/ч)* | Use short acronyms, or keep expanded form for consistency with pack |
| DOW | Not confirmed in pack | *День недели* | Verify the exact wording used |
| CBT | Pack keeps English | *Тренинг* (vs English) | Keep English acronym or use *Тренинг* |
| Qualif. | Seeded value seems to mean "incomplete" | *Неполный* | Verify actual meaning in pack — should mean "Qualified" |
| Tot. | Pack uses full form | *Суммарное время* | Keep full or abbreviate to *Сум.* |
| Att. | Pack uses full form | *Попытки* | Keep full or abbreviate to *Попыт.* |
| Ag. | Seeded value is plural "agents" | *Агентов* | Should be singular *Агент* or abbreviated *Аг.* |
| sec. | Seeded value is too broad | *Продолжительность* | Should be abbreviated or phrase as *(сек.)* |
| Inbound / Outbound | Not confirmed from pack | *Входящий / Исходящий* | Verify against pack's actual usage |
| Disposition | Seeded value is an action | *Клонировать правила размещения* | Should be a noun; verify actual term |
| Feature | Seeded value may be wrong | *Код* | Verify that "Код" is correct; may need different term |
| Realtime | Pack keeps English | *Real-time* | Keep English or translate to *Режим реального времени* |
| Transfer | Seeded from past tense | *Переведенные* | Should be infinitive or noun; verify correct form |
| Spill | Seeded value unclear | *Дополнительный* | Verify actual meaning; should refer to overflow |
