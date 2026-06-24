# Glossary — QueueMetrics (it_IT)

Italian terminology master for QueueMetrics. Derived from
[glossary_en_US.md](glossary_en_US.md); see that file and
[CLAUDE.md](CLAUDE.md) for how the glossary is used.

> **Seeded from existing labels.** The **Translation** column was pre-filled with
> the terms **already in use** in [queuemetrics_it_IT.md](queuemetrics_it_IT.md)
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
| ACD | Automatic Call Distribution | ACD | `clage_agent_performance_acd_group` | Acronym kept; used as-is in labels |
| IVR | Interactive Voice Response | IVR | `aout_inforec` | Italian pack keeps English |
| DNIS | Dialed Number Identification Service | DNIS | `cld_asterisk_dnis` | Kept in English |
| DID | Direct Inward Dialing | DID/DNIS | `fp_dnis_edit` | Rendered as *Linee DID/DNIS* |
| CLID | Calling Line Identification | CLID | `carea_select_number_of_clid_digits_to_search` | Used in tech context |
| PBX | Private Branch Exchange | PBX | `pgag_popup_cannot_send_message` | Kept in English |
| MOH | Music On Hold | Musica di attesa | `cld_asterisk_mohdur` | *Durata mus. attesa* |
| AMO | Assisted Manual Outbound | AMO | `hdr_amo` | Kept (Loway term) |
| AGAW | Agent real-time monitoring module | AGAW | `edit_record_agawqueue_title` | Kept (QueueMetrics-specific term) |

---

## 2. Metrics & KPI acronyms

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| SLA | Service Level Agreement | SLA | `td_ancod_answered_calls_sla` | Kept in English |
| SPH | Sales per Hour | SPH | `aout_index_sph` | Expanded as *Vendite all'ora (SPH)* |
| CPH | Contacts per Hour | CPH | `aout_cph` | Kept |
| QCPH | Qualified Contacts per Hour | QCPH | `aout_index_qcph` | Expanded as *Contatti qualificati per ora (QCPH)* |
| DOW | Day Of Week | Giorno della settimana | `cldst_ta_traffic_analysis_by_period_dow` | Full form used |

---

## 3. Quality / training / system acronyms

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| QA | Quality Assurance | QA | `art_lblQAForm` | Kept (*Modulo QA*) |
| QC | Quality Control | QC | `ko_succ_q` | Kept in labels |
| CBT | Computer-Based Training | CBT | `hdr_cbt` | Kept (*CBTs*) |
| Prompt | A prompt for an AI model to perform QA | Prompt | `edit_qa_prompt`, `edit_record_qa_aiprompt` | New AI term; kept in English — verify against pack |

---

## 4. Common UI abbreviations

Keep the Italian abbreviated too (tight headers/menus).

| Term | Full form | Translation | Example label(s) | Notes |
|------|-----------|-------------|------------------|-------|
| Avg. | Average | Media | `aout_avg_sec` | |
| Max. | Maximum | Max | `cldst_ta_ag_max` | |
| Min. | Minimum | Min. | `aout_min_sec` | |
| Tot. | Total | Tot. | `clage_acd_tot_calls` | *Tot chiam.* in some labels |
| Num. | Number | N. | `aout_fcr_n_calls` | *N. Chiam.* in labels |
| Dur. | Duration | Dur. | `clage_acd_duration` | |
| Att. | Attempts | Sq. | `hdr_attempts` | **Decided:** *Squilli* (ring attempts), abbreviated *Sq.* — distinct from *Tentativi* = retry/dial attempts |
| Ans. | Answered | Prs. | `aout_taken` | **Decided:** standardized on *Prese* / abbr. *Prs.* (was mixed *Risposte*/*Rsp.*) |
| Unans. | Unanswered | Perse | `cldst_unans` | |
| Conv. | Conversation | Conv. | `aout_ftrconv` | *Ftr Conv.* in labels |
| Qualif. | Qualified | Qualif. | `td_calloutc_qualif` | |
| Cont. | Contacts | Cont. | `aout_contacts_n` | |
| Bill. | Billable | Fatt. | `aout_billable_s` | *Fatt.* abbreviation |
| Succ. | Successful | Succ. | `ko_succ_q` | *Succ. Coda* |
| Short. | Short | Short. | `ko_sho_q` | *Short. Coda.* |
| Ag. | Agent | Ag. | `cldst_ta_ag_max` | *Max Ag.* |
| Ext. | Extension | Int | `art_localExtension` | Italian abbreviation *Int* |
| Ref. | Reference | Rif. | `ccase_case_xref` | *Rif. #* |
| sec. | seconds | sec. | `rt3_duration` | *Durata (sec.)* |

---

## 5. Telephony domain terms (full words)

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| Agent | Operator | Agente | `td_agstatus_agent_is_currently_logged_off` | |
| Queue | Call queue | Coda | `td_ancod_answered_calls_agents_on_queue` | |
| Caller | Person calling in | Chiamante | `td_cko_caller_abandon` | |
| Call (answered) | Answered call | Chiamate prese | `td_ancod_answered_calls_details` | |
| Unanswered / Lost | Not answered | Chiamate perse | `td_ancod_unanswered_calls_details`, `aout_fcr_detail_lost` | |
| Abandon(ed) | Caller hung up while queued | Abbandonata | `td_cko_abandon` | |
| Hangup | Call termination | Appeso | `aout_ivr_hangups` | |
| Wait time | Queue time before answer | Attesa media | `edit_record_agawqueue_avgwait` | *Tempo Medio Wait* |
| Talk time | Conversation time | Tempo chiamata | `qap_details_talk` | |
| Wrap-up | Post-call work time | Wrap-up | `td_autoconf_wz_queuewrapup` | **Decided:** kept in English |
| Pause | Agent not taking calls | Pausa | `td_agawlogon_paused` | *In pausa* |
| Session | Logged-on period | Sessione | `td_ancod_agent_sessions_detail` | |
| Inbound / Outbound | Call direction | Entranti / Uscenti | `aout_inforec` | **Decided** |
| Transfer | Pass call onward | Trasferita | `td_callstatus_html_transferred` | |
| Spill | Overflow call | Backup | `td_aglev_spill` | **Decided:** *Backup* |
| Ringing | Phone ringing | Squilla | `evt_ringing` | **Decided:** *Squilla* (was *Sta squillando*) |
| Extension | Phone extension | Interno | `art_localExtension` | Abbreviated as *Int* |
| Skill | Agent competency | Skill | `cldst_skills_per_day` | **Decided:** kept in English |
| Voicemail | Recorded message | Segreteria | `td_cko_timeout_voicemail` | |
| Recall | Scheduled call-back | Richiamata | `art_lblWbRecallPanel` | *Pianifica richiamata* |
| Supervisor | Agent overseer | Supervisore | `edit_ac_supervisor` | |
| Barge / Whisper / Spy | Live-call monitoring | Barge / Whisper | `rt3_actions_barge`, `rt3_actions_whisper` | Pack keeps English terms |
| Billable | Billed time/activity | Attività fatturabili | `aout_act_billable` | |
| Outcome | Call result | Outcome | `aout_call_res_by_outcome` | **Decided:** kept in English |
| Disposition | Coded result / rule | Disposition | `cdp_clonedispositions` | **Decided:** kept in English |
| Tag | Call tag | Tag | `aout_calltag` | Kept in English |
| Realtime | Live view | Tempo reale | `art_active_polling_error` | |
| Wallboard | Real-time display | Wallboard | `rt3_delete_current_wallboard_confirm` | **Decided:** kept in English |
| Alarm | Threshold alert | Allarmi | `edit_record_agawqueue_title` | *Allarmi AGAW* |
| Threshold | Trigger value | Soglie | `custrep_skills_valhrd` | |

---

## 6. General UI terms

| Term | Context | Translation | Example label(s) | Notes |
|------|---------|-------------|------------------|-------|
| Report | Analysis output | Report | `aout_agent_report` | To verify pack usage |
| Edit / Add / Delete / Create | CRUD actions | Modifica / Aggiungi / Elimina / Crea | `*_edit`, `*_add`, `*_delete` | |
| Export | Export to file | Esporta | `cld_btn_export_calls` | |
| Configuration / Settings | Setup screens | Configurazione | `td_synchronier_configuration` | |
| Visibility | Access/visibility key | Visibilità | visibility-key labels | **Decided:** *Visibilità* |
| Group | Grouping | Gruppo | `clage_agent_performance_acd_group` | |
| Period | Report time range | Periodo | `custrep_time_period` | |
| Status | Current state | Status | `td_agstatus_agent_status_cannot_be_determined` | |
| Details / Detail | Drill-down view | Dettaglio | `td_ancod_answered_calls_details` | |
| Feature | Licensable capability | Feature | `aout_feature` | **Decided:** kept in English |
| Password / User / Code | Login & identity | Password / Utente / Codice | `td_autoconf_wz_agentpwd`, `td_autoconf_wz_users` | |

---

## 7. Doubts & items needing review

Terms where the seeded value is uncertain or the existing pack is inconsistent.
Resolve each, then update the table above and remove the row here.

| Term | Issue | Seeded choice | Options to decide between |
|------|-------|---------------|---------------------------|
| Report | Not fully confirmed | *Report* | Verify if *Report* is used as-is or translated to *Rapporto* |
