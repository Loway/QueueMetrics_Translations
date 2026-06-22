# Glossary — QueueMetrics (de_DE)

German terminology master for QueueMetrics. Derived from
[glossary_en_US.md](glossary_en_US.md); see that file and
[CLAUDE.md](CLAUDE.md) for how the glossary is used.

> **Seeded from existing labels.** The **Translation** column was pre-filled with
> the terms **already in use** in [queuemetrics_de_DE.md](queuemetrics_de_DE.md)
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
| ACD | Automatic Call Distribution | ACD | `clage_agent_performance_acd_group` | Acronym kept; *Agentenleistung nach ACD-Gruppe* |
| IVR | Interactive Voice Response | Sprachdialog | `aout_inforec` | *Sprachdialog* used in pack |
| DNIS | Dialed Number Identification Service | DNIS | `cld_asterisk_dnis` | Kept in English |
| DID | Direct Inward Dialing | DID/DNIS | `fp_dnis_edit` | Rendered as *DID/DNIS-Leitungen* |
| CLID | Calling Line Identification | Anruferkennung | `carea_select_number_of_clid_digits_to_search` | Full form used |
| PBX | Private Branch Exchange | PBX | `pgag_popup_cannot_send_message` | Kept in English |
| MOH | Music On Hold | Wartemusik | `cld_asterisk_mohdur` | *Dauer der Wartemusik* |
| AMO | Assisted Manual Outbound | AMO | `hdr_amo` | Kept (Loway term) |
| AGAW | Agent real-time monitoring module | AGAW | `edit_record_agawqueue_title` | Kept (QueueMetrics term); *AGAW aufräumen*, *AGAW-Alarme* |

---

## 2. Metrics & KPI acronyms

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| SLA | Service Level Agreement | SLA | `td_ancod_answered_calls_sla` | Kept in English; *Qualitätsindex* also used |
| SPH | Sales per Hour | VPS | `aout_index_sph` | Expanded as *Verkäufe pro Stunde (VPS)* |
| CPH | Contacts per Hour | KPS | `aout_cph` | Rendered as *KPS* in pack |
| QCPH | Qualified Contacts per Hour | QKPS | `aout_index_qcph` | *Qualifizierte Kontakte pro Stunde* |
| DOW | Day Of Week | Wochentag | `cldst_ta_traffic_analysis_by_period_dow` | Full form; *pro Wochentag* |

---

## 3. Quality / training / system acronyms

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| QA | Quality Assurance | QA | `art_lblQAForm` | Kept; *QA Form* in pack |
| QC | Quality Control | QC | `ko_succ_q` | Kept in abbreviations like *Erfolgreiche Q.* |
| CBT | Computer-Based Training | CBT | `hdr_cbt` | Kept; *CBTs* in pack |

---

## 4. Common UI abbreviations

Keep the German abbreviated too (tight headers/menus).

| Term | Full form | Translation | Example label(s) | Notes |
|------|-----------|-------------|------------------|-------|
| Avg. | Average | Durchschnitt | `aout_avg_sec` | *Durchschnitt Sekunde*; no abbreviation in pack |
| Max. | Maximum | Max. | `cldst_ta_ag_max` | *Max Ag.* (no period) |
| Min. | Minimum | Min. | `aout_min_sec` | *Minimum* (full form) |
| Tot. | Total | Gesamtzeit | `aout_tot_sec` | *Gesamtzeit* used; also *Total* |
| Num. | Number | Anz. | `propedit_key_phone_maxsessions` | *Maximale Anzahl* (full form) |
| Dur. | Duration | Dauer | `clage_acd_duration` | *Dauer* (full form, no abbreviation) |
| Att. | Attempts | Versuche | `hdr_attempts` | *Versuche* (full form); some as *Att.* in labels |
| Ans. | Answered | Beantw. | `cldst_ans` | *Beantw.* (abbreviated) |
| Unans. | Unanswered | Unbeantw. | cldst_unans | *Unbeantw.* (abbreviated) |
| Conv. | Conversation | Konv. | `aout_ftrconv` | *Ftr. Konv.* (abbreviated) |
| Qualif. | Qualified | Qualif. | `td_calloutc_qualif` | *Qualif.* (kept abbreviated) |
| Cont. | Contacts | Cont. | `aout_contacts_n` | *Kontakte* or *Cont.* (inconsistent) |
| Bill. | Billable | Abrechnungsfähige | `aout_billable_s` | Full form; *Abrechnungsfähige Sekunden* |
| Succ. | Successful | Erfolgreiche | `ko_succ_q` | *Erfolgreiche Q.* (abbreviated Q) |
| Short. | Short | Kurzes | `ko_sho_q` | *Kurzes Q.* (abbreviated Q) |
| Ag. | Agent | Ag. | `cldst_ta_ag_max` | *Max Ag.* (no period after Ag in pack) |
| Ext. | Extension | Ext. | `art_localExtension` | *Ext.* (abbreviated) |
| Ref. | Reference | Ref. | `ccase_case_xref` | *Ref. Nr.* |
| sec. | seconds | sec. | `rt3_duration` | *Dauer* (full form; verify if sec. abbreviation used) |

---

## 5. Telephony domain terms (full words)

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| Agent | Operator | Agent | `td_agstatus_agent_is_currently_logged_off` | |
| Queue | Call queue | Warteschlange | `td_ancod_answered_calls_agents_on_queue` | *Angenommene Anrufe: Agenten in der Warteschlange* |
| Caller | Person calling in | Anrufer | `td_cko_caller_abandon` | *Abbruch durch Anrufer* |
| Call (answered) | Answered call | Angenommene Anrufe | `td_ancod_answered_calls_details` | *Angenommene Anrufe: Details* |
| Unanswered / Lost | Not answered | Nicht angenommene Anrufe | `td_ancod_unanswered_calls_details`, `aout_fcr_detail_lost` | *Nicht angenommene* vs *Verlorene Anrufe* (both used) |
| Abandon(ed) | Caller hung up while queued | Abbruch | `td_cko_abandon` | |
| Hangup | Call termination | Abgebrochenen | `aout_ivr_hangups` | *Abgebrochenen* (past participle) |
| Wait time | Queue time before answer | Wartezeit | `edit_record_agawqueue_avgwait` | *Durchschnittliche Wartezeit* |
| Talk time | Conversation time | Gesprächszeit | `qap_details_talk` | *Gesprächsdauer* |
| Wrap-up | Post-call work time | Nachbearbeitung | `td_autoconf_wz_queuewrapup` | *Nachbearbeitungszeit* |
| Pause | Agent not taking calls | Pause | `td_agawlogon_paused` | *Angehalten* in some labels (alternative phrasing) |
| Session | Logged-on period | Sitzung | `td_ancod_agent_sessions_detail` | *Agentensitzungen* |
| Inbound / Outbound | Call direction | Eingehend / Ausgehend | `td_qdir_inbound_calls`, `td_qdir_outbound_calls` | *Eingehende Gespräche* / *Ausgehende Gespräche* |
| Transfer | Pass call onward | Weiterleitung | `td_callstatus_html_transferred` | *Weitergeleitet*; *Übertragen auf* also used |
| Spill | Overflow call | Ersatz | `td_aglev_spill` | *Ersatz* (alternative for overflow level) |
| Ringing | Phone ringing | Klingeln | `evt_ringing` | |
| Extension | Phone extension | Nebenstelle | `art_localExtension` | *Ext.* (abbreviated form) |
| Skill | Agent competency | Fähigkeit | `cldst_skills_per_day` | *Fähigkeiten pro Tag* |
| Voicemail | Recorded message | Anrufbeantworter | `td_cko_timeout_voicemail` | *Zeitüberschreitung (Anrufbeantworter)* |
| Recall | Scheduled call-back | Abruf | `art_lblWbRecallPanel` | *Planer abrufen* (recall scheduler); terminology varies |
| Supervisor | Agent overseer | Supervisor | `edit_ac_supervisor` | Full form in pack |
| Barge / Whisper / Spy | Live-call monitoring | Unterbrechen / Flüstern / (Beobachten) | `rt3_actions_barge`, `rt3_actions_whisper` | *barge* kept English, *Flüstern* for whisper |
| Billable | Billed time/activity | Abrechnungsfähig | `aout_act_billable` | *Abrechnungsfähige Aktivitäten* |
| Outcome | Call result | Ergebnis | `aout_call_res_by_outcome` | *Gesprächsresultat, nach Ergebnis* |
| Disposition | Coded result / rule | Regeln | `cdp_clonedispositions` | *Regeln für die Entsorgung von Klonen* |
| Tag | Call tag | markiert | `aout_calltag` | *markiert* or *Markierung* |
| Realtime | Live view | Echtzeit | `art_active_polling_error` | *Echtzeitüberwachung* in context |
| Wallboard | Real-time display | Wallboard | `rt3_delete_current_wallboard_confirm` | Kept in English |
| Alarm | Threshold alert | Alarme | `edit_record_agawqueue_title` | *AGAW-Alarme* |
| Threshold | Trigger value | Schwellenwert | `custrep_skills_valhrd` | |

---

## 6. General UI terms

| Term | Context | Translation | Example label(s) | Notes |
|------|---------|-------------|------------------|-------|
| Report | Analysis output | Bericht | `aout_agent_report` | *Detaillierter Bericht des Agenten* |
| Edit / Add / Delete / Create | CRUD actions | Bearbeiten / Hinzufügen / Entfernen / Erstellen | `*_edit`, `*_add`, `*_delete` | Full forms used in pack; varies by context |
| Export | Export to file | Exportieren | `cld_btn_export_calls` | *Anrufe exportieren* |
| Configuration / Settings | Setup screens | Konfiguration | `td_synchronier_configuration` | |
| Visibility | Access/visibility key | Sichtbarkeit | visibility-key labels | Verify against pack |
| Group | Grouping | Gruppe | `clage_agent_performance_acd_group` | *Agentengruppe*, *ACD-Gruppe* |
| Period | Report time range | Zeitraum | `custrep_time_period` | |
| Status | Current state | Status | `td_agstatus_agent_status_cannot_be_determined` | *Agentenstatus* (compound) |
| Details / Detail | Drill-down view | Details | `td_ancod_answered_calls_details` | |
| Feature | Licensable capability | Funktion | `aout_feature` | *Funktion* or *Funktionscode* |
| Password / User / Code | Login & identity | Passwort / Benutzer / Code | `td_autoconf_wz_agentpwd`, `td_autoconf_wz_users` | |

---

## 7. Doubts & items needing review

Terms where the seeded value is uncertain or the existing pack is inconsistent.
Resolve each, then update the table above and remove the row here.

| Term | Issue | Seeded choice | Options to decide between |
|------|-------|---------------|---------------------------|
| Pause | Alternative phrasing in some labels | *Pause* | Keep *Pause*, or also accept *Angehalten* (halted) as variant |
| Unanswered / Lost | Two different translations used | *Nicht angenommene Anrufe* | Standardize between *Nicht angenommene* (unanswered) and *Verlorene Anrufe* (lost) |
| Avg. (Average) | Full form used, no abbreviation | *Durchschnitt* | Keep full form, or introduce abbreviated *Durchschn.* in tight headers |
| Cont. (Contacts) | Inconsistent: full form vs abbreviation | *Cont.* or *Kontakte* | Standardize between full *Kontakte* and abbreviated *Cont.* |
| Att. (Attempts) | May use both full and abbreviated forms | *Versuche* or *Att.* | Verify if *Att.* abbreviation actually used in pack |
| Inbound / Outbound | Verify exact phrasing in pack | *Eingehend / Ausgehend* | Confirm *Eingehende Gespräche* / *Ausgehende Gespräche* terminology |
| Spy (monitoring) | *barge* kept English; what about Spy? | (no German equivalent found) | Determine if *Beobachten*, *Abhören*, or keep English |
| Recall | Terminology varies in pack | *Abruf* | Verify if *Abruf* or *Rückruf* (callback) is preferred |
| Visibility | Not confirmed from pack labels | *Sichtbarkeit* | Search pack for actual visibility-key labels to verify term |
| sec. (seconds) | Pack may use full *Sekunde* | *sec.* | Verify if abbreviation is actually used in column headers |
