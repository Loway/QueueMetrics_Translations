# Glossary — QueueMetrics (ca_ES)

Catalan terminology master for QueueMetrics. Derived from
[glossary_en_US.md](glossary_en_US.md); see that file and
[CLAUDE.md](CLAUDE.md) for how the glossary is used.

> **Seeded from existing labels.** The **Translation** column was pre-filled with
> the terms **already in use** in [queuemetrics_ca_ES.md](queuemetrics_ca_ES.md)
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
| ACD | Automatic Call Distribution | ACD | `clage_agent_performance_acd_group` | Kept in English |
| IVR | Interactive Voice Response | IVR | `aout_inforec` | Kept in English |
| DNIS | Dialed Number Identification Service | DNIS | `cld_asterisk_dnis` | Kept in English |
| DID | Direct Inward Dialing | DID/DNIS | `fp_dnis_edit` | Rendered as "Editar línies DID/DNIS" |
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
| SPH | Sales per Hour | SPH | `aout_index_sph` | Expanded as "Vendes per hora (SPH)" |
| CPH | Contacts per Hour | CPH | `aout_cph` | Kept in English |
| QCPH | Qualified Contacts per Hour | QCPH | `aout_index_qcph` | Expanded as "Contactes qualificats per hora (QCPH)" |
| DOW | Day Of Week | Dia de la setmana | `cldst_ta_traffic_analysis_by_period_dow` | |

---

## 3. Quality / training / system acronyms

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| QA | Quality Assurance | QA | `art_lblQAForm` | Kept in English (rendered "Formulari QA") |
| QC | Quality Control | Succ. Q | `ko_succ_q` | Verify against pack |
| CBT | Computer-Based Training | CBTs | `hdr_cbt` | Kept in English |

---

## 4. Common UI abbreviations

Keep the translation **abbreviated** too — these sit in tight table headers and
menus. Match the source's truncation style (trailing `.`).

| Term | Full form | Translation | Example label(s) | Notes |
|------|-----------|-------------|------------------|-------|
| Avg. | Average | Mitjana | `aout_avg_sec` | No period in Catalan |
| Max. | Maximum | Max. | `cldst_ta_ag_max` | Kept abbreviation |
| Min. | Minimum | Min. | (paired with Max.) | Verify against pack |
| Tot. | Total | Total | `aout_tot_sec` | Full word used |
| Num. | Number | Núm. | `propedit_key_phone_maxsessions` | Verify against pack |
| Dur. | Duration | Duració | `clage_acd_duration` | Full word used |
| Att. | Attempts | Intents | `hdr_attempts` | Full word used |
| Ans. | Answered | Ateses | `cldst_ans` | Full word used |
| Unans. | Unanswered | No ateses | `cldst_unans` | Full phrase |
| Conv. | Conversation | Conv. | `aout_ftrconv` | Abbreviated as in English |
| Qualif. | Qualified | Qualif. | `td_calloutc_qualif` | Abbreviated as in English |
| Cont. | Contacts | Contacte | `aout_contacts_n` | Full word used |
| Bill. | Billable | Facturable | `aout_billable_s` | Full word used |
| Succ. | Successful | Succ. | `ko_succ_q` | Abbreviated as in English |
| Short. | Short | Curt | `ko_sho_q` | Full word used |
| Ag. | Agent | Ag. | `cldst_ta_ag_max` | Verify against pack |
| Ext. | Extension | Ext. | `art_localExtension` | Abbreviated as in English |
| Ref. | Reference | Ref. # | `ccase_case_xref` | Seeded as alien (verify) |
| sec. | seconds | Duració | `rt3_duration` | Full word used |

---

## 5. Telephony domain terms (full words)

The high-frequency vocabulary of the product. Pick one translation per term and
keep it consistent everywhere.

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| Agent | Operator who handles calls | Agent | `td_agstatus_agent_is_currently_logged_off` | Verify against pack |
| Queue | Call queue | Cua | `td_ancod_answered_calls_agents_on_queue` | Verify against pack |
| Caller | The person calling in | Trucant | `td_cko_caller_abandon` | Seeded as "Abandonament del Trucant" |
| Call (answered) | Answered call | Trucada | `td_ancod_answered_calls_details` | Verify against pack |
| Unanswered / Lost call | Call that was not answered | Trucades perdudes | `td_ancod_unanswered_calls_details`, `aout_fcr_detail_lost` | |
| Abandon(ed) | Caller hung up while waiting | Abandon | `td_cko_abandon` | |
| Hangup | Call termination | Penjades | `aout_ivr_hangups` | Verify translation |
| Wait time | Time spent queued before answer | Temps mitjà d'espera | `edit_record_agawqueue_avgwait` | Full phrase used |
| Talk time | Time spent in conversation | Temps de conversa | `qap_details_talk` | Seeded as alien (verify) |
| Wrap-up | Post-call work time | Temps administratiu | `td_autoconf_wz_queuewrapup` | |
| Pause | Agent paused / not taking calls | En pausa | `td_agawlogon_paused` | Full phrase |
| Session | An agent's logged-on period | Sessió | `td_ancod_agent_sessions_detail` | Verify against pack |
| Inbound / Outbound | Call direction | Inbound / Outbound | `aout_*` | Verify against pack |
| Transfer | Passing a call to another party | Transferit | `td_callstatus_html_transferred` | |
| Spill | Overflow call routed onward | Vessament | `td_aglev_spill` | |
| Ringing | Phone is ringing | Trucant | `evt_ringing` | |
| Extension | Phone extension number | Ext. | `art_localExtension` | Abbreviated |
| Skill | Agent skill / competency tag | Habilitat | `cldst_skills_per_day` | Verify against pack |
| Voicemail | Recorded message | Voicemail | `td_cko_timeout_voicemail` | Verify against pack |
| Recall | Scheduled call-back | Re-trucada | `art_lblWbRecallPanel` | Seeded as "Programador de Re-trucades" |
| Supervisor | Agent overseer | Supervisor | `edit_ac_supervisor` | |
| Spy / Barge / Whisper | Live-call monitoring actions | Intromissió / Xiuxiuejar | `rt3_actions_barge`, `rt3_actions_whisper` | Seeded as alien (verify) |
| Billable | Time/activity that is billed | Temps productiu | `aout_act_billable` | Full phrase |
| Outcome | Result/disposition of a call | Resultat | `aout_call_res_by_outcome` | Verify against pack |
| Disposition | Coded call result / rule | Disposició | (no key found) | Verify against pack |
| Tag | Call tag / label | Etiqueta | `aout_calltag` | |
| Realtime | Live monitoring view | Realtime | `art_active_polling_error` | Verify against pack |
| Wallboard | Large real-time status display | Quadre de comandament | `rt3_delete_current_wallboard_confirm` | Seeded as alien (verify) |
| Alarm | Threshold alert | Alarma | `edit_record_agawqueue_title` | Verify against pack |
| Threshold | Trigger value for alarms/SLA | Llindar | (no key found) | Verify against pack |

---

## 6. General UI terms

Recurring application-chrome vocabulary. Worth fixing once for menu/button
consistency.

| Term | Context | Translation | Example label(s) | Notes |
|------|---------|-------------|------------------|-------|
| Report | Analysis output | Informe | `aout_*`, report menus | Verify against pack |
| Edit / Add / Delete / Create | CRUD actions on forms | Editar / Afegir / Eliminar | `*_edit`, `*_add`, `*_delete` | Verify against pack |
| Export | Export to CSV/PDF/XLS | Exportar | export buttons | Verify against pack |
| Configuration / Settings | Setup screens | Configuració | `*configuration*`, `*settings*` | Verify against pack |
| Visibility | Access/visibility key | Visibilitat | visibility-key labels | Verify against pack |
| Group | Agent / report grouping | Grup | `clage_agent_performance_acd_group` | Verify against pack |
| Period | Time range of a report | Període | period selectors | Verify against pack |
| Status | Current state | Estat | `td_agstatus_*` | Verify against pack |
| Details / Detail | Drill-down view | Detall | `td_ancod_answered_calls_details` | Full word used |
| Feature | Licensable capability | Característica | feature-key labels | Verify against pack |
| Password / User / Code | Login & identity fields | Contrasenya / Usuari / Codi | `td_autoconf_wz_agentpwd` | Verify against pack |

---

## 7. Doubts & items needing review

Per-language glossaries add rows here for any term whose translation is
uncertain or whose existing pack is inconsistent.

| Term | Issue | Seeded choice | Options to decide between |
|------|-------|---------------|---------------------------|
| QC | Appears with "Q" suffix in pack; unclear if Quality Control or kept-English | Succ. Q | Clarify whether "Q" stands for "Qualitat" or if it's kept-English |
| Min. | Minimum — not found in pack, assumed parallel to Max. | Min. | Verify if pack uses equivalent |
| Tot. | Total — pack uses full word "Temps total" not abbreviated | Total | Keep full or abbreviate? |
| Num. | Number — not found in pack under different keys; assumed standard abbreviation | Núm. | Verify or use full word "Nombre" |
| Ag. | Agent abbreviation — not found directly; assumed from "Max. Ag." pattern | Ag. | Verify or use full word |
| sec. | Pack uses "Duració" for duration context, not literal "seg." | Duració | Verify abbreviation standard |
| Agent | Core term — not directly found; assumed from context | Agent | Verify consistent usage |
| Queue | Core term — not directly found under different key patterns | Cua | Verify consistent usage |
| Call | Assumed from "Trucada" in context | Trucada | Verify consistent usage |
| Hangup | Pack uses "Penjades" — verify this is correct translation | Penjades | Clarify if "Penjada" or alternative term preferred |
| Talk time | Seeded as alien from pack; needs human review | Temps de conversa | Verify preferred term |
| Session | Not directly found; assumed standard term | Sessió | Verify or use alternative |
| Inbound / Outbound | Not found as standalone entries in pack | Inbound / Outbound | Verify or provide pack translations |
| Skill | Seeded from "Habilitats" in context | Habilitat | Verify singular/plural consistency |
| Voicemail | Assumed kept English; verify if localized option exists | Voicemail | Check if translation needed |
| Spy / Barge / Whisper | All seeded as alien translations; need review | Intromissió / Xiuxiuejar | Verify standard telephony terms in Catalan |
| Disposition | Not found in pack; standard term guessed | Disposició | Verify or use alternative |
| Realtime | Assumed kept English; verify localization | Realtime | Check if alternative exists |
| Wallboard | Seeded as alien; awkward translation | Quadre de comandament | Verify or propose alternative |
| Alarm | Not verified; assumed from context | Alarma | Verify consistency in pack |
| Threshold | Not found; assumed standard term | Llindar | Verify or use alternative |
| Report | Not directly verified; assumed standard term | Informe | Verify consistency across pack |
| Group | Seeded from context; verify consistency | Grup | Verify all "group" contexts use this |
| Details / Detail | Both forms found; verify usage distinction | Detall | Check if separate singular/plural needed |
| Feature | Seeded from pack; verify consistency | Característica | Verify all feature contexts |
| Password / User / Code | Not all verified individually | Contrasenya / Usuari / Codi | Verify each independently in pack |
