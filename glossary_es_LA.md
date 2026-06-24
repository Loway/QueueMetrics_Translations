# Glossary — QueueMetrics (es_LA)

This is the **terminology master** for QueueMetrics in Spanish (Latin America). It collects the telephony
jargon, abbreviations and recurring UI terms that appear — often hundreds of
times — across [queuemetrics_es_LA.md](queuemetrics_es_LA.md).

> **Note:** This glossary was seeded from existing labels in queuemetrics_es_LA.md. It has been auto-populated with translations already in use, but still requires human review to ensure consistency and address any uncertainties listed in Section 7.

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
| ACD | Automatic Call Distribution — the routing engine that assigns calls to agents | Grupo ACD | `clage_agent_performance_acd_group` | |
| IVR | Interactive Voice Response — the automated voice menu | IVR | `aout_inforec` | Kept in English |
| DNIS | Dialed Number Identification Service — the number that was called | DNIS | `cld_asterisk_dnis` | Kept in English |
| DID | Direct Inward Dialing — a directly-reachable inbound number | DID/DNIS | `fp_dnis_edit` (DID/DNIS Lines) | Kept in English (compound) |
| CLID | Calling Line Identification — the caller's number / caller-ID | CLID | `carea_select_number_of_clid_digits_to_search` | Kept in English |
| PBX | Private Branch Exchange — the phone system QueueMetrics monitors | PBX | `pgag_popup_cannot_send_message` | Kept in English |
| MOH | Music On Hold | Música en Espera | `cld_asterisk_mohdur` (MOH duration) | |
| AMO | Assisted Manual Outbound (Loway term) | AMO | `hdr_amo` | Kept in English (product-specific) |
| AGAW | Agent real-time monitoring module (QueueMetrics-specific term) | AGAW | `td_dbtest_wz_agawcleanup`, `edit_record_agawqueue_title` | Kept in English (product-specific) |

---

## 2. Metrics & KPI acronyms

| Term | English meaning / context | Translation | Example label(s) | Notes |
|------|---------------------------|-------------|------------------|-------|
| SLA | Service Level Agreement — % of calls answered within target time | A.N.S. | `td_ancod_answered_calls_sla` | Pack uses "A.N.S." (Acuerdo de Nivel de Servicio) |
| SPH | Sales per Hour | VPH | `aout_index_sph` | Pack uses "VPH" (Ventas Por Hora) |
| CPH | Contacts per Hour | CPH | `aout_cph` | Kept in English |
| QCPH | Qualified Contacts per Hour | Contactos cual. por hora | `aout_index_qcph` | Full form used |
| DOW | Day Of Week | Día de la Semana | `cldst_ta_traffic_analysis_by_period_dow` | |

---

## 3. Quality / training / system acronyms

| Term | English meaning / context | Translation | Example label(s) | Notes |
|------|---------------------------|-------------|------------------|-------|
| QA | Quality Assurance (grading / scorecards) | Módulo QA | `art_lblQAForm` (QA Form) | |
| QC | Quality Control | QC | `ko_succ_q` | Kept in English |
| CBT | Computer-Based Training | CBTs | `hdr_cbt` (CBTs) | Kept in English |
| Prompt | A prompt for an AI model to perform QA | Prompt | `edit_qa_prompt`, `edit_record_qa_aiprompt` | New AI term; kept in English — verify against pack |

---

## 4. Common UI abbreviations

Keep the translation **abbreviated** too — these sit in tight table headers and
menus. Match the source's truncation style (trailing `.`).

| Term | Full form | Translation | Example label(s) | Notes |
|------|-----------|-------------|------------------|-------|
| Avg. | Average | Prom. | `aout_avg_sec` | |
| Max. | Maximum | Max. | `cldst_ta_ag_max` | |
| Min. | Minimum | Min. | (paired with Max.) | |
| Tot. | Total | Tiempo Tot. | `aout_tot_sec` (Tot. Time) | |
| Num. | Number | Num. | `propedit_key_phone_maxsessions` | Kept in English |
| Dur. | Duration | Duración | `clage_acd_duration` | |
| Att. | Attempts | Att. | `hdr_attempts` | |
| Ans. | Answered | Atendidas | `cldst_ans` | |
| Unans. | Unanswered | No atend. | `cldst_unans` | |
| Conv. | Conversation | Ftr. Conv. | `aout_ftrconv` (Ftr. Conv.) | |
| Qualif. | Qualified | Calif. | `td_calloutc_qualif` | |
| Cont. | Contacts | Cont. | `aout_contacts_n` | |
| Bill. | Billable | Facturable | `aout_billable_s` | |
| Succ. | Successful | Exitosos Cola | `ko_succ_q` (Succ.Q.) | |
| Short. | Short | Q Corta | `ko_sho_q` (Short.Q.) | |
| Ag. | Agent | Max. Ag. | `cldst_ta_ag_max` (Max Ag.) | |
| Ext. | Extension | Ext. | `art_localExtension` | |
| Ref. | Reference | Ref. N° | `ccase_case_xref` (Ref. #) | |
| sec. | seconds | Duración | `rt3_duration` (Duration (sec.)) | |

---

## 5. Telephony domain terms (full words)

The high-frequency vocabulary of the product. Pick one translation per term and
keep it consistent everywhere.

| Term | English meaning / context | Translation | Example label(s) | Notes |
|------|---------------------------|-------------|------------------|-------|
| Agent | Operator who handles calls | Agente | `td_agstatus_agent_is_currently_logged_off` | |
| Queue | Call queue | Cola | `td_ancod_answered_calls_agents_on_queue` | |
| Caller | The person calling in | Llamante | `carea_select_number_of_clid_digits_to_search` | |
| Call (answered) | Answered call | Llamadas contestadas | `td_ancod_answered_calls_details` | |
| Unanswered / Lost call | Call that was not answered | Llamadas no contestadas | `td_ancod_unanswered_calls_details`, `aout_fcr_detail_lost` | |
| Abandon(ed) | Caller hung up while waiting | Abandono | `td_cko_abandon` | |
| Hangup | Call termination | Desconexión | `td_callstatus_html_transferred` | |
| Wait time | Time spent queued before answer | Espera | `edit_record_agawqueue_avgwait` | |
| Talk time | Time spent in conversation | Tiempo Llamada | `qap_details_talk` | |
| Wrap-up | Post-call work time | Tiempo de Wrap-up | `td_autoconf_wz_queuewrapup` | |
| Pause | Agent paused / not taking calls | En pausa | `td_agawlogon_paused` | |
| Session | An agent's logged-on period | Sesiones | `td_ancod_agent_sessions_detail` | |
| Inbound / Outbound | Call direction | Entrante / Saliente | `aout_*` (Outbound), `aout_inforec` | |
| Transfer | Passing a call to another party | Transferido | `td_callstatus_html_transferred` | |
| Spill | Overflow call routed onward | Desborde | `td_aglev_spill` | |
| Ringing | Phone is ringing | Llamando | `evt_ringing` | |
| Extension | Phone extension number | Ext. | `art_localExtension` | |
| Skill | Agent skill / competency tag | Habilidades | `cldst_skills_per_day` | |
| Voicemail | Recorded message | Voicemail | `td_cko_timeout_voicemail` | Kept in English |
| Recall | Scheduled call-back | Programador de Rellamados | `art_lblWbRecallPanel` (Recall Scheduler) | |
| Supervisor | Agent overseer | Supervisor | `edit_ac_supervisor` | |
| Spy / Barge / Whisper | Live-call monitoring actions | Barge / Whisper | `rt3_actions_barge`, `rt3_actions_whisper` | Kept in English (technical terms) |
| Billable | Time/activity that is billed | Facturable | `aout_act_billable` | |
| Outcome | Result/disposition of a call | Resultado | `aout_call_res_by_outcome` | |
| Disposition | Coded call result / rule | Tipo de contactación | `aout_outcome` | |
| Tag | Call tag / label | Tag | `aout_calltag` | Kept in English |
| Realtime | Live monitoring view | Tiempo Real | `art_active_polling_error` | |
| Wallboard | Large real-time status display | Tablero | `rt3_delete_current_wallboard_confirm` | |
| Alarm | Threshold alert | Alarmas | `edit_record_agawqueue_title` (AGAW alarms) | |
| Threshold | Trigger value for alarms/SLA | Umbrales | `custrep_skills_valhrd` | |

---

## 6. General UI terms

Recurring application-chrome vocabulary. Worth fixing once for menu/button
consistency.

| Term | Context | Translation | Example label(s) | Notes |
|------|---------|-------------|------------------|-------|
| Report | Analysis output | Informe | `aout_*`, report menus | |
| Edit / Add / Delete / Create | CRUD actions on forms | Editar / Añadir / Eliminar / Crear | `*_edit`, `*_add`, `*_delete` | |
| Export | Export to CSV/PDF/XLS | Exportar | export buttons | |
| Configuration / Settings | Setup screens | Configuración | `*configuration*`, `*settings*` | |
| Visibility | Access/visibility key | Visibilidad | visibility-key labels | |
| Group | Agent / report grouping | Grupo | `clage_agent_performance_acd_group` | |
| Period | Time range of a report | Período | period selectors | |
| Status | Current state | Estado | `td_agstatus_*` | |
| Details / Detail | Drill-down view | Detalles | `td_ancod_answered_calls_details` | |
| Feature | Licensable capability | Característica | feature-key labels | |
| Password / User / Code | Login & identity fields | Contraseña / Usuario / Código | `td_autoconf_wz_agentpwd` | |

---

## 7. Doubts & items needing review

| Term | Issue | Seeded choice | Options to decide between |
|------|-------|---------------|---------------------------|
| SLA | Pack uses "A.N.S." abbreviation | A.N.S. | A.N.S. (Acuerdo de Nivel de Servicio) vs. SLA (if preferred internationally) |
| QCPH | Full form used instead of acronym | Contactos cual. por hora | Keep full form vs. use QCPH |
| Tot. | Pack uses "Tiempo Tot." (longer) | Tiempo Tot. | Tiempo Tot. vs. Tot. (shorter abbreviation) |
| Num. | English acronym kept | Num. | Keep Num. or use "Número"? |
| Unans. | Pack uses "No atend." | No atend. | No atend. vs. "Sin Respuesta" |
| Caller | Pack uses "Llamante" in some contexts | Llamante | Consistency: ensure used everywhere Caller appears |
| Disposition | Multiple possible translations | Tipo de contactación | Tipo de contactación vs. Disposición |
| Tag | Kept in English | Tag | Tag vs. Etiqueta or Marcador |
| Voicemail | Kept in English | Voicemail | Voicemail vs. Buzón de voz |
| Realtime | Full translation used | Tiempo Real | Tiempo Real vs. Realtime (kept English) |
| Barge / Whisper | Technical monitoring terms, kept English | Barge / Whisper | Keep English vs. translate to Spanish equivalents |
| Alarm | Used as "Alarmas AGAW" in context | Alarmas | Alarmas vs. Alerta |
| Ext. / Extension | Pack uses both "Ext." and "Extensión" | Ext. | Ensure consistency; standardize on one |
| MOH | Translated to full form | Música en Espera | Música en Espera vs. keep MOH |
| QC | Kept in English | QC | QC vs. Control de Calidad |
| CBT | Kept in English | CBTs | CBTs vs. Capacitación Basada en Computadora |
| Skill | Translated to "Habilidades" | Habilidades | Habilidades vs. Competencia or Destreza |
| Outcome | Pack sometimes uses "Resultado" | Resultado | Resultado vs. Desenlace |
| Recall | Full phrase used | Programador de Rellamados | Programador de Rellamados vs. Rellamada |
