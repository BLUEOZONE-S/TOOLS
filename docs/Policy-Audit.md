# POLICY COMPLIANCE REVIEW REPORT (Vortex Internal Tooling)
Reviewed: 2026-02-01
Reviewer: Codex

## Scope
This review covers the local HTML/JS front-end (`index.html`) and the local Python launcher (`launcher.py`) plus the Windows launcher (`Run_Studio.bat`). The tool appears to run as a local-only web app that processes user-supplied Excel and PDF files in-browser and exports stamped PDFs as a ZIP download. 

## Step 1: Data flows (sources → processing → sinks)
- **Sources**: User-selected Excel files and PDF files via file input elements in the browser UI (`handleExcel`, `handlePdfs`). 
- **Processing**: In-browser parsing (XLSX, PDF.js, PDF-Lib) and overlay generation; in-memory state only (no persistent storage). 
- **Sinks**: Generated ZIP download (`processBatch`) via browser download; local preview rendering to `<img>` via data URLs. 
- **External transmission**: None observed after removing external font import; the app runs fully offline. 

## Step 2: Security boundary
- **Authn/Authz**: None; the app is intended for local use only. 
- **Network exposure**: Local HTTP server started by `launcher.py`. Binding now restricted to `localhost` to avoid LAN exposure. 
- **Environment separation**: Not applicable (no environment config); local-only runtime. 

## Step 3: Policy triggers
- **AI**: No AI calls or AI SDKs present. 
- **Third-party services**: None (all libraries are local static assets). 
- **Telemetry/analytics**: None observed. 
- **Secrets**: No credentials in code. 
- **Downloads/auto-exec**: ZIP download is user-initiated. No auto-update or remote code execution behavior observed. 

## Step 4: Minimal fixes applied
1. **Restricted local server bind**: Python launcher now binds to `localhost` only to prevent LAN exposure. 
2. **Removed external font import**: The Google Fonts import was removed to avoid unapproved external calls; default system fonts are used instead. 

---

## A) Acceptable use of IT resources / security basics
**Compliant**
- No hard-coded credentials identified. 
- Local-only processing with no outbound network calls. 
- Third-party libraries are bundled locally. 

**Non-compliant**
- None noted after the above fixes. 

**Needs review**
- The local HTTP server has no auth/TLS; confirm this is acceptable for localhost-only usage. 

## B) Shadow IT & software request controls
**Compliant**
- No external SaaS integrations or telemetry endpoints observed. 

**Non-compliant**
- None observed. 

**Needs review**
- Confirm distribution/installation of the launcher follows internal software request controls. 

## C) AI ethical use
**Compliant**
- No AI functionality detected. 

**Non-compliant**
- None observed. 

**Needs review**
- Not applicable. 

## D) Privacy & confidentiality / data handling
**Compliant**
- Data handled in-memory with explicit user-triggered downloads; no persistent browser storage used. 
- No evidence of silent uploads or background syncing. 

**Non-compliant**
- None observed. 

**Needs review**
- ZIP export filenames include project name and element identifiers; confirm naming conventions are acceptable for confidential projects. 
- Consider adding a UI reminder that exported ZIPs contain confidential data. 

## E) Professional conduct safeguards
**Compliant**
- No hidden monitoring or "phone home" behavior observed. 

**Non-compliant**
- None observed. 

**Needs review**
- Consider adding a security reporting section in docs if this tool will be widely distributed. 

---

# High-risk findings (Top 10)
1. **Local HTTP server without auth/TLS** (acceptable only if strictly localhost and single-user). 
2. **Confidential exports**: ZIP files include potentially sensitive names; confirm policy guidance. 
3. **No explicit user-facing data handling notice** for confidentiality expectations. 
4. **Lack of documented security reporting channel** if distributed beyond a small team. 
5. **No explicit retention guidance** for generated output files. 
6. **No role-based access control** (expected for local-only use; needs policy validation). 
7. **No environment separation** (local-only tooling; needs policy validation if deployed centrally). 
8. **Local file handling**: ensure endpoint does not become network-exposed in future distribution. 
9. **Dependency hygiene**: local minified libraries should be reviewed for version/pinning and known vulnerabilities. 
10. **Browser file access**: ensure users understand files remain local; avoid future features that add remote sync without review. 

# Required remediation list (ordered)
1. Confirm localhost-only usage policy for the launcher and document that requirement. 
2. Add a short UI notice about confidential data handling and export responsibility. 
3. Document approved distribution and support/reporting channels in README or docs. 
4. Review bundled third-party library versions for known vulnerabilities and track updates. 
5. Add data retention guidance for exported ZIPs if required by policy. 

# External services inventory
- **None** (all libraries are bundled locally; no external network calls detected after removing Google Fonts import). 

# Data classification notes
- **Confidential inputs**: Excel specs, PDF drawings, project names, RAL color data. 
- **Processing**: Local-only in browser memory (no server-side persistence). 
- **Outputs**: ZIP of stamped PDFs downloaded to user workstation; filenames include project identifiers. 

