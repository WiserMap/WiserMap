# WiserMap

Create and manage a complete local business profile through Claude, using WiserMap's existing business tools.

This repository contains the WiserMap plugin bundle and a single-plugin marketplace. The bundle connects to the hosted WiserMap MCP service at https://wisermap.com/mcp/wisermap. It contains workflow instructions and public configuration—not the private WiserMap application, database, OAuth secrets, or a local replacement backend.

**Publisher:** WiserMap · **Plugin:** `wisermap` · **Package version:** 1.0.2

**Repository:** https://github.com/WiserMap/WiserMap

## What is included

- `plugins/wisermap/`: the installable plugin and public plugin-submission folder.
- `.claude-plugin/marketplace.json`: marketplace metadata for repository installs.
- Four skills for creating or improving profiles, updating restaurant menus, checking completeness, and reading listing status.
- `tools/validate_package.py`: maintainer-only static checks, not an installation hook.
- `evals/scenarios.json`: behavioral acceptance scenarios, not executed AI evaluation results.

## Get started

Read [the plugin README](plugins/wisermap/README.md) and the [WiserMap connection guide](https://wisermap.com/claude). Use your own WiserMap business-owner account and confirm changes on WiserMap before submission.

For a plugin ZIP, package only the contents of `plugins/wisermap`, or that folder as the archive's single top-level entry. Do not upload the entire repository as a plugin ZIP.

Run `python3 tools/validate_package.py` for local package checks. Where Claude Code is installed, also run `claude plugin validate ./plugins/wisermap` and `claude plugin validate .` for the marketplace. Static validation does not establish authenticated client compatibility or directory acceptance.

## Publication status

GitHub source publication and acceptance into Anthropic's directory are separate steps. This repository does **not** assert Claude Directory approval, a Verified badge, or placement in Popular or Trending. Authenticated reviewer testing and the directory's validation remain separate release gates.

Submit the hosted endpoint as an MCP connector and `plugins/wisermap` as a plugin bundle through the WiserMap-controlled Claude developer account. See [Anthropic's publishing instructions](https://claude.com/docs/directory/publish). Never publish production source, backups, credentials, or reviewer login details here.

## License

Original plugin instructions and configuration are MIT-licensed. The remote service, business data, and WiserMap and Claude trademarks are outside that license.
