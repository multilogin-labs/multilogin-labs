# 2FA — Two-factor authentication

> [Partner pricing →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · **`SAAS50`** · **`MIN50`** · [← API hub](../README.md) · [Cheatsheet](../CHEATSHEET.md) · [Swagger UI](../swagger.html)

Manage workspace and account-level 2FA: enable, verify, devices, backup codes.

## Endpoints in this category

- **`POST`** [Set up 2FA](../endpoints/set-up-2fa.md) — `https://api.multilogin.com/2fa/setup`
- **`POST`** [Enable 2FA](../endpoints/enable-2fa.md) — `https://api.multilogin.com/2fa/enable`
- **`POST`** [Verify 2FA](../endpoints/verify-2fa.md) — `https://api.multilogin.com/2fa/verify`
- **`POST`** [Set up New Device for 2FA](../endpoints/set-up-new-device-for-2fa.md) — `https://api.multilogin.com/2fa/device/setup`
- **`GET`** [Get Devices for 2FA](../endpoints/get-devices-for-2fa.md) — `https://api.multilogin.com/2fa/devices`
- **`GET`** [Get Backup Codes for 2FA](../endpoints/get-backup-codes-for-2fa.md) — `https://api.multilogin.com/2fa/backup_codes`
- **`POST`** [Revoke Device for 2FA](../endpoints/revoke-device-for-2fa.md) — `https://api.multilogin.com/2fa/device/revoke`
- **`POST`** [Enable/Disable 2FA for Workspace](../endpoints/enable-disable-2fa-for-workspace.md) — `https://api.multilogin.com/2fa/workspace`
- **`POST`** [Disable 2FA](../endpoints/disable-2fa.md) — `https://api.multilogin.com/2fa/disable`

## Common use cases

- Force 2FA for all members in an agency workspace
- Backup-code rotation script for compliance audits
- Provision new operator device after onboarding

## Quick example

```bash
# Enable 2FA on the current account
curl -X POST https://api.multilogin.com/2fa/enable \
  -H "Authorization: Bearer $MULTILOGIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"code":"123456"}'
```

## Related

- [Cookbook ×40](../cookbook/README.md)
- [Related guide](../../guides/multilogin-2fa-workflow.md)
- [Quick start](../quick-start.md) · [Authentication](../authentication.md)
- [SEARCH_INDEX](../../SEARCH_INDEX.md)

**Keywords:** multilogin 2fa api · multilogin x · two-factor authentication
