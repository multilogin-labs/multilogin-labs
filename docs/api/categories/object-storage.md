# Object storage — Workspace files & artifacts

> [Partner pricing →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · **`SAAS50`** · **`MIN50`** · [← API hub](../README.md) · [Cheatsheet](../CHEATSHEET.md) · [Swagger UI](../swagger.html)

Upload screenshots, exports, and shared assets at workspace level.

## Endpoints in this category

- **`POST`** [Upload Object](../endpoints/upload-object.md) — `https://api.multilogin.com/storage/upload`
- **`POST`** [Create and Upload](../endpoints/create-and-upload.md) — `https://api.multilogin.com/storage/create_upload`
- **`GET`** [Object Profile Usages](../endpoints/object-profile-usages.md) — `https://api.multilogin.com/storage/object/usages`
- **`GET`** [Get List of Object Types](../endpoints/get-list-of-object-types.md) — `https://api.multilogin.com/storage/types`
- **`GET`** [Get Statistics for Objects](../endpoints/get-statistics-for-objects.md) — `https://api.multilogin.com/storage/statistics`
- **`GET`** [Get Objects Meta](../endpoints/get-objects-meta.md) — `https://api.multilogin.com/storage/objects/meta`
- **`GET`** [Get Object Meta by ID](../endpoints/get-object-meta-by-id.md) — `https://api.multilogin.com/storage/object/meta`
- **`GET`** [Delete Object](../endpoints/delete-object.md) — `https://api.multilogin.com/storage/object/delete`
- **`GET`** [Restore Object](../endpoints/restore-object.md) — `https://api.multilogin.com/storage/object/restore`
- **`POST`** [Cloud to Local](../endpoints/cloud-to-local.md) — `https://api.multilogin.com/storage/cloud_to_local`
- **`POST`** [Local to Cloud](../endpoints/local-to-cloud.md) — `https://api.multilogin.com/storage/local_to_cloud`
- **`GET`** [Download Object](../endpoints/download-object.md) — `https://api.multilogin.com/storage/object/download`
- **`POST`** [Create Extension](../endpoints/create-extension.md) — `https://api.multilogin.com/storage/extension/create`
- **`POST`** [Enable Extension](../endpoints/enable-extension.md) — `https://api.multilogin.com/storage/extension/enable`
- **`POST`** [Disable Extension](../endpoints/disable-extension.md) — `https://api.multilogin.com/storage/extension/disable`
- **`POST`** [List of Objects per Profile](../endpoints/list-of-objects-per-profile.md) — `https://api.multilogin.com/storage/profile/objects`

## Common use cases

- Store proof-of-task screenshots for clients
- Share warmup logs across the team
- Persist exported profiles for retention policy

## Quick example

```bash
curl -X POST https://api.multilogin.com/storage/upload \
  -H "Authorization: Bearer $MULTILOGIN_TOKEN" \
  -F "file=@screenshot.png" \
  -F "tag=campaign-q3" 
```

## Related

- [Cookbook ×40](../cookbook/README.md)
- [Quick start](../quick-start.md) · [Authentication](../authentication.md)
- [SEARCH_INDEX](../../SEARCH_INDEX.md)

**Keywords:** multilogin object storage api · multilogin x · workspace files & artifacts
