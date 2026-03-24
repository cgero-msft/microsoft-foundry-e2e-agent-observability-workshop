#!/usr/bin/env bash
# ============================================================
#  Contoso Travel LangGraph Agent — Deploy to Foundry Agent Service
# ============================================================
#  Prerequisites:
#    - Azure CLI (az) installed and logged in
#    - Azure Developer CLI (azd) installed
#    - A Foundry project already created (see Lab 00)
#    - Environment variables set (see .env or sample.env)
#
#  Usage:
#    chmod +x deploy.sh
#    ./deploy.sh
# ============================================================

set -euo pipefail

CYAN='\033[0;36m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo ""
echo -e "${CYAN}╔══════════════════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║  🧳 Contoso Travel Agent (LangGraph) — Deployment      ║${NC}"
echo -e "${CYAN}╚══════════════════════════════════════════════════════════╝${NC}"
echo ""

# ── Step 1: Check prerequisites ──
echo -e "${CYAN}[1/4]${NC} Checking prerequisites..."

if ! command -v azd &> /dev/null; then
    echo -e "${RED}  ✗ Azure Developer CLI (azd) not found.${NC}"
    echo "    Install: https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd"
    exit 1
fi
echo -e "${GREEN}  ✓ azd installed${NC}"

if ! command -v az &> /dev/null; then
    echo -e "${RED}  ✗ Azure CLI (az) not found.${NC}"
    exit 1
fi
echo -e "${GREEN}  ✓ az installed${NC}"

if ! az account show &> /dev/null; then
    echo -e "${YELLOW}  ⚠ Not logged in. Running az login...${NC}"
    az login --use-device-code
fi
echo -e "${GREEN}  ✓ Authenticated${NC}"

# ── Step 2: Load environment ──
echo ""
echo -e "${CYAN}[2/4]${NC} Loading environment..."

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ -f "${SCRIPT_DIR}/.env" ]; then
    set -a; source "${SCRIPT_DIR}/.env"; set +a
    echo -e "${GREEN}  ✓ Loaded .env from ${SCRIPT_DIR}${NC}"
elif [ -f "${SCRIPT_DIR}/../../labs/notebooks/.env" ]; then
    set -a; source "${SCRIPT_DIR}/../../labs/notebooks/.env"; set +a
    echo -e "${GREEN}  ✓ Loaded .env from labs/notebooks/${NC}"
else
    echo -e "${YELLOW}  ⚠ No .env found. Ensure environment variables are set.${NC}"
fi

if [ -z "${AZURE_AI_PROJECT_ENDPOINT:-}" ]; then
    echo -e "${RED}  ✗ AZURE_AI_PROJECT_ENDPOINT not set${NC}"
    exit 1
fi
echo -e "${GREEN}  ✓ AZURE_AI_PROJECT_ENDPOINT set${NC}"

# ── Step 3: Deploy the agent ──
echo ""
echo -e "${CYAN}[3/4]${NC} Deploying agent to Foundry Agent Service..."
echo ""

cd "${SCRIPT_DIR}"
azd ai agent deploy --project-endpoint "${AZURE_AI_PROJECT_ENDPOINT}"

# ── Step 4: Verify ──
echo ""
echo -e "${CYAN}[4/4]${NC} Deployment complete!"
echo ""
echo -e "${GREEN}╔══════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║  ✅ Agent deployed! Test it from the Foundry portal     ║${NC}"
echo -e "${GREEN}║     or run the tracing/eval notebooks against it.       ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "  ${CYAN}Next steps:${NC}"
echo -e "    1. Open the Foundry portal → Agents tab to verify"
echo -e "    2. Run Lab 04 (Tracing) to observe the deployed agent"
echo -e "    3. Run Lab 05 (Evaluation) to assess quality & safety"
echo -e "    4. Run Lab 06 (Red Teaming) to stress-test security"
echo ""
