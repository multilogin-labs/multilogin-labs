# Profile access management — Sharing & permissions

> [Partner pricing →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · **`SAAS50`** · **`MIN50`** · [← API hub](../README.md) · [Cheatsheet](../CHEATSHEET.md) · [Swagger UI](../swagger.html)

Share profiles with team members, transfer ownership, manage roles.

## Endpoints in this category

- **`POST`** [User Sign In](../endpoints/user-sign-in.md) — `https://api.multilogin.com/user/signin`
- **`POST`** [User Refresh Token (Switch Workspace)](../endpoints/user-refresh-token-switch-workspace.md) — `https://api.multilogin.com/user/refresh_token`
- **`POST`** [User Revoke Token](../endpoints/user-revoke-token.md) — `https://api.multilogin.com/user/revoke_token`
- **`POST`** [User Change Password](../endpoints/user-change-password.md) — `https://api.multilogin.com/user/change_password`
- **`GET`** [User Workspaces](../endpoints/user-workspaces.md) — `https://api.multilogin.com/user/workspaces`
- **`GET`** [User Token List](../endpoints/user-token-list.md) — `https://api.multilogin.com/user/tokens`
- **`GET`** [Workspace Restrictions](../endpoints/workspace-restrictions.md) — `https://api.multilogin.com/workspace/restrictions`
- **`GET`** [Workspace Folders](../endpoints/workspace-folders.md) — `https://api.multilogin.com/workspace/folders`
- **`GET`** [Workspace Folders For User](../endpoints/workspace-folders-for-user.md) — `https://api.multilogin.com/workspace/folders/user`
- **`GET`** [Workspace Statistics](../endpoints/workspace-statistics.md) — `https://api.multilogin.com/workspace/statistics`
- **`GET`** [Workspace Automation Token](../endpoints/workspace-automation-token.md) — `https://api.multilogin.com/workspace/automation_token`
- **`POST`** [Workspace Create Folder](../endpoints/workspace-create-folder.md) — `https://api.multilogin.com/workspace/folder/create`
- **`POST`** [Workspace Update Folder](../endpoints/workspace-update-folder.md) — `https://api.multilogin.com/workspace/folder/update`
- **`POST`** [Workspace Remove Folders](../endpoints/workspace-remove-folders.md) — `https://api.multilogin.com/workspace/folders/remove`
- **`POST`** [Workspace Leave](../endpoints/workspace-leave.md) — `https://api.multilogin.com/workspace/leave`

## Common use cases

- Onboard a new agency member to a client folder
- Revoke access when an operator leaves
- Audit who has access to which profile

## Quick example

```bash
curl -X POST https://api.multilogin.com/profile/share \
  -H "Authorization: Bearer $MULTILOGIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"profile_id":"...","member_email":"ops@example.com","role":"editor"}'
```

## Related

- [Cookbook ×40](../cookbook/README.md)
- [Related guide](../../guides/multilogin-team-workspace.md)
- [Quick start](../quick-start.md) · [Authentication](../authentication.md)
- [SEARCH_INDEX](../../SEARCH_INDEX.md)

**Keywords:** multilogin profile access management api · multilogin x · sharing & permissions
