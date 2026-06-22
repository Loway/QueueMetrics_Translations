# Glossary — QueueMetrics (fr_FR)

French terminology master for QueueMetrics. Derived from
[glossary_en_US.md](glossary_en_US.md); see that file and
[CLAUDE.md](CLAUDE.md) for how the glossary is used.

> **Seeded from existing labels.** The **Translation** column was pre-filled with
> the terms **already in use** in [queuemetrics_fr_FR.md](queuemetrics_fr_FR.md)
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
| ACD | Automatic Call Distribution | ACD | `clage_agent_performance_acd_group` | Acronym kept; some labels phrase it as *groupe de Files* |
| IVR | Interactive Voice Response | SVI | `aout_inforec` | Serveur Vocal Interactif |
| DNIS | Dialed Number Identification Service | SDA | `cld_asterisk_dnis` | Sélection Directe à l'Arrivée |
| DID | Direct Inward Dialing | SDA | `fp_dnis_edit` | Rendered *lignes SDA* (DID/DNIS) |
| CLID | Calling Line Identification | Numéro d'appelant | `carea_select_number_of_clid_digits_to_search` | |
| PBX | Private Branch Exchange | PBX | `pgag_popup_cannot_send_message` | Kept in English |
| MOH | Music On Hold | Musique de patience | `cld_asterisk_mohdur` | |
| AMO | Assisted Manual Outbound | AMO | `hdr_amo` | Kept (Loway term) |
| AGAW | Agent real-time monitoring module | AGAW | `edit_record_agawqueue_title` | Kept (QueueMetrics term) |

---

## 2. Metrics & KPI acronyms

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| SLA | Service Level Agreement | SLA | `td_ancod_answered_calls_sla` | Kept in English |
| SPH | Sales per Hour | SPH | `aout_index_sph` | Expanded as *Ventes par heure (SPH)* |
| CPH | Contacts per Hour | CPH | `aout_cph` | Kept |
| QCPH | Qualified Contacts per Hour | QCPH | `aout_index_qcph` | Expanded as *Contacts qualifiés par Heure (QCPH)* |
| DOW | Day Of Week | Jour de la semaine | `cldst_ta_traffic_analysis_by_period_dow` | |

---

## 3. Quality / training / system acronyms

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| QA | Quality Assurance | QA | `art_lblQAForm` | Kept (*Module QA*) |
| QC | Quality Control | QC | `ko_succ_q` | Kept |
| CBT | Computer-Based Training | CBT | `hdr_cbt` | Kept (*CBTs*) |

---

## 4. Common UI abbreviations

Keep the French abbreviated too (tight headers/menus).

| Term | Full form | Translation | Example label(s) | Notes |
|------|-----------|-------------|------------------|-------|
| Avg. | Average | Moy. | `aout_avg_sec` | |
| Max. | Maximum | Max | `cldst_ta_ag_max` | |
| Min. | Minimum | Min. | `aout_min_sec` | |
| Tot. | Total | Tot. | `clage_acd_tot_calls` | |
| Num. | Number | Nb | `aout_fcr_n_calls` | *Nb d'appels* |
| Dur. | Duration | Durée | `clage_acd_duration` | |
| Att. | Attempts | Tentatives | `hdr_attempts` | Existing pack uses full *Tentatives*; shorten to *Tent.* if space-constrained |
| Ans. | Answered | Répondus | `aout_taken` | Consider *Rép.* in tight headers |
| Unans. | Unanswered | Non répondus | `cldst_unans` | Pack also uses *Pas répondus* — pick one |
| Conv. | Conversation | Conv. | `aout_ftrconv` | |
| Qualif. | Qualified | Qualif. | `td_calloutc_qualif` | |
| Cont. | Contacts | Cont. | `aout_contacts_n` | |
| Bill. | Billable | Facturable | `aout_billable_s` | No abbreviation in pack |
| Succ. | Successful | Succ. | `ko_succ_q` | |
| Short. | Short | Court. | `ko_sho_q` | |
| Ag. | Agent | Ag. | `cldst_ta_ag_max` | |
| Ext. | Extension | Ext. | `art_localExtension` | |
| Ref. | Reference | Ref. | `ccase_case_xref` | *Ref. N°* |
| sec. | seconds | sec. | `rt3_duration` | *Durée (sec.)* |

---

## 5. Telephony domain terms (full words)

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| Agent | Operator | Agent | `td_agstatus_agent_is_currently_logged_off` | |
| Queue | Call queue | File | `td_ancod_answered_calls_agents_on_queue` | *File(s)* |
| Caller | Person calling in | Appelant | `td_cko_caller_abandon` | |
| Call (answered) | Answered call | Appel répondu | `td_ancod_answered_calls_details` | |
| Unanswered / Lost | Not answered | Appel non répondu | `td_ancod_unanswered_calls_details`, `aout_fcr_detail_lost` | Pack mixes *non répondu* / *non-répondu* — standardize |
| Abandon(ed) | Caller hung up while queued | Abandon | `td_cko_abandon` | |
| Hangup | Call termination | Raccroché | `aout_ivr_hangups` | |
| Wait time | Queue time before answer | Durée d'attente | `edit_record_agawqueue_avgwait` | |
| Talk time | Conversation time | Temps de parole | `qap_details_talk` | |
| Wrap-up | Post-call work time | Wrap-up | `td_autoconf_wz_queuewrapup` | ⚠️ Pack keeps English (*Temps de wrap-up*); consider *Post-appel* |
| Pause | Agent not taking calls | Pause | `td_agawlogon_paused` | *En pause* |
| Session | Logged-on period | Session | `td_ancod_agent_sessions_detail` | |
| Inbound / Outbound | Call direction | Entrant / Sortant | `aout_inforec` | Verify against pack |
| Transfer | Pass call onward | Transfert | `td_callstatus_html_transferred` | *Transféré* |
| Spill | Overflow call | Débordement | `td_aglev_spill` | |
| Ringing | Phone ringing | Sonnerie | `evt_ringing` | |
| Extension | Phone extension | Extension | `art_localExtension` | *Ext.* |
| Skill | Agent competency | Compétence | `cldst_skills_per_day` | |
| Voicemail | Recorded message | Boîte vocale | `td_cko_timeout_voicemail` | |
| Recall | Scheduled call-back | Rappel | `art_lblWbRecallPanel` | |
| Supervisor | Agent overseer | Superviseur | `edit_ac_supervisor` | |
| Barge / Whisper / Spy | Live-call monitoring | Couper la parole / Susurrer / Espionner | `rt3_actions_barge`, `rt3_actions_whisper` | Verify *Espionner* in pack |
| Billable | Billed time/activity | Facturable | `aout_act_billable` | |
| Outcome | Call result | Issue (d'appel) | `aout_call_res_by_outcome` | |
| Disposition | Coded result / rule | Disposition | `cdp_clonedispositions` | *règles de disposition* |
| Tag | Call tag | Marqueur | `aout_calltag` | |
| Realtime | Live view | Temps réel | `art_active_polling_error` | |
| Wallboard | Real-time display | Tableau de bord | `rt3_delete_current_wallboard_confirm` | |
| Alarm | Threshold alert | Alarme | `edit_record_agawqueue_title` | |
| Threshold | Trigger value | Seuil | `custrep_skills_valhrd` | |

---

## 6. General UI terms

| Term | Context | Translation | Example label(s) | Notes |
|------|---------|-------------|------------------|-------|
| Report | Analysis output | Rapport | `aout_agent_report` | |
| Edit / Add / Delete / Create | CRUD actions | Éditer / Ajouter / Supprimer / Créer | `*_edit`, `*_add`, `*_delete` | |
| Export | Export to file | Exporter | `cld_btn_export_calls` | |
| Configuration / Settings | Setup screens | Configuration | `td_synchronier_configuration` | |
| Visibility | Access/visibility key | Visibilité | visibility-key labels | Verify against pack |
| Group | Grouping | Groupe | `clage_agent_performance_acd_group` | |
| Period | Report time range | Période | `custrep_time_period` | |
| Status | Current state | Statut | `td_agstatus_agent_status_cannot_be_determined` | |
| Details / Detail | Drill-down view | Détails | `td_ancod_answered_calls_details` | |
| Feature | Licensable capability | Fonction | `aout_feature` | |
| Password / User / Code | Login & identity | Mot de passe / Utilisateur / Code | `td_autoconf_wz_agentpwd`, `td_autoconf_wz_users` | |

---

## 7. Doubts & items needing review

Terms where the seeded value is uncertain or the existing pack is inconsistent.
Resolve each, then update the table above and remove the row here.

| Term | Issue | Seeded choice | Options to decide between |
|------|-------|---------------|---------------------------|
| Wrap-up | Pack keeps the English word | *Wrap-up* (*Temps de wrap-up*) | Keep English, or adopt *Post-appel* / *Temps de post-traitement* |
| Unanswered | Pack is inconsistent | *Non répondus* | *Non répondus* vs *Pas répondus* — pick one everywhere |
| Att. (Attempts) | No abbreviation in pack | *Tentatives* | Keep full, or shorten to *Tent.* in tight headers |
| Ans. (Answered) | No abbreviation in pack | *Répondus* | Keep full, or shorten to *Rép.* in tight headers |
| ACD | Acronym vs phrasing | *ACD* | Keep acronym, or phrase as *groupe de Files* like some labels |
| Inbound / Outbound | Not confirmed from a label | *Entrant / Sortant* | Verify the wording actually used in the pack |
| Spy (monitoring) | Not confirmed from a label | *Espionner* | Verify against the pack's live-monitoring labels |
| Visibility | Not confirmed from a label | *Visibilité* | Verify against the visibility-key labels |
