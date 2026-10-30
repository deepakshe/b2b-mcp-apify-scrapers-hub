# ⚡ 62 Zero-Proxy B2B Data Scrapers, Compliance Monitors & MCP Tools (Apify + n8n + Claude)

[![Apify Store](https://img.shields.io/badge/Apify_Store-62_Production_Actors-00C853?style=for-the-badge)](https://apify.com/deepaksheoran172)
[![MCP Ready](https://img.shields.io/badge/Model_Context_Protocol-Claude_%26_Cursor_Ready-7C3AED?style=for-the-badge)](https://apify.com/deepaksheoran172)
[![3D Icons Gallery](https://img.shields.io/badge/Luxury_3D_Icons-62_Bespoke_macOS_Grade-F59E0B?style=for-the-badge)](https://deepakshe.github.io/b2b-mcp-apify-scrapers-hub/gallery.html)
[![Pricing](https://img.shields.io/badge/Pay_Per_Event-$0.003_%2F_Record_(Zero_Proxy_Tax)-2563EB?style=for-the-badge)](https://apify.com/deepaksheoran172)

> **Why Automation Builders & Agencies Switch to This Fleet:** Most scrapers require expensive Residential Proxies ($15–$50/GB) and heavy headless browsers. All 62 tools below are engineered on **pure async HTTP/REST/DNS protocols**, executing in **3–5 seconds inside 512MB RAM** with **$0.00 proxy fees** and **Zero-Charge-on-Error protection** ($3.00 per 1,000 verified records).

---

## 📦 Downloadable Ready-to-Import n8n Workflow Templates (`n8n-templates/`)

We provide ready-to-import `.json` workflow templates for our core B2B actors. Import directly into your self-hosted n8n instance or n8n Cloud in seconds:

| Template Name | Target Apify Actor | Direct Download Link |
|---|---|---|
| **Bulk Email Verifier (MX & SMTP)** | `deepaksheoran172/bulk-email-verifier-mx-smtp` | [Download JSON](n8n-templates/bulk-email-verifier-mx-smtp-workflow.json) |
| **B2B Decision Maker Email Finder** | `deepaksheoran172/b2b-decision-maker-email-finder` | [Download JSON](n8n-templates/b2b-decision-maker-email-finder-workflow.json) |
| **Local Business Phone & WhatsApp Scraper** | `deepaksheoran172/local-business-website-phone-whatsapp-scraper` | [Download JSON](n8n-templates/local-business-website-phone-whatsapp-scraper-workflow.json) |
| **LinkedIn Public Jobs Scraper (No Login)** | `deepaksheoran172/linkedin-jobs-scraper-no-login` | [Download JSON](n8n-templates/linkedin-jobs-scraper-no-login-workflow.json) |
| **YouTube Sponsor Email Finder** | `deepaksheoran172/youtube-channel-sponsor-email-lead-finder` | [Download JSON](n8n-templates/youtube-channel-sponsor-email-lead-finder-workflow.json) |
| **Website Contact Extractor** | `deepaksheoran172/website-contact-extractor` | [Download JSON](n8n-templates/website-contact-extractor-workflow.json) |
| **SAM.gov Federal Contracting Monitor** | `deepaksheoran172/sam-gov-opportunity-monitor` | [Download JSON](n8n-templates/sam-gov-opportunity-monitor-workflow.json) |
| **Grants.gov Opportunity Matcher** | `deepaksheoran172/grants-gov-opportunity-matcher` | [Download JSON](n8n-templates/grants-gov-opportunity-matcher-workflow.json) |
| **India Public Tender & GeM Parser** | `deepaksheoran172/indian-public-tender-parser` | [Download JSON](n8n-templates/indian-public-tender-parser-workflow.json) |
| **Bulk Domain Security & SSL/DMARC Auditor** | `deepaksheoran172/domain-security-super-auditor` | [Download JSON](n8n-templates/domain-security-super-auditor-workflow.json) |
| **OFAC SDN Sanctions Screener** | `deepaksheoran172/ofac-sdn-delta-screener` | [Download JSON](n8n-templates/ofac-sdn-delta-screener-workflow.json) |
| **Shopify & WooCommerce Catalog Redirects** | `deepaksheoran172/store-catalog-redirect-extractor` | [Download JSON](n8n-templates/store-catalog-redirect-extractor-workflow.json) |
| **CISA KEV Vulnerability Alert Monitor** | `deepaksheoran172/cisa-kev-delta-monitor` | [Download JSON](n8n-templates/cisa-kev-delta-monitor-workflow.json) |
| **OSV Dependency CVE Scanner** | `deepaksheoran172/osv-dependency-cve-scanner` | [Download JSON](n8n-templates/osv-dependency-cve-scanner-workflow.json) |
| **OpenRouter AI Models & Pricing Registry** | `deepaksheoran172/openrouter-mcp-registry` | [Download JSON](n8n-templates/openrouter-mcp-registry-workflow.json) |

---

## 🔌 1-Click Integration Blueprints (n8n, Make.com, Claude MCP, Python)

### A. n8n / Make.com HTTP Request Node (Sync JSON Output in 1 Call)
```http
POST https://api.apify.com/v2/acts/deepaksheoran172~<ACTOR-SLUG>/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN
Content-Type: application/json

{}
```

### B. Claude Desktop / Cursor / Windsurf MCP Server Config (`claude_desktop_config.json`)
```json
{
  "mcpServers": {
    "apify-b2b-fleet": {
      "command": "npx",
      "args": ["-y", "@apify/actors-mcp-server"],
      "env": {
        "APIFY_TOKEN": "YOUR_APIFY_TOKEN"
      }
    }
  }
}
```

---

## 📊 Complete 62-Actor Production Directory (Direct Store & API Links)

### 📂 B2B Lead Gen & Email

| # | Tool Name & Apify Store Link | Direct Sync API Slug | High-Intent Use Cases & Keywords |
|---|---|---|---|
| 01 | **[⚡ Bulk Email Verifier MX SMTP](https://apify.com/deepaksheoran172/bulk-email-verifier-mx-smtp)** | `deepaksheoran172/bulk-email-verifier-mx-smtp` | bulk email verifier, mx smtp validation, millionverifier alternative, n8n email cleaner |
| 02 | **[⚡ B2B Decision Maker Email Finder](https://apify.com/deepaksheoran172/b2b-decision-maker-email-finder)** | `deepaksheoran172/b2b-decision-maker-email-finder` | b2b decision maker emails, ceo founder email finder, clay.com alternative, cold email leads |
| 03 | **[⚡ Social Bio Contact Email Extractor](https://apify.com/deepaksheoran172/social-bio-contact-email-extractor)** | `deepaksheoran172/social-bio-contact-email-extractor` | social media bio email scraper, creator contact extractor, influencer lead generation |
| 04 | **[⚡ Local Business Website Phone Whatsapp Scraper](https://apify.com/deepaksheoran172/local-business-website-phone-whatsapp-scraper)** | `deepaksheoran172/local-business-website-phone-whatsapp-scraper` | google maps whatsapp scraper, local business phone email extractor, b2b local leads |
| 05 | **[⚡ Website Contact Extractor](https://apify.com/deepaksheoran172/website-contact-extractor)** | `deepaksheoran172/website-contact-extractor` | website email phone social scraper, contact page parser, zero proxy lead extractor |

### 📂 YouTube & Social Intelligence

| # | Tool Name & Apify Store Link | Direct Sync API Slug | High-Intent Use Cases & Keywords |
|---|---|---|---|
| 01 | **[⚡ Youtube Bulk Transcript Captions Scraper](https://apify.com/deepaksheoran172/youtube-bulk-transcript-captions-scraper)** | `deepaksheoran172/youtube-bulk-transcript-captions-scraper` | youtube transcript api, bulk youtube captions downloader, llm rag video data |
| 02 | **[⚡ Youtube Channel Sponsor Email Lead Finder](https://apify.com/deepaksheoran172/youtube-channel-sponsor-email-lead-finder)** | `deepaksheoran172/youtube-channel-sponsor-email-lead-finder` | youtube sponsor finder, youtuber business email scraper, brand deal lead generation |
| 03 | **[⚡ Youtube Comments Painpoint Sentiment Miner](https://apify.com/deepaksheoran172/youtube-comments-painpoint-sentiment-miner)** | `deepaksheoran172/youtube-comments-painpoint-sentiment-miner` | youtube comments scraper, audience pain point miner, product research tool |
| 04 | **[⚡ Youtube Shorts Viral Hook Trend Tracker](https://apify.com/deepaksheoran172/youtube-shorts-viral-hook-trend-tracker)** | `deepaksheoran172/youtube-shorts-viral-hook-trend-tracker` | youtube shorts trend tracker, viral hook analyzer, short form video metrics |

### 📂 LinkedIn & Recruitment Intent

| # | Tool Name & Apify Store Link | Direct Sync API Slug | High-Intent Use Cases & Keywords |
|---|---|---|---|
| 01 | **[⚡ Linkedin Jobs Scraper No Login](https://apify.com/deepaksheoran172/linkedin-jobs-scraper-no-login)** | `deepaksheoran172/linkedin-jobs-scraper-no-login` | linkedin jobs scraper no login, zero proxy job board api, hiring intent scraper |
| 02 | **[⚡ Linkedin Hiring Company Lead Enricher](https://apify.com/deepaksheoran172/linkedin-hiring-company-lead-enricher)** | `deepaksheoran172/linkedin-hiring-company-lead-enricher` | hiring company lead enricher, b2b recruiting intent signals, headhunter automation |
| 03 | **[⚡ Linkedin Remote Salary Filter](https://apify.com/deepaksheoran172/linkedin-remote-salary-filter)** | `deepaksheoran172/linkedin-remote-salary-filter` | remote jobs salary scraper, compensation benchmark api, tech job aggregator |
| 04 | **[⚡ Linkedin Public Company Profiler](https://apify.com/deepaksheoran172/linkedin-public-company-profiler)** | `deepaksheoran172/linkedin-public-company-profiler` | company profile enricher, firmographic data api, b2b account enrichment |
| 05 | **[⚡ ATS Jobs Extractor](https://apify.com/deepaksheoran172/ats-jobs-extractor)** | `deepaksheoran172/ats-jobs-extractor` | greenhouse lever ashby workable scraper, ats job postings api, hiring tracker |

### 📂 E-Commerce & Web Audit

| # | Tool Name & Apify Store Link | Direct Sync API Slug | High-Intent Use Cases & Keywords |
|---|---|---|---|
| 01 | **[⚡ Store Catalog Redirect Extractor](https://apify.com/deepaksheoran172/store-catalog-redirect-extractor)** | `deepaksheoran172/store-catalog-redirect-extractor` | shopify catalog extractor, e-commerce redirect auditor, store product feed spy |
| 02 | **[⚡ Catalog Feed Normalizer](https://apify.com/deepaksheoran172/catalog-feed-normalizer)** | `deepaksheoran172/catalog-feed-normalizer` | product catalog normalizer, e-commerce json feed cleaner, merchant center tool |
| 03 | **[⚡ Website Health Checker](https://apify.com/deepaksheoran172/website-health-checker)** | `deepaksheoran172/website-health-checker` | website uptime response checker, broken link technical seo auditor, bulk http status |
| 04 | **[⚡ Google Keyword Suggester](https://apify.com/deepaksheoran172/google-keyword-suggester)** | `deepaksheoran172/google-keyword-suggester` | google autocomplete keyword api, long tail seo keyword scraper, content research |
| 05 | **[⚡ App Store Reviews Scraper](https://apify.com/deepaksheoran172/app-store-reviews-scraper)** | `deepaksheoran172/app-store-reviews-scraper` | apple app store reviews api, mobile app sentiment scraper, competitor review monitor |
| 06 | **[⚡ Website Screenshot PDF](https://apify.com/deepaksheoran172/website-screenshot-pdf)** | `deepaksheoran172/website-screenshot-pdf` | website screenshot to pdf api, headless browser visual capture, compliance archiving |
| 07 | **[⚡ Google Ads Transparency](https://apify.com/deepaksheoran172/google-ads-transparency)** | `deepaksheoran172/google-ads-transparency` | google ads transparency center scraper, competitor ad spy api, b2b ad intelligence |

### 📂 Cybersecurity & DevSecOps

| # | Tool Name & Apify Store Link | Direct Sync API Slug | High-Intent Use Cases & Keywords |
|---|---|---|---|
| 01 | **[⚡ Domain Security Super Auditor](https://apify.com/deepaksheoran172/domain-security-super-auditor)** | `deepaksheoran172/domain-security-super-auditor` | dmarc spf dkim bulk checker, ssl tls security header auditor, domain posture api |
| 02 | **[⚡ Domain Protocol Signals Enricher](https://apify.com/deepaksheoran172/domain-protocol-signals-enricher)** | `deepaksheoran172/domain-protocol-signals-enricher` | domain dns http protocol signals, tech stack security enricher, b2b domain intel |
| 03 | **[⚡ CISA KEV Delta Monitor](https://apify.com/deepaksheoran172/cisa-kev-delta-monitor)** | `deepaksheoran172/cisa-kev-delta-monitor` | cisa known exploited vulnerabilities api, kev cve alert feed, secops automation |
| 04 | **[⚡ OSV Dependency CVE Scanner](https://apify.com/deepaksheoran172/osv-dependency-cve-scanner)** | `deepaksheoran172/osv-dependency-cve-scanner` | google osv vulnerability scanner, pypi npm go maven cve checker, sbom security |
| 05 | **[⚡ Runtime And Container EOL Radar](https://apify.com/deepaksheoran172/runtime-and-container-eol-radar)** | `deepaksheoran172/runtime-and-container-eol-radar` | endoflife.date api, python nodejs ubuntu kubernetes eol tracker, devops compliance |
| 06 | **[⚡ Github Actions Pinning Auditor](https://apify.com/deepaksheoran172/github-actions-pinning-auditor)** | `deepaksheoran172/github-actions-pinning-auditor` | github actions sha pinning security auditor, ci cd supply chain vulnerability |
| 07 | **[⚡ RDAP Domain Registration Monitor](https://apify.com/deepaksheoran172/rdap-domain-registration-monitor)** | `deepaksheoran172/rdap-domain-registration-monitor` | icann rdap whois domain expiry registration monitor, brand protection api |
| 08 | **[⚡ TLS Certificate Expiry Auditor](https://apify.com/deepaksheoran172/tls-certificate-expiry-auditor)** | `deepaksheoran172/tls-certificate-expiry-auditor` | ssl tls x509 certificate expiry san auditor, port 443 handshake security scanner |
| 09 | **[⚡ DNS Record Drift Monitor](https://apify.com/deepaksheoran172/dns-record-drift-monitor)** | `deepaksheoran172/dns-record-drift-monitor` | dns a mx txt cname ns drift monitor, subdomain takeover hijack detector |

### 📂 GovTech, Tenders & Procurement

| # | Tool Name & Apify Store Link | Direct Sync API Slug | High-Intent Use Cases & Keywords |
|---|---|---|---|
| 01 | **[⚡ Indian Public Tender Parser](https://apify.com/deepaksheoran172/indian-public-tender-parser)** | `deepaksheoran172/indian-public-tender-parser` | indian government tenders api, eprocurement cppp gem scraper, b2b tender alerts |
| 02 | **[⚡ Usaspending Award Intelligence](https://apify.com/deepaksheoran172/usaspending-award-intelligence)** | `deepaksheoran172/usaspending-award-intelligence` | usaspending.gov federal contract awards api, government prime contractor intelligence |
| 03 | **[⚡ TED EU Tender Monitor](https://apify.com/deepaksheoran172/ted-eu-tender-monitor)** | `deepaksheoran172/ted-eu-tender-monitor` | eu ted tenders electronic daily api v3, european public procurement monitor |
| 04 | **[⚡ Grants Gov Opportunity Matcher](https://apify.com/deepaksheoran172/grants-gov-opportunity-matcher)** | `deepaksheoran172/grants-gov-opportunity-matcher` | grants.gov federal funding api keyless, grant opportunity matcher, non-profit rfp |
| 05 | **[⚡ World Bank Project Pipeline Matcher](https://apify.com/deepaksheoran172/world-bank-project-pipeline-matcher)** | `deepaksheoran172/world-bank-project-pipeline-matcher` | world bank project procurement api, global infrastructure funding pipeline |
| 06 | **[⚡ Sam Gov Opportunity Monitor](https://apify.com/deepaksheoran172/sam-gov-opportunity-monitor)** | `deepaksheoran172/sam-gov-opportunity-monitor` | sam.gov federal contract opportunities api keyless, govcon rfp solicitation monitor |
| 07 | **[⚡ State And Local RFP Aggregator](https://apify.com/deepaksheoran172/state-and-local-rfp-aggregator)** | `deepaksheoran172/state-and-local-rfp-aggregator` | us state municipal local rfp bid aggregator, socrata open procurement api |

### 📂 AI Agents & Developer Ecosystem

| # | Tool Name & Apify Store Link | Direct Sync API Slug | High-Intent Use Cases & Keywords |
|---|---|---|---|
| 01 | **[⚡ Openrouter MCP Registry](https://apify.com/deepaksheoran172/openrouter-mcp-registry)** | `deepaksheoran172/openrouter-mcp-registry` | openrouter models api, mcp server registry, llm pricing context benchmark |
| 02 | **[⚡ Scanned Document OCR](https://apify.com/deepaksheoran172/scanned-document-ocr)** | `deepaksheoran172/scanned-document-ocr` | scanned pdf image ocr api, document text extraction, automated invoice parser |
| 03 | **[⚡ npm Package Health Auditor](https://apify.com/deepaksheoran172/npm-package-health-auditor)** | `deepaksheoran172/npm-package-health-auditor` | npm package security deprecation auditor, supply chain health check, nodejs audit |
| 04 | **[⚡ PyPI Package Health Auditor](https://apify.com/deepaksheoran172/pypi-package-health-auditor)** | `deepaksheoran172/pypi-package-health-auditor` | pypi python package auditor, yanked release maintainer check, python supply chain |
| 05 | **[⚡ OpenAPI Breaking Change Diff](https://apify.com/deepaksheoran172/openapi-breaking-change-diff)** | `deepaksheoran172/openapi-breaking-change-diff` | openapi swagger breaking change detector, api contract diff tool, ci cd api check |
| 06 | **[⚡ Hacker News Launch And Trend Monitor](https://apify.com/deepaksheoran172/hacker-news-launch-and-trend-monitor)** | `deepaksheoran172/hacker-news-launch-and-trend-monitor` | algolia hacker news show hn launch monitor, tech trend velocity scraper |
| 07 | **[⚡ Github Competitive Repo Tracker](https://apify.com/deepaksheoran172/github-competitive-repo-tracker)** | `deepaksheoran172/github-competitive-repo-tracker` | github repository star velocity issue tracker, open source competitor intelligence |
| 08 | **[⚡ Package Dependency Graph Enricher](https://apify.com/deepaksheoran172/package-dependency-graph-enricher)** | `deepaksheoran172/package-dependency-graph-enricher` | google deps.dev dependency graph openssf scorecard api, transitive package risk |
| 09 | **[⚡ Docker Hub Image Staleness Monitor](https://apify.com/deepaksheoran172/docker-hub-image-staleness-monitor)** | `deepaksheoran172/docker-hub-image-staleness-monitor` | docker hub container image tag staleness digest monitor, devops registry audit |
| 10 | **[⚡ npm Download Trend Reporter](https://apify.com/deepaksheoran172/npm-download-trend-reporter)** | `deepaksheoran172/npm-download-trend-reporter` | npm package weekly download growth velocity api, developer adoption trend tracker |

### 📂 Cloud Health & SRE

| # | Tool Name & Apify Store Link | Direct Sync API Slug | High-Intent Use Cases & Keywords |
|---|---|---|---|
| 01 | **[⚡ Statuspage Incident Aggregator](https://apify.com/deepaksheoran172/statuspage-incident-aggregator)** | `deepaksheoran172/statuspage-incident-aggregator` | atlassian statuspage api aggregator, saas outage monitor, cloudflare github datadog status |
| 02 | **[⚡ AWS Health Incident Monitor](https://apify.com/deepaksheoran172/aws-health-incident-monitor)** | `deepaksheoran172/aws-health-incident-monitor` | aws service health dashboard api, amazon web services outage monitor, sre alerting |
| 03 | **[⚡ GCP Incident Monitor](https://apify.com/deepaksheoran172/gcp-incident-monitor)** | `deepaksheoran172/gcp-incident-monitor` | google cloud status incident api, gcp regional outage monitor, cloud reliability |
| 04 | **[⚡ Azure Status Feed Monitor](https://apify.com/deepaksheoran172/azure-status-feed-monitor)** | `deepaksheoran172/azure-status-feed-monitor` | microsoft azure status rss api, azure cloud outage monitor, devops incident feed |
| 05 | **[⚡ API SDK Deprecation Radar](https://apify.com/deepaksheoran172/api-sdk-deprecation-radar)** | `deepaksheoran172/api-sdk-deprecation-radar` | rfc 8594 sunset deprecation header monitor, api lifecycle radar, sdk breaking changes |

### 📂 Recalls, Compliance & Registries

| # | Tool Name & Apify Store Link | Direct Sync API Slug | High-Intent Use Cases & Keywords |
|---|---|---|---|
| 01 | **[⚡ FDA Food And Drug Enforcement Monitor](https://apify.com/deepaksheoran172/fda-food-and-drug-enforcement-monitor)** | `deepaksheoran172/fda-food-and-drug-enforcement-monitor` | openfda food drug recall enforcement api, class i ii iii recall monitor, supply chain |
| 02 | **[⚡ CPSC Recall Monitor](https://apify.com/deepaksheoran172/cpsc-recall-monitor)** | `deepaksheoran172/cpsc-recall-monitor` | cpsc saferproducts consumer recall api, product hazard monitor, e-commerce compliance |
| 03 | **[⚡ NHTSA Vehicle Recall Monitor](https://apify.com/deepaksheoran172/nhtsa-vehicle-recall-monitor)** | `deepaksheoran172/nhtsa-vehicle-recall-monitor` | nhtsa vehicle safety recall api, automotive vin campaign monitor, fleet safety |
| 04 | **[⚡ FDA 510(k) Clearance Intelligence](https://apify.com/deepaksheoran172/fda-510k-clearance-intelligence)** | `deepaksheoran172/fda-510k-clearance-intelligence` | openfda 510k medical device clearance api, medtech regulatory approval intelligence |
| 05 | **[⚡ OFAC SDN Delta Screener](https://apify.com/deepaksheoran172/ofac-sdn-delta-screener)** | `deepaksheoran172/ofac-sdn-delta-screener` | us treasury ofac sdn sanctions screener api, aml kyc compliance check, watchlist |
| 06 | **[⚡ ECHA SVHC RASFF Chemical Alert Monitor](https://apify.com/deepaksheoran172/echa-svhc-rasff-chemical-alert-monitor)** | `deepaksheoran172/echa-svhc-rasff-chemical-alert-monitor` | eu echa svhc candidate list api, reach chemical compliance monitor, rasff alerts |
| 07 | **[⚡ SEC Filing Event Intelligence](https://apify.com/deepaksheoran172/sec-filing-event-intelligence)** | `deepaksheoran172/sec-filing-event-intelligence` | sec edgar 8-k 10-k 10-q filings api, cik corporate event monitor, financial intel |
| 08 | **[⚡ GLEIF LEI Resolver](https://apify.com/deepaksheoran172/gleif-lei-resolver)** | `deepaksheoran172/gleif-lei-resolver` | gleif legal entity identifier lei api, corporate parent child ownership resolver |
| 09 | **[⚡ Companies House Event Monitor](https://apify.com/deepaksheoran172/companies-house-event-monitor)** | `deepaksheoran172/companies-house-event-monitor` | uk companies house registry scraper keyless, british corporate filing kyc monitor |
| 10 | **[⚡ Opensanctions Screening Enricher](https://apify.com/deepaksheoran172/opensanctions-screening-enricher)** | `deepaksheoran172/opensanctions-screening-enricher` | opensanctions global pep sanctions screening api, kyc compliance entity matcher |


## 📦 Official Open-Source MCP & Python Micro-Repositories

Each high-value B2B Actor has a dedicated, zero-dependency Open-Source SDK and MCP repository with ready-to-use Python wrappers, n8n workflows, and Cursor/Claude configs:

| Micro-Repository | Target Capability | Apify Store Badge | MCP / n8n Template |
| :--- | :--- | :--- | :--- |
| [`deepakshe/b2b-lead-domain-intelligence-suite-mcp-api`](https://github.com/deepakshe/b2b-lead-domain-intelligence-suite-mcp-api) | **⭐ All-in-One Lead & Domain Intelligence Suite** | [![Run](https://img.shields.io/badge/Store-Run-blue)](https://apify.com/deepaksheoran172/b2b-lead-domain-intelligence-suite) | [Workflow JSON](https://github.com/deepakshe/b2b-lead-domain-intelligence-suite-mcp-api/blob/main/workflow.json) |
| [`deepakshe/bulk-email-verifier-mx-smtp-mcp-api`](https://github.com/deepakshe/bulk-email-verifier-mx-smtp-mcp-api) | **B2B Lead Gen & Email Verification** | [![Run](https://img.shields.io/badge/Store-Run-blue)](https://apify.com/deepaksheoran172/bulk-email-verifier-mx-smtp) | [Workflow JSON](https://github.com/deepakshe/bulk-email-verifier-mx-smtp-mcp-api/blob/main/workflow.json) |
| [`deepakshe/b2b-decision-maker-email-finder-mcp-api`](https://github.com/deepakshe/b2b-decision-maker-email-finder-mcp-api) | **B2B Lead Gen & Prospecting** | [![Run](https://img.shields.io/badge/Store-Run-blue)](https://apify.com/deepaksheoran172/b2b-decision-maker-email-finder) | [Workflow JSON](https://github.com/deepakshe/b2b-decision-maker-email-finder-mcp-api/blob/main/workflow.json) |
| [`deepakshe/local-business-website-phone-whatsapp-scraper-mcp-api`](https://github.com/deepakshe/local-business-website-phone-whatsapp-scraper-mcp-api) | **Local Business & Lead Gen** | [![Run](https://img.shields.io/badge/Store-Run-blue)](https://apify.com/deepaksheoran172/local-business-website-phone-whatsapp-scraper) | [Workflow JSON](https://github.com/deepakshe/local-business-website-phone-whatsapp-scraper-mcp-api/blob/main/workflow.json) |
| [`deepakshe/linkedin-jobs-scraper-no-login-mcp-api`](https://github.com/deepakshe/linkedin-jobs-scraper-no-login-mcp-api) | **LinkedIn & Recruitment Intent** | [![Run](https://img.shields.io/badge/Store-Run-blue)](https://apify.com/deepaksheoran172/linkedin-jobs-scraper-no-login) | [Workflow JSON](https://github.com/deepakshe/linkedin-jobs-scraper-no-login-mcp-api/blob/main/workflow.json) |
| [`deepakshe/youtube-channel-sponsor-email-lead-finder-mcp-api`](https://github.com/deepakshe/youtube-channel-sponsor-email-lead-finder-mcp-api) | **YouTube & Social Intelligence** | [![Run](https://img.shields.io/badge/Store-Run-blue)](https://apify.com/deepaksheoran172/youtube-channel-sponsor-email-lead-finder) | [Workflow JSON](https://github.com/deepakshe/youtube-channel-sponsor-email-lead-finder-mcp-api/blob/main/workflow.json) |
| [`deepakshe/website-contact-extractor-mcp-api`](https://github.com/deepakshe/website-contact-extractor-mcp-api) | **B2B Lead Gen & Data Enrichment** | [![Run](https://img.shields.io/badge/Store-Run-blue)](https://apify.com/deepaksheoran172/website-contact-extractor) | [Workflow JSON](https://github.com/deepakshe/website-contact-extractor-mcp-api/blob/main/workflow.json) |
| [`deepakshe/domain-security-super-auditor-mcp-api`](https://github.com/deepakshe/domain-security-super-auditor-mcp-api) | **Cybersecurity & DevSecOps** | [![Run](https://img.shields.io/badge/Store-Run-blue)](https://apify.com/deepaksheoran172/domain-security-super-auditor) | [Workflow JSON](https://github.com/deepakshe/domain-security-super-auditor-mcp-api/blob/main/workflow.json) |
| [`deepakshe/sam-gov-opportunity-monitor-mcp-api`](https://github.com/deepakshe/sam-gov-opportunity-monitor-mcp-api) | **GovTech, Tenders & Procurement** | [![Run](https://img.shields.io/badge/Store-Run-blue)](https://apify.com/deepaksheoran172/sam-gov-opportunity-monitor) | [Workflow JSON](https://github.com/deepakshe/sam-gov-opportunity-monitor-mcp-api/blob/main/workflow.json) |
| [`deepakshe/ofac-sdn-delta-screener-mcp-api`](https://github.com/deepakshe/ofac-sdn-delta-screener-mcp-api) | **Compliance, KYC & AML** | [![Run](https://img.shields.io/badge/Store-Run-blue)](https://apify.com/deepaksheoran172/ofac-sdn-delta-screener) | [Workflow JSON](https://github.com/deepakshe/ofac-sdn-delta-screener-mcp-api/blob/main/workflow.json) |
| [`deepakshe/osv-dependency-cve-scanner-mcp-api`](https://github.com/deepakshe/osv-dependency-cve-scanner-mcp-api) | **Cybersecurity & Vulnerability Management** | [![Run](https://img.shields.io/badge/Store-Run-blue)](https://apify.com/deepaksheoran172/osv-dependency-cve-scanner) | [Workflow JSON](https://github.com/deepakshe/osv-dependency-cve-scanner-mcp-api/blob/main/workflow.json) |
