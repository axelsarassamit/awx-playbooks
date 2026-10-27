# awx-playbooks

## Licensing

This project's original code is licensed under the [MIT License](LICENSE),
including commercial use, modification and redistribution with preservation of
the copyright and license notice. Third-party materials retain their own terms.
Project names and branding are not licensed as trademarks by this grant.

## Independent configuration

No AWX server, credential, inventory ID, host list or address range is configured by default.
Set AWX_URL, AWX_OAUTH_TOKEN and AWX_INVENTORY_ID in your own runtime environment.
For import_specific_hosts.yml, pass hosts_to_add in a private extra-vars file.
For import_hosts.yml, pass ip_prefix, ip_range_start and ip_range_end explicitly.
The first task refuses missing configuration before any API request. API tasks suppress secrets.
No existing AWX inventory or remote account is changed by this source cleanup.
