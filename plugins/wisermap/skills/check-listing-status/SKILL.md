---
name: check-listing-status
description: Check whether a WiserMap business listing or draft is saved, awaiting owner confirmation, submitted for review or approved, and return its actual reference or public URL. Use for listing-review and submission-status questions.
---

# Check WiserMap listing status

Use action-specific tools from the connected WiserMap server. Use
`wisermap_list_businesses` only as needed to identify the authorized business. For a draft,
call `wisermap_get_draft`; use `wisermap_status` with the actual `business_id` or `draft_id`
when a business has been submitted. Do not guess a business ID or public URL.

Report the exact state with a short explanation. A private draft is not submitted.
An owner-confirmed draft still needs a successful submission response. A pending
review is not an approval. Return a public URL only when the server confirms
approval/publication. If the server reports a suspended or unauthorized business,
refer the owner to WiserMap Support or the existing ownership-claim process.

Do not create a draft, change profile data, resubmit, approve, or reactivate anything
in response to a status question. Do not promise an approval time, email delivery,
automatic background checks or notifications that have not been configured and
verified. This skill does a single requested status check.
