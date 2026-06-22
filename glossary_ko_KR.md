# Glossary — QueueMetrics (ko_KR)

Korean terminology master for QueueMetrics. Derived from
[glossary_en_US.md](glossary_en_US.md); see that file and
[CLAUDE.md](CLAUDE.md) for how the glossary is used.

> **Seeded from existing labels.** The **Translation** column was pre-filled with
> the terms **already in use** in [queuemetrics_ko_KR.md](queuemetrics_ko_KR.md)
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
| ACD | Automatic Call Distribution | ACD | `clage_agent_performance_acd_group` | Kept; pack phrases as *ACD그룹별* |
| IVR | Interactive Voice Response | IVR | `aout_inforec` | Kept in English |
| DNIS | Dialed Number Identification Service | DNIS | `cld_asterisk_dnis` | Kept in English |
| DID | Direct Inward Dialing | DID/DNIS Lines | `fp_dnis_edit` | Kept; rendered as *DID/DNIS Lines* |
| CLID | Calling Line Identification | 전화번호 | `carea_select_number_of_clid_digits_to_search` | Translated in context |
| PBX | Private Branch Exchange | 교환기 | `pgag_popup_cannot_send_message` | Context reference to 교환기 |
| MOH | Music On Hold | MOH 경과시간 | `cld_asterisk_mohdur` | Kept in English (duration context) |
| AMO | Assisted Manual Outbound | AMO | `hdr_amo` | Kept (Loway term) |
| AGAW | Agent real-time monitoring module | AGAW | `edit_record_agawqueue_title` | Kept (QueueMetrics term) |

---

## 2. Metrics & KPI acronyms

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| SLA | Service Level Agreement | SLA | `td_ancod_answered_calls_sla` | Kept in English |
| SPH | Sales per Hour | SPH | `aout_index_sph` | Kept; expanded as *시간당 Sales(SPH)* in context |
| CPH | Contacts per Hour | CPH | `aout_cph` | Kept in English |
| QCPH | Qualified Contacts per Hour | QCPH | `aout_index_qcph` | Kept; expanded as *시간당 Qualified Contacts (QCPH)* |
| DOW | Day Of Week | 요일 | `cldst_ta_traffic_analysis_by_period_dow` | Translated in context as 요일별 |

---

## 3. Quality / training / system acronyms

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| QA | Quality Assurance | QA 양식 | `art_lblQAForm` | Kept acronym; expanded as *QA 양식* in context |
| QC | Quality Control | QC | `ko_succ_q` | Kept in English (abbreviation context) |
| CBT | Computer-Based Training | CBTs | `hdr_cbt` | Kept in English |

---

## 4. Common UI abbreviations

Keep Korean abbreviated too (tight headers/menus).

| Term | Full form | Translation | Example label(s) | Notes |
|------|-----------|-------------|------------------|-------|
| Avg. | Average | 평균 | `aout_avg_sec` | |
| Max. | Maximum | 최대 | `cldst_ta_ag_max` | Rendered as *최대 상담원* |
| Min. | Minimum | 최소 | `aout_min_sec` | |
| Tot. | Total | 총 시간 | `aout_tot_sec` | Rendered as *총 시간* in context |
| Num. | Number | Num. | `propedit_key_phone_maxsessions` | Kept (no dedicated abbrev. found) |
| Dur. | Duration | Dur. | `clage_acd_duration` | Kept in English |
| Att. | Attempts | 시도호 | `hdr_attempts` | Rendered as *콜시도* and *시도호 별* in context |
| Ans. | Answered | 응답 | `cldst_ans` | |
| Unans. | Unanswered | 미수신 | `cldst_unans` | |
| Conv. | Conversation | For. Conv. | `aout_ftrconv` | Kept as *For. Conv.* |
| Qualif. | Qualified | Qualif. | `td_calloutc_qualif` | Kept in English |
| Cont. | Contacts | Cont. | `aout_contacts_n` | Kept in English |
| Bill. | Billable | 과금 | `aout_billable_s` | Translated in context |
| Succ. | Successful | Succ.Q. | `ko_succ_q` | Kept; rendered as *Succ.Q.* |
| Short. | Short | Short.Q. | `ko_sho_q` | Kept; rendered as *Short.Q.* |
| Ag. | Agent | 상담원 | `cldst_ta_ag_max` | Rendered as *최대 상담원* |
| Ext. | Extension | 내선 | `art_localExtension` | |
| Ref. | Reference | Ref.NO | `ccase_case_xref` | Rendered as *Ref.NO* |
| sec. | seconds | 초 | `rt3_duration` | Rendered as *Duration (초)* |

---

## 5. Telephony domain terms (full words)

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| Agent | Operator | 상담원 | `td_agstatus_agent_is_currently_logged_off` | |
| Queue | Call queue | 대기큐 | `td_ancod_answered_calls_agents_on_queue` | Rendered with context *대기큐(Queue)* |
| Caller | Person calling in | Caller | `td_cko_caller_abandon` | Kept in English |
| Call (answered) | Answered call | 응대콜 | `td_ancod_answered_calls_details` | Rendered as *응대콜 : 상세정보* |
| Unanswered / Lost | Not answered | 미응대콜 | `td_ancod_unanswered_calls_details` | Rendered as *미응대콜* |
| Abandon(ed) | Caller hung up while queued | Abandon | `td_cko_abandon` | Kept in English |
| Hangup | Call termination | Hangups | `aout_ivr_hangups` | Kept in English |
| Wait time | Queue time before answer | 대기시간 | `edit_record_agawqueue_avgwait` | Rendered as *평균 대기시간* |
| Talk time | Conversation time | 통화 시간 | `qap_details_talk` | |
| Wrap-up | Post-call work time | Wrap-up 시간 | `td_autoconf_wz_queuewrapup` | Kept English; rendered as *Wrap-up 시간* |
| Pause | Agent not taking calls | Paused | `td_agawlogon_paused` | Kept in English |
| Session | Logged-on period | 세션 | `td_ancod_agent_sessions_detail` | Rendered as *상담원 세션* |
| Inbound / Outbound | Call direction | Inbound / Outbound | `td_qdir_inbound_calls`, `td_qdir_outbound_calls` | Kept in English |
| Transfer | Pass call onward | Transferred | `td_callstatus_html_transferred` | Kept in English |
| Spill | Overflow call | Spill | `td_aglev_spill` | Kept in English |
| Ringing | Phone ringing | Ringing | `evt_ringing` | Kept in English |
| Extension | Phone extension | 내선 | `art_localExtension` | |
| Skill | Agent competency | 스킬 | `cldst_skills_per_day` | Rendered as *스킬* |
| Voicemail | Recorded message | Timeout (voicemail) | `td_cko_timeout_voicemail` | Context reference |
| Recall | Scheduled call-back | 재통화 스케쥴러 | `art_lblWbRecallPanel` | Rendered as *재통화 스케쥴러* |
| Supervisor | Agent overseer | 감독자 | `edit_ac_supervisor` | Rendered as *감독자(Supervisor)* |
| Barge / Whisper / Spy | Live-call monitoring | Barge / Whisper | `rt3_actions_barge`, `rt3_actions_whisper` | Kept in English (Spy not found in pack) |
| Billable | Billed time/activity | 과금대상 | `aout_act_billable` | Rendered as *과금대상 활동* |
| Outcome | Call result | 통화결과 | `aout_call_res_by_outcome` | Rendered as *통화내역(Outcomes별)* |
| Disposition | Coded result / rule | Clone Disposition 규칙 | `cdp_clonedispositions` | Context-specific; *규칙* is translation |
| Tag | Call tag | Tag | `aout_calltag` | Kept in English |
| Realtime | Live view | realtime | `art_active_polling_error` | Context reference to *realtime.useActivePolling* |
| Wallboard | Real-time display | 월보드 | `rt3_delete_current_wallboard_confirm` | Rendered as *월보드* |
| Alarm | Threshold alert | AGAW경고 | `edit_record_agawqueue_title` | Context: *AGAW경고* |
| Threshold | Trigger value | 임계값 | `custrep_skills_valhrd` | |

---

## 6. General UI terms

| Term | Context | Translation | Example label(s) | Notes |
|------|---------|-------------|------------------|-------|
| Report | Analysis output | 보고서 | `aout_agent_report` | Rendered as *상세보고서* in context |
| Edit / Add / Delete / Create | CRUD actions | 편집 / 추가 / 삭제 / 생성 | `rt3_menu_edit`, `rt3_add`, `rt3_menu_delete` | Varied rendering; *편집* (Edit), *추가* (Add), *삭제* (Delete) confirmed |
| Export | Export to file | 내보내기 | `cld_btn_export_calls` | Rendered as *통화 내보내기* |
| Configuration / Settings | Setup screens | 설정 | `propedit_feature_platformactions_settings` | Rendered as *General Settings* (kept English in config context) |
| Visibility | Access/visibility key | 조회권한 | `edit_record_export_visibility` | Rendered as *조회권한 키(Key)* |
| Group | Grouping | 그룹 | `filter_idAgentGroup` | Rendered as *상담원 그룹* |
| Period | Report time range | 기간 | `edit_record_export_period` | |
| Status | Current state | 상태 | `td_agstatus_agent_is_currently_logged_off` | Rendered as *상담원 상태* in context |
| Details / Detail | Drill-down view | 상세정보 | `td_ancod_answered_calls_details` | Rendered as *상세정보* |
| Feature | Licensable capability | Feature | `aout_feature` | Kept in English |
| Password / User / Code | Login & identity | 비밀번호 / 사용자 / 코드 | `td_autoconf_wz_agentpwd`, `td_autoconf_wz_agentname` | *비밀번호* (Password), *전체 이름* (User context), *상담원 코드* (Code) |

---

## 7. Doubts & items needing review

Terms where the seeded value is uncertain or the existing pack is inconsistent.
Resolve each, then update the table above and remove the row here.

| Term | Issue | Seeded choice | Options to decide between |
|------|-------|---------------|---------------------------|
| CLID | Context-only reference; no direct key lookup | 전화번호 | Verify against a dedicated CLID label |
| PBX | Context-only reference in error message | 교환기 | Verify preferred rendering *교환기* vs *사설교환기* |
| Spy (monitoring) | Not found in pack; only Barge/Whisper present | — | Confirm whether Spy feature exists or omit from pack |
| Inbound / Outbound | Kept in English in most UI contexts | Inbound / Outbound | Verify if Korean *인바운드* / *아웃바운드* should replace |
| Num. | No abbreviation in pack | Num. | Verify whether to keep English abbreviation |
| Realtime | Context reference only; not standalone term | realtime | Confirm preferred rendering *실시간* vs keeping English |
| Configuration | Settings kept as English in some contexts | 설정 | Config screens mix English (*General Settings*) and Korean — standardize |
| Feature | Kept in English throughout | Feature | Verify if should be *기능* or kept English |
| Disposition | Rendered as *규칙* in compound; no standalone entry | 규칙 | Confirm whether to use *처리결과* or *규칙* consistently |
| Tag | Kept in English | Tag | Verify if should be *태그* or *표시* |
| Modem/Timeout (voicemail) | Voicemail rendered in compound only | 음성메일 제한시간 | Confirm standalone term for voicemail |
| Caller | Kept in English | Caller | Verify if should be *발신자* or keep English |
| Hangup | Kept in English | Hangups | Verify if should be *통화 종료* or keep English |
| Pause | Kept in English | Paused | Verify if should be *일시중지* or keep English; pack uses *일시중지(Pause)* mixed |
| Transfer | Kept in English | Transferred | Verify if should be *전송* or *이전* or keep English |
| Spill | Kept in English | Spill | Verify if should be *이월* or keep English |
| Ringing | Kept in English | Ringing | Verify if should be *울림* or keep English |
| Abandoned | Kept in English | Abandon | Verify if should be *포기* or keep English |
| Wrap-up | Kept as English hybrid | Wrap-up 시간 | Confirm whether to use *마무리 시간* or keep hybrid |
