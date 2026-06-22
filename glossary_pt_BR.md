# Glossary — QueueMetrics (pt_BR)

> **Note:** This glossary was **seeded from existing labels** in `queuemetrics_pt_BR.md` and still needs human review. Some terms may have been kept in English due to lack of existing translations, or may show inconsistencies across the label pack. See Section 7 for items flagged for review.

This is the **terminology master** for QueueMetrics in Portuguese (Brazil). It collects the telephony
jargon, abbreviations and recurring UI terms that appear — often hundreds of
times — across [queuemetrics_pt_BR.md](queuemetrics_pt_BR.md).

## Why this file exists

Many labels reuse the same handful of domain terms (`agente`, `fila`, `espera`,
`SLA`, `wrap-up`, `Média`…). If each label is translated in isolation, the
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
|------|---------------------------|-------------|------|-------|
| ACD | Automatic Call Distribution — the routing engine that assigns calls to agents | Resultado do agente por grupo ACD | `clage_agent_performance_acd_group` | Kept in English (ACD is used in context) |
| IVR | Interactive Voice Response — the automated voice menu | URA | `aout_inforec` | (Unidade de Resposta Automática) |
| DNIS | Dialed Number Identification Service — the number that was called | DNIS | `cld_asterisk_dnis` | Kept in English |
| DID | Direct Inward Dialing — a directly-reachable inbound number | DID | `fp_dnis_edit` | Kept in English |
| CLID | Calling Line Identification — the caller's number / caller-ID | CLID | `carea_select_number_of_clid_digits_to_search` | Kept in English |
| PBX | Private Branch Exchange — the phone system QueueMetrics monitors | PBX | `pgag_popup_cannot_send_message` | Kept in English |
| MOH | Music On Hold | Música em Espera | `cld_asterisk_mohdur` | (From "Duração Música em Espera") |
| AMO | Assisted Manual Outbound (Loway term) | AMO | `hdr_amo` | Kept in English (product-specific term) |
| AGAW | Agent real-time monitoring module (QueueMetrics-specific term) | AGAW | `td_dbtest_wz_agawcleanup`, `edit_record_agawqueue_title` | Kept in English |

---

## 2. Metrics & KPI acronyms

| Term | English meaning / context | Translation | Example label(s) | Notes |
|------|---------------------------|-------------|------|-------|
| SLA | Service Level Agreement — % of calls answered within target time | SLA | `td_ancod_answered_calls_sla` | Kept in English |
| SPH | Sales per Hour | VPH | `aout_index_sph` | (Vendas por Hora) |
| CPH | Contacts per Hour | CPH | `aout_cph` | Kept in English |
| QCPH | Qualified Contacts per Hour | QCPH | `aout_index_qcph` | Kept in English |
| DOW | Day Of Week | | `cldst_ta_traffic_analysis_by_period_dow` | Verify against pack |

---

## 3. Quality / training / system acronyms

| Term | English meaning / context | Translation | Example label(s) | Notes |
|------|---------------------------|-------------|------|-------|
| QA | Quality Assurance (grading / scorecards) | Formulário PR | `art_lblQAForm` | (Packed as "Formulário PR") |
| QC | Quality Control | Filas Sucesso | `ko_succ_q` | Verify against pack |
| CBT | Computer-Based Training | CBTs | `hdr_cbt` | Kept in English |

---

## 4. Common UI abbreviations

Keep the translation **abbreviated** too — these sit in tight table headers and
menus. Match the source's truncation style (trailing `.`).

| Term | Full form | Translation | Example label(s) | Notes |
|------|-----------|-------------|------|-------|
| Avg. | Average | Média | `aout_avg_sec` | |
| Max. | Maximum | Máx. | `cldst_ta_ag_max` | |
| Min. | Minimum | Mín. | `cldst_ta_ag_min` | (paired with Max.) |
| Tot. | Total | Tot. | `clage_totwaittime` | |
| Num. | Number | Num. | `propedit_key_phone_maxsessions` | Verify against pack |
| Dur. | Duration | Dur. | `clage_acd_duration` | |
| Att. | Attempts | Tentativas | `hdr_attempts` | Verify against pack |
| Ans. | Answered | Atend. | `clhdr_ans` | |
| Unans. | Unanswered | Não Atend. | `cldst_unans` | |
| Conv. | Conversation | Conv. | `clage_conversions` | |
| Qualif. | Qualified | Qualif. | `td_calloutc_qualif` | Verify against pack |
| Cont. | Contacts | Cont. | `aout_contacts_n` | |
| Bill. | Billable | Cob. | `aout_billable_s` | (Cobrável) |
| Succ. | Successful | Succ. | `ko_succ_q` | Verify against pack |
| Short. | Short | Short. | `ko_sho_q` | Verify against pack |
| Ag. | Agent | Ag. | `cldst_ta_ag_max` | Verify against pack |
| Ext. | Extension | Ext. | `art_localExtension` | |
| Ref. | Reference | Ref. | `ccase_case_xref` | Verify against pack |
| sec. | seconds | seg. | `rt3_duration` | (Portuguese: "segundos") |

---

## 5. Telephony domain terms (full words)

The high-frequency vocabulary of the product. Pick one translation per term and
keep it consistent everywhere.

| Term | English meaning / context | Translation | Example label(s) | Notes |
|------|---------------------------|-------------|------|-------|
| Agent | Operator who handles calls | Agente | `td_agstatus_agent_is_currently_logged_off` | |
| Queue | Call queue | Fila | `td_ancod_answered_calls_agents_on_queue` | |
| Caller | The person calling in | Originador | `td_cko_caller_abandon` | |
| Call (answered) | Answered call | Chamadas atendidas | `td_ancod_answered_calls_details` | |
| Unanswered / Lost call | Call that was not answered | Chamadas perdidas | `td_ancod_unanswered_calls_details`, `aout_fcr_detail_lost` | |
| Abandon(ed) | Caller hung up while waiting | Abandono | `td_cko_abandon` | |
| Hangup | Call termination | Desligamentos | `aout_ivr_hangups` | |
| Wait time | Time spent queued before answer | Tempo médio de espera | `clage_avg_wait_time` | |
| Talk time | Time spent in conversation | Conversa | `cld_talk` | |
| Wrap-up | Post-call work time | Wrap-up | `td_pautype_wrap-up_time` | Kept in English |
| Pause | Agent paused / not taking calls | Pausa | `clage_pauses` | |
| Session | An agent's logged-on period | Sessão | `td_ancod_agent_sessions_detail` | |
| Inbound / Outbound | Call direction | Entrantes / Saintes | `td_qdir_inbound_calls`, `td_qdir_outbound_calls` | |
| Transfer | Passing a call to another party | Transferida | `cld_transfer_to` | |
| Spill | Overflow call routed onward | Transbordo | `td_aglev_spill` | |
| Ringing | Phone is ringing | Chamando | `evt_ringing` | |
| Extension | Phone extension number | Ext. | `art_localExtension` | |
| Skill | Agent skill / competency tag | Competências | `cldst_skills_per_day` | |
| Voicemail | Recorded message | voicemail | `td_cko_timeout_voicemail` | Kept in English (as compound) |
| Recall | Scheduled call-back | Rechamadas | `art_lblWbRecallPanel` | (Calendário de Rechamadas) |
| Supervisor | Agent overseer | Supervisor | `edit_ac_supervisor` | |
| Spy / Barge / Whisper | Live-call monitoring actions | Interromper / Sussurrar | `rt3_actions_barge`, `rt3_actions_whisper` | |
| Billable | Time/activity that is billed | Tempo produtivo | `aout_act_billable` | |
| Outcome | Result/disposition of a call | Tipo da chamada | `aout_outcome` | |
| Disposition | Coded call result / rule | Regras de Disposição | `cdp_clonedispositions` | |
| Tag | Call tag / label | Marcação | `aout_calltag` | |
| Realtime | Live monitoring view | Realtime | `art_active_polling_error` | Kept in English |
| Wallboard | Large real-time status display | wallboard | `rt3_delete_current_wallboard_confirm` | Kept in English |
| Alarm | Threshold alert | Alarmas | `edit_record_agawqueue_title` | |
| Threshold | Trigger value for alarms/SLA | Limite | `custrep_skills_valhrd` | |

---

## 6. General UI terms

Recurring application-chrome vocabulary. Worth fixing once for menu/button
consistency.

| Term | Context | Translation | Example label(s) | Notes |
|------|---------|-------------|------|-------|
| Report | Analysis output | Relatório | `aout_agent_report` | |
| Edit / Add / Delete / Create | CRUD actions on forms | Editar / Adicionar / Excluir / Criar | `edit_*`, `*_add`, `*_delete` | Verify against pack |
| Export | Export to CSV/PDF/XLS | Exportar | `cld_btn_export_calls` | |
| Configuration / Settings | Setup screens | Configuração | `td_synchronier_configuration` | |
| Visibility | Access/visibility key | Chave de visibilidade | visibility-key labels | Verify against pack |
| Group | Agent / report grouping | Grupo | `clage_agent_performance_acd_group` | |
| Period | Time range of a report | Período | period selectors | Verify against pack |
| Status | Current state | Situação | `td_agstatus_*` | Verify against pack |
| Details / Detail | Drill-down view | Detalhes | `td_ancod_answered_calls_details` | |
| Feature | Licensable capability | Funcionalidade | `cld_features` | |
| Password / User / Code | Login & identity fields | Senha / Usuário / Código | `td_autoconf_wz_agentpwd` | |

---

## 7. Doubts & items needing review

Per-language glossaries add rows here for any term whose translation is
uncertain or whose existing pack is inconsistent. Whenever you have a
doubt about a translation — the pack is inconsistent, keeps the English term,
or you couldn't confirm a value from a label — add a row here with the term,
the issue, the seeded choice, and the options to decide between.

| Term | Issue | Seeded choice | Options to decide between |
|------|-------|---------------|---------------------------|
| DOW | Not found in pack; abbreviation handling unclear | (empty) | "Dia da Semana" (full) or "DSem" (abbreviated) or keep "DOW" |
| QC (Quality Control) | Ambiguous; "Filas Sucesso" seems to be a specific label value, not the translation | Filas Sucesso | "Controle de Qualidade" (full) or "CQ" (abbr.) or reconsider |
| Att. (Attempts) | Found as full "Tentativas", not abbreviated form in pack | Tentativas | "Tent." (abbreviated) or "Att." (keep English abbr.) |
| Num. (Number) | Not explicitly found for this abbreviation in pack | Num. | "Qtde." (Quantidade) or "Nº" (symbol) or keep "Num." |
| Qualif. (Qualified) | Not explicitly abbreviated in pack; only saw "Qualif." in context | Qualif. | Verify abbreviation in real usage |
| Succ. (Successful) | Appears as "Filas Sucesso"; context suggests outcome classification | Filas Sucesso | "Suc." (Portuguese) or "Succ." (English abbr.) |
| Short. (Short) | Saw "Fila Curta" (short queue); "Short." abbr. unclear | Fila Curta | "Curta" (full) or "Cur." (abbr.) or "Short." (English) |
| Ag. (Agent) | Found in compound contexts; standalone abbreviation not verified | Ag. | "Agente" (full) or "Ag." (confirmed abbr.) or "Agt." |
| Ref. (Reference) | Context: "No. ref." suggests "No." (Número) + "ref."; not clear | Ref. | "Ref." (keep) or "Nº ref." or reconsider |
| Wrap-up | Kept in English in pack; verify if Portuguese translation exists elsewhere | Wrap-up | "Encerramento pós-chamada" or keep "Wrap-up" |
| QA (Quality Assurance) | Found as "Formulário PR"; "PR" may mean "Pesquisa/Revisão" or may be abbreviation inconsistency | Formulário PR | Verify what "PR" stands for; consider "QA" vs. "PR" vs. "AQ" (Asseguração de Qualidade) |
| Edit / Add / Delete / Create | Pattern found but exact terms not consolidated into a glossary entry | (see context) | Verify preferred translations: "Editar / Adicionar / Eliminar / Criar" vs. alternatives |
| Visibility | Not found in pack explicitly | Chave de visibilidade | Verify against actual pack usage |
| Period | Not found in pack explicitly | Período | Verify against actual pack usage |
| Status | Found as "Situação" in some contexts; inconsistency possible | Situação | "Status" (keep) or "Situação" (translate) or "Estado" |
| Realtime | Kept in English in active monitoring error message | Realtime | "Tempo real" or keep "Realtime" |
| Wallboard | Kept in English; verify if wallboard has a Portuguese term in this context | wallboard | "Painel de status" or "Quadro de avisos" or keep "wallboard" |
