# Glossary — QueueMetrics (jp_JP)

Japanese terminology master for QueueMetrics. Derived from
[glossary_en_US.md](glossary_en_US.md); see that file and
[CLAUDE.md](CLAUDE.md) for how the glossary is used.

> **Seeded from existing labels.** The **Translation** column was pre-filled with
> the terms **already in use** in [queuemetrics_jp_JP.md](queuemetrics_jp_JP.md)
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
| IVR | Interactive Voice Response | IVR | `aout_inforec` | Kept in English |
| DNIS | Dialed Number Identification Service | DNIS | `cld_asterisk_dnis` | Kept in English |
| DID | Direct Inward Dialing | DID | `fp_dnis_edit` | Kept in English |
| CLID | Calling Line Identification | CLID | `carea_select_number_of_clid_digits_to_search` | Kept in English |
| PBX | Private Branch Exchange | PBX | `pgag_popup_cannot_send_message` | Kept in English |
| MOH | Music On Hold | MOH時間 | `cld_asterisk_mohdur` | Found as "MOH時間" (MOH + time) |
| AMO | Assisted Manual Outbound | AMO | `hdr_amo` | Kept (Loway term) |
| AGAW | Agent real-time monitoring module | AGAW | `edit_record_agawqueue_title` | Kept (QueueMetrics term) |

---

## 2. Metrics & KPI acronyms

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| SLA | Service Level Agreement | SLA | `td_ancod_answered_calls_sla` | Kept in English |
| SPH | Sales per Hour | 時間毎セールス | `aout_index_sph` | Expanded form |
| CPH | Contacts per Hour | CPH | `aout_cph` | Kept |
| QCPH | Qualified Contacts per Hour | 時間毎正規コンタクト | `aout_index_qcph` | Expanded form |
| DOW | Day Of Week | 曜日毎 | `cldst_ta_traffic_analysis_by_period_dow` | Found as "曜日毎" |

---

## 3. Quality / training / system acronyms

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| QA | Quality Assurance | QA | `art_lblQAForm` | Kept (*QAフォーム*) |
| QC | Quality Control | Q. | `ko_succ_q` | Abbreviated |
| CBT | Computer-Based Training | CBT | `hdr_cbt` | Kept |
| Prompt | A prompt for an AI model to perform QA | プロンプト | `edit_qa_prompt`, `edit_record_qa_aiprompt` | New AI term — verify against pack |

---

## 4. Common UI abbreviations

Keep the Japanese abbreviated too (tight headers/menus).

| Term | Full form | Translation | Example label(s) | Notes |
|------|-----------|-------------|------------------|-------|
| Avg. | Average | 平均値 | `aout_avg_sec` | |
| Max. | Maximum | 最大 | `cldst_ta_ag_max` | Found as "最大Ag." |
| Min. | Minimum | 最小 | `aout_min_sec` | |
| Tot. | Total | Tot. Time | `aout_tot_sec` | Kept in English ("Tot. Time") |
| Num. | Number | 番号 | `propedit_key_phone_maxsessions` | Full form (verify abbreviation) |
| Dur. | Duration | 持続時間 | `clage_acd_duration` | |
| Att. | Attempts | 試行 | `hdr_attempts` | |
| Ans. | Answered | 応答 | `cldst_ans` | |
| Unans. | Unanswered | 捨て呼 | `cldst_unans` | Verify against pack |
| Conv. | Conversation | 機能変換 | `aout_ftrconv` | Verify — may be "conversation" not "feature conversion" |
| Qualif. | Qualified | Qualif. | `td_calloutc_qualif` | Kept in English |
| Cont. | Contacts | コンタクト | `aout_contacts_n` | |
| Bill. | Billable | 請求書 | `aout_billable_s` | Verify — may mean "invoice" |
| Succ. | Successful | 成功.Q. | `ko_succ_q` | Verify — unusual format |
| Short. | Short | ショート.Q. | `ko_sho_q` | Verify — unusual format |
| Ag. | Agent | Ag. | `cldst_ta_ag_max` | Kept in English |
| Ext. | Extension | 内線 | `art_localExtension` | |
| Ref. | Reference | 参照# | `ccase_case_xref` | Found as "参照#" |
| sec. | seconds | 期間（秒） | `rt3_duration` | Verify — full form found |

---

## 5. Telephony domain terms (full words)

The high-frequency vocabulary of the product. Pick one translation per term and keep it consistent everywhere.

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| Agent | Operator who handles calls | エージェント | `td_agstatus_agent_is_currently_logged_off` | |
| Queue | Call queue | キュー | `td_ancod_answered_calls_agents_on_queue` | |
| Caller | The person calling in | 発信者 | `td_cko_caller_abandon` | |
| Call (answered) | Answered call | 応答コール | `td_ancod_answered_calls_details` | |
| Unanswered / Lost call | Call that was not answered | 捨て呼 | `td_ancod_unanswered_calls_details` | |
| Abandon(ed) | Caller hung up while waiting | 捨て呼 | `td_cko_abandon` | Rendered as "捨て呼" |
| Hangup | Call termination | ハングアップ | `aout_ivr_hangups` | |
| Wait time | Time spent queued before answer | 平均待ち時間 | `edit_record_agawqueue_avgwait` | |
| Talk time | Time spent in conversation | 通話時間 | `qap_details_talk` | |
| Wrap-up | Post-call work time | 最終時間 | `td_autoconf_wz_queuewrapup` | Verify — may mean "final time" not "wrap-up" |
| Pause | Agent paused / not taking calls | 中断された | `td_agawlogon_paused` | |
| Session | An agent's logged-on period | セッション | `td_ancod_agent_sessions_detail` | Verify against pack |
| Inbound / Outbound | Call direction | IVR / アウトバウンド | `aout_inforec` | Mixed; outbound found |
| Transfer | Passing a call to another party | 転送された | `td_callstatus_html_transferred` | |
| Spill | Overflow call routed onward | 流出 | `td_aglev_spill` | |
| Ringing | Phone is ringing | 呼び出し中 | `evt_ringing` | |
| Extension | Phone extension number | 内線 | `art_localExtension` | |
| Skill | Agent skill / competency tag | スキル | `cldst_skills_per_day` | Verify against pack |
| Voicemail | Recorded message | ボイスメール | `td_cko_timeout_voicemail` | Found as "ボイスメール" |
| Recall | Scheduled call-back | リコールスケジューラ | `art_lblWbRecallPanel` | |
| Supervisor | Agent overseer | スーパーバイザー | `edit_ac_supervisor` | |
| Spy / Barge / Whisper | Live-call monitoring actions | 割り込み / ささやき | `rt3_actions_barge` | Barge="割り込み"; Whisper="ささやき" |
| Billable | Time/activity that is billed | 支払請求可能なアクティビティ | `aout_act_billable` | |
| Outcome | Result/disposition of a call | 呼び出し結果 | `aout_call_res_by_outcome` | |
| Disposition | Coded call result / rule | 破棄ルール | `cdp_clonedispositions` | Verify — may not mean "disposition" |
| Tag | Call tag / label | タグ | `aout_calltag` | |
| Realtime | Live monitoring view | リアルタイム | `art_active_polling_error` | Verify against pack |
| Wallboard | Large real-time status display | ウォールボード | `rt3_delete_current_wallboard_confirm` | |
| Alarm | Threshold alert | AGAW | `edit_record_agawqueue_title` | Verify — kept as AGAW |
| Threshold | Trigger value for alarms/SLA | 閾値 | `custrep_skills_valhrd` | |

---

## 6. General UI terms

Recurring application-chrome vocabulary. Worth fixing once for menu/button consistency.

| Term | Context | Translation | Example label(s) | Notes |
|------|---------|-------------|------------------|-------|
| Report | Analysis output | リポート | `aout_agent_report` | Verify — found as part of longer phrase |
| Edit / Add / Delete / Create | CRUD actions on forms | 編集 / 追加 / 削除 | `rt3_edit` / `rt3_add` / `edit_record_delete` | Separate terms found |
| Export | Export to CSV/PDF/XLS | エクスポート | export buttons | Verify against pack |
| Configuration / Settings | Setup screens | 構成 / 設定 | `hdr_dbtest_configuration` | |
| Visibility | Access/visibility key | 表示キー | `edit_record_queue_visibility` | |
| Group | Agent / report grouping | グループ | `clage_agent_performance_acd_group` | Verify — found as "ACDグループ" |
| Period | Time range of a report | 期間 | period selectors | Verify against pack |
| Status | Current state | ステータス | `td_agstatus_agent_is_currently_logged_off` | Verify — found as part of longer labels |
| Details / Detail | Drill-down view | 詳細 | `td_ancod_answered_calls_details` | |
| Feature | Licensable capability | 機能 | `aout_call_res_by_feature` | |
| Password / User / Code | Login & identity fields | パスワード / ユーザー / エージェントコード | `td_autoconf_wz_agentpwd` | Separate terms |

---

## 7. Doubts & items needing review

| Term | Issue | Seeded choice | Options to decide between |
|------|-------|---------------|---------------------------|
| MOH | Pack renders as "MOH時間" (MOH + time modifier) rather than standalone acronym | MOH時間 | Keep "MOH時間" vs. use standalone "MOH" |
| Unans. | Rendered as "捨て呼" (literally "discarded call") — confirm this is intentional | 捨て呼 | Keep "捨て呼" vs. use neutral "未応答" or "応答なし" |
| Conv. | Labeled as "機能変換" (feature conversion) — verify this is not a mistranslation | 機能変換 | Verify intent; likely should be "会話" (conversation) |
| Bill. | Rendered as "請求書" (invoice/bill document) rather than "billable" adjective | 請求書 | Keep "請求書" vs. use "請求可能" |
| Succ. / Short. | Abbreviated format "成功.Q." and "ショート.Q." seems unusual; verify intended abbreviation | 成功.Q. / ショート.Q. | Verify if abbreviation should be different |
| Num. | Full form "番号" (number) found; abbreviation not confirmed | 番号 | Confirm if abbreviation like "番" would be preferred |
| Tot. | Kept as English "Tot. Time" rather than abbreviated Japanese | Tot. Time | Consider "合計時間" or keep "Tot. Time" |
| sec. | Full form "期間（秒）" (duration in seconds) found; abbreviation not confirmed | 期間（秒） | Confirm if abbreviation like "秒" would be preferred |
| Ag. | Kept as English "Ag." in "最大Ag." | Ag. | Consider Japanese abbreviation vs. keep English |
| Wrap-up | Rendered as "最終時間" (final time) — verify this correctly conveys post-call work time | 最終時間 | Verify intent; consider "ラップアップ" or "事後処理" |
| Disposition | Rendered as "破棄ルール" (disposal/discard rule) — verify this means call disposition code | 破棄ルール | Verify intent; likely should be "コード" (code) or similar |
| Skill | Not found in sample; used "スキル" (common tech term) | スキル | Verify against pack |
| Session | Not found in sample; used "セッション" (common tech term) | セッション | Verify against pack |
| Realtime | Not found in sample; used "リアルタイム" (common tech term) | リアルタイム | Verify against pack |
| Alarm | Kept as "AGAW" (QueueMetrics product term) rather than Japanese "警告" | AGAW | Keep AGAW vs. use "警告" (warning/alarm) |
| Inbound | Only "outbound" (as "IVR" and "アウトバウンド") found; inbound not directly seeded | IVR / アウトバウンド | Confirm "インバウンド" for inbound calls |
| Group | Found as "ACDグループ" (ACD + group); standalone "グループ" not confirmed | グループ | Verify if "グループ" or "ACDグループ" preferred |
| Report | Not found in sample; used "リポート" (common tech term) | リポート | Verify against pack |
| Period | Not found in sample; used "期間" (common tech term) | 期間 | Verify against pack |
| Export | Not found in sample; used "エクスポート" (common tech term) | エクスポート | Verify against pack |
| Status | Found only as part of longer labels like "td_agstatus_*"; standalone "ステータス" not confirmed | ステータス | Verify preferred standalone term |
