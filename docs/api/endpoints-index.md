# Multilogin X API — Endpoints Index


**90 endpoints**

| Category | Method | URL | Doc |
|---|---|---|---|
| Launcher | `GET` | `https://launcher.mlx.yt:45001/api/v2/profile/f/:folder_id/p/:profile_id/start` | [Start Browser Profile](endpoints/start-browser-profile.md) |
| Launcher | `POST` | `https://launcher.mlx.yt:45001/api/v3/profile/quick` | [Start Quick Profile v3](endpoints/start-quick-profile-v3.md) |
| Launcher | `POST` | `https://launcher.mlx.yt:45001/api/v2/profile/quick` | [Start Quick Profile (Deprecated)](endpoints/start-quick-profile-deprecated.md) |
| Launcher | `GET` | `https://launcher.mlx.yt:45001/api/v1/profile/stop` | [Stop Browser Profile](endpoints/stop-browser-profile.md) |
| Launcher | `GET` | `https://launcher.mlx.yt:45001/api/v1/profile/stop_all` | [Stop All Profiles](endpoints/stop-all-profiles.md) |
| Launcher | `GET` | `https://launcher.mlx.yt:45001/api/v1/version` | [Get Version](endpoints/get-version.md) |
| Launcher | `GET` | `https://launcher.mlx.yt:45001/api/v1/profile/active` | [Get Profile Status](endpoints/get-profile-status.md) |
| Launcher | `GET` | `https://launcher.mlx.yt:45001/api/v2/profile/active` | [Get All Profiles Status](endpoints/get-all-profiles-status.md) |
| Launcher | `GET` | `https://launcher.mlx.yt:45001/api/v1/quick-profiles/active` | [Get All Quick Profiles Status](endpoints/get-all-quick-profiles-status.md) |
| Launcher | `GET` | `https://launcher.mlx.yt:45001/api/v1/core/loaded` | [Loaded Browser Cores](endpoints/loaded-browser-cores.md) |
| Launcher | `GET` | `https://launcher.mlx.yt:45001/api/v1/core/list` | [Browser Core List](endpoints/browser-core-list.md) |
| Launcher | `GET` | `https://launcher.mlx.yt:45001/api/v1/core/load` | [Load Browser Core](endpoints/load-browser-core.md) |
| Launcher | `DELETE` | `https://launcher.mlx.yt:45001/api/v1/core` | [Delete Browser Core](endpoints/delete-browser-core.md) |
| Launcher | `POST` | `https://launcher.mlx.yt:45001/api/v1/proxy/validate` | [Validate Proxy](endpoints/validate-proxy.md) |
| Launcher | `POST` | `https://launcher.mlx.yt:45001/api/v1/cookies/import` | [Cookie Import](endpoints/cookie-import.md) |
| Launcher | `POST` | `https://launcher.mlx.yt:45001/api/v1/cookies/export` | [Cookie Export](endpoints/cookie-export.md) |
| Launcher | `POST` | `https://launcher.mlx.yt:45001/api/v1/profile/convert_qbp` | [Convert QBP to Profile](endpoints/convert-qbp-to-profile.md) |
| Launcher | `GET` | `https://launcher.mlx.yt:45001/api/v1/profile/qbp_status` | [Get QBP Status](endpoints/get-qbp-status.md) |
| Profile Access Management | `POST` | `https://api.multilogin.com/user/signin` | [User Sign In](endpoints/user-sign-in.md) |
| Profile Access Management | `POST` | `https://api.multilogin.com/user/refresh_token` | [User Refresh Token (Switch Workspace)](endpoints/user-refresh-token-switch-workspace.md) |
| Profile Access Management | `POST` | `https://api.multilogin.com/user/revoke_token` | [User Revoke Token](endpoints/user-revoke-token.md) |
| Profile Access Management | `POST` | `https://api.multilogin.com/user/change_password` | [User Change Password](endpoints/user-change-password.md) |
| Profile Access Management | `GET` | `https://api.multilogin.com/user/workspaces` | [User Workspaces](endpoints/user-workspaces.md) |
| Profile Access Management | `GET` | `https://api.multilogin.com/user/tokens` | [User Token List](endpoints/user-token-list.md) |
| Profile Access Management | `GET` | `https://api.multilogin.com/workspace/restrictions` | [Workspace Restrictions](endpoints/workspace-restrictions.md) |
| Profile Access Management | `GET` | `https://api.multilogin.com/workspace/folders` | [Workspace Folders](endpoints/workspace-folders.md) |
| Profile Access Management | `GET` | `https://api.multilogin.com/workspace/folders/user` | [Workspace Folders For User](endpoints/workspace-folders-for-user.md) |
| Profile Access Management | `GET` | `https://api.multilogin.com/workspace/statistics` | [Workspace Statistics](endpoints/workspace-statistics.md) |
| Profile Access Management | `GET` | `https://api.multilogin.com/workspace/automation_token` | [Workspace Automation Token](endpoints/workspace-automation-token.md) |
| Profile Access Management | `POST` | `https://api.multilogin.com/workspace/folder/create` | [Workspace Create Folder](endpoints/workspace-create-folder.md) |
| Profile Access Management | `POST` | `https://api.multilogin.com/workspace/folder/update` | [Workspace Update Folder](endpoints/workspace-update-folder.md) |
| Profile Access Management | `POST` | `https://api.multilogin.com/workspace/folders/remove` | [Workspace Remove Folders](endpoints/workspace-remove-folders.md) |
| Profile Access Management | `POST` | `https://api.multilogin.com/workspace/leave` | [Workspace Leave](endpoints/workspace-leave.md) |
| Profile Management | `POST` | `https://api.multilogin.com/profile/create` | [Profile Create](endpoints/profile-create.md) |
| Profile Management | `POST` | `https://api.multilogin.com/profile/search` | [Profile Search](endpoints/profile-search.md) |
| Profile Management | `POST` | `https://api.multilogin.com/profile/remove` | [Profile Remove](endpoints/profile-remove.md) |
| Profile Management | `POST` | `https://api.multilogin.com/profile/update` | [Profile Update](endpoints/profile-update.md) |
| Profile Management | `POST` | `https://api.multilogin.com/profile/move` | [Profile Move](endpoints/profile-move.md) |
| Profile Management | `POST` | `https://api.multilogin.com/profile/partial_update` | [Profile Partial Update](endpoints/profile-partial-update.md) |
| Profile Management | `POST` | `https://api.multilogin.com/profile/restore` | [Profile Restore](endpoints/profile-restore.md) |
| Profile Management | `POST` | `https://api.multilogin.com/profile/metas` | [Profile Metas](endpoints/profile-metas.md) |
| Profile Management | `GET` | `https://api.multilogin.com/profile/summary` | [Profile Summary](endpoints/profile-summary.md) |
| Profile Management | `POST` | `https://api.multilogin.com/profile/clone` | [Profile Clone](endpoints/profile-clone.md) |
| Profile Management | `POST` | `https://api.multilogin.com/profile/convert` | [Profile Convert](endpoints/profile-convert.md) |
| Profile Management | `GET` | `https://api.multilogin.com/profile/screen_resolutions` | [Screen Resolution](endpoints/screen-resolution.md) |
| Browser Profile Data | `GET` | `https://api.multilogin.com/profile/unlock` | [Unlock Locked Profiles](endpoints/unlock-locked-profiles.md) |
| Proxy | `POST` | `https://api.multilogin.com/proxy/generate` | [Generate Proxy](endpoints/generate-proxy.md) |
| Proxy | `GET` | `https://api.multilogin.com/proxy/data` | [Fetch Proxy Data](endpoints/fetch-proxy-data.md) |
| Pre-made Cookies | `GET` | `https://api.multilogin.com/cookies/websites` | [Target Website List](endpoints/target-website-list.md) |
| Pre-made Cookies | `POST` | `https://api.multilogin.com/cookies/metadata/create` | [Create Cookies Metadata](endpoints/create-cookies-metadata.md) |
| Pre-made Cookies | `GET` | `https://api.multilogin.com/cookies/list` | [Cookies List](endpoints/cookies-list.md) |
| Pre-made Cookies | `PUT` | `https://api.multilogin.com/cookies/metadata/update` | [Update Cookies Metadata](endpoints/update-cookies-metadata.md) |
| Script Runner | `GET` | `https://launcher.mlx.yt:45001/api/v2/profile/f/:folder_id/p/:profile_id/start?automation_type=selenium&script_file=script.py` | [Start Browser Profile with Selenium](endpoints/start-browser-profile-with-selenium.md) |
| Script Runner | `POST` | `https://api.multilogin.com/script/start` | [Start Script Runner](endpoints/start-script-runner.md) |
| Script Runner | `POST` | `https://api.multilogin.com/script/stop` | [Stop Script Runner](endpoints/stop-script-runner.md) |
| Script Runner | `GET` | `https://api.multilogin.com/script/list` | [Script List](endpoints/script-list.md) |
| Profile Import/Export | `POST` | `https://api.multilogin.com/profile/export` | [Profile Export](endpoints/profile-export.md) |
| Profile Import/Export | `GET` | `https://api.multilogin.com/profile/export/status` | [Export Status by Profile](endpoints/export-status-by-profile.md) |
| Profile Import/Export | `GET` | `https://api.multilogin.com/profile/export/status/all` | [Export Status All](endpoints/export-status-all.md) |
| Profile Import/Export | `POST` | `https://api.multilogin.com/profile/import` | [Profile Import](endpoints/profile-import.md) |
| Profile Import/Export | `GET` | `https://api.multilogin.com/profile/import/status` | [Import Status by Profile](endpoints/import-status-by-profile.md) |
| Profile Import/Export | `GET` | `https://api.multilogin.com/profile/import/status/all` | [Import Status All](endpoints/import-status-all.md) |
| Object Storage | `POST` | `https://api.multilogin.com/storage/upload` | [Upload Object](endpoints/upload-object.md) |
| Object Storage | `POST` | `https://api.multilogin.com/storage/create_upload` | [Create and Upload](endpoints/create-and-upload.md) |
| Object Storage | `GET` | `https://api.multilogin.com/storage/object/usages` | [Object Profile Usages](endpoints/object-profile-usages.md) |
| Object Storage | `GET` | `https://api.multilogin.com/storage/types` | [Get List of Object Types](endpoints/get-list-of-object-types.md) |
| Object Storage | `GET` | `https://api.multilogin.com/storage/statistics` | [Get Statistics for Objects](endpoints/get-statistics-for-objects.md) |
| Object Storage | `GET` | `https://api.multilogin.com/storage/objects/meta` | [Get Objects Meta](endpoints/get-objects-meta.md) |
| Object Storage | `GET` | `https://api.multilogin.com/storage/object/meta` | [Get Object Meta by ID](endpoints/get-object-meta-by-id.md) |
| Object Storage | `GET` | `https://api.multilogin.com/storage/object/delete` | [Delete Object](endpoints/delete-object.md) |
| Object Storage | `GET` | `https://api.multilogin.com/storage/object/restore` | [Restore Object](endpoints/restore-object.md) |
| Object Storage | `POST` | `https://api.multilogin.com/storage/cloud_to_local` | [Cloud to Local](endpoints/cloud-to-local.md) |
| Object Storage | `POST` | `https://api.multilogin.com/storage/local_to_cloud` | [Local to Cloud](endpoints/local-to-cloud.md) |
| Object Storage | `GET` | `https://api.multilogin.com/storage/object/download` | [Download Object](endpoints/download-object.md) |
| Object Storage | `POST` | `https://api.multilogin.com/storage/extension/create` | [Create Extension](endpoints/create-extension.md) |
| Object Storage | `POST` | `https://api.multilogin.com/storage/extension/enable` | [Enable Extension](endpoints/enable-extension.md) |
| Object Storage | `POST` | `https://api.multilogin.com/storage/extension/disable` | [Disable Extension](endpoints/disable-extension.md) |
| Object Storage | `POST` | `https://api.multilogin.com/storage/profile/objects` | [List of Objects per Profile](endpoints/list-of-objects-per-profile.md) |
| Bookmark Management | `GET` | `https://api.multilogin.com/bookmarks/export` | [Export Bookmarks](endpoints/export-bookmarks.md) |
| Bookmark Management | `POST` | `https://api.multilogin.com/bookmarks/import` | [Import Bookmarks](endpoints/import-bookmarks.md) |
| Bookmark Management | `POST` | `https://api.multilogin.com/bookmarks/copy` | [Copy Bookmarks](endpoints/copy-bookmarks.md) |
| 2FA | `POST` | `https://api.multilogin.com/2fa/setup` | [Set up 2FA](endpoints/set-up-2fa.md) |
| 2FA | `POST` | `https://api.multilogin.com/2fa/enable` | [Enable 2FA](endpoints/enable-2fa.md) |
| 2FA | `POST` | `https://api.multilogin.com/2fa/verify` | [Verify 2FA](endpoints/verify-2fa.md) |
| 2FA | `POST` | `https://api.multilogin.com/2fa/device/setup` | [Set up New Device for 2FA](endpoints/set-up-new-device-for-2fa.md) |
| 2FA | `GET` | `https://api.multilogin.com/2fa/devices` | [Get Devices for 2FA](endpoints/get-devices-for-2fa.md) |
| 2FA | `GET` | `https://api.multilogin.com/2fa/backup_codes` | [Get Backup Codes for 2FA](endpoints/get-backup-codes-for-2fa.md) |
| 2FA | `POST` | `https://api.multilogin.com/2fa/device/revoke` | [Revoke Device for 2FA](endpoints/revoke-device-for-2fa.md) |
| 2FA | `POST` | `https://api.multilogin.com/2fa/workspace` | [Enable/Disable 2FA for Workspace](endpoints/enable-disable-2fa-for-workspace.md) |
| 2FA | `POST` | `https://api.multilogin.com/2fa/disable` | [Disable 2FA](endpoints/disable-2fa.md) |