# Glossary — QueueMetrics (pt_PT)

Portuguese (Portugal) terminology master for QueueMetrics. Derived from
[glossary_en_US.md](glossary_en_US.md); see that file and
[CLAUDE.md](CLAUDE.md) for how the glossary is used.

> **Seeded from existing labels.** The **Translation** column was pre-filled with
> the terms **already in use** in [queuemetrics_pt_PT.md](queuemetrics_pt_PT.md)
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
| ACD | Automatic Call Distribution | ACD | `clage_agent_performance_acd_group` | Acronym kept; phrase used is "Grupo ACD" |
| IVR | Interactive Voice Response | IVR | `aout_inforec` | Kept in English |
| DNIS | Dialed Number Identification Service | DNIS | `cld_asterisk_dnis` | Kept in English |
| DID | Direct Inward Dialing | DID | `fp_dnis_edit` | Rendered as "DID/Linhas DNIS" |
| CLID | Calling Line Identification | CLID | `carea_select_number_of_clid_digits_to_search` | Kept in English |
| PBX | Private Branch Exchange | PBX | `pgag_popup_cannot_send_message` | Kept in English |
| MOH | Music On Hold | Música em Espera | `cld_asterisk_mohdur` | Full form used; consider shortening to "Múc. Esp." |
| AMO | Assisted Manual Outbound | AMO | `hdr_amo` | Kept (Loway term) |
| AGAW | Agent real-time monitoring module | AGAW | `edit_record_agawqueue_title` | Kept (QueueMetrics term) |

---

## 2. Metrics & KPI acronyms

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| SLA | Service Level Agreement | SLA | `td_ancod_answered_calls_sla` | Kept in English |
| SPH | Sales per Hour | VPH | `aout_index_sph` | Expanded as "Vendas por Hora (VPH)" |
| CPH | Contacts per Hour | CPH | `aout_cph` | Kept in English |
| QCPH | Qualified Contacts per Hour | CQPH | `aout_index_qcph` | Expanded as "Contactos Qualificados por Hora (CQPH)" |
| DOW | Day Of Week | Dia da semana | `cldst_ta_traffic_analysis_by_period_dow` | |

---

## 3. Quality / training / system acronyms

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| QA | Quality Assurance | QA | `art_lblQAForm` | Kept (*Formulário QA*) |
| QC | Quality Control | QC | `ko_succ_q` | Kept |
| CBT | Computer-Based Training | CBT | `hdr_cbt` | Kept (*CBTs*) |
| Prompt | A prompt for an AI model to perform QA | Prompt | `edit_qa_prompt`, `edit_record_qa_aiprompt` | New AI term; kept in English — verify against pack |

---

## 4. Common UI abbreviations

Keep the Portuguese abbreviated too (tight headers/menus).

| Term | Full form | Translation | Example label(s) | Notes |
|------|-----------|-------------|------------------|-------|
| Avg. | Average | Méd. | `aout_avg_sec` | |
| Max. | Maximum | Máx. | `cldst_ta_ag_max` | |
| Min. | Minimum | Mín. | (not confirmed) | Verify against pack |
| Tot. | Total | Tot. | `aout_tot_sec` | *Tempo Tot.* |
| Num. | Number | Nº | (not confirmed) | Verify against pack |
| Dur. | Duration | Dur. | `clage_acd_duration` | |
| Att. | Attempts | Tent. | `hdr_attempts` | |
| Ans. | Answered | Atend. | `cldst_ans` | |
| Unans. | Unanswered | Não Atend. | `cldst_unans` | |
| Conv. | Conversation | Conv. | `aout_ftrconv` | *Ftr. Conv.* |
| Qualif. | Qualified | Qualif. | `td_calloutc_qualif` | |
| Cont. | Contacts | Contac. | `aout_contacts_n` | |
| Bill. | Billable | Fact. | `aout_billable_s` | Short form used |
| Succ. | Successful | Succ. | `ko_succ_q` | Keep as-is or standardize |
| Short. | Short | Curta | `ko_sho_q` | *Fila Curta* (seeded but marked alien) |
| Ag. | Agent | Agt. | `cldst_ta_ag_max` | *Máx. Agt.* |
| Ext. | Extension | Ext. | `art_localExtension` | |
| Ref. | Reference | Ref. | `ccase_case_xref` | *No. ref.* (seeded but marked alien) |
| sec. | seconds | seg. | `rt3_duration` | *Duração (seg.)* |

---

## 5. Telephony domain terms (full words)

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| Agent | Operator | Agente | `td_agstatus_agent_is_currently_logged_off` | |
| Queue | Call queue | Queue | `td_ancod_answered_calls_agents_on_queue` | Kept in English; some contexts use "Fila" |
| Caller | Person calling in | Originador | `td_cko_caller_abandon` | *Abandonada pelo originador* |
| Call (answered) | Answered call | Chamada atendida | `td_ancod_answered_calls_details` | Rendered as "Chamadas atendidas" |
| Unanswered / Lost | Not answered | Chamada perdida | `td_ancod_unanswered_calls_details`, `aout_fcr_detail_lost` | Also "Chamadas não atendidas" |
| Abandon(ed) | Caller hung up while queued | Abandonada | `td_cko_abandon` | |
| Hangup | Call termination | Desconexão | `aout_ivr_hangups` | *Desconexões* |
| Wait time | Queue time before answer | Tempo de Espera | `edit_record_agawqueue_avgwait` | *Tempo de Espera Médio* |
| Talk time | Conversation time | Tempo de fala | `qap_details_talk` | Seeded but marked alien; verify |
| Wrap-up | Post-call work time | Tempo de wrap-up | `td_autoconf_wz_queuewrapup` | Keeps English term |
| Pause | Agent not taking calls | Pausa | `td_agawlogon_paused` | *Em pausa* |
| Session | Logged-on period | Sessão | `td_ancod_agent_sessions_detail` | *Sessões de agente* |
| Inbound / Outbound | Call direction | Entrada / Saída | (not confirmed) | Verify against pack |
| Transfer | Pass call onward | Transferida | `td_callstatus_html_transferred` | |
| Spill | Overflow call | Spill | `td_aglev_spill` | Kept in English |
| Ringing | Phone ringing | A Tocar | `evt_ringing` | |
| Extension | Phone extension | Extensão | `art_localExtension` | *Ext.* in abbreviation |
| Skill | Agent competency | Competência | `cldst_skills_per_day` | *Competências* |
| Voicemail | Recorded message | Voicemail | `td_cko_timeout_voicemail` | Kept in English; used as "Timeout (voicemail)" |
| Recall | Scheduled call-back | Remarcação | `art_lblWbRecallPanel` | *Agendador de Remarcações* |
| Supervisor | Agent overseer | Supervisor | `edit_ac_supervisor` | |
| Barge / Whisper / Spy | Live-call monitoring | Barge / Whisper / Espiar | `rt3_actions_barge`, `rt3_actions_whisper` | Barge and Whisper kept in English |
| Billable | Billed time/activity | Facturável | `aout_act_billable` | *Actividades Facturáveis* |
| Outcome | Call result | Tipo de contacto | `aout_call_res_by_outcome` | Rendered as *Categorização de chamadas, por tipo de contacto* |
| Disposition | Coded result / rule | Disposição | `cdp_clonedispositions` | *Clonar Disposição de Regras* |
| Tag | Call tag | Tag | `aout_calltag` | Kept in English |
| Realtime | Live view | Tempo real | `art_active_polling_error` | Verify against pack |
| Wallboard | Real-time display | Wallboard | `rt3_delete_current_wallboard_confirm` | Kept in English (seeded marked alien) |
| Alarm | Threshold alert | Alarme | `edit_record_agawqueue_title` | *Alarmes AGAW* |
| Threshold | Trigger value | Limite | `custrep_skills_valhrd` | |

---

## 6. General UI terms

| Term | Context | Translation | Example label(s) | Notes |
|------|---------|-------------|------------------|-------|
| Report | Analysis output | Relatório | `aout_agent_report` | |
| Edit / Add / Delete / Create | CRUD actions | Editar / Adicionar / Eliminar / Criar | `*_edit`, `*_add`, `*_delete` | Pack uses "Eliminar", "Adicionado", "Criado" |
| Export | Export to file | Exportar | `cld_btn_export_calls` | |
| Configuration / Settings | Setup screens | Configuração | `td_synchronier_configuration` | |
| Visibility | Access/visibility key | Visibilidade | (not confirmed) | Verify against pack |
| Group | Grouping | Grupo | `clage_agent_performance_acd_group` | *Grupo ACD* |
| Period | Report time range | Período | `custrep_time_period` | *Período de tempo* |
| Status | Current state | Estado | `td_agstatus_agent_status_cannot_be_determined` | *Estado de agente* |
| Details / Detail | Drill-down view | Detalhe / Detalhes | `td_ancod_answered_calls_details` | |
| Feature | Licensable capability | Feature | `aout_feature` | Kept in English |
| Password / User / Code | Login & identity | Password / Utilizador / Código | `td_autoconf_wz_agentpwd`, `td_autoconf_wz_users` | Password kept; User = Utilizador |

---

## 7. Doubts & items needing review

Terms where the seeded value is uncertain or the existing pack is inconsistent.
Resolve each, then update the table above and remove the row here.

| Term | Issue | Seeded choice | Options to decide between |
|------|-------|---------------|---------------------------|
| MOH | Full form used; may need abbreviation | Música em Espera | Keep full, or shorten to *Múc. Esp.* or similar |
| Min. | Not confirmed in pack (paired with Max.) | Mín. | Verify abbreviation style matches Max. |
| Num. | Not confirmed in pack | Nº | Verify against labels with "Number" |
| Succ. | Kept as English abbr. or translated? | Succ. | Keep as-is, or use "Suces." or similar |
| Short. | Seeded as alien; full form ambiguous | Curta | Verify exact rendering in "Short queue" contexts |
| Ref. | Seeded as alien; full form "Ref. #" | Ref. | Verify against pack for reference labels |
| Queue | Inconsistent — kept English in some contexts, "Fila" in others | Queue | Standardize: use Queue everywhere, or Queue + Fila where appropriate |
| Caller | Rendered as "originador" (originator) | Originador | Verify if consistent across pack |
| Talk time | Seeded as alien; may be machine-generated | Tempo de fala | Verify against pack's conversation-time labels |
| Inbound / Outbound | Not confirmed from a label | Entrada / Saída | Verify the exact terms used in the pack |
| Realtime | Not confirmed; phrase may differ | Tempo real | Verify against realtime/polling labels |
| Spy (monitoring) | Not confirmed in pack | Espiar | Verify against pack's live-monitoring labels |
| Visibility | Not confirmed in pack | Visibilidade | Verify against the visibility-key labels |
| Wallboard | Seeded as alien; kept English | Wallboard | Verify if English term is intentional or needs Portuguese phrase |
