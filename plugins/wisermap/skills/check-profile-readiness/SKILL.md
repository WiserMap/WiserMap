---
name: check-profile-readiness
description: Check an existing WiserMap business draft for missing information, failed photo imports, blocked submission or incomplete category-specific sections. Use when the user asks why Submit is unavailable or wants a profile completeness review.
---

# Check WiserMap profile readiness

Use the connected WiserMap action-specific tools. This is an assessment
request, not blanket permission to change or submit a profile.

Get the user's existing draft with `wisermap_get_draft`. If only an existing business is
identified, use `wisermap_list_businesses` to resolve it; do not make a new draft without a
request to prepare edits. For a known draft call `wisermap_preview` or `wisermap_assess_draft` and read
the current payload, media inventory, `content_review`, `completion_protocol`,
errors, revision and confirmation state. Read `wisermap_requirements` for the actual
category IDs when needed. Never invent a numerical SEO or Google quality score.

Separate three types of findings:

- **Blocks submission:** missing native required fields, invalid location or local
  eligibility, failed/missing actual assets, unresolved duplicate, expired/stale
  approval, missing ownership authorization, suspension or required review.
- **Useful improvements:** verified additional services, relevant FAQs, menu/ordering
  details and available business links that improve usefulness but are not blockers.
- **Owner decision:** fact conflicts, unknown policies, image rights or evidence that
  Claude cannot verify. Unknown information is not automatically No or Not applicable.

Show the actual blocking messages in plain language and group them by WiserMap's
existing sections. Include the exact returned preview/upload link. Make clear that
an image visible in Claude chat or an image URL in text is not a stored WiserMap
photo. Do not claim the submit button is enabled unless the current server result
supports that claim.

If the user authorizes repairs, follow `manage-business-profile`: preserve existing
content, patch at the latest revision, reassess, and require a new owner confirmation
when the version changes. Never submit merely to test the button.
