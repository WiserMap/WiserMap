# WiserMap

Create and manage your local business profile through Claude, using the existing
WiserMap business tools. Prepare services, menus, hours, photos, contact details
and factual FAQs in a private draft. Review the exact profile on WiserMap before
submitting it. New business listings still require WiserMap Support review.

This is a skills-and-connector plugin. It connects to the hosted WiserMap service;
it does not install a new directory, start a local server, replace WiserMap's
interface, or access your computer's credentials.

## Get started

You need a Claude app that supports plugins and an active, email-verified WiserMap
business-owner account. Claim an existing business through WiserMap before trying
to manage it. The connector enforces your account's authorization and existing
verification requirements.

In Claude, open **Customize > Plugins > Add > Upload plugin**, choose the plugin
ZIP, open its **Connectors** tab, and connect **WiserMap**. Sign in on WiserMap and
review the permission request. If WiserMap is already connected, use that existing
connection; this plugin references the same endpoint.

For a repository install, add this repository as a plugin marketplace and install
**wisermap**. The initial connection flow targets Claude chat and its hosted OAuth callback.
Claude Code may load and validate the plugin files, but authenticated Claude Code
compatibility has not been verified. Do not assume that a localhost callback is
supported by the hosted service.
The ZIP upload is a way to test or directly distribute the plugin. It is not proof
that the plugin has been approved or published in Anthropic's public directory.

## Connector version and permissions

This bundle targets the hosted action-specific tools introduced in server 0.7.0.
There are eight read-only tools and five write tools, each with a descriptive title
and permission annotations. Refresh the WiserMap connection to discover the new
tool list after upgrading from the earlier mixed-action tool. Researching a website
saves a source record and is therefore treated as a write.

## Things to ask

- “Add my business to WiserMap. Use my website and ask for anything missing.”
- “Improve my existing WiserMap profile without removing accurate information.”
- “Update our restaurant menu and ordering link, keeping WiserMap's menu format.”
- “Check what is preventing my draft from being submitted.”
- “What is the review status of my WiserMap listing?”

## How it works

Claude checks the connected account, looks for an existing listing, reads real
category requirements, and researches information you identify. It saves a private
draft, reviews missing information and uploaded-media inventory, and returns the
real WiserMap preview/upload link. You confirm the facts and image rights on
WiserMap. Claude then submits that version when you request it. A saved draft is
not a submission; a submitted new listing is not an approved or published listing.

## Business-specific details, existing WiserMap layout

Doctors and dentists can describe appointment policies, new-patient availability,
accepted insurance, services and languages. Restaurants and bars can add their
real menus, ordering information, outdoor seating and entertainment details.
Repairs and other local services can explain their offerings, service areas,
turnaround and warranty information. Claude checks what WiserMap actually supports
and uses existing descriptions or FAQs for facts without dedicated fields.

Services remain in WiserMap's native service format. Food businesses use its
existing menu format. Teams and products are optional. Unknown menu prices or
ingredients are not invented. Hours are presented to the owner in AM/PM format,
while saved values follow the server's schema.

Only genuine local storefront businesses or legitimate local service operations
are eligible. Online-only sites cannot be listed. Real evidence and authentic
photos are required; a public website alone does not prove ownership. Claude-chat
attachments are not automatically transferred to WiserMap.

## Permissions and payments

The bundled MCP server uses OAuth. Do not paste your password, authentication
codes, access tokens, API keys or AWS credentials into chat. Only manage businesses
your connected account is authorized to manage. This plugin cannot approve claims,
reactivate suspended listings or bypass WiserMap review. It does not read patient
records, manage customers' appointments, generate reviews or activate paid services.

Basic profile tools are separate from optional paid booking. Claude may ask once
about booking interest. Interest is not a purchase; any subscription must be
reviewed and authorized separately through WiserMap.

## Privacy Policy

WiserMap's [Privacy Policy](https://wisermap.com/privacy-policy) applies to its
service. Tool calls send the listing information and sources needed for the
requested task to WiserMap; requested results are returned to Claude. Do not send
unrelated conversation history, patient records, insurance cards, payment-card
data or confidential identity documents through this listing workflow. Public
profile fields and approved images are intended for publication. Consult the service Privacy Policy and WiserMap Support for retention and deletion
requests; this plugin does not promise an automatic deletion interval. Claude's own terms govern your use of
Claude. There is no plugin-side telemetry, installer or analytics code.

## Disconnect and get help

Manage or revoke your connection in
[WiserMap's connected-apps page](https://wisermap.com/business/claude/connections).
Disconnecting stops access; it does not by itself delete a submitted listing or
cancel a paid subscription. Open [WiserMap Support](https://wisermap.com/support-ticket)
for authorization, eligibility, data-correction or deletion requests. The current
support-ticket page asks you to sign in.

When reporting an error, share the affected action and a redacted error message,
not passwords, tokens, private preview links or personal records.

## License

The plugin's instructions and configuration are MIT-licensed. See LICENSE and
NOTICE.md. WiserMap branding and the remote service are not relicensed by this
package.
