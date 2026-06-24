# Glossary — QueueMetrics (es_ES)

Spanish terminology master for QueueMetrics. Derived from
[glossary_en_US.md](glossary_en_US.md); see that file and
[CLAUDE.md](CLAUDE.md) for how the glossary is used.

> **Seeded from existing labels.** The **Translation** column was pre-filled with
> the terms **already in use** in [queuemetrics_es_ES.md](queuemetrics_es_ES.md)
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
| ACD | Automatic Call Distribution | ACD | `clage_agent_performance_acd_group` | Kept in English; appears in context *grupo ACD* |
| IVR | Interactive Voice Response | IVR | `aout_inforec` | Kept in English |
| DNIS | Dialed Number Identification Service | DNIS | `cld_asterisk_dnis` | Kept in English |
| DID | Direct Inward Dialing | DID | `fp_dnis_edit` | Kept in English; rendered as *líneas DID/DNIS* |
| CLID | Calling Line Identification | CLID | `carea_select_number_of_clid_digits_to_search` | Kept in English |
| PBX | Private Branch Exchange | PBX | `pgag_popup_cannot_send_message` | Kept in English |
| MOH | Music On Hold | Música en Espera | `cld_asterisk_mohdur` | *Duración Música en Espera* |
| AMO | Assisted Manual Outbound | AMO | `hdr_amo` | Kept (Loway term) |
| AGAW | Agent real-time monitoring module | AGAW | `edit_record_agawqueue_title` | Kept (QueueMetrics term); *Alarmas AGAW* |

---

## 2. Metrics & KPI acronyms

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| SLA | Service Level Agreement | SLA | `td_ancod_answered_calls_sla` | Kept in English; context *Llamadas contestadas: ANS* suggests SLA implicit |
| SPH | Sales per Hour | VPH | `aout_index_sph` | *Ventas por Hora (VPH)* — expanded form preferred |
| CPH | Contacts per Hour | CPH | `aout_cph` | Kept in English |
| QCPH | Qualified Contacts per Hour | Contactos cualificados por hora | `aout_index_qcph` | Full form used, consider abbreviating |
| DOW | Day Of Week | Día de la semana | `cldst_ta_traffic_analysis_by_period_dow` | |

---

## 3. Quality / training / system acronyms

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| QA | Quality Assurance | QA | `art_lblQAForm` | Kept; *Módulo QA* |
| QC | Quality Control | QC | `ko_succ_q` | Kept in English |
| CBT | Computer-Based Training | CBT | `hdr_cbt` | Kept; *CBTs* |
| Prompt | A prompt for an AI model to perform QA | Prompt | `edit_qa_prompt`, `edit_record_qa_aiprompt` | New AI term; kept in English — verify against pack |

---

## 4. Common UI abbreviations

Keep the Spanish abbreviated too (tight headers/menus).

| Term | Full form | Translation | Example label(s) | Notes |
|------|-----------|-------------|------------------|-------|
| Avg. | Average | Prom. | `aout_avg_sec` | |
| Max. | Maximum | Máx. | `cldst_ta_ag_max` | |
| Min. | Minimum | Mín. | `aout_min_sec` | |
| Tot. | Total | Tot. | `aout_tot_sec` | |
| Num. | Number | Nro. | `aout_fcr_n_calls` | *Nro. Llamadas* |
| Dur. | Duration | Dur. | `clage_acd_duration` | |
| Att. | Attempts | Att. | `hdr_attempts` | |
| Ans. | Answered | Cons. | `aout_taken` | *Consumido* in pack; verify abbreviation |
| Unans. | Unanswered | No atendidas | `cldst_unans` | Full form used; abbreviate if space-tight |
| Conv. | Conversation | Conv. | `aout_ftrconv` | |
| Qualif. | Qualified | Qualif. | `td_calloutc_qualif` | |
| Cont. | Contacts | Cont. | `aout_contacts_n` | |
| Bill. | Billable | Prod. | `aout_billable_s` | *Productivo* in pack; possibly *Fact.* for Facturable |
| Succ. | Successful | Exitosos | `ko_succ_q` | *Exitosos Cola* |
| Short. | Short | Corta | `ko_sho_q` | *Q Corta* |
| Ag. | Agent | Ag. | `cldst_ta_ag_max` | |
| Ext. | Extension | Ext. | `art_localExtension` | |
| Ref. | Reference | Ref. N° | `ccase_case_xref` | |
| sec. | seconds | Dur. | `rt3_duration` | Verify context |

---

## 5. Telephony domain terms (full words)

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| Agent | Operator | Agente | `td_agstatus_agent_is_currently_logged_off` | |
| Queue | Call queue | Cola | `td_ancod_answered_calls_agents_on_queue` | *Agentes en cola* |
| Caller | Person calling in | Llamante | `td_cko_caller_abandon` | |
| Call (answered) | Answered call | Llamada contestada | `td_ancod_answered_calls_details` | |
| Unanswered / Lost | Not answered | Llamadas no contestadas | `td_ancod_unanswered_calls_details`, `aout_fcr_detail_lost` | *Llamadas perdidas* for lost calls |
| Abandon(ed) | Caller hung up while queued | Abandono | `td_cko_abandon` | |
| Hangup | Call termination | Corte | `aout_ivr_hangups` | |
| Wait time | Queue time before answer | Tiempo promedio Espera | `edit_record_agawqueue_avgwait` | |
| Talk time | Conversation time | Tiempo Llamada | `qap_details_talk` | |
| Wrap-up | Post-call work time | Wrap-up | `td_autoconf_wz_queuewrapup` | Pack keeps English; *Tiempo de Wrap-up* |
| Pause | Agent not taking calls | En Pausa | `td_agawlogon_paused` | |
| Session | Logged-on period | Sesión | `td_ancod_agent_sessions_detail` | |
| Inbound / Outbound | Call direction | Entrante / Saliente | `td_qdir_inbound_calls` / `clok_outbound` | *Llamadas entrantes* / *Llamada saliente* |
| Transfer | Pass call onward | Transferido | `td_callstatus_html_transferred` | |
| Spill | Overflow call | Spill | `td_aglev_spill` | Kept in English |
| Ringing | Phone ringing | Llamando | `evt_ringing` | |
| Extension | Phone extension | Extensión | `art_localExtension` | |
| Skill | Agent competency | Habilidades | `cldst_skills_per_day` | |
| Voicemail | Recorded message | Voicemail | `td_cko_timeout_voicemail` | *Tiempo agotado (voicemail)* |
| Recall | Scheduled call-back | Programador de Rellamados | `art_lblWbRecallPanel` | |
| Supervisor | Agent overseer | Supervisor | `edit_ac_supervisor` | |
| Barge / Whisper / Spy | Live-call monitoring | Barge / Whisper / Espiar | `rt3_actions_barge`, `rt3_actions_whisper`, `propedit_option_spy` | Pack keeps English for Barge/Whisper; *Espiar* for Spy |
| Billable | Billed time/activity | Tiempo productivo | `aout_act_billable` | |
| Outcome | Call result | Resultados por tipo de contacto | `aout_call_res_by_outcome` | |
| Disposition | Coded result / rule | Disposición | `cdp_clonedispositions` | *Reglas de Disposición* |
| Tag | Call tag | Tag | `aout_calltag` | Kept in English |
| Realtime | Live view | Tiempo real | `art_active_polling_error` | Verify context — complex label |
| Wallboard | Real-time display | Tablero | `rt3_delete_current_wallboard_confirm` | |
| Alarm | Threshold alert | Alarma | `edit_record_agawqueue_title` | |
| Threshold | Trigger value | Umbrales | `custrep_skills_valhrd` | |

---

## 6. General UI terms

| Term | Context | Translation | Example label(s) | Notes |
|------|---------|-------------|------------------|-------|
| Report | Analysis output | Informe | `aout_agent_report` | |
| Edit / Add / Delete / Create | CRUD actions | Editar / Añadir / Eliminar / Crear | `*_edit`, `*_add`, `*_delete`, `*_create` | Pack uses *Editar*, *Añadir*, *Eliminar*, *Crear* |
| Export | Export to file | Exportar | `cld_btn_export_calls` | |
| Configuration / Settings | Setup screens | Configuración | `td_synchronier_configuration` | |
| Visibility | Access/visibility key | Visibilidad | `edit_record_export_visibility` | *Llaves Visibilidad* or *Llave visibilidad* |
| Group | Grouping | Grupo | `edit_ac_group` | *Grupo personalizado* when custom |
| Period | Report time range | Período de tiempo | `custrep_time_period` | |
| Status | Current state | Estado | `td_agstatus_agent_status_cannot_be_determined` | *Estado del agente* |
| Details / Detail | Drill-down view | Detalles | `td_ancod_answered_calls_details` | |
| Feature | Licensable capability | Característica | `aout_feature` | |
| Password / User / Code | Login & identity | Contraseña / Usuarios / Código | `td_autoconf_wz_agentpwd`, `td_autoconf_wz_users` | |

---

## 7. Doubts & items needing review

Terms where the seeded value is uncertain, inconsistent, kept in English by default, or unconfirmed from the pack.
Resolve each, then update the table above and remove the row here.

| Term | Issue | Seeded choice | Options to decide between |
|------|-------|---------------|---------------------------|
| Ans. (Answered) | Pack uses full form *Consumido*, no abbreviation | *Cons.* | Keep full *Consumido*, or adopt *Cons.* abbreviation for tight headers; verify against actual UI |
| Bill. (Billable) | Pack uses *Productivo* (lit. "productive"), possibly inconsistent with *Facturable* | *Prod.* | Use *Prod.* (productive), or *Fact.* (billable/chargeable) — verify pack consistency |
| Unans. (Unanswered) | Pack uses full form, no abbreviation | *No atendidas* | Keep full form, or create abbreviation *N.At.* or similar |
| SLA | Label context suggests SLA but shows *ANS* | SLA | Verify what SLA should expand to in Spanish |
| Barge / Whisper | Pack keeps English | Barge / Whisper | Keep English, or translate to Spanish equivalents |
| Voicemail | Pack keeps English in context | Voicemail | Keep English, or translate to *Buzón de voz* or *Correo de voz* |
| Spill | Pack keeps English | Spill | Keep English, or translate to Spanish *Desbordamiento* or similar |
| Tag | Pack keeps English | Tag | Keep English, or translate to *Etiqueta* or *Marcador* |
| Realtime | Complex label with property name | Tiempo real | Verify this is correct translation in context |
| QCPH | Pack uses full expanded form | Contactos cualificados por hora | Verify if abbreviation should be created (e.g., *CCPH*) |
