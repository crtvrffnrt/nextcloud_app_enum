# Nextcloud app enumeration

Identify Nextcloud app fingerprints from public endpoints and static assets. Only scan systems you are authorized to assess.

## Python

Requires Python 3; no third-party packages are needed.

```bash
python3 nextcloud_app_enum.py https://example.com/nextcloud
python3 nextcloud_app_enum.py https://example.com/nextcloud --json
```

Use `--help` for timeout, concurrency and color options. The script checks a large catalog and can send thousands of requests; `--workers` controls concurrency (default 8, maximum 20).

## Nuclei

With Nuclei installed, run:

```bash
nuclei -u https://example.com/nextcloud -t nextcloud-app-enum.yaml
```

Capability matches indicate enabled providers. An app-list match does not establish enabled state; an asset match only shows that a file is accessible. Missing matches do not prove an app is absent. The Nuclei template checks a smaller set of fingerprints than the Python script.
