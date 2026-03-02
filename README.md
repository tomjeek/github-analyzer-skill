# GitHub Analyzer Skill

> A comprehensive skill for analyzing GitHub repositories and extracting insights

## 📖 Overview

**github-analyzer** is an Agent Skill that automatically analyzes GitHub repositories by:

- 🔍 Extracting key information (README, features, tech stack)
- 💡 Identifying core insights and innovations
- 🔗 Building connections with existing knowledge
- 📊 Generating structured analysis reports
- 💾 Auto-saving to Obsidian knowledge base
- 🧠 Updating knowledge graph
- 🚀 Supporting co-evolution with larger projects

## 🎯 Use Cases

### 1. Discover New Tools
```
User: https://github.com/some-cool-tool
→ memU automatically analyzes and saves to Obsidian
```

### 2. Research Competitors
```
User: Analyze https://github.com/competitor/project
→ memU extracts key info and compares with existing tools
```

### 3. Learn Best Practices
```
User: What can we learn from this project?
→ memU identifies adoptable patterns and designs
```

### 4. Build Tool Systems
```
User: Research AI tools on GitHub
→ memU auto-categorizes and updates tool matrix
```

## 🛠️ Installation

### Method 1: Copy to Skills Directory

```bash
# Copy to your agent's skills directory
cp -r github-analyzer-skill /path/to/agent/skills/
```

### Method 2: Use with Claude Code / Cursor

```bash
# Copy to Claude Code skills
cp -r github-analyzer-skill ~/.claude/skills/

# Or Cursor skills
cp -r github-analyzer-skill ~/.cursor/skills/
```

## 📋 Workflow

```
GitHub URL Input
    ↓
Phase 1: URL Recognition & Validation
    ↓
Phase 2: Content Acquisition (Browser)
    ↓
Phase 3: Information Extraction (5 dimensions)
    ↓
Phase 4: Knowledge Graph Update
    ↓
Phase 5: Structured Output Generation
    ↓
Phase 6: Save Records (3 locations)
    ├─ Obsidian (Primary) ⭐
    ├─ Private (Backup)
    └─ Collaborative (Co-evolution)
    ↓
Phase 7: Co-evolution Update
```

## 💾 Output Locations

### Priority Order

1. **Obsidian Knowledge Base** (Primary) ⭐
   ```
   E:\Seed-Obsidian\Seed-Origin\Allinone\A1-Github\githubs\[project-name].md
   ```
   - Integrated into your knowledge system
   - Supports wikilinks and graph view

2. **Private Directory** (Backup)
   ```
   C:\Users\Lenovo\AppData\Roaming\memu-bot\agent-output\documents\[project-name].md
   ```

3. **Collaborative Directory** (Co-evolution)
   ```
   E:\Seed-memU\memU-context\2026-03-01\[project-name]-analysis.md
   ```

## 🎮 Usage Examples

### Example 1: Basic Analysis

```
User: https://github.com/anthropics/anthropic-sdk-python

memU:
✅ Analysis complete!
📁 Saved to Obsidian: anthropic-sdk-python.md
💡 Open Obsidian to view full analysis!
```

### Example 2: Deep Analysis

```
User: Analyze https://github.com/AutoMaker-Org/automaker in detail

memU:
🎯 Automaker - Autonomous AI Development Studio

## 📊 Project Overview
- **Core Philosophy**: Stop typing code. Start directing AI agents.
- **Stars**: 3k
- **Forks**: 577

## 💡 Core Insights
- Agentic Coding is the future
- Fully aligned with memU

## 📊 Inspiration for memU
1. Kanban workflow
2. Git worktree isolation
3. Plan approval mechanism

## 🔗 Co-evolution
- **Tool Category**: Building Tool (🔨)
- **Adoptable**: Kanban, Git isolation, Plan approval
```

## 📊 Output Format

### Obsidian-Ready Markdown

```markdown
# 🎯 [Project Name] - [Description]

## 📊 Project Overview
...

## 💡 Core Insights
- [[Related Insight]]
- [[Another Insight]]

## 🔗 Connections
| Dimension | [Project] | [Related Tool] |
|-----------|-----------|----------------|

## 🔗 Co-evolution
- **Tool Category**: [[Building Tool]]
- **For memU**: [Inspirations]

---
#github #tool #ai #[category]
*Analysis: [timestamp]*
*Project: [[Three Systems from Scratch]]*
```

**Features**:
- ✅ Wikilinks `[[link]]`
- ✅ Tags `#tag`
- ✅ Graph view support
- ✅ Editable in Obsidian

## 🎯 Tool Classification

Auto-identifies tool categories:

1. **Thinking Tools** (🤔) - Planning, analysis, research
2. **Building Tools** (🔨) - Creation, development, coding
3. **Execution Tools** (⚡) - Running, tasks, automation
4. **Integration Tools** (🔗) - Connection, coordination

## 🚀 Co-evolution

Each analysis automatically:

1. ✅ Updates "Three Systems from Scratch" progress
2. ✅ Identifies tool category
3. ✅ Extracts best practices
4. ✅ Updates tool matrix
5. ✅ Identifies collaboration opportunities

## 📝 Metadata

| Attribute | Value |
|-----------|-------|
| **Skill Name** | github-analyzer |
| **Version** | v1.2 |
| **Status** | 🟢 Active |
| **Created With** | skill-creator (meta-skill) |
| **Inspired By** | Claude Scientific Skills |
| **Project** | Three Systems from Scratch - System 2: Tool System |
| **Type** | Analysis Skill |
| **Obsidian** | ✅ Integrated |

## 🔗 Related Resources

- [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) - Meta-skill used to create this
- [Claude Scientific Skills](https://github.com/K-Dense-AI/claude-scientific-skills) - Inspiration for best practices
- [Agent Skills Standard](https://agentskills.io) - Skills specification

## 💬 Feedback & Contributions

This skill is part of the "Three Systems from Scratch" project - building a comprehensive tool system from zero.

Feedback and suggestions welcome!

---

**Made with ❤️ using skill-creator**

**Version**: v1.2  
**Status**: 🟢 Active  
**Last Updated**: 2026-03-02
