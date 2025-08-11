#!/bin/bash

# 90-Day SRE Journey - Progress Update Script
# This script updates the progress indicators in README.md

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 90-Day SRE Journey - Progress Update${NC}"
echo -e "${BLUE}======================================${NC}"
echo

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Error: python3 is required but not installed.${NC}"
    exit 1
fi

# Check if README.md exists
if [[ ! -f "$PROJECT_ROOT/README.md" ]]; then
    echo -e "${RED}❌ Error: README.md not found in project root.${NC}"
    exit 1
fi

# Run the Python script
echo -e "${YELLOW}🔄 Running progress calculation...${NC}"
echo

# Execute the Python script
python3 "$SCRIPT_DIR/update_progress.py"

# Check if the script ran successfully
if [[ $? -eq 0 ]]; then
    echo
    echo -e "${GREEN}✅ Progress update completed successfully!${NC}"
    echo
    echo -e "${BLUE}📁 Updated files:${NC}"
    echo "   - README.md"
    echo
    echo -e "${BLUE}💡 Usage tips:${NC}"
    echo "   - Mark tasks as completed by changing [ ] to [x]"
    echo "   - Run this script daily to keep progress current"
    echo "   - Script automatically calculates based on elapsed time and completed tasks"
    echo
    echo -e "${BLUE}🔧 To run manually:${NC}"
    echo "   ./scripts/update_progress.sh"
    echo "   or"
    echo "   python3 scripts/update_progress.py"
else
    echo -e "${RED}❌ Error: Progress update failed.${NC}"
    exit 1
fi
