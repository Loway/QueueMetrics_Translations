# Glossary — QueueMetrics (ro_RO)

Romanian terminology master for QueueMetrics. Derived from
[glossary_en_US.md](glossary_en_US.md); see that file and
[CLAUDE.md](CLAUDE.md) for how the glossary is used.

> **Seeded from existing labels.** The **Translation** column was pre-filled with
> the terms **already in use** in [queuemetrics_ro_RO.md](queuemetrics_ro_RO.md)
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

| Term | English meaning / context | Translation | Example label(s) | Notes |
|------|---------------------------|-------------|------------------|-------|
| ACD | Automatic Call Distribution — the routing engine that assigns calls to agents | ACD | `clage_agent_performance_acd_group` | Kept in English; also rendered as *grup ACD* |
| IVR | Interactive Voice Response — the automated voice menu | IVR | `aout_inforec` | Kept in English |
| DNIS | Dialed Number Identification Service — the number that was called | DNIS | `cld_asterisk_dnis` | Kept in English |
| DID | Direct Inward Dialing — a directly-reachable inbound number | DID/DNIS | `fp_dnis_edit` | Kept in English; label phrase includes both |
| CLID | Calling Line Identification — the caller's number / caller-ID | CLID | `carea_select_number_of_clid_digits_to_search` | Kept in English |
| PBX | Private Branch Exchange — the phone system QueueMetrics monitors | PBX | `pgag_popup_cannot_send_message` | Kept in English |
| MOH | Music On Hold | Muzică în așteptare | `cld_asterisk_mohdur` | *Durata MOH (muzică în așteptare)* |
| AMO | Assisted Manual Outbound (Loway term) | AMO | `hdr_amo` | Kept in English (product-specific) |
| AGAW | Agent real-time monitoring module (QueueMetrics-specific term) | AGAW | `edit_record_agawqueue_title` | Kept in English (product-specific term) |

---

## 2. Metrics & KPI acronyms

| Term | English meaning / context | Translation | Example label(s) | Notes |
|------|---------------------------|-------------|------------------|-------|
| SLA | Service Level Agreement — % of calls answered within target time | SLA | `td_ancod_answered_calls_sla` | Kept in English |
| SPH | Sales per Hour | SPH | `aout_index_sph` | Expanded as *Vânzări pe oră (SPH)* |
| CPH | Contacts per Hour | CPH | `aout_cph` | Kept in English |
| QCPH | Qualified Contacts per Hour | QCPH | `aout_index_qcph` | Expanded as *Contacte calificate pe oră (QCPH)* |
| DOW | Day Of Week | Ziua săptămânii | `cldst_ta_traffic_analysis_by_period_dow` | |

---

## 3. Quality / training / system acronyms

| Term | English meaning / context | Translation | Example label(s) | Notes |
|------|---------------------------|-------------|------------------|-------|
| QA | Quality Assurance (grading / scorecards) | QA | `art_lblQAForm` | Kept in English; *Formular QA* |
| QC | Quality Control | QC | `ko_succ_q` | Kept in English (used in abbreviations) |
| CBT | Computer-Based Training | CBT-uri | `hdr_cbt` | Alien translation; needs review |

---

## 4. Common UI abbreviations

Keep the translation **abbreviated** too — these sit in tight table headers and
menus. Match the source's truncation style (trailing `.`).

| Term | Full form | Translation | Example label(s) | Notes |
|------|-----------|-------------|------------------|-------|
| Avg. | Average | Media | `aout_avg_sec` | |
| Max. | Maximum | Max. | `cldst_ta_ag_max` | Kept abbreviated |
| Min. | Minimum | Min. | (paired with Max.) | Kept abbreviated |
| Tot. | Total | Durata totala | `aout_tot_sec` | Needs truncation for headers |
| Num. | Number | Nr. | `propedit_key_phone_maxsessions` | Standard abbreviation |
| Dur. | Duration | Durata | `clage_acd_duration` | |
| Att. | Attempts | Incer. | `hdr_attempts` | Abbreviated form used |
| Ans. | Answered | Preluate | `cldst_ans` | Full word in pack; needs abbreviation |
| Unans. | Unanswered | Nepreluate | `cldst_unans` | Full word in pack; needs abbreviation |
| Conv. | Conversation | Cod conversie | `aout_ftrconv` | Needs abbreviation |
| Qualif. | Qualified | Calif. | `td_calloutc_qualif` | Abbreviated form used |
| Cont. | Contacts | Contacte | `aout_contacts_n` | Full word in pack; needs abbreviation |
| Bill. | Billable | Productiv | `aout_billable_s` | Full word; needs abbreviation for headers |
| Succ. | Successful | Succ.Q. | `ko_succ_q` | Abbreviated; partial form in use |
| Short. | Short | Scurte.Q. | `ko_sho_q` | Abbreviated; alien translation |
| Ag. | Agent | Ag. | `cldst_ta_ag_max` | Kept abbreviated |
| Ext. | Extension | Ext. | `art_localExtension` | Kept abbreviated |
| Ref. | Reference | Ref. # | `ccase_case_xref` | Alien translation; used as *Ref. #* |
| sec. | seconds | sec. | `rt3_duration` | Used as *Durată (sec.)* |

---

## 5. Telephony domain terms (full words)

The high-frequency vocabulary of the product. Pick one translation per term and
keep it consistent everywhere.

| Term | English meaning / context | Translation | Example label(s) | Notes |
|------|---------------------------|-------------|------------------|-------|
| Agent | Operator who handles calls | Agent | `td_agstatus_agent_is_currently_logged_off` | |
| Queue | Call queue | Coada | `td_ancod_answered_calls_agents_on_queue` | Also used in label contexts |
| Caller | The person calling in | Apelant | `td_cko_caller_abandon` | *Abandon apelant* |
| Call (answered) | Answered call | Apel preluat | `td_ancod_answered_calls_details` | Expanded in labels as *Apeluri preluate: Detalii* |
| Unanswered / Lost call | Call that was not answered | Apel nepreluat | `td_ancod_unanswered_calls_details` | Used as *Apeluri nepreluate* |
| Abandon(ed) | Caller hung up while waiting | Abandon | `td_cko_abandon` | |
| Hangup | Call termination | Închise | `aout_ivr_hangups` | IVR-specific context |
| Wait time | Time spent queued before answer | Durata de așteptare | `edit_record_agawqueue_avgwait` | *Durata medie de așteptare* |
| Talk time | Time spent in conversation | Timp de Vorbire | `qap_details_talk` | Alien translation |
| Wrap-up | Post-call work time | Timp de impachetare | `td_autoconf_wz_queuewrapup` | |
| Pause | Agent paused / not taking calls | În pauza | `td_agawlogon_paused` | |
| Session | An agent's logged-on period | Sesiune | `td_ancod_agent_sessions_detail` | *Sesiuni agent: Detalii* |
| Inbound / Outbound | Call direction | Inbound / Outbound | `aout_*` | English terms kept in context |
| Transfer | Passing a call to another party | Transfer | `td_callstatus_html_transferred` | |
| Spill | Overflow call routed onward | Depășire | `td_aglev_spill` | |
| Ringing | Phone is ringing | Sună | `evt_ringing` | |
| Extension | Phone extension number | Ext. | `art_localExtension` | Abbreviated form |
| Skill | Agent skill / competency tag | Abilități | `cldst_skills_per_day` | Alien translation; needs review |
| Voicemail | Recorded message | Voice mail | `td_cko_timeout_voicemail` | English term; in context *Depășire timp (voice mail)* |
| Recall | Scheduled call-back | Programare reapelări | `art_lblWbRecallPanel` | |
| Supervisor | Agent overseer | Supraveghetor | `edit_ac_supervisor` | Alien translation |
| Spy / Barge / Whisper | Live-call monitoring actions | Intruziune / Șoaptă | `rt3_actions_barge`, `rt3_actions_whisper` | Alien translations for both |
| Billable | Time/activity that is billed | Productiv | `aout_act_billable` | Antonym *Neproductive* for non-billable |
| Outcome | Result/disposition of a call | Rezultat | `aout_call_res_by_outcome` | |
| Disposition | Coded call result / rule | Dispoziție | `cdp_clonedispositions` | Alien translation; not verified |
| Tag | Call tag / label | Etichetă | `aout_calltag` | |
| Realtime | Live monitoring view | Realtime | `art_active_polling_error` | English term kept |
| Wallboard | Large real-time status display | Wallboard | `rt3_delete_current_wallboard_confirm` | English term kept (alien translation) |
| Alarm | Threshold alert | Alarme | `edit_record_agawqueue_title` | *Alarme AGAW* |
| Threshold | Trigger value for alarms/SLA | Prag | `custrep_skills_valhrd` | Alien translation |

---

## 6. General UI terms

Recurring application-chrome vocabulary. Worth fixing once for menu/button
consistency.

| Term | Context | Translation | Example label(s) | Notes |
|------|---------|-------------|------------------|-------|
| Report | Analysis output | Raport | `aout_*`, report menus | General UI term |
| Edit / Add / Delete / Create | CRUD actions on forms | Editare / Adăugare / Ștergere / Creare | `*_edit`, `*_add`, `*_delete` | Alien translations for most |
| Export | Export to CSV/PDF/XLS | Export | export buttons | *Export apeluri*, *Exporta ca* |
| Configuration / Settings | Setup screens | Configurare / Setări | `*configuration*`, `*settings*` | Alien translations; mixed usage |
| Visibility | Access/visibility key | Vizibilitate | visibility-key labels | |
| Group | Agent / report grouping | Grup | `clage_agent_performance_acd_group` | *Grup ACD* context |
| Period | Time range of a report | Perioada | period selectors | |
| Status | Current state | Stare | `td_agstatus_*` | *Stare agent*, *Stare apel* |
| Details / Detail | Drill-down view | Detalii | `td_ancod_answered_calls_details` | |
| Feature | Licensable capability | Funcție | feature-key labels | Alien translations used |
| Password / User / Code | Login & identity fields | Parolă / Utilizator / Cod | `td_autoconf_wz_agentpwd` | Mixed translations; alien for most |

---

## 7. Doubts & items needing review

| Term | Issue | Seeded choice | Options to decide between |
|------|-------|---------------|---------------------------|
| CBT | Pack uses alien translation *CBT-uri*; uncertain if correct | CBT-uri | Instructie bazata pe calculator / CBT (acronym kept) |
| Skill | Pack uses alien *Abilități*; inconsistent with other technical terms | Abilități | Abilități / Competență / Skill (keep English) |
| Disposition | Pack has alien *Dispoziție* but not verified against common usage | Dispoziție | Dispoziție / Rezultat codificat / Disposition (keep English) |
| QC | Part of *Succ.Q.* abbreviation; uncertain if QC should be abbreviated or expanded | (in Succ.Q. context) | QC / Control de Calitate / Keep English |
| Tot. | Used as full word *Durata totala* not abbreviated; headers need truncation | Durata totala (needs **Dur. Tot.**) | Dur. Tot. / Total (abbrev) / Totală (abbrev) |
| Ans./Unans. | Pack uses full words; headers need abbreviation | Preluate / Nepreluate | **Prel.** / **Neprel.** / **Răsp.** / **Nerăsp.** (Answered/Unanswered) |
| Conv. | Pack uses *Cod conversie* (conversion code); needs to distinguish from abbreviation for Conversation | Cod conversie | Conversație / Cod conversie (already clear) — keep as-is |
| Bill./Billable | Pack mixes *Productiv* and *Neproductive*; abbreviations needed | Productiv / Neproductive | **Prod.** / **Neprod.** / **Fac.** / **Nefac.** (Facturabil) |
| Suit. | Pack has *Succ.Q.* and *Scurte.Q.* (alien); unclear standard form | Succ.Q. / Scurte.Q. | Reîntrebare standardizată: Reușit.Î. / Scurt.Î. (Q = Question/Întrebare) |
| Ref. | Pack uses *Ref. #* but not confirmed across all contexts | Ref. # | **Ref.** / **Ref. #** / Referință / Referință # |
| Wallboard | English term kept (alien); decision needed on translation | Wallboard | Panou de Control / Tablă de Bord / Wallboard (keep English) |
| Realtime | English term kept; decide on translation | Realtime | Timp Real / În Timp Real / Realtime (keep English) |
| Talk time | Alien translation *Timp de Vorbire*; check against context | Timp de Vorbire | Timp de convorbire / Timp de Vorbire / Conversație (time) |
| Barge/Whisper | Alien translations *Intruziune* / *Șoaptă*; uncertain if correct technical terms | Intruziune / Șoaptă | Verify against QM documentation / industry standard |
| Supervisor | Alien translation *Supraveghetor*; may conflict with other contexts | Supraveghetor | Supraveghetor / Responsabil / Conducător |
| Spam/Skill per Day | Pack has alien *Abilități pe zi*; confirm meaning | Abilități pe zi | Abilități pe zi / Competențe pe zi / Skills per Day (keep English) |

