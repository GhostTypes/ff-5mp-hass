---
name: project-bootstrap
description: Bootstrap Claude Code setup for greenfield (new) or brownfield (existing) projects. Automatically detects project type, copies relevant skills from your skill library, and creates engineer agents with best practices skills. Use when starting work on a new project or wanting to upgrade an existing project's Claude Code setup with skills and agents.
---

# Project Bootstrap

Automated setup skill for bootstrapping Claude Code in any project. Detects whether you're in a greenfield or brownfield project, identifies the tech stack, copies relevant skills from your skill library, and creates specialized engineer agents.

## Configuration

This skill uses hardcoded paths for personal use:
- **Skill Library**: `C:\Users\coper\Documents\GitHub\agent-skills\skills`
- **Unpack Destination**: `.claude/skills/` in the current project

## Workflow

### Phase 1: Project Detection

1. Check if `.claude/` exists (indicates brownfield with some setup)
2. Check for common project files: `package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml`, etc.
3. If no project files found → **greenfield project**
4. If project files found → **brownfield project**

### Phase 2: Information Gathering

**For Greenfield Projects:**
1. Search for README.md, specs, or planning documents
2. If found, extract project intent from those files
3. If not found or unclear, use AskUserQuestion to interview user about:
   - What are you building?
   - Primary language/framework?
   - Backend, frontend, or full-stack?
   - Any specific libraries or tools needed?

**For Brownfield Projects:**
1. Spawn Explore sub-agent to analyze codebase (stack, structure, patterns)
2. Spawn Explore sub-agent to check existing `.claude/` setup (agents, skills, commands)
3. Wait for both reports before proceeding

### Phase 3: Skill Selection

1. Read `references/skill-categories.md` for available skills mapping
2. Match project stack to relevant skills using keyword matching
3. Always include `best-practices` skill if available
4. Present selections to user via AskUserQuestion for confirmation
5. User can add/remove skills from the selection

### Phase 4: Skill Deployment

1. Create `.claude/skills/` directory if needed
2. Copy selected `.skill` files from skill library
3. Unpack each skill (extract zip to folder, delete .skill file)
4. Verify unpacked structure (SKILL.md exists)

### Phase 5: Agent Creation

Automatically create agents without further confirmation (per user preference).

**CRITICAL: Agent Prompt Quality**

Each agent must have a rich, comprehensive system prompt following the agent creation architect framework. DO NOT create basic or minimal prompts. Each agent prompt should include:

1. **Expert Persona**: A compelling identity with deep domain knowledge
2. **Core Intent**: Clear purpose and success criteria
3. **Comprehensive Instructions**: Methodologies, best practices, edge case handling
4. **Decision Frameworks**: How to approach choices and trade-offs
5. **Quality Control**: Self-verification steps and output expectations
6. **Workflow Patterns**: Step-by-step process for task execution

**Agent Types to Create:**

**Engineer Agents (1-3 based on stack):**
- Create stack-specific engineers (e.g., `typescript-engineer`, `python-engineer`)
- Include best-practices skill reference
- Include relevant library skills
- Use rich prompts from `references/agent-templates.md`

**Code Quality Agents:**
- Create `code-quality` agent for the primary language
- Include linting/formatting skills (biome, ruff, etc.)
- Include best-practices skill
- Define clear quality checklist and verification steps

**Library-Specific Agents (if applicable):**
- Create agents for major frameworks (react, angular, express, etc.)
- Only if corresponding skill was copied
- Keep minimal (don't create agent for every skill)
- Include framework-specific patterns and best practices

See `references/agent-templates.md` for comprehensive agent creation patterns with rich prompts.

### Phase 6: Validation & Summary

1. Run `scripts/validate_setup.py` to check all skills and agents
2. Report any issues found
3. Print summary of what was set up:
   - Skills copied and unpacked
   - Agents created
   - Any issues or warnings

## Decision Framework

### When to Ask vs. Automate

| Situation | Action |
|-----------|--------|
| Greenfield with no specs | Ask about project intent |
| Skill selection | Always confirm with user |
| Agent creation | Fully automatic |
| Unclear stack | Ask for clarification |
| Multiple valid approaches | Ask for preference |

### Stack Detection Keywords

| Keyword | Skills to Suggest |
|---------|------------------|
| `typescript`, `javascript` | typescript-best-practices, biome, vite |
| `react` | react-19, react-ecosystem skills |
| `python` | python-best-practices, ruff-dev, pytest |
| `go` | go-best-practices |
| `rust` | rust-dev |
| `angular` | angular skill |
| `fastapi` | fastapi skill |
| `express` | express skill |

## Scripts

### scripts/validate_setup.py

Validates all unpacked skills and agents in `.claude/`:
- Checks SKILL.md exists in each skill folder
- Validates agent YAML frontmatter
- Reports missing or malformed files

### scripts/unpack_skill.py

Unpacks a .skill file to a directory:
```bash
python scripts/unpack_skill.py <source.skill> <destination-dir>
```

## References

- **references/skill-categories.md** - Complete mapping of skill library categories and stacks
- **references/agent-templates.md** - Templates for creating engineer and quality agents
