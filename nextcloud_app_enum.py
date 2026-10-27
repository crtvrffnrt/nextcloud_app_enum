#!/usr/bin/env python3
"""Anonymous, read-only Nextcloud app fingerprints; no credentials or redirects.

Catalog: official Nextcloud App Store apps.json, fetched 2026-10-27. Catalog
membership is only a candidate list, not proof of compatibility or installation.
"""
import argparse
import concurrent.futures
import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

CATALOG = """
aaaaa aaochat abonnieren activity admin_audit admin_audit_http_client admin_notifications admincockpit
afterlogic agenda_bot agora ai_hub aiquila ak_language_switcher all_in_one_accessibility allinoneaccessibility
analytics analytics_sourcepack android_nextcloud_app announcementbanner announcementcenter antony_api antonyapi aone
app_api app_versions appdrop apple_photos_connector appointments apporder approval approval_signature
approve_links appstore appstore_switcher arbeitszeitcheck assistant astrolabe asyntai atrium_secureshare
attendance audioarchive audiocheck audiocoverpreview audiolog audioplayer audioplayer_sonos audiowaveform_preview_provider
auto_groups auto_mail_accounts autocomplete_settings autocurrency backgroundchanger backup batch_renamer bbb
better_app_menu birthday_widget bluemind bookmarks bookmarks_fulltextsearch bookshelfs breezedark brewmemo
browser_warning bruteforcesettings budget budgetcheck buildiq cadviewer cage cairn
calcbase calendar calendar_news calendar_resource_management call_summary_bot camerarawpreviews caniupdate capauth
carfuelmaintance carnet cas certificate24 cfg_share_links chamade_talk checksum checksum_api
chores churchtools_chat churchtools_integration cidgravity circles circlesdb civicrm_nextcloud_integration classic_appmenu
claudebot cloud_federation_api cloud_py_api cms_pico co2clock cobudget codeinjector collaborativephotocleanup
collectives collectives_todos command_bot comments compact_calendar_widget contacts contactsinteraction context_chat
contractmanager cookbook coremail_sync cospend countdown cpanelmailsync crate cristal
cromcull cromqr cryptoinvestmenttracker csp_editor cups_print curio custom_public_share custom_public_share_domain
customercheck customproperties dailyverses dailyzenquote dashboard dashboard_links dashboardcharts dashboardlauncher
dashlink dashy data_request dav dav_push davx5_caldav_carddav_sync_suite_on_android deadmanswitch decidesk
decidiq deck deck_trello deckchecklist deckgithubsync deckimportfromtrello deckloud defaultlinkopen
deferendum deliver desktop_workspace devnull diary dicomviewer digikam_face_sync digitalsignage
discoursesso discretepdfsigner diskmap dkmunicipalorganisation doconext_finder docudesk documents documentserver_community
dokuwiki domus done doom_nextcloud doriath dossiq dpatracker drawio
drivermanager droneci_fast_lane drop_account dropit duplicatefinder dutycheck ebookreader editbase
educai edusign ehr eidlogin eimzo_sign electronicsignatures elementaryenglish elementarymath
em_client_with_nextcloud emailbridge emlviewer empleados empreintelive encryption end_to_end_encryption epc_qrcode_generator
epubreader epubviewer eurooffice eva_ai event_update_notification extended_occweb external external_folder_refresh
externalpassword externalportal extract facerecognition fairmeeting fairregister familybudget familytree
federatedfilesharing federation file_checksum_search file_sharing_invalid_notifier file_upload_notification files files_360viewer files_3d
files_3dmodelviewer files_accesscontrol files_activitymonitor files_antivirus files_archive files_automatedtagging files_autorename files_bpm
files_clipboard files_confidential files_downloadactivity files_downloadlimit files_ebookreader files_emailviewer files_excludedirs files_external
files_external_dropbox files_external_ethswarm files_external_gdrive files_external_gdrive_v2 files_external_ipfs files_external_onedrive files_external_sia files_frommail
files_fulltextsearch files_fulltextsearch_metadata files_fulltextsearch_tesseract files_inotify files_isdoc files_linkeditor files_lock files_markdown
files_mindmap files_notify_redis files_opds files_pdfviewer files_photospheres files_reader files_readme_extended files_readmemd
files_reminders files_retention files_rightclick files_scripts files_set_target files_sharing files_sharing_raw files_snapshots
files_staticmimecontrol files_texteditor files_trackdownloads files_trashbin files_ublcii_viewer files_versions files_versions_s3 files_vrmviewer
files_zip fileslibreofficeedit fileviewer filinq findling fintrack firstrunwizard fit_tracker
floccus flow_notifications flowline flowupload folder_protection folder_retention folderplayer forms
forms_deck formulabase formvox forum frontend_insight fts_sql fulltextsearch fulltextsearch_elasticsearch
fulltextsearch_postgresql fulltextsearch_sql gdatavaas gefex_provisioning generatebluemindexternalaccount geoblocker gestion globalsiteselector
gluusso gnome google_synchronization google_workspace_calendar_sync googledocsredirect gpgmailer gpoddersync gptfreeprompt
gpxedit gpxmotion gpxpod grafana_sync grauphel grimoire group_default_quota group_everyone
group_manager groupfolder_filesystem_snapshots groupfolder_tags groupfolders groupquota guests hc_shared_app_core health
hedgenext hermiq hfivep hibp hibp_login_check hidden_groups hidesidebars hideuseremails
hitobitologin holiday_calendars homecheck homescreen hsts htmlviewer hwpdocuments iframewidget
imageconverter impersonate integration_alephalpha integration_basecamp integration_collaboard integration_davc integration_deepl integration_dilingual
integration_discourse integration_documenso integration_docuseal integration_docusign integration_dropbox integration_ews integration_excalidraw integration_forgejo
integration_forgejo_gitea integration_giphy integration_github integration_gitlab integration_google integration_gptzero integration_grist integration_homeassistant
integration_immich integration_inspect360 integration_itop integration_jira integration_jupyterhub integration_libretranslate integration_m365 integration_mastodon
integration_matrix integration_mattermost integration_miro integration_moodle integration_nepenthes integration_notion integration_nuiteq integration_oidc
integration_onedrive integration_openai integration_openproject integration_openstreetmap integration_overleaf integration_paperless integration_peertube integration_pexip
integration_reddit integration_replicate integration_restya integration_sendrec integration_signd integration_slack integration_suitecrm integration_tmdb
integration_trackmania integration_twitter integration_vuisio integration_watsonx integration_whiteboard integration_windmill integration_youtube integration_zammad
integration_zimbra integration_zulip integriq interfonts intravox intros introvox inventory
inventorycheck invite_registration ios_and_macosx ios_nextcloud_app issuetemplate jalali_calendar jitsi journal
journal_caldav journalnotes journeys jsloader kanso keepassnc keepiq keeporsweep
keeweb kinship kooksession koreader_companion ktec_talkbot kursumstufung l10n_override lager
large_file_previews larpingapp larpinq last_opened launchpad ldap_contacts_backend ldap_write_support ldapcontacts
learning learniq legal_advice les_pas les_pas_photo_app_for_android_phone lettermaker libresign limesurvey_nextcloud
limit_login_to_ip linkboard linto listman llm llmchat loanledger localsend_share
localthumbs logcheck logcleaner login_notes logreader lookup_server_connector lycee_francais_international_de_delhi magicmirror_deck_client
mail mail_roundcube mail_roundcube_bridge maildrop mailnotifier maintenancecheck majordomo maps
markdown_wiki markdownreadme markdownsite mastermind matomo mcp media_embedding_connector mediadc
mediafetch meetree memberadmin memegen memories messagevault metadata metavox
mfazones mjms_pdf_viewer mmm_ncdeck money moneybuster mood moodle moodle_collectives_sync
moodle_deck_sync moodle_talk_bridge moviedb multiboards music musiccurator musicsheetviewer musicstats
mydash myscan n8n_sync nc_connector_for_thunderbird nc_gantt nc_netherrack ncc_backend_4mc ncdownloader
ncgrisbi nddownloader neon_web netbase neura_google_calendar_sync news nextant nextbackup
nextbookmarks nextcloud_all_in_one nextcloud_announcements nextcloud_bookmarks_android_app nextcloud_deck_android_app nextcloud_news_android_app nextcloud_notes_android_app nextcloud_notes_ios_app
nextcloud_passwords_for_android nextcloud_roundcube nextcloud_sms_android_app nextcloud_tables_android_app nextcloud_talk_desktop_client nextcloud_talk_for_android nextcloud_talk_for_ios nextcloud_tunes
nextcloud_video_gallery nextcloudamarillo nextdiary nextfleet nextframe nextledger nextlibrary nextpod
nextsnapmail ng_backup nldesign nomadtracks nopstation_analytics noteberg notes notes_caldav
notifications notify_push noxtr nvscode nxtree oauth2 occweb occweb_v2
ocdownloader ocdownloader_extension_for_pale_moon ocdownloader_webextension_for_bravechromechromiumedgeoperavivaldi ocdownloader_webextension_for_firefox ocjobs ocmremotewebapp ocr ocr_search
ocs_api_viewer ocsms office office_switcher officeonline oidc oidc_claim_mapping oidc_groups_mapping
oidc_login ojsxc olvid onlyoffice openbuild opencase opencatalogi openconnector
openhab openincryptpad openotp_auth openotp_sign openregister openrouter_connector ops_suite opsdash
orchestrascoresmanager orchestration_gateway orcid organization_folders orostelco otpmanager ownbackup ownershiptransfer
ownpad pandoc pantry paperless_sync paperless_unified_search passman password_policy passwords
passwords_for_nextcloud_ios_client passwords_handbook pax_fax pdf_downloader pdfdraw penpot_sync permissions_overwrite phonetrack
photo_frames photos photosphere_tours photosweep picker pipelinq piwik podcast
polls pomodoro portaliq preferred_providers previewgenerator pride pride_flags prinotes
printer privacy privacyidea privatedata procest profile profile_fields projectcheck
projectmanager proofing_gallery provisioning_api pto public_share_control pulse pwa_suite qownnotes
qownnotesapi qrcode quantumchess quest quickaccesssorting quicknotes quota_warning radfahrschule
radio rainloop ransomware_detection ransomware_protection rechnungswerk recognize recommendation_assistant recommendations
regibase registertocontact registration reinhardterp related_resources remotestorage rename_with_metadata repod
report_uri requrvhive richdocuments richdocumentscode richdocumentscode_arm64 rides riotchat rocketchat_nextcloud
roll_dice_bot rolls roomvox root_cache_cleaner rotatingwallpapers roundcubemail runbook s3_api
safe_html_viewer salattime samewindow santacloud savapage scanner scholiq schoolplanner
schwarzes_brett sciencemesh scim_client scimserviceprovider scores scoreview secrets secsignid
secure_office sefaria_dashboard sendent sendentsynchroniser sensorlogger sentry serverinfo settings
sfbridge share_audit_dashboard share_via_device sharebymail sharegate shareimporter sharelisting sharemover
sharepath sharepermissions sharepoint sharerenamer sharereview sharing sharingpath shifts
shiftsnext shillinq shopping_list shortcuts side_menu sidebar signdocs_brasil signlive
signotecsignosignuniversal simpledms simpledms_integration single_sign_on_sso_for_nextcloud_with_miniorange sip_trip_phone sketch_picker skyprint smartcook
smartvideo smb_test sms_relentless snackcheck snappymail snowflakestheme social sociallogin
socialsharing_bluesky socialsharing_diaspora socialsharing_email socialsharing_facebook socialsharing_telegram socialsharing_twitter socialsharing_whatsapp softwarecatalog
solar_weather_page solid solitaire solitaire_ce sorts souvenirs spgverein spiresearch
spreed spreedme sqreen_sdk stackiq standesamt_170726_sh starrate stepupauth storageusage
storj stromquittung structura_integration_gateway stt_helper stt_whisper sumoffice support survey_client
suspicious_login synaplan_integration syncblue systemtags tables tachyon talk_matterbridge talk_rh
talk_simple_poll talked task_proc_util taskbook tasks teamhub teamtrip telephoneprovider
televisorium tencentcloudcosconfig terms_of_service test text text2image_helper text2image_stablediffusion text_templates
thematiq theming theming_customcss theming_domain thesearchpage thinkfree threedviewer thunderbird
tickbuddy ticketcheck ticky_crm tigersprite time_archive timebox timemanager timesheet
timesister timetracker transfer transfer_quota_monitor translate transmission tutamail tuya_cloud
tvshownamer twainwebscan twofactor_admin twofactor_backupcodes twofactor_email twofactor_gateway twofactor_nextcloud_notification twofactor_oath
twofactor_reminder twofactor_totp twofactor_u2f twofactor_webauthn twofactor_webeid twothousandandfortyeight uniteos_notifier unroundedcorners
unsplash updatenotification upload_monitor uppush uptimekuma urbanduplicati user_backend_sql_raw user_external
user_ispconfig user_ispconfig_api user_ldap user_lockdown user_migration user_oidc user_pwauth user_rename
user_retention user_saml user_status user_usage_report user_vo userrightsoverview users_picker vapor
vdirsyncerui verein vereinsbuchhaltung vereinsflieger_login versioniq vibeetoee video_converter video_thumbs_relay
viewer vinarium virtualoffice vuisio vulndexbeacon w2g2 w3ds_login weather_status
webapppassword webex_picker webhook_listeners webhooks weekplanner welcome werkstattmanager wfs_downloader
whereami whiteboard windows_10 wopi wordfind workflow_kitinerary workflow_media_converter workflow_ocr
workflow_pdf_converter workflow_script workflow_xopp2pdf_converter workflowengine workin2gether workplanner workspace worktime
worktimepunch wrikesync x2mail xfiles xwiki yoomail yumisign_nextcloud zaakafhandelapp
zeitwerk zenodo zimbradrive zzq_a2_integration_probe zzq_a_integration_probe zzq_b2_integration_probe zzq_b_integration_probe zzq_none
""".split()
SPECIAL_ASSETS = {'bookmarks': 'js/bookmarks-vendors-node_modules_rehype-highlight_index_js.js', 'calendar': 'img/favicon.svg', 'contacts': 'img/clone.svg', 'cookbook': 'img/favicon-api.svg', 'deck': 'img/notifications-dark.svg', 'forms': 'img/favicon.svg', 'mail': 'img/favicon.svg', 'news': 'img/favicon.svg', 'notes': 'img/badge_playstore.svg', 'polls': 'img/app.svg', 'tasks': 'img/favicon.svg', 'richdocuments': 'img/x-office-presentation.svg'}
# Only map capability keys whose provider was verified in Nextcloud source.
CAPABILITIES = {
    'bookmarks': 'bookmarks', 'calendar': 'calendar', 'cookbook': 'cookbook',
    'deck': 'deck', 'forms': 'forms', 'polls': 'polls', 'theming': 'theming',
}

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('url', help='Nextcloud base URL, optionally including its installation path')
    parser.add_argument('--timeout', type=float, default=8, help='per-request timeout in seconds (default: 8)')
    parser.add_argument('--workers', type=int, default=8, help='concurrent requests (default: 8, maximum: 20)')
    parser.add_argument('--json', action='store_true', help='output only JSON')
    parser.add_argument('--color', choices=('auto', 'always', 'never'), default='auto')
    args = parser.parse_args()
    url = urllib.parse.urlsplit(args.url)
    if (url.scheme not in ('http', 'https') or not url.hostname or url.username
            or url.password or url.query or url.fragment):
        parser.error('supply an http(s) base URL without credentials, query or fragment')
    if args.timeout <= 0 or not 1 <= args.workers <= 20:
        parser.error('timeout must be positive and workers must be between 1 and 20')
    base = args.url.rstrip('/')
    colored = args.color == 'always' or (args.color == 'auto' and sys.stdout.isatty() and 'NO_COLOR' not in os.environ)
    def paint(text, code):
        return f'\033[{code}m{text}\033[0m' if colored else text

    def get(path):
        # One opener per request avoids shared opener state across worker threads.
        opener = urllib.request.build_opener(NoRedirect())
        req = urllib.request.Request(base + '/' + path, headers={
            'Accept': 'application/json, image/svg+xml, */*',
            'OCS-APIRequest': 'true', 'User-Agent': 'Nextcloud-Anonymous-App-Audit/2.0'})
        try:
            with opener.open(req, timeout=args.timeout) as response:
                return response.status, response.headers.get('Content-Type', '').lower(), response.read(262144)
        except urllib.error.HTTPError as exc:
            return exc.code, exc.headers.get('Content-Type', '').lower(), exc.read(262144)
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            return None, '', str(exc).encode(errors='replace')

    def parse_json(response):
        try:
            return json.loads(response[2]) if response[0] == 200 else None
        except (ValueError, UnicodeDecodeError):
            return None

    findings = {}
    def add(app, kind, detail, version=None):
        entry = findings.setdefault(app, {'app': app, 'level': kind, 'version': None, 'evidence': []})
        if kind == 'capability' or (kind == 'app-list' and entry['level'] != 'capability'):
            entry['level'] = kind
        if version and isinstance(version, (str, int, float)):
            entry['version'] = str(version)
        if detail not in entry['evidence']:
            entry['evidence'].append(detail)

    if not args.json:
        print(paint(r'''
  _   _           _       _                 _
 | \ | | _____  _| |_ ___| | ___  _   _  __| |
 |  \| |/ _ \ \/ / __/ __| |/ _ \| | | |/ _` |
 | |\  |  __/>  <| || (__| | (_) | |_| | (_| |
 |_| \_|\___/_/\_\\__\___|_|\___/ \__,_|\__,_|
                APP DISCOVERY''', '1;36'))
        print(f'  {paint("Target", "1")}  {base}  {paint("|", "90")}  {len(CATALOG)} catalog candidates')
        print(paint('  Checking public endpoints and app assets...', '90'), file=sys.stderr)

    status_response = get('status.php')
    status = parse_json(status_response)
    version = status.get('versionstring') if isinstance(status, dict) and status.get('productname') == 'Nextcloud' else None
    cap_response = get('ocs/v2.php/cloud/capabilities?format=json')
    if status_response[0] is None and cap_response[0] is None:
        print('Error: target is unreachable; scan stopped.', file=sys.stderr)
        return 1
    cap_json = parse_json(cap_response)
    caps = {}
    if isinstance(cap_json, dict):
        ocs = cap_json.get('ocs', {})
        if isinstance(ocs, dict) and isinstance(ocs.get('meta'), dict) and ocs['meta'].get('status') == 'ok':
            data = ocs.get('data', {})
            if isinstance(data, dict) and isinstance(data.get('capabilities'), dict):
                caps = data['capabilities']
    for key, app in CAPABILITIES.items():
        if key in caps:
            value = caps[key]
            add(app, 'capability', 'Public capability: ' + key,
                value.get('version') if isinstance(value, dict) else None)
    # Some providers register beneath client_integration rather than at top level.
    integration = caps.get('client_integration', {})
    if isinstance(integration, dict) and 'contacts' in integration:
        add('contacts', 'capability', 'Public capability: client_integration.contacts')

    app_response = get('ocs/v2.php/cloud/apps?format=json')
    app_json = parse_json(app_response)
    try:
        ocs = app_json['ocs']
        apps = ocs['data']['apps'] if ocs['meta']['status'] == 'ok' else []
        if isinstance(apps, list):
            for app in apps:
                if isinstance(app, str) and re.fullmatch(r'[a-z0-9_]+', app):
                    add(app, 'app-list', 'Public installed-app list (enabled state unspecified)')
    except (TypeError, KeyError):
        pass

    # Reject wildcard/fallback pages that return the same content for missing paths.
    controls = [get('custom_apps/nc_enum_missing_48f6d/img/app.svg'),
                get('apps/nc_enum_missing_48f6d/img/app.svg'),
                get('custom_apps/nc_enum_missing_48f6d/js/nc_enum_missing_48f6d-main.js'),
                get('apps/nc_enum_missing_48f6d/js/nc_enum_missing_48f6d-main.js')]
    control_hashes = {hashlib.sha256(body).digest() for status_code, _, body in controls if status_code == 200}
    jobs = []
    for app in CATALOG:
        paths = ['img/app.svg', 'img/favicon.svg', 'js/' + app + '-main.js']
        if app in SPECIAL_ASSETS:
            paths.insert(0, SPECIAL_ASSETS[app])
        for root in ('custom_apps', 'apps'):
            for path in dict.fromkeys(paths):
                jobs.append((app, root + '/' + app + '/' + path))
    def probe(job):
        app, path = job
        code, mime, body = get(path)
        if code is None:
            return app, path, 'error'
        valid = (('svg' in mime and b'<svg' in body[:4096].lower()) if path.endswith('.svg')
                 else ('javascript' in mime and len(body) > 100))
        if code == 200 and valid and hashlib.sha256(body).digest() not in control_hashes:
            return app, path, 'match'
        return app, path, 'none'

    failures = 0
    # executor.map yields incrementally and has a bounded worker count.
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        for index, (app, path, outcome) in enumerate(pool.map(probe, jobs), 1):
            if not args.json and sys.stderr.isatty() and index % 500 == 0:
                print(f'  Checked {index}/{len(jobs)} asset paths...', file=sys.stderr)
            if outcome == 'match':
                add(app, 'asset', 'Public asset: /' + path)
            elif outcome == 'error':
                failures += 1
    result = {'target': base, 'version': version, 'catalog_candidates': len(CATALOG),
              'requests_planned': len(jobs) + 7, 'capabilities_status': cap_response[0],
              'app_list_status': app_response[0], 'request_errors': failures,
              'findings': sorted(findings.values(), key=lambda x: x['app'])}
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f'  {paint("Server", "1")}  Nextcloud {version or "version unknown"}')
        print(f'  {paint("Found", "1")}   {len(findings)} app fingerprints  {paint("|", "90")}  App list: HTTP {app_response[0] or "unreachable"}\n')
        for level, heading, color in [('capability', 'ENABLED CAPABILITIES', '1;32'),
                                      ('app-list', 'INSTALLED APP LIST', '1;36'),
                                      ('asset', 'APP FILES FOUND', '1;33')]:
            rows = [x for x in result['findings'] if x['level'] == level]
            if not rows:
                continue
            print('  ' + paint(heading + '  (' + str(len(rows)) + ')', color))
            for row in rows:
                version_text = paint('  v' + row['version'], '90') if row['version'] else ''
                print('    ' + paint('+', color) + ' ' + row['app'] + version_text)
            print()
        if not findings:
            print('  No app fingerprints found.\n')
        print(paint('  Asset matches show files are accessible; enablement is unknown.', '90'))
        print(paint('  No match does not prove an app is absent. Use --json for evidence paths.', '90'))
        if failures:
            print(paint(f'  Warning: {failures} asset requests failed; results may be incomplete.', '1;33'), file=sys.stderr)
    return 0 if version or caps else 1

if __name__ == '__main__':
    sys.exit(main())
