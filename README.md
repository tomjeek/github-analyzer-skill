# GitHub Analyzer Skill

Professional GitHub repository analysis skill for memU AI assistant.

## Overview

This skill provides comprehensive GitHub repository analysis capabilities, including:
- Repository metadata extraction
- Technical stack identification
- Architecture analysis
- Best practices extraction
- Knowledge graph integration
- Structured report generation

## Installation

1. Copy this skill folder to your memU skills directory
2. Import the skill through memU's UI
3. The skill will be automatically triggered when:
   - You provide a GitHub repository URL
   - You ask to analyze a GitHub repository
   - You need to understand a project's architecture

## Usage Examples

- "Analyze https://github.com/owner/repo"
- "What's the tech stack of this repository?"
- "Extract best practices from this project"
- "How can memU learn from this repository?"

## Features

- **6-Phase Analysis Workflow**: Comprehensive repository examination
- **Knowledge Graph Integration**: Automatic entity and relation creation
- **Multi-Location Saving**: Saves to Obsidian, private directory, and collaboration directory
- **memU-Centric**: Identifies integration opportunities with memU

## Output

Analysis reports are saved to:
- Obsidian: `memu-soul/github-analysis/[owner]-[repo-name].md`
- Private: `agent-output/documents/github-analysis/[owner]-[repo-name].md`
- Collaboration: `memU-context/[date]/github-analysis-[owner]-[repo-name].md`

## Requirements

- GitHub MCP server configured
- Memory MCP server configured
- Filesystem access enabled

## License

MIT