# Glossary — QueueMetrics (nl_NL)

Dutch terminology master for QueueMetrics. Derived from
[glossary_en_US.md](glossary_en_US.md); see that file and
[CLAUDE.md](CLAUDE.md) for how the glossary is used.

> **Seeded from existing labels.** The **Translation** column was pre-filled with
> the terms **already in use** in [queuemetrics_nl_NL.md](queuemetrics_nl_NL.md)
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
| IVR | Interactive Voice Response | IVR | `aout_inforec` | Kept in English |
| DNIS | Dialed Number Identification Service | DNIS | `cld_asterisk_dnis` | Kept in English |
| DID | Direct Inward Dialing | DID/DNIS | `fp_dnis_edit` | Rendered *DID/DNIS lijnen* |
| CLID | Calling Line Identification | CLID | `carea_select_number_of_clid_digits_to_search` | Kept in English |
| PBX | Private Branch Exchange | PBX | `pgag_popup_cannot_send_message` | Kept in English |
| MOH | Music On Hold | MOH | `cld_asterisk_mohdur` | Kept in English |
| AMO | Assisted Manual Outbound | AMO | `hdr_amo` | Kept (Loway term) |
| AGAW | Agent real-time monitoring module | AGAW | `edit_record_agawqueue_title` | Kept (QueueMetrics term) |

---

## 2. Metrics & KPI acronyms

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| SLA | Service Level Agreement | SLA | `td_ancod_answered_calls_sla` | Kept in English |
| SPH | Sales per Hour | SPH | `aout_index_sph` | Kept in English |
| CPH | Contacts per Hour | CPH | `aout_cph` | Kept in English |
| QCPH | Qualified Contacts per Hour | QCPH | `aout_index_qcph` | Kept in English |
| DOW | Day Of Week | DOW | `cldst_ta_traffic_analysis_by_period_dow` | Kept in English |

---

## 3. Quality / training / system acronyms

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| QA | Quality Assurance | QA | `art_lblQAForm` | Kept (*QM formulier*) |
| QC | Quality Control | QC | `ko_succ_q` | Kept |
| CBT | Computer-Based Training | CBT | `hdr_cbt` | Kept |

---

## 4. Common UI abbreviations

Keep the Dutch abbreviated too (tight headers/menus).

| Term | Full form | Translation | Example label(s) | Notes |
|------|-----------|-------------|------------------|-------|
| Avg. | Average | Gem. | `aout_avg_sec` | |
| Max. | Maximum | Max | `cldst_ta_ag_max` | |
| Min. | Minimum | Min. | `aout_min_sec` | |
| Tot. | Total | Tot. | `aout_tot_sec` | |
| Num. | Number | Num. | `propedit_key_phone_maxsessions` | Verify against pack |
| Dur. | Duration | Duur | `clage_acd_duration` | |
| Att. | Attempts | Pogingen | `hdr_attempts` | Full word, not abbreviated |
| Ans. | Answered | Antw. | `cldst_ans` | |
| Unans. | Unanswered | Onbeantw. | `cldst_unans` | |
| Conv. | Conversation | Conv. | `aout_ftrconv` | Kept in English |
| Qualif. | Qualified | Qualif. | `td_calloutc_qualif` | |
| Cont. | Contacts | Gespr. | `aout_contacts_n` | *Gespr.* = short for *Gespreken* |
| Bill. | Billable | Facturable | `aout_billable_s` | No abbreviation in pack |
| Succ. | Successful | Succ. | `ko_succ_q` | Kept in English |
| Short. | Short | Kort. | `ko_sho_q` | |
| Ag. | Agent | Ag. | `cldst_ta_ag_max` | Kept in English |
| Ext. | Extension | Tst. | `art_localExtension` | *Tst.* = *Toestel* |
| Ref. | Reference | Ref. | `ccase_case_xref` | Kept in English |
| sec. | seconds | sec. | `rt3_duration` | Kept in English |

---

## 5. Telephony domain terms (full words)

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| Agent | Operator | Agent | `td_agstatus_agent_is_currently_logged_off` | |
| Queue | Call queue | Wachtrij | `td_ancod_answered_calls_agents_on_queue` | |
| Caller | Person calling in | Beller | `td_cko_caller_abandon` | Verify exact wording |
| Call (answered) | Answered call | Beantwoord gesprek | `td_ancod_answered_calls_details` | |
| Unanswered / Lost | Not answered | Onbeantwoord | `td_ancod_unanswered_calls_details`, `aout_fcr_detail_lost` | |
| Abandon(ed) | Caller hung up while queued | Abandon | `td_cko_abandon` | |
| Hangup | Call termination | Afgebroken | `aout_ivr_hangups` | |
| Wait time | Queue time before answer | Wachttijd | `edit_record_agawqueue_avgwait` | Verify exact phrasing |
| Talk time | Conversation time | Gesprekstijd | `qap_details_talk` | |
| Wrap-up | Post-call work time | Wrap-up tijd | `td_autoconf_wz_queuewrapup` | Kept English term |
| Pause | Agent not taking calls | Status | `td_agawlogon_paused` | Pack uses *Status* for pause |
| Session | Logged-on period | Sessie | `td_ancod_agent_sessions_detail` | |
| Inbound / Outbound | Call direction | Inkomend / Uitgaand | `aout_inforec` | Verify exact wording |
| Transfer | Pass call onward | Transferred | `td_callstatus_html_transferred` | Kept in English |
| Spill | Overflow call | Spill | `td_aglev_spill` | Kept in English |
| Ringing | Phone ringing | Bellen | `evt_ringing` | |
| Extension | Phone extension | Toestel | `art_localExtension` | *Tst.* abbreviated |
| Skill | Agent competency | Vaardigheid | `cldst_skills_per_day` | |
| Voicemail | Recorded message | Voicemail | `td_cko_timeout_voicemail` | Kept in English |
| Recall | Scheduled call-back | Terugbel planning | `art_lblWbRecallPanel` | |
| Supervisor | Agent overseer | Leidinggevende | `edit_ac_supervisor` | |
| Barge / Whisper / Spy | Live-call monitoring | Binnenvallen / Fluisteren / Espionage | `rt3_actions_barge`, `rt3_actions_whisper` | Verify full set |
| Billable | Billed time/activity | Facturabeel | `aout_act_billable` | Verify exact term |
| Outcome | Call result | Uitkomst | `aout_call_res_by_outcome` | |
| Disposition | Coded result / rule | Disposition | `cdp_clonedispositions` | Kept in English |
| Tag | Call tag | Tag | `aout_calltag` | |
| Realtime | Live view | Realtime | `art_active_polling_error` | Kept in English |
| Wallboard | Real-time display | Wallboard | `rt3_delete_current_wallboard_confirm` | Kept in English |
| Alarm | Threshold alert | Alarm | `edit_record_agawqueue_title` | Verify in pack |
| Threshold | Trigger value | Drempel | `custrep_skills_valhrd` | |

---

## 6. General UI terms

| Term | Context | Translation | Example label(s) | Notes |
|------|---------|-------------|------------------|-------|
| Report | Analysis output | Rapportage | `aout_agent_report` | |
| Edit / Add / Delete / Create | CRUD actions | Bewerken / Toevoegen / Verwijderen / Creëren | `*_edit`, `*_add`, `*_delete` | Verify exact forms |
| Export | Export to file | Export | `cld_btn_export_calls` | |
| Configuration / Settings | Setup screens | Configuratie | `td_synchronier_configuration` | |
| Visibility | Access/visibility key | Zichtbaarheidssleutel | visibility-key labels | Verify exact term |
| Group | Grouping | Groep | `clage_agent_performance_acd_group` | |
| Period | Report time range | Tijds periode | `custrep_time_period` | |
| Status | Current state | Status | `td_agstatus_agent_is_currently_logged_off` | |
| Details / Detail | Drill-down view | Details | `td_ancod_answered_calls_details` | |
| Feature | Licensable capability | Code | `aout_feature` | |
| Password / User / Code | Login & identity | Wachtwoord / Gebruiker / Code | `td_autoconf_wz_agentpwd` | Verify exact terms |

---

## 7. Doubts & items needing review

Terms where the seeded value is uncertain or the existing pack is inconsistent.
Resolve each, then update the table above and remove the row here.

| Term | Issue | Seeded choice | Options to decide between |
|------|-------|---------------|---------------------------|
| Num. | Not confirmed in pack | Num. | Verify if used as abbreviation or kept as-is |
| Caller | No direct label found | Beller | Verify exact term used (*Beller*, *Aanroeper*, *Inbeller*) |
| Wait time | Phrase not directly seeded | Wachttijd | Verify exact phrase (*Wachttijd*, *Gemiddelde wachttijd*, etc.) |
| Inbound / Outbound | Not confirmed from single label | Inkomend / Uitgaand | Verify exact Dutch terms used for call direction |
| Barge / Whisper / Spy | Only Binnenvallen/Fluisteren seeded | Binnenvallen / Fluisteren / Espionage | Verify if "Spy" is used; confirm full set of monitoring actions |
| Billable | Exact form uncertain | Facturabeel | Verify if *Facturabeel* or *Facturable* is preferred |
| Alarm | Pack usage uncertain | Alarm | Verify if used in AGAW context or elsewhere |
| Visibility | Not confirmed | Zichtbaarheidssleutel | Verify exact terminology in visibility-key labels |
| Edit/Add/Delete/Create | Forms not all seeded | Bewerken / Toevoegen / Verwijderen / Creëren | Verify exact Dutch terms used for CRUD actions |
| Feature | Context-dependent | Code | Verify if "Feature" = "Code" in QueueMetrics context |
