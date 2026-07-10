#!/usr/bin/env python3
"""PreToolUse guard: allow Supabase MCP calls only against known dev branch
projects. Prod projects (and any project not on the allowlist) are denied.
Fail-closed by design."""
import json, sys

# Supabase DEV branch project refs — the ONLY projects Claude may touch.
DEV_REFS = {
    "pxfmystogjhanuoxeezl",  # operations · develop
    "ovmthcycmrasxxevixia",  # users · develop
    "woqnzxapdflzgfebngig",  # signals · develop
    "tjzyvnuhtecwffuskmmr",  # vault · develop
}

try:
    data = json.load(sys.stdin)
except Exception:
    # If we can't parse input, fail closed.
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": "block-prod-supabase: unparseable hook input; denying."
    }}))
    sys.exit(0)

ref = (data.get("tool_input") or {}).get("project_id")

if ref not in DEV_REFS:
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": (
            f"block-prod-supabase: Supabase project '{ref}' is not an allowlisted "
            "dev project. Production and unknown projects are off-limits to Claude."
        )
    }}))
    sys.exit(0)

# Allowed dev project — stay silent, let the call proceed.
sys.exit(0)
