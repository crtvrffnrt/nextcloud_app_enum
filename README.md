# Nextcloud app enumeration

Identify Nextcloud app fingerprints from public endpoints and static assets. Only scan systems you are authorized to assess.

## Python

Requires Python 3

```bash
python3 nextcloud_app_enum.py https://example.com/nextcloud
python3 nextcloud_app_enum.py https://example.com/nextcloud --json
```

Use `--help` for timeout, concurrency and color options. The script checks a large catalog and can send thousands of requests; `--workers` controls concurrency (default 8, maximum 20).

## Nuclei

With Nuclei installed, run:

```bash
nuclei -u https://example.com/nextcloud -t nextcloud-app-enum.yaml
nuclei -u https://example.com/nextcloud -t nextcloud-app-enum-version.yaml
```

Capability matches indicate enabled providers. An app-list match does not establish enabled state; an asset match only shows that a file is accessible. Missing matches do not prove an app is absent. The Nuclei template checks a smaller set of fingerprints than the Python script.

### Observed version fingerprints

`nextcloud-app-enum-versions.yaml` is a copy of the original template with 35 additional SHA-256 fingerprints of publicly accessible JavaScript files from one installation, matched to the versions reported by its `occ app:list` output:

```bash
nuclei -u https://example.com/nextcloud -t nextcloud-app-enum-versions.yaml
```

A result such as `baseline-calendar-6-6-4` means that the response matches the file observed with Calendar 6.6.4. It is a version **candidate**, not proof: different releases can contain identical files, and builds or modifications of the same release can produce different files. Fingerprints are tied to the observed `/apps` or `/custom_apps` location and may miss other installations. Accessible assets do not prove an app is enabled; the baseline includes the disabled but installed `app_api`. An absent result does not rule out a version or app. Confirm versions with `occ app:list` when server access is available. The remaining listed apps have no version fingerprint in this template.
