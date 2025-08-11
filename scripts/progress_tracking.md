# 📊 Progress Tracking System

This document explains how the automated progress tracking works for the 90-Day SRE Journey.

## 🎯 Overview

The progress tracking system automatically calculates and updates progress indicators based on:
- **Time elapsed** (40% weight): Days since August 11, 2025
- **Task completion** (60% weight): Marked completed tasks in README.md

## 🔧 How It Works

### Automatic Updates
- **Daily Schedule**: Progress updates automatically at 10:30 AM SAST via GitHub Actions
- **Push Triggers**: Updates whenever you push changes to the main branch
- **Manual Trigger**: Can be run manually from GitHub Actions tab

### Manual Updates
```bash
# Run locally
./scripts/update_progress.sh

# Or run Python script directly
python3 scripts/update_progress.py
```

## 📝 Marking Tasks Complete

To mark a task as completed, change `[ ]` to `[x]` in README.md:

```markdown
- [x] Completed task
- [ ] Incomplete task
```

### What Gets Tracked

1. **Weekly Tasks**: Main learning objectives for each week
2. **Deliverables**: Blog posts, GitHub repos, presentations, etc.
3. **Skills Acquired**: Technical competencies from the skills list

## 📊 Progress Indicators Updated

### 1. Progress Badge
```markdown
![Progress](https://img.shields.io/badge/Progress-25%25-yellow)
```
- **Colors**: Red (0-24%), Yellow (25-49%), Orange (50-74%), Green (75-100%)

### 2. Status Badge
```markdown
![Status](https://img.shields.io/badge/Status-Day%2020%20-%20Foundation-yellow)
```
- Shows current day and phase

### 3. Overall Progress Counter
```markdown
### Overall Progress: 25/90 days (28%)
```

### 4. Phase Progress Bars
```
Foundation:     ⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜ 30%
Technical:      ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ 0%
Production:     ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ 0%
```

## 🎯 Progress Calculation Formula

```
Overall Progress = (Task Completion × 60%) + (Time Elapsed × 40%)
```

### Task Categories:
- **Weekly Tasks**: 48 total (12 weeks × 4 tasks)
- **Deliverables**: 36 total (12 weeks × 3 deliverables)
- **Skills**: 9 total (from skills acquired list)

### Phase Progress:
- **Foundation**: Weeks 1-4 (16 tasks)
- **Technical**: Weeks 5-8 (16 tasks)
- **Production**: Weeks 9-12 (16 tasks)

## 🚀 Getting Started

1. **Mark your first completed task** by changing `[ ]` to `[x]`
2. **Push to GitHub** or wait for the daily update
3. **Watch the progress indicators update automatically**

## 🔍 Troubleshooting

### Script Not Running?
```bash
# Check if script is executable
ls -la scripts/update_progress.sh

# Make executable if needed
chmod +x scripts/update_progress.sh
```

### Python Issues?
```bash
# Check Python version
python3 --version

# Should be Python 3.6+ for f-string support
```

### GitHub Action Not Working?
- Check the Actions tab in GitHub
- Ensure you have write permissions to the repository
- Verify the workflow file syntax

## 📋 Files in the System

```
scripts/
├── update_progress.py      # Main Python script
├── update_progress.sh      # Shell wrapper script
└── progress_tracking.md    # This documentation

.github/workflows/
└── update-progress.yml     # GitHub Action workflow
```

## 💡 Tips

1. **Be consistent**: Mark tasks as complete when you finish them
2. **Check daily**: Progress updates automatically, but manual checks ensure accuracy
3. **Use git**: All updates are tracked in version control
4. **Customize**: Adjust weights and formulas in `update_progress.py` if needed
5. **Follow conventions**: See [Contributing Guidelines](../docs/CONTRIBUTING.md) for commit message format

## 🎉 Benefits

- **Motivation**: Visual progress keeps you motivated
- **Accountability**: Automated tracking prevents forgetting to update
- **Professional**: Shows systematic approach to learning
- **Data-driven**: Objective measurement of learning progress

---

*Last updated: August 2025*
