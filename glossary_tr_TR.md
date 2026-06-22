# Glossary — QueueMetrics (tr_TR)

Turkish terminology master for QueueMetrics. Derived from
[glossary_en_US.md](glossary_en_US.md); see that file and
[CLAUDE.md](CLAUDE.md) for how the glossary is used.

> **Seeded from existing labels.** The **Translation** column was pre-filled with
> the terms **already in use** in [queuemetrics_tr_TR.md](queuemetrics_tr_TR.md)
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
| DID | Direct Inward Dialing | DID/DNIS | `fp_dnis_edit` | Rendered as *DID /DNIS hatlar* |
| CLID | Calling Line Identification | CLID | `carea_select_number_of_clid_digits_to_search` | Kept in English |
| PBX | Private Branch Exchange | PBX | `pgag_popup_cannot_send_message` | Kept in English |
| MOH | Music On Hold | Bekletme süresi | `cld_asterisk_mohdur` | |
| AMO | Assisted Manual Outbound | AMO | `hdr_amo` | Kept (Loway term) — marked alien |
| AGAW | Agent real-time monitoring module | AGAW | `edit_record_agawqueue_title` | Kept (QueueMetrics term) |

---

## 2. Metrics & KPI acronyms

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| SLA | Service Level Agreement | SLA | `td_ancod_answered_calls_sla` | Kept in English |
| SPH | Sales per Hour | SPH | `aout_index_sph` | Kept; pack expands as *Saatlik Satışlar (SPH)* |
| CPH | Contacts per Hour | CPH | `aout_cph` | Kept in English |
| QCPH | Qualified Contacts per Hour | QCPH | `aout_index_qcph` | Kept; pack expands as *Saatlik Nitelikli Kontaktlar (QCPH)* |
| DOW | Day Of Week | DOW | `cldst_ta_traffic_analysis_by_period_dow` | Kept in English |

---

## 3. Quality / training / system acronyms

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| QA | Quality Assurance | QA | `art_lblQAForm` | Kept in English |
| QC | Quality Control | Kalite Kontrol | `ko_succ_q` | Verify abbreviation used |
| CBT | Computer-Based Training | CBT | `hdr_cbt` | Kept in English |

---

## 4. Common UI abbreviations

Keep the translation **abbreviated** too — these sit in tight table headers and
menus. Match the source's truncation style (trailing `.`).

| Term | Full form | Translation | Example label(s) | Notes |
|------|-----------|-------------|------------------|-------|
| Avg. | Average | Ort. | `aout_avg_sec` | |
| Max. | Maximum | Max | `cldst_ta_ag_max` | |
| Min. | Minimum | Min. | `aout_min_sec` | |
| Tot. | Total | Top. | `aout_tot_sec` | |
| Num. | Number | S. | `aout_fcr_n_calls` | *S. Çağrılar* |
| Dur. | Duration | Sür. | `clage_acd_duration` | |
| Att. | Attempts | Att. | `hdr_attempts` | Pack uses *Att.* |
| Ans. | Answered | Cvp. | `cldst_ans` | |
| Unans. | Unanswered | Cvplmamış. | `cldst_unans` | |
| Conv. | Conversation | Conv. | `aout_ftrconv` | *Ftr. Conv.* |
| Qualif. | Qualified | Nitelik | `td_calloutc_qualif` | No abbreviation in pack |
| Cont. | Contacts | Kontaklar | `aout_contacts_n` | No abbreviation in pack |
| Bill. | Billable | ücrete Tabi | `aout_billable_s` | Pack uses full form |
| Succ. | Successful | Başarılı | `ko_succ_q` | Marked alien; verify abbreviation |
| Short. | Short | Kısa | `ko_sho_q` | Marked alien; verify abbreviation |
| Ag. | Agent | Ag. | `cldst_ta_ag_max` | *Max Ag.* |
| Ext. | Extension | Dahili | `art_localExtension` | No abbreviation in pack |
| Ref. | Reference | Ref. | `ccase_case_xref` | Marked alien; *Ref. No.* |
| sec. | seconds | sn | `rt3_duration` | *Süre (sn)* |

---

## 5. Telephony domain terms (full words)

| Term | English meaning | Translation | Example label(s) | Notes |
|------|-----------------|-------------|------------------|-------|
| Agent | Operator | Müşteri Temsilcisi | `td_agstatus_agent_is_currently_logged_off` | |
| Queue | Call queue | Havuz | `td_ancod_answered_calls_agents_on_queue` | *Kuyruk* also used |
| Caller | Person calling in | Arayan | `td_cko_caller_abandon` | *Arayanın* (possessive) |
| Call (answered) | Answered call | Cevaplanan çağrı | `td_ancod_answered_calls_details` | Full phrase |
| Unanswered / Lost | Not answered | Cevapsız çağrı | `td_ancod_unanswered_calls_details` | *Kayıp çağrılar* also used |
| Abandon(ed) | Caller hung up while queued | Abondone | `td_cko_abandon` | |
| Hangup | Call termination | Kapatmalar | `aout_ivr_hangups` | |
| Wait time | Queue time before answer | Bekleme süresi | `edit_record_agawqueue_avgwait` | *Ortalama bekleme süresi* |
| Talk time | Conversation time | Konuşma Süresi | `qap_details_talk` | Marked alien |
| Wrap-up | Post-call work time | Wrap-up | `td_autoconf_wz_queuewrapup` | Kept in English (*Wrap-up süresi*) |
| Pause | Agent not taking calls | Mola | `td_agawlogon_paused` | *Durduruldu* in status; *Duraklama* in descriptions |
| Session | Logged-on period | Oturum | `td_ancod_agent_sessions_detail` | *Müşteri Temsilcisi oturumları* |
| Inbound / Outbound | Call direction | Gelen / Giden | `td_qdir_inbound_calls` | *Gelen çağrılar* / *Giden çağrılar* |
| Transfer | Pass call onward | Transfer | `td_callstatus_html_transferred` | *Transfer edildi* / *Transféré* (both used) |
| Spill | Overflow call | Fazlalık | `td_aglev_spill` | |
| Ringing | Phone ringing | Telefon çalması | `evt_ringing` | |
| Extension | Phone extension | Dahili | `art_localExtension` | |
| Skill | Agent competency | Beceri | `cldst_skills_per_day` | *Müşteri Temsilcileri özellikleri* / *Beceriler* |
| Voicemail | Recorded message | Sesli mesaj | `td_cko_timeout_voicemail` | *Zaman aşımı (sesli mesaj)* |
| Recall | Scheduled call-back | Hatırlama | `art_lblWbRecallPanel` | *Hatırlama Takvimi* |
| Supervisor | Agent overseer | Denetmen | `edit_ac_supervisor` | *Supervisor* also used |
| Barge / Whisper / Spy | Live-call monitoring | Barge / Fısıltı / Espionner | `rt3_actions_barge`, `rt3_actions_whisper` | Verify *Spy* translation |
| Billable | Billed time/activity | Ücrete tabi | `aout_act_billable` | *Ücrete tabi mola etkinlikleri* |
| Outcome | Call result | Sonuç | `aout_call_res_by_outcome` | |
| Disposition | Coded result / rule | Yerleşim | `cdp_clonedispositions` | *Yerleşim Kuralları* |
| Tag | Call tag | Etiket | `aout_calltag` | |
| Realtime | Live view | Realtime | `art_active_polling_error` | Kept in English; description context |
| Wallboard | Real-time display | Duvarpanosu | `rt3_delete_current_wallboard_confirm` | |
| Alarm | Threshold alert | Alarm | `edit_record_agawqueue_title` | *AGAW alarmları* |
| Threshold | Trigger value | Eşik | `custrep_skills_valhrd` | |

---

## 6. General UI terms

Recurring application-chrome vocabulary. Worth fixing once for menu/button
consistency.

| Term | Context | Translation | Example label(s) | Notes |
|------|---------|-------------|------------------|-------|
| Report | Analysis output | Raporu | `aout_agent_report` | *Detaylı müşteri temsilcisi raporu* |
| Edit / Add / Delete / Create | CRUD actions | Düzenle / Ekle / Sil / Oluştur | `*_edit`, `*_add`, `*_delete` | |
| Export | Export to file | Dışa aktar | `cld_btn_export_calls` | *Çağrıları dışa aktar* |
| Configuration / Settings | Setup screens | Konfigrasyon | `td_synchronier_configuration` | |
| Visibility | Access/visibility key | Görünürlük | `edit_record_export_visibility` | *Görünürlük anahtarı* |
| Group | Grouping | Grup | `clage_agent_performance_acd_group` | *Müşteri Temsilcisi grubu* (in descriptions) |
| Period | Report time range | Dönem | `custrep_time_period` | *Zaman dilimi* / *Zaman periyodu* |
| Status | Current state | Durumu | `td_agstatus_agent_status_cannot_be_determined` | *Müşteri Temsilcisi durumu* |
| Details / Detail | Drill-down view | Detaylar | `td_ancod_answered_calls_details` | |
| Feature | Licensable capability | özellik | `aout_feature` | Lowercase in pack |
| Password / User / Code | Login & identity | Şifre / Kullanıcılar / Kodu | `td_autoconf_wz_agentpwd`, `td_autoconf_wz_users` | *Müşteri Temsilcisi kodu* (code context) |

---

## 7. Doubts & items needing review

Terms where the seeded value is uncertain or the existing pack is inconsistent.
Resolve each, then update the table above and remove the row here.

| Term | Issue | Seeded choice | Options to decide between |
|------|-------|---------------|---------------------------|
| QC | No context/abbreviation found in pack | Kalite Kontrol | Verify if abbreviation *KK* or *QC* is used; or full form *Kalite Kontrol* |
| Qualif. | No abbreviation in pack | Nitelik | Keep full *Nitelik*, or shorten to *Nitf.* in tight headers |
| Cont. | No abbreviation in pack | Kontaklar | Keep full *Kontaklar*, or shorten to *Kont.* in tight headers |
| Succ. / Short. | Marked alien, no clear abbreviation | Başarılı / Kısa | Verify whether pack uses abbreviations *Başarılı.K.* / *Kısa.K.* or full forms |
| Ref. | Marked alien; *Ref. No.* phrasing | Ref. | Verify abbreviation usage; likely *Ref. No.* or similar |
| Ext. | No abbreviation in pack | Dahili | Typically abbreviated *Ext.* in English; verify if Turkish pack uses *Dahili* or *Dah.* in headers |
| Skill | Inconsistent phrasing in pack | Beceri | Pack uses both *Beceri* and *Müşteri Temsilcileri özellikleri* — standardize |
| Pause | Inconsistent across contexts | Mola / Durduruldu | Pack uses *Mola* (action/code context) and *Durduruldu* (status); clarify usage |
| Wrap-up | Kept in English by fallback | Wrap-up | Consider Turkish equivalent like *Çağrı sonrası işler* or *Post-işlem süresi*, or keep English |
| Queue | Two variants in pack | Havuz | Pack uses *Havuz*, *Kuyruk*, *Sıra* — standardize on primary term |
| Unanswered / Lost | Multiple phrasings | Cevapsız çağrı / Kayıp çağrılar | Pack uses both *Cevapsız çağrılar* and *Kayıp çağrılar* — pick one primary |
| Spy (monitoring) | Not confirmed from pack | Espionner | Verify against the pack's live-monitoring labels (likely *Gizle* or similar Turkish equivalent) |
| Transfer | Multiple forms | Transfer / Transfer edildi | Clarify verb form usage (infinitive vs past participle) for consistency |
| Report | Context-dependent phrasing | Raporu | Pack uses *Raporu*, *Rapor*, *Raporla* — standardize |
| Feature | Lowercase in pack | özellik | Verify capitalization and context consistency |
| Period / Dönem | Two variants found | Dönem / Zaman dilimi | Pack uses *Zaman dilimi* and *Dönem* — standardize |
