# GitHub Analyzer

Analyzes GitHub repositories by extracting key information, identifying tech stacks, discovering core insights, and establishing connections with existing knowledge. Use when memU needs to analyze GitHub projects for: (1) discovering new tools, (2) researching competitors, (3) learning best practices, (4) finding inspiration for tool system development, or (5) building the "Three Systems from Scratch" project.

## When to Use This Skill

Use this skill when:
- User sends a GitHub URL (https://github.com/owner/repo)
- User asks to "analyze this GitHub repository"
- User wants to understand or research a GitHub project
- User is building tool systems and needs to discover tools
- User needs to extract insights from GitHub projects

## Quick Start

### Basic Usage

```
User: https://github.com/anthropics/anthropic-sdk-python

memU automatically:
1. Recognizes GitHub URL
2. Triggers github-analyzer skill
3. Executes 7-phase workflow
4. Saves to Obsidian knowledge base
5. Updates knowledge graph
```

### Workflow Overview

```
Phase 1: URL Recognition & Validation
   ↓
Phase 2: Content Acquisition (Browser automation)
   ↓
Phase 3: Information Extraction (5 dimensions)
   ↓
Phase 4: Knowledge Graph Update
   ↓
Phase 5: Structured Output Generation
   ↓
Phase 6: Save Records (3 locations)
   ↓
Phase 7: Co-evolution Update
```

## Core Workflow

### Phase 1: URL Recognition & Validation

**Tools**: Pattern matching, string parsing

**Steps**:
1. Detect if input contains GitHub URL
2. Extract owner and repo name
3. Validate URL format
4. Construct complete GitHub URL

**Output**: Standardized GitHub URL

### Phase 2: Content Acquisition

**Tools**: `mcp_playwright_browser_navigate`, `mcp_playwright_browser_snapshot`

**Steps**:
1. Navigate to GitHub page
2. Wait for page load completion
3. Get page snapshot
4. Extract key information:
   - README content
   - Stars/Forks/Contributors count
   - Tech stack (Languages)
   - License type
   - Release information
   - Topics/Tags

**Output**: Page content and metadata

### Phase 3: Information Extraction

**Tools**: Content analysis, pattern recognition

**Extraction Dimensions**:

1. **Project Basic Information**
   - Project name
   - Project description
   - Creator/Organization
   - Project status (active/archived)

2. **Core Features**
   - Extract feature list from README
   - Identify key functionalities
   - Understand project goals

3. **Technical Architecture**
   - Main programming languages
   - Tech stack
   - Frameworks and libraries
   - Deployment methods

4. **Project Data**
   - Stars count
   - Forks count
   - Contributors count
   - Releases count
   - Last update time

5. **Core Insights**
   - Project innovations
   - Problems solved
   - Target users
   - Unique value proposition

**Output**: Structured project information

### Phase 4: Knowledge Graph Update

**Tools**: `mcp_memory_create_entities`, `mcp_memory_create_relations`, `mcp_memory_add_observations`

**Steps**:
1. Create Entity (tool)
2. Create Relations (with known tools, insights, memU)
3. Link Existing Knowledge

**Output**: Updated knowledge graph

### Phase 5: Structured Output Generation

**Output Template**:

```markdown
# 🎯 [Project Name] - [One-line Description]

## 📊 Project Overview
- **Definition**: [Project definition]
- **Core Philosophy**: [Core concept]
- **GitHub**: [URL]
- **Stars**: [count]
- **Forks**: [count]
- **License**: [type]

## 🔑 Key Features
1. [Feature 1]
2. [Feature 2]
3. [Feature 3]

## 💡 Core Insights
- [Insight 1]
- [Insight 2]
- [Insight 3]

## 🔗 Connections with Existing Tools
| Dimension | [Project] | [Related Tool] |
|-----------|-----------|----------------|
| **Positioning** | ... | ... |
| **Technology** | ... | ... |
| **Philosophy** | ... | ... |

## 📊 Inspiration for memU
1. [Inspiration 1]
2. [Inspiration 2]
3. [Inspiration 3]

## 🔗 Co-evolution
- **Tool System Category**: [Thinking/Building/Execution/Integration Tool]
- **Relationship with memU**: [Similar/Complementary/Competitive]
- **Adoptable Features**: [Feature list]

---
#github #tool #[category]
```

### Phase 6: Save Records

**Tools**: `str_replace_editor`

**Save Locations** (Priority Order):

1. **Obsidian Working Directory** (Primary) ⭐
   - Path: `E:\Seed-Obsidian\Seed-Origin\Allinone\A1-Github\githubs\[project-name].md`
   
2. **Private Directory** (Backup)
   - Path: `C:\Users\Lenovo\AppData\Roaming\memu-bot\agent-output\documents\[project-name].md`
   
3. **Collaborative Directory** (Co-evolution)
   - Path: `E:\Seed-memU\memU-context\2026-03-01\[project-name]-analysis.md`

### Phase 7: Co-evolution Update

**Tools**: File system + Knowledge Graph

**Steps**:
1. Update "Three Systems from Scratch" Progress
2. Extract Tool System Insights
3. Update Tool Matrix
4. Identify Collaboration Opportunities

**Output**: Updated "Three Systems from Scratch" documentation

## Tool Classification

### Four Tool Categories

1. **Thinking Tools** (🤔) - Planning, analysis, research
2. **Building Tools** (🔨) - Creation, development, coding
3. **Execution Tools** (⚡) - Running, task execution, automation
4. **Integration Tools** (🔗) - Connection, coordination, orchestration

## Best Practices

### Information Extraction
- ✅ Prioritize README - Most comprehensive project description
- ✅ Check tech stack - Understand project dependencies
- ✅ Verify project status - active/archived
- ✅ Observe community activity - stars/forks/commits

### Insight Generation
- ✅ Identify innovations - What's unique about this project?
- ✅ Solve problems - What problem does it solve?
- ✅ Target users - Who will use this project?
- ✅ Unique value - Why is it worth attention?

### Connection Building
- ✅ Link known insights - Connect with previous discoveries
- ✅ Compare similar tools - Find similarities and differences
- ✅ Inspire memU - What can memU learn?
- ✅ Update knowledge graph - Persist knowledge

## Example Usage

### Input
```
https://github.com/AutoMaker-Org/automaker
```

### Output
```markdown
# 🎯 Automaker - Autonomous AI Development Studio

## 📊 Project Overview
- **Definition**: Autonomous AI development studio
- **Core Philosophy**: Stop typing code. Start directing AI agents.
- **GitHub**: https://github.com/AutoMaker-Org/automaker
- **Stars**: 3k
- **Forks**: 577

## 💡 Core Insights
- **Agentic Coding is the future**: From manual coding to directing AI agents
- **Fully aligned with memU**: Both are AI agent systems

## 🔗 Co-evolution
- **Tool System Category**: Building Tool (🔨)
- **Adoptable Features**: Kanban workflow, Git isolation, Plan approval

---
#github #ai #agentic-coding #tool
```

## Metadata

- **Skill Type**: Analysis Skill
- **Project**: "Three Systems from Scratch" - System 2: Tool System
- **Version**: v1.2
- **Status**: 🟢 Active
- **Created Using**: skill-creator (meta-skill)
- **Inspired By**: Claude Scientific Skills (K-Dense-AI)
