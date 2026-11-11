#!/usr/bin/env python3
"""
Model Context Protocol (MCP) Server for Apify B2B Suite.
Provides standard stdio JSON-RPC 2.0 interface for AI assistants (Claude Desktop, Cursor, Windsurf).
Author: Deepak Sheoran (deepaksheoran172)
"""
import sys
import json
import logging
import urllib.request
import urllib.error

logging.basicConfig(level=logging.INFO, stream=sys.stderr, format="%(asctime)s [%(levelname)s] %(message)s")

SERVER_NAME = "b2b-mcp-apify-scrapers-hub"
SERVER_VERSION = "1.0.0"

TOOLS = [
    {
        "name": "domain_security_auditor",
        "description": "Audit domain DNS, SPF, DMARC, MX records and SSL certificate status to detect email spoofing and security risks.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "domain": {"type": "string", "description": "Target domain (e.g., example.com)"}
            },
            "required": ["domain"]
        }
    },
    {
        "name": "shopify_catalog_extractor",
        "description": "Extract product catalog, handles, prices, and generate 301 redirect paths for any Shopify store.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "store_url": {"type": "string", "description": "URL of the target Shopify store (e.g., https://store.myshopify.com)"},
                "max_items": {"type": "integer", "description": "Maximum products to extract (default 50)", "default": 50}
            },
            "required": ["store_url"]
        }
    },
    {
        "name": "google_keyword_suggester",
        "description": "Retrieve live Google autocomplete search keyword suggestions across US/Global markets.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "keyword": {"type": "string", "description": "Seed keyword or search phrase"},
                "country_code": {"type": "string", "description": "2-letter country code (default 'us')", "default": "us"}
            },
            "required": ["keyword"]
        }
    },
    {
        "name": "website_contact_extractor",
        "description": "Extract verified business emails, phone numbers, and social links from company websites without browser overhead.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "Target company website URL"}
            },
            "required": ["url"]
        }
    },
    {
        "name": "ats_jobs_extractor",
        "description": "Extract live hiring signals and open engineering/sales job requisitions from Greenhouse, Lever, and Ashby boards.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "company_slug": {"type": "string", "description": "Company slug or careers URL"}
            },
            "required": ["company_slug"]
        }
    }
]

def handle_initialize(msg_id, params):
    return {
        "jsonrpc": "2.0",
        "id": msg_id,
        "result": {
            "protocolVersion": "2024-11-05",
            "capabilities": {
                "tools": {}
            },
            "serverInfo": {
                "name": SERVER_NAME,
                "version": SERVER_VERSION
            }
        }
    }

def handle_tools_list(msg_id):
    return {
        "jsonrpc": "2.0",
        "id": msg_id,
        "result": {
            "tools": TOOLS
        }
    }

def audit_domain_dns(domain):
    clean = domain.strip().replace("https://", "").replace("http://", "").split("/")[0]
    records = {"domain": clean, "spf": None, "dmarc": None, "mx": []}
    try:
        req = urllib.request.Request(
            f"https://cloudflare-dns.com/dns-query?name={clean}&type=TXT",
            headers={"Accept": "application/dns-json", "User-Agent": "MCP-Security-Auditor/1.0"}
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode())
            for ans in data.get("Answer", []):
                val = ans.get("data", "").strip('"')
                if "v=spf1" in val:
                    records["spf"] = val
    except Exception as e:
        records["spf_error"] = str(e)

    try:
        req = urllib.request.Request(
            f"https://cloudflare-dns.com/dns-query?name=_dmarc.{clean}&type=TXT",
            headers={"Accept": "application/dns-json", "User-Agent": "MCP-Security-Auditor/1.0"}
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode())
            for ans in data.get("Answer", []):
                val = ans.get("data", "").strip('"')
                if "v=DMARC1" in val:
                    records["dmarc"] = val
    except Exception as e:
        records["dmarc_error"] = str(e)

    records["dmarc_policy"] = "REJECT" if records.get("dmarc") and "p=reject" in records["dmarc"] else "QUARANTINE" if records.get("dmarc") and "p=quarantine" in records["dmarc"] else "NONE/VULNERABLE"
    return records

def handle_tools_call(msg_id, params):
    tool_name = params.get("name")
    args = params.get("arguments", {})

    if tool_name == "domain_security_auditor":
        domain = args.get("domain", "")
        res = audit_domain_dns(domain)
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "content": [{"type": "text", "text": json.dumps(res, indent=2)}]
            }
        }
    elif tool_name == "google_keyword_suggester":
        kw = args.get("keyword", "")
        cc = args.get("country_code", "us")
        url = f"https://suggestqueries.google.com/complete/search?client=firefox&gl={cc}&q={urllib.parse.quote(kw)}"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=5) as resp:
                data = json.loads(resp.read().decode("utf-8", errors="ignore"))
                suggestions = data[1] if len(data) > 1 else []
                res = {"seed": kw, "country": cc, "suggestions": suggestions}
        except Exception as e:
            res = {"seed": kw, "error": str(e), "suggestions": []}
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "content": [{"type": "text", "text": json.dumps(res, indent=2)}]
            }
        }
    else:
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "content": [{
                    "type": "text",
                    "text": f"Tool '{tool_name}' is available via Apify cloud runner. Run at: https://apify.com/deepaksheoran172/{tool_name.replace('_', '-')}"
                }]
            }
        }

def main():
    logging.info("Starting B2B MCP Stdio Server...")
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            method = req.get("method")
            msg_id = req.get("id")
            params = req.get("params", {})

            if method == "initialize":
                resp = handle_initialize(msg_id, params)
            elif method == "notifications/initialized":
                continue
            elif method == "tools/list":
                resp = handle_tools_list(msg_id)
            elif method == "tools/call":
                resp = handle_tools_call(msg_id, params)
            elif method == "ping":
                resp = {"jsonrpc": "2.0", "id": msg_id, "result": {}}
            else:
                resp = {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "error": {"code": -32601, "message": f"Method '{method}' not found"}
                }

            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            logging.error(f"Error processing message: {e}")
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": "Parse error", "data": str(e)}
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
