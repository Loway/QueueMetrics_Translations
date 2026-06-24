# Glossary — QueueMetrics (hu_HU)

Hungarian terminology master for QueueMetrics. Derived from
[glossary_en_US.md](glossary_en_US.md); see that file and
[CLAUDE.md](CLAUDE.md) for how the glossary is used.

> **Seeded from existing labels.** The **Translation** column was pre-filled with
> the terms **already in use** in [queuemetrics_hu_HU.md](queuemetrics_hu_HU.md)
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
| ACD | Automatic Call Distribution | ACD | `clage_agent_performance_acd_group` | Kept as acronym; paired with "Ügynök teljesítmény" |
| IVR | Interactive Voice Response | IVR | `aout_inforec` | Kept in English |
| DNIS | Dialed Number Identification Service | DNIS | `cld_asterisk_dnis` | Kept in English |
| DID | Direct Inward Dialing | DID | `fp_dnis_edit` | Kept; rendered as *DID/DNIS vonalak* |
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
| SPH | Sales per Hour | SPH | `aout_index_sph` | Kept; expanded as *óránkénti eladások (SPH)* |
| CPH | Contacts per Hour | CPH | `aout_cph` | Kept in English |
| QCPH | Qualified Contacts per Hour | QCPH | `aout_index_qcph` | Kept; expanded as *Ellenőrzött óránkénti kapcsolatok (CPH)* |
| DOW | Day Of Week | Napi forgalom | `cldst_ta_traffic_analysis_by_period_dow` | Expanded in context |

---

## 3. Quality / training / system acronyms

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| QA | Quality Assurance | QA | `art_lblQAForm` | Kept (*QA űrlap*) |
| QC | Quality Control | QC | `ko_succ_q` | Kept |
| CBT | Computer-Based Training | CBT | `hdr_cbt` | Kept (*CBT-k*) |
| Prompt | A prompt for an AI model to perform QA | Prompt | `edit_qa_prompt`, `edit_record_qa_aiprompt` | New AI term; kept in English — verify against pack |

---

## 4. Common UI abbreviations

Keep the Hungarian abbreviated too (tight headers/menus).

| Term | Full form | Translation | Example label(s) | Notes |
|------|-----------|-------------|------------------|-------|
| Avg. | Average | átlagérték | `aout_avg_sec` | No period abbreviation in pack |
| Max. | Maximum | Max | `cldst_ta_ag_max` | Abbreviated; paired with *Ügyn.* |
| Min. | Minimum | Min. | `aout_min_sec` | From pack search |
| Tot. | Total | Teljes | `aout_tot_sec` | Rendered as *Teljes idő* |
| Num. | Number | szám | `aout_fcr_n_calls` | Used as *száma* / *számú* in context |
| Dur. | Duration | Időtartam | `clage_acd_duration` | Full form without abbreviation |
| Att. | Attempts | Szűrve | `hdr_attempts` | Pack shows *Próbálkozások* elsewhere; inconsistent |
| Ans. | Answered | Fogad. | `cldst_ans` | Abbreviated |
| Unans. | Unanswered | Válaszolatlan. | `cldst_unans` | Abbreviated with period |
| Conv. | Conversation | Ftr. Konv. | `aout_ftrconv` | Abbreviated |
| Qualif. | Qualified | Jogos. | `td_calloutc_qualif` | Abbreviated |
| Cont. | Contacts | Kapcsolat | `aout_contacts_n` | Full form |
| Bill. | Billable | Számla | `aout_billable_s` | Short form |
| Succ. | Successful | Siker.Q. | `ko_succ_q` | Abbreviated |
| Short. | Short | Rövid.Q. | `ko_sho_q` | Abbreviated |
| Ag. | Agent | Ügyn. | `cldst_ta_ag_max` | Abbreviated; paired with *Max* |
| Ext. | Extension | Mellék | `art_localExtension` | Full form; *Ext.* abbreviation used elsewhere |
| Ref. | Reference | Ref. # | `ccase_case_xref` | With hash symbol |
| sec. | seconds | mp. | `rt3_duration` | *Időtartam (mp.)* |

---

## 5. Telephony domain terms (full words)

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| Agent | Operator | Közvetítő | `td_agstatus_agent_is_currently_logged_off` | Alternate: *Ügynök* used in some labels |
| Queue | Call queue | Sor | `td_ancod_answered_calls_agents_on_queue` | *Sor(ok)* |
| Caller | Person calling in | Hívó | `td_cko_caller_abandon` | |
| Call (answered) | Answered call | Fogadott hívás | `td_ancod_answered_calls_details` | *Fogadott* |
| Unanswered / Lost | Not answered | Nem fogadott hívás | `td_ancod_unanswered_calls_details`, `aout_fcr_detail_lost` | *Elveszett hívások* in some contexts |
| Abandon(ed) | Caller hung up while queued | Elhagy | `td_cko_abandon` | |
| Hangup | Call termination | Beszélgetés bontások | `aout_ivr_hangups` | Literally "conversation breaks" |
| Wait time | Queue time before answer | Átlagos Várakozási Idő | `edit_record_agawqueue_avgwait` | Full phrase in pack |
| Talk time | Conversation time | Beszélgetési idő | `qap_details_talk` | |
| Wrap-up | Post-call work time | Lezárási idő | `td_autoconf_wz_queuewrapup` | Alien translation |
| Pause | Agent not taking calls | Szünetelve | `td_agawlogon_paused` | |
| Session | Logged-on period | Gyűlés | `td_ancod_agent_sessions_detail` | *Közvetítő gyűlés* |
| Inbound / Outbound | Call direction | Entrant / Kimenő | `aout_inforec` | *Outbound* evident from context; verify inbound |
| Transfer | Pass call onward | Átszállítva | `td_callstatus_html_transferred` | |
| Spill | Overflow call | Kiesés | `td_aglev_spill` | |
| Ringing | Phone ringing | Csörgés | `evt_ringing` | |
| Extension | Phone extension | Mellék | `art_localExtension` | |
| Skill | Agent competency | Képességek | `cldst_skills_per_day` | *Képességek naponta* |
| Voicemail | Recorded message | Hangposta | `td_cko_timeout_voicemail` | |
| Recall | Scheduled call-back | Visszahívás | `art_lblWbRecallPanel` | |
| Supervisor | Agent overseer | Felügyelő | `edit_ac_supervisor` | |
| Barge / Whisper / Spy | Live-call monitoring | Beszélgetésbeavatkozás / Súgás | `rt3_actions_barge`, `rt3_actions_whisper` | Pack has only first two; spy not found |
| Billable | Billed time/activity | Számlázási Tevékenységek | `aout_act_billable` | Full phrase |
| Outcome | Call result | Eredmény | `aout_call_res_by_outcome` | *Eredmény lekérése* |
| Disposition | Coded result / rule | Elrendezési Szabályok | `cdp_clonedispositions` | *Klónozási Elrendezési Szabályok* |
| Tag | Call tag | Címke | `aout_calltag` | |
| Realtime | Live view | Valós idő | `art_active_polling_error` | Pack phrase unclear; verify |
| Wallboard | Real-time display | Falitábla | `rt3_delete_current_wallboard_confirm` | |
| Alarm | Threshold alert | Riasztások | `edit_record_agawqueue_title` | *AGAW riasztások* |
| Threshold | Trigger value | Küszöbérték | `custrep_skills_valhrd` | |

---

## 6. General UI terms

| Term | Context | Translation | Example label(s) | Notes |
|------|---------|-------------|------------------|-------|
| Report | Analysis output | Jelentés | `aout_agent_report` | *Részletes közvetítői jelentés* |
| Edit / Add / Delete / Create | CRUD actions | Szerkesztés / Hozzáadás / Törlés / Létrehozás | `*_edit`, `*_add`, `*_delete` | Pack uses *Szerkesztése* (Edit), *Hozzáadás* (Add), *Törlés* (Delete) |
| Export | Export to file | Exportálás | `cld_btn_export_calls` | *Hívások exportálása* |
| Configuration / Settings | Setup screens | Konfiguráció | `td_synchronier_configuration` | *Konfiguráció* (alien) |
| Visibility | Access/visibility key | Láthatósági kulcs | visibility-key labels | *Láthatósági kulcs* used consistently |
| Group | Grouping | Csoport | `clage_agent_performance_acd_group` | *Ügynökcsoport* / *ACD csoportonként* |
| Period | Report time range | Időszak | `custrep_time_period` | |
| Status | Current state | Állapot | `td_agstatus_agent_status_cannot_be_determined` | *Ügynök állapota* |
| Details / Detail | Drill-down view | Részletek | `td_ancod_answered_calls_details` | |
| Feature | Licensable capability | Funkció | `aout_feature` | |
| Password / User / Code | Login & identity | Jelszó / Felhasználó / Kód | `td_autoconf_wz_agentpwd`, `td_autoconf_wz_users` | |

---

## 7. Doubts & items needing review

Terms where the seeded value is uncertain or the existing pack is inconsistent.
Resolve each, then update the table above and remove the row here.

| Term | Issue | Seeded choice | Options to decide between |
|------|-------|---------------|---------------------------|
| Agent | Two variants used | *Közvetítő* | *Közvetítő* vs *Ügynök* — standardize throughout |
| Att. (Attempts) | Pack shows inconsistency | *Szűrve* | Verify actual usage; *Próbálkozások* appears elsewhere |
| Num. (Number) | No abbreviation in pack | *szám* | Decide if abbreviation is needed; context-dependent use |
| Inbound | Not directly found | *Entrant* | Verify against pack; usually inferred from *Outbound* labels |
| Spy (monitoring) | Key not found in pack | — | Not found; may not be needed for hu_HU |
| Realtime | Context unclear | *Valós idő* | Verify from *art_active_polling_error* context |
| Barge / Whisper / Spy | Only two found | *Beszélgetésbeavatkozás / Súgás* | Verify if all three terms are used in hu_HU pack |
| Create | Not explicitly found | *Létrehozás* | Verify against standard UI patterns in pack |
| Unanswered | Mixed forms | *Nem fogadott hívás* | *Nem fogadott* vs *Válaszolatlan* — determine standard form |
