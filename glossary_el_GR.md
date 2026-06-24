# Glossary — QueueMetrics (el_GR)

Greek terminology master for QueueMetrics. Derived from
[glossary_en_US.md](glossary_en_US.md); see that file and
[CLAUDE.md](CLAUDE.md) for how the glossary is used.

> **Seeded from existing labels.** The **Translation** column was pre-filled with
> the terms **already in use** in [queuemetrics_el_GR.md](queuemetrics_el_GR.md)
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
| ACD | Automatic Call Distribution | ACD | `clage_agent_performance_acd_group` | Acronym kept |
| IVR | Interactive Voice Response | IVR | `aout_inforec` | |
| DNIS | Dialed Number Identification Service | DNIS | `cld_asterisk_dnis` | |
| DID | Direct Inward Dialing | DID | `fp_dnis_edit` | Rendered *Γραμμές DID/DNIS* |
| CLID | Calling Line Identification | Ταυτότητα Καλούντος | `carea_select_number_of_clid_digits_to_search` | |
| PBX | Private Branch Exchange | PBX | `pgag_popup_cannot_send_message` | Kept in English |
| MOH | Music On Hold | Μουσική Αναμονής | `cld_asterisk_mohdur` | |
| AMO | Assisted Manual Outbound | AMO | `hdr_amo` | Kept (Loway term) |
| AGAW | Agent real-time monitoring module | AGAW | `edit_record_agawqueue_title` | Kept (QueueMetrics term) |

---

## 2. Metrics & KPI acronyms

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| SLA | Service Level Agreement | SLA | `td_ancod_answered_calls_sla` | Kept in English |
| SPH | Sales per Hour | Πωλήσεις ανά ώρα | `aout_index_sph` | Full expanded form used |
| CPH | Contacts per Hour | CPH | `aout_cph` | Kept |
| QCPH | Qualified Contacts per Hour | Qualified Contacts ανά ώρα | `aout_index_qcph` | Kept in English for qualification part |
| DOW | Day Of Week | Ημέρα της εβδομάδας | `cldst_ta_traffic_analysis_by_period_dow` | |

---

## 3. Quality / training / system acronyms

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| QA | Quality Assurance | QA | `art_lblQAForm` | Kept (*Φόρμα QA*) |
| QC | Quality Control | QC | `ko_succ_q` | Kept |
| CBT | Computer-Based Training | CBTs | `hdr_cbt` | Kept |
| Prompt | A prompt for an AI model to perform QA | Prompt | `edit_qa_prompt`, `edit_record_qa_aiprompt` | New AI term; kept in English — verify against pack |

---

## 4. Common UI abbreviations

Keep the Greek abbreviated too (tight headers/menus).

| Term | Full form | Translation | Example label(s) | Notes |
|------|-----------|-------------|------------------|-------|
| Avg. | Average | Μέσ. όρ. | `aout_avg_sec` | |
| Max. | Maximum | Μέγ. | `cldst_ta_ag_max` | |
| Min. | Minimum | Ελάχ. | `aout_min_sec` | |
| Tot. | Total | Συνόλ. | `aout_tot_sec` | Full form *Συνόλ. χρον.* used in some labels |
| Num. | Number | Αρ. | `propedit_key_phone_maxsessions` | Full form *Αριθμός* or *Αρ.* used |
| Dur. | Duration | Διάρκ. | `clage_acd_duration` | |
| Att. | Attempts | Απόπειρ. | `hdr_attempts` | |
| Ans. | Answered | Απαντημ. | `cldst_ans` | |
| Unans. | Unanswered | Αναπάντ. | `cldst_unans` | |
| Conv. | Conversation | Αναφ. Μετατρ. | `aout_ftrconv` | Abbreviated as "Feature Conversion" |
| Qualif. | Qualified | Τεκμηριωμένες | `td_calloutc_qualif` | |
| Cont. | Contacts | Επαφ. | `aout_contacts_n` | |
| Bill. | Billable | Χρεώσ. | `aout_billable_s` | |
| Succ. | Successful | Succ.Q. | `ko_succ_q` | Kept partial English |
| Short. | Short | Short.Q. | `ko_sho_q` | Kept partial English |
| Ag. | Agent | Αριθμ. χρηστών | `cldst_ta_ag_max` | Full form used in pack |
| Ext. | Extension | Εσωτ. | `art_localExtension` | |
| Ref. | Reference | Αριθμός αναφοράς | `ccase_case_xref` | Full form used |
| sec. | seconds | Διάρκεια (δευτ.) | `rt3_duration` | Full form used in context |

---

## 5. Telephony domain terms (full words)

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| Agent | Operator | Χρήστης | `td_agstatus_agent_is_currently_logged_off` | Also *Agent* in some contexts |
| Queue | Call queue | Ουρά αναμονής | `td_ancod_answered_calls_agents_on_queue` | |
| Caller | Person calling in | Καλών | `td_cko_caller_abandon` | |
| Call (answered) | Answered call | Απαντημένες κλήσεις | `td_ancod_answered_calls_details` | |
| Unanswered / Lost | Not answered | Αναπάντητες κλήσεις | `td_ancod_unanswered_calls_details`, `aout_fcr_detail_lost` | *Χαμένες κλήσεις* also used |
| Abandon(ed) | Caller hung up while queued | Εγκαταλήφθηκε | `td_cko_abandon` | |
| Hangup | Call termination | Τερματισμός κλήσης | `aout_ivr_hangups` | |
| Wait time | Queue time before answer | Μέσος χρόνος αναμονής | `edit_record_agawqueue_avgwait` | |
| Talk time | Conversation time | Χρόνος Ομιλίας | `qap_details_talk` | |
| Wrap-up | Post-call work time | Χρόνος wrap-up | `td_autoconf_wz_queuewrapup` | Kept English term |
| Pause | Agent not taking calls | Σε παύση | `td_agawlogon_paused` | |
| Session | Logged-on period | Συνεδρίες χρήστη | `td_ancod_agent_sessions_detail` | |
| Inbound / Outbound | Call direction | Εισερχόμενη / Εξερχόμενη | `aout_inforec` | Verify against pack |
| Transfer | Pass call onward | Μεταφέρθηκε | `td_callstatus_html_transferred` | |
| Spill | Overflow call | Υπέρβαση | `td_aglev_spill` | |
| Ringing | Phone ringing | Κουδουνισμός | `evt_ringing` | |
| Extension | Phone extension | Εσωτ. | `art_localExtension` | Abbreviated form |
| Skill | Agent competency | Δεξιότητες | `cldst_skills_per_day` | |
| Voicemail | Recorded message | Τέλος χρόνου (μήνυμα τηλεφωνητή) | `td_cko_timeout_voicemail` | Full context-specific form used |
| Recall | Scheduled call-back | Προγραμματισμός επανακλήσεων | `art_lblWbRecallPanel` | |
| Supervisor | Agent overseer | Επιβλέπων | `edit_ac_supervisor` | |
| Barge / Whisper / Spy | Live-call monitoring | Παρέμβαση (Barge-in) / Ψυθιρισμός | `rt3_actions_barge`, `rt3_actions_whisper` | Verify *Spy* in pack |
| Billable | Billed time/activity | Χρεώσιμες ενέργειες | `aout_act_billable` | |
| Outcome | Call result | Αποτελέσματα κλήσεων ανά τύπο επαφής | `aout_call_res_by_outcome` | Full form used |
| Disposition | Coded result / rule | Κανόνες διάθεσης κλώνων | `cdp_clonedispositions` | |
| Tag | Call tag | Tag | `aout_calltag` | Kept in English |
| Realtime | Live view | Πραγματικός χρόνος | `art_active_polling_error` | |
| Wallboard | Real-time display | Wallboard | `rt3_delete_current_wallboard_confirm` | Kept in English (product feature name) |
| Alarm | Threshold alert | Συναγερμοί AGAW | `edit_record_agawqueue_title` | Context-specific with AGAW |
| Threshold | Trigger value | Όριο | `custrep_skills_valhrd` | |

---

## 6. General UI terms

| Term | Context | Translation | Example label(s) | Notes |
|------|---------|-------------|------------------|-------|
| Report | Analysis output | Αναφορά | `hdr_qa_report` | |
| Edit / Add / Delete / Create | CRUD actions | Επεξεργασία / Προσθήκη / Διαγραφή / Δημιουργία | `*_edit`, `*_add`, `*_delete` | |
| Export | Export to file | Εξαγωγή | `propedit_feature_misc_export` | |
| Configuration / Settings | Setup screens | Παραμετροποίηση | `td_synchronier_configuration` | |
| Visibility | Access/visibility key | Ορατότητα | visibility-key labels | Verify against pack |
| Group | Grouping | Ομάδα | `clage_agent_performance_acd_group` | |
| Period | Report time range | Χρονική περίοδος | `custrep_time_period` | |
| Status | Current state | Κατάσταση | `td_agstatus_agent_is_currently_logged_on` | |
| Details / Detail | Drill-down view | Λεπτομέρειες | `td_ancod_answered_calls_details` | |
| Feature | Licensable capability | Feature | `aout_feature` | Kept in English (product jargon) |
| Password / User / Code | Login & identity | Κωδικός / Χρήστης / Κωδικός | `td_autoconf_wz_agentpwd`, `qa_frm_user` | |

---

## 7. Doubts & items needing review

Terms where the seeded value is uncertain or the existing pack is inconsistent.
Resolve each, then update the table above and remove the row here.

| Term | Issue | Seeded choice | Options to decide between |
|------|-------|---------------|---------------------------|
| SPH | Pack uses full expanded form | *Πωλήσεις ανά ώρα* | Keep expanded form or abbreviate for tight headers |
| CLID | Not directly seeded; derived from label context | *Ταυτότητα Καλούντος* | Verify standard Greek term for "Calling Line ID" |
| Tot. | Full form used in some labels; check if abbreviation exists elsewhere | *Συνόλ.* or *Συνόλ. χρον.* | Standardize on which variant |
| Num. | Pack uses full form *Αριθμός*; verify abbreviation | *Αρ.* | Keep abbreviated or use full *Αριθμός* everywhere |
| Ag. | Pack uses *Αριθμ. χρηστών* (not strictly "Agent" abbreviation) | *Αριθμ. χρηστών* | Verify correct abbreviation for *Agent* |
| Inbound / Outbound | Not directly confirmed in pack; inferred from context | *Εισερχόμενη / Εξερχόμενη* | Verify exact pack terminology |
| Voicemail | Pack uses context-specific form; verify standalone term | *Μήνυμα τηλεφωνητή* or *Τηλεφωνητής* | Verify standard term when not in context |
| Spy (monitoring) | Not confirmed from a live-monitoring label | *Κατασκοπεία* or similar | Verify against the pack's live-monitoring labels |
| Visibility | Not directly confirmed in pack | *Ορατότητα* | Verify against the visibility-key labels in pack |
| Feature | Kept in English; verify if Greek term used elsewhere | *Feature* | Verify if Greek term is ever used in pack |
| Wallboard | Kept in English as product feature name | *Wallboard* | Verify if this is consistently kept in English |
| Outcome | Full expanded label form used; verify standalone term | *Αποτέλεσμα* or *Αποτελέσματα* | Standardize on singular/plural and context |
| Disposition | Pack uses full context-specific form | *Διάθεση* or *Κανόνες διάθεσης* | Verify standalone terminology |
| Tag | Kept in English | *Tag* | Verify if Greek term ever used in pack |
| Wrap-up | Pack keeps English | *Wrap-up* | Consider Greek alternative like *Μετα-επεξεργασία* or keep English |
