# GitHub Analyzer

Analyzes GitHub repositories by extracting key information, identifying tech stacks, discovering core insights, and establishing connections with existing knowledge. Use when memU needs to analyze GitHub projects for: (1) discovering new tools, (2) researching competitors, (3) learning best practices, (4) finding inspiration for tool system development, or (5) building the "Three Systems from Scratch" project.

## When to Use This Skill

Use this skill when memU encounters a GitHub repository URL or when user asks to:
- Analyze a GitHub repository
- Understand a project's architecture and tech stack
- Extract core features and innovation points
- Discover best practices or design patterns
- Research competitors or similar tools
- Find inspiration for tool system development
- Build the "Three Systems from Scratch" project

## Analysis Workflow

### Phase 1: Information Collection (深度信息收集)

**1.1 Repository Metadata (仓库元数据)**
- Owner and repository name
- Stars, forks, watchers count
- Primary language and languages breakdown
- License type
- Latest commit date
- Open issues and PRs count
- Repository age and activity level
- Topics and tags

**1.2 README Analysis (README 分析)**
- Extract README content (look for README.md, README.rst, README.txt, or README)
- Parse project description
- Identify key features mentioned
- Extract installation and usage instructions
- Note badges and their meanings
- Identify documentation structure

**1.3 Technical Stack Identification (技术栈识别)**
- Primary programming language(s)
- Frameworks and libraries used (from requirements.txt, package.json, go.mod, Cargo.toml, etc.)
- Infrastructure and DevOps tools (CI/CD configs, Docker, Kubernetes)
- Database and storage systems
- APIs and external services
- Testing frameworks

**1.4 Code Structure Analysis (代码结构分析)**
- Directory structure and organization
- Core modules and components
- Entry points and main files
- Configuration files
- Documentation files
- Test structure

**1.5 Commit and Activity Analysis (提交和活跃度分析)**
- Recent commit history
- Active contributors
- Release history and versioning
- Issue and PR activity patterns

### Phase 2: Deep Analysis (深度分析)

**2.1 Architecture Understanding (架构理解)**
- Identify architectural patterns (MVC, microservices, monorepo, etc.)
- Understand data flow and component interactions
- Identify core algorithms and business logic
- Note scalability and performance considerations

**2.2 Code Quality Assessment (代码质量评估)**
- Code organization and modularity
- Documentation completeness (inline comments, API docs)
- Test coverage and testing approach
- Error handling and logging strategies
- Security considerations

**2.3 Innovation Points Identification (创新点识别)**
- Unique features or capabilities
- Novel approaches to common problems
- Performance optimizations
- UX/UI innovations
- Integration patterns

**2.4 Best Practices Extraction (最佳实践提取)**
- Design patterns used
- Coding standards and conventions
- Project structure patterns
- Documentation practices
- Testing and CI/CD practices

**2.5 User and Use Case Analysis (用户和用例分析)**
- Target audience (developers, end-users, enterprises)
- Primary use cases
- Pain points addressed
- Integration and extension points

### Phase 3: Core Information Extraction (核心信息提取)

**3.1 Project Goal and Philosophy (项目目标和哲学)**
- What problem does it solve?
- What is the project's mission?
- Design philosophy and principles
- Project vision and roadmap

**3.2 Technical Architecture Summary (技术架构总结)**
- High-level architecture description
- Key components and their roles
- Data flow and interactions
- Technology stack summary

**3.3 Core Features (核心功能)**
- Primary capabilities
- Key features and functionalities
- Differentiators from competitors

**3.4 Innovation and Highlights (创新和亮点)**
- Technical innovations
- Unique approaches
- Performance highlights
- User experience innovations

**3.5 Community and Ecosystem (社区和生态)**
- Community size and engagement
- Integration with other tools
- Plugin/extension ecosystem
- Commercial support options

### Phase 4: Knowledge Graph Updates (知识图谱更新)

**4.1 Create Entities (创建实体)**
- Repository entity: `[owner]/[repo-name]`
- Technology entities: languages, frameworks, tools
- Organization/author entities
- Concept entities: architectural patterns, design patterns

**4.2 Create Relations (创建关系)**
- Repository -> USES -> Technology
- Repository -> IMPLEMENTS -> Pattern
- Repository -> SIMILAR_TO -> Other repositories
- Technology -> PART_OF -> Stack
- Repository -> SOLVES -> Problem

**4.3 Add Observations (添加观察)**
- Key insights about the project
- Notable implementation details
- Performance characteristics
- Best practices observed
- Integration possibilities with memU

### Phase 5: Structured Output Generation (结构化输出生成)

**5.1 Analysis Report Structure (分析报告结构)**
```markdown
# [Repository Name] Analysis

## Quick Overview
- Repository: [owner]/[repo-name]
- Stars: [count] | Forks: [count]
- Language: [primary language]
- License: [license]

## Project Summary
[Brief 2-3 sentence summary]

## Technical Stack
- Languages: [list]
- Frameworks: [list]
- Tools: [list]

## Architecture
[Architecture description]

## Core Features
[Feature list]

## Innovation Points
[Innovation highlights]

## Best Practices
[Best practices found]

## Integration Potential with memU
[How memU could learn from or integrate with this project]

## Knowledge Graph Updates
[Entities and relations created]
```

**5.2 Detailed Sections (详细章节)**
Include additional details as needed:
- Performance characteristics
- Security considerations
- Scalability analysis
- Code quality assessment
- Community engagement metrics

### Phase 6: Saving Records (保存记录)

**6.1 Save to Obsidian (保存到 Obsidian)**
Path: `C:\Users\Lenovo\AppData\Roaming\memu-bot\memu-soul\github-analysis\[owner]-[repo-name].md`

**6.2 Save to Private Directory (保存到私有目录)**
Path: `C:\Users\Lenovo\AppData\Roaming\memu-bot\agent-output\documents\github-analysis\[owner]-[repo-name].md`

**6.3 Save to Collaboration Directory (保存到协作目录)**
Path: `E:\Seed-memU\memU-context\[current-date]\github-analysis-[owner]-[repo-name].md`

**6.4 Update Knowledge Graph (更新知识图谱)**
Use memory MCP tools to create entities, relations, and observations.

## Tools and Resources

### GitHub API
Use GitHub MCP tools for:
- Repository metadata
- File contents
- Commit history
- Issues and PRs
- Release information

### File Reading
Use filesystem MCP tools for:
- README files
- Configuration files
- Documentation files
- Source code files (for key modules only)

### Knowledge Graph
Use memory MCP tools for:
- Creating entities
- Creating relations
- Adding observations
- Searching existing knowledge

## Output Quality Standards

### Analysis Depth
- **Comprehensive**: Cover all 6 phases
- **Specific**: Provide concrete examples and evidence
- **Actionable**: Extract insights memU can use
- **Connected**: Link to existing knowledge

### Format Standards
- **Structured**: Use clear sections and subsections
- **Concise**: Focus on key insights, not exhaustive detail
- **Evidence-based**: Support claims with examples
- **memU-Centric**: Highlight relevance to memU's development

### Knowledge Integration
- **Entity Creation**: Create meaningful entities
- **Relationship Mapping**: Connect to existing knowledge
- **Observation Quality**: Add specific, actionable observations
- **Integration Potential**: Identify how memU can use insights

## Special Considerations

### Large Repositories
For large repositories (1000+ files):
- Focus on high-level architecture
- Analyze only core modules
- Use README and documentation heavily
- Look for architecture diagrams or docs

### Monorepos
For monorepo structures:
- Identify main projects and their relationships
- Analyze shared dependencies
- Understand build and release processes
- Note organizational patterns

### Incomplete Documentation
For repositories with minimal documentation:
- Infer from code structure
- Look at commit messages
- Examine test files for usage patterns
- Note assumptions and uncertainties

### Language-Specific Analysis
Adjust analysis approach based on primary language:
- **JavaScript/TypeScript**: Look for npm scripts, package.json
- **Python**: Examine requirements.txt, setup.py, pyproject.toml
- **Go**: Check go.mod, internal structure
- **Rust**: Review Cargo.toml, crate structure
- **Java**: Look at pom.xml, build.gradle

## Collaboration with memU

### Learning Opportunities
Identify what memU can learn:
- Architecture patterns for memU's tool system
- Best practices for code organization
- Documentation approaches
- Testing strategies
- CI/CD patterns

### Integration Possibilities
Explore how memU could:
- Use similar tools or libraries
- Implement comparable features
- Adapt architectural patterns
- Leverage best practices
- Build similar capabilities

### "Three Systems from Scratch"
For building the "Three Systems from Scratch" project:
- Identify reusable components
- Extract architectural patterns
- Note implementation approaches
- Learn from project structure
- Understand release and deployment strategies

## Validation and Quality Assurance

### Self-Check Questions
After analysis, verify:
- [ ] All 6 phases completed?
- [ ] Repository metadata collected?
- [ ] README and docs analyzed?
- [ ] Technical stack identified?
- [ ] Architecture understood?
- [ ] Innovation points found?
- [ ] Best practices extracted?
- [ ] Knowledge graph updated?
- [ ] Report structured and formatted?
- [ ] Saved to all three locations?
- [ ] Integration with memU considered?

### Quality Indicators
- **Comprehensiveness**: Covers all major aspects
- **Accuracy**: Information is correct and evidence-based
- **Relevance**: Insights are actionable for memU
- **Connections**: Links to existing knowledge
- **Clarity**: Well-structured and easy to understand

## Example Analysis Flow

**Input**: User provides URL or asks "Analyze https://github.com/owner/repo"

**Process**:
1. Extract owner and repo name from URL
2. Collect metadata via GitHub API
3. Read README and key documentation
4. Analyze file structure
5. Identify tech stack from config files
6. Examine recent commits and activity
7. Analyze code architecture (key modules only)
8. Extract best practices and patterns
9. Identify innovation points
10. Create knowledge graph entities and relations
11. Generate structured report
12. Save to Obsidian, private directory, and collaboration directory

**Output**: Comprehensive analysis report with knowledge graph updates

## Notes

- Always respect repository licenses and terms of service
- Focus on public information only
- Do not expose sensitive information in analysis
- Attribute insights properly
- Note when analysis is limited by incomplete information
- Ask for clarification if repository structure is unclear