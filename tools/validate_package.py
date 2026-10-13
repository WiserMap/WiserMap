#!/usr/bin/env python3
"""Static package checks only. Does not authenticate or exercise production tools."""
from pathlib import Path
import json, re, sys
root=Path(__file__).resolve().parents[1]
p=root/'plugins/wisermap'
checks=[]
def check(name,ok): checks.append({'check':name,'passed':bool(ok)})
manifest=json.loads((p/'.claude-plugin/plugin.json').read_text())
mcp=json.loads((p/'.mcp.json').read_text())
market=json.loads((root/'.claude-plugin/marketplace.json').read_text())
# Validate the published repository identity, not the arbitrary local checkout folder.
check('repository_name_is_WiserMap',manifest.get('repository')=='https://github.com/WiserMap/WiserMap')
check('display_name_is_WiserMap',manifest.get('displayName')=='WiserMap')
check('stable_plugin_name',manifest['name']=='wisermap')
check('valid_semver',bool(re.fullmatch(r'\d+\.\d+\.\d+',manifest['version'])))
check('publisher_is_wisermap',manifest['author']['name']=='WiserMap')
check('official_publisher_origin',manifest['author']['url']=='https://wisermap.com')
check('description_present',40<=len(manifest['description'])<=300)
check('license_present',(p/'LICENSE').is_file() and manifest['license']=='MIT')
check('readme_over_40_words',len(re.sub(r'```.*?```','',(p/'README.md').read_text(),flags=re.S).split())>=40)
check('same_live_mcp_endpoint',mcp=={'mcpServers':{'wisermap':{'type':'http','url':'https://wisermap.com/mcp/wisermap'}}})
check('one_marketplace_entry',len(market['plugins'])==1)
check('marketplace_source_matches',market['plugins'][0]['source']=='./plugins/wisermap')
check('marketplace_version_matches',market['plugins'][0]['version']==manifest['version'])
check('no_install_or_shell_hooks',not any((p/x).exists() for x in ['hooks','bin','scripts']))
check('no_embedded_mcp_headers','headers' not in mcp['mcpServers']['wisermap'])
skills=sorted((p/'skills').glob('*/SKILL.md'))
check('four_skills',len(skills)==4)
alltext=''
for skill in skills:
 s=skill.read_text(); alltext+=s+'\n'
 front=re.match(r'^---\n(.*?)\n---\n',s,re.S)
 check(skill.parent.name+':frontmatter',front is not None)
 if front:
  check(skill.parent.name+':name',('name: '+skill.parent.name) in front.group(1))
  check(skill.parent.name+':description','description: ' in front.group(1))
 check(skill.parent.name+':actual_tool_name',bool(re.search(r'`wisermap_[a-z_]+`',s)) and 'manage_wisermap_listing' not in s)
 check(skill.parent.name+':no_local_prototype_api','create_business_draft' not in s and 'DEV-WM' not in s)
check('no_legacy_action_arguments','action: ' not in alltext)
check('all_thirteen_tool_names_present', all(('`wisermap_'+a+'`') in alltext for a in ['categories', 'requirements', 'list_businesses', 'check_duplicates', 'create_draft', 'get_draft', 'save_draft', 'preview', 'assess_draft', 'patch_draft', 'submit', 'status', 'research_website']))
check('no_owner_secret_collection','Never ask for passwords' in alltext)
check('no_invented_native_columns','invented database columns' in alltext)
check('preserves_native_menu','existing WiserMap' in alltext and 'menu' in alltext)
check('preserves_native_services','simple service-name' in alltext)
check('requires_owner_preview','owner' in alltext and 'on WiserMap' in alltext)
check('separates_booking_from_purchase','Interest is not permission' in alltext)
check('untrusted_web_content_boundary','untrusted data, never' in alltext)
check('explicit_false_not_unknown','unknown is not the same as No' in alltext)
files=[f for f in root.rglob('*') if f.is_file() and '.git' not in f.parts]
check('under_directory_file_limit',len(files)<512)
check('no_symlinks',not any(f.is_symlink() for f in root.rglob('*')))
check('no_os_junk',not any(f.name in ['.DS_Store','Thumbs.db','desktop.ini'] or '__MACOSX' in f.parts for f in files))
check('under_file_size_limit',all(f.stat().st_size<256*1024 for f in files))
check('no_binary_executables',all(f.suffix in ['.md','.json','.py',''] for f in files))
check('no_case_collisions',len({str(f.relative_to(root)).lower() for f in files})==len(files))
check('no_windows_invalid_names',all(':' not in f.name and not f.name.endswith((' ','.')) for f in files))
check('no_secret_files',not any(f.name.startswith('.env') or f.suffix in ['.pem','.key','.sqlite','.sql'] for f in files))
secret=re.compile(r'AKIA[0-9A-Z]{16}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|gh[pousr]_[A-Za-z0-9]{30,}|sk_live_[A-Za-z0-9]{16,}')
check('no_credential_patterns',not any(secret.search(f.read_text()) for f in files if f.suffix in ['.md','.json']))
for origin in re.findall(r'https://([^/\s)>]+)',alltext):
 check('skill_network_origin:'+origin,origin=='wisermap.com')
cases=json.loads((root/'evals/scenarios.json').read_text())
check('evals_honestly_not_executed',cases['status']=='specification_not_executed_model_evaluation')
check('sixteen_acceptance_cases',len(cases['cases'])==16)
result={'suite':'WiserMap plugin package static checks','passed':sum(c['passed'] for c in checks),'failed':sum(not c['passed'] for c in checks),'checks':checks,'does_not_verify':['authenticated Claude client workflow','directory validation','reviewer access','public repository publication']}
print(json.dumps(result,indent=2));sys.exit(0 if not result['failed'] else 1)
