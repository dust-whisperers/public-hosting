#!/usr/bin/env python3
"""PreToolUse guard for sessions in bypassPermissions mode (decision D10).

Bypass mode stays on for speed. This hook narrows the blast radius of a
prompt injection (an issue body, a Slack message, a fetched page steering
the session) to what a human would notice, by acting on a short list:

  DENY  force-push or branch deletion of main / develop / master
  DENY  editing GitHub Actions secrets or variables (gh secret / gh variable,
        gh api .../secrets|variables with a write method)
  DENY  piping a download straight into a shell (curl ... | sh)
  DENY  curl / wget SENDING data (-d, -F, -T, POST/PUT/PATCH/DELETE) to a
        host outside ALLOWED_HOSTS -- the exfiltration shape
  ASK   sending Slack messages, e-mail, and Drive writes / shares

Everything else passes untouched. It is a deny-list, so it fails OPEN on
input it cannot parse (unlike block-prod-supabase.py, which is an allowlist
and fails closed). To let an upload reach a new host, add its domain below.
"""
import json, re, shlex, sys

ALLOWED_HOSTS = (
    "dustwhisperers.com", "supabase.co", "supabase.com", "github.com",
    "githubusercontent.com", "railway.app", "railway.internal", "npmjs.org",
    "anthropic.com", "claude.ai", "expo.dev", "sentry.io", "localhost",
    "127.0.0.1",
)
PROTECTED = r"(main|develop|master)"

ASK_TOOLS = re.compile(
    r"^mcp__(Slack__slack_(send_message|schedule_message|create_canvas|update_canvas)"
    r"|Gmail__(send_message|forward|reply)"
    r"|Google_Drive__(create_file|update_file|copy_file|share_file|trash_file))$"
)


def decide(decision, reason):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": decision,
        "permissionDecisionReason": f"guard-risky-actions: {reason}",
    }}))
    sys.exit(0)


def host_allowed(host):
    host = host.lower().split("@")[-1].split(":")[0]
    return any(host == h or host.endswith("." + h) for h in ALLOWED_HOSTS)


def check_bash(cmd):
    c = " ".join(cmd.split())
    for part in re.split(r"&&|\|\||;|\n", c):
        p = part.strip()
        if re.search(r"\bgit\b.*\bpush\b", p):
            forced = re.search(r"(\s--force(-with-lease)?\b|\s-f\b|\s\+\S)", p)
            if forced and re.search(rf"(\s|:|/|\+){PROTECTED}(\s|$)", p):
                decide("deny", "force-push to main/develop/master is blocked. Push to a feature branch.")
            if re.search(rf"(--delete\s+\S*\s*{PROTECTED}\b|\s:{PROTECTED}(\s|$))", p):
                decide("deny", "deleting main/develop/master is blocked.")
        if re.search(r"\bgh\s+(secret|variable)\s+(set|delete|remove)\b", p):
            decide("deny", "editing GitHub secrets/variables from a session is blocked. Do it in the GitHub UI.")
        if re.search(r"\bgh\s+api\b", p) and re.search(r"/(secrets|variables)\b", p) \
                and re.search(r"(-X|--method)\s*(PUT|POST|PATCH|DELETE)", p, re.I):
            decide("deny", "writing GitHub secrets/variables through gh api is blocked.")
    if re.search(r"\b(curl|wget)\b[^|]*\|\s*(sudo\s+)?(ba|z|da)?sh\b", c):
        decide("deny", "piping a download into a shell is blocked. Download, read, then run.")
    for seg in re.split(r"\||&&|\|\||;", c):
        if not re.search(r"\b(curl|wget)\b", seg):
            continue
        sends = re.search(
            r"(\s-d\b|\s-d\S|--data|\s-F\b|--form|\s-T\b|--upload-file|--post-(data|file)"
            r"|(-X|--request|--method)\s*['\"]?(POST|PUT|PATCH|DELETE))", seg, re.I)
        if not sends:
            continue
        for host in re.findall(r"https?://([^/\s'\"?#]+)", seg):
            if not host_allowed(host):
                decide("deny", f"sending data to {host} is blocked (not in ALLOWED_HOSTS in "
                               ".claude/hooks/guard-risky-actions.py). Add the domain there if it is legitimate.")


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)  # deny-list: fail open
    tool = data.get("tool_name") or ""
    tin = data.get("tool_input") or {}
    if tool == "Bash":
        check_bash(str(tin.get("command") or ""))
    elif ASK_TOOLS.match(tool):
        decide("ask", f"{tool} sends or shares content outside the repo -- confirm it is intended.")
    sys.exit(0)


if __name__ == "__main__":
    main()
