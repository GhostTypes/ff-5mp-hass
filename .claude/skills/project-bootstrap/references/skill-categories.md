# Skill Categories and Stack Mapping

This file maps the skill library structure to tech stacks for automatic skill selection.

## Skill Library Location

`C:\Users\coper\Documents\GitHub\agent-skills\skills`

## Categories and Skills

### Frontend Frameworks

| Skill | Path | Keywords |
|-------|------|----------|
| angular | `angular/angular.skill` | angular, ng, standalone components, signals |
| astro-build | `astro/astro-build.skill` | astro, content-driven, ssr |
| react-19 | `react-ecosystem/react-19.skill` | react, react-dom, jsx, hooks |
| react-native | `react-ecosystem/react-native.skill` | react-native, mobile, expo |
| svelte5 | `svelte/svelte5.skill` | svelte, runes, sveltekit |

### UI Components & Styling

| Skill | Path | Keywords |
|-------|------|----------|
| lucide-react | `design/lucide-react.skill` | lucide, icons, react icons |
| nativewind | `styling/nativewind.skill` | nativewind, tailwind native |
| radix-ui | `design/radix-ui.skill` | radix, primitives, themes |
| shadcn | `design/shadcn.skill` | shadcn, ui components |
| tailwind-css | `styling/tailwind-css.skill` | tailwind, utility-first css |

### Animation & Graphics

| Skill | Path | Keywords |
|-------|------|----------|
| auto-animate | `animation-graphics/auto-animate-skill.skill` | auto-animate, transitions |
| gsap | `animation-graphics/gsap.skill` | gsap, greensock, animation |
| lenis | `animation-graphics/lenis-skill.skill` | lenis, smooth scroll |
| motion | `animation-graphics/motion.skill` | framer-motion, motion |
| pixijs-v8 | `animation-graphics/pixijs-v8.skill` | pixi, webgl, 2d graphics |
| react-three-fiber | `animation-graphics/react-three-fiber.skill` | r3f, three.js react, 3d |
| threejs | `animation-graphics/threejs.skill` | three.js, 3d, webgl |

### Desktop & Mobile Development

| Skill | Path | Keywords |
|-------|------|----------|
| electron | `electron/electron.skill` | electron, desktop |
| electron-builder | `electron/electron-builder.skill` | electron-builder, packaging |
| electron-store | `electron/electron-store.skill` | electron-store, persistence |
| electron-vite | `electron/electron-vite.skill` | electron-vite, build |
| expo | `expo/expo.skill` | expo, react native |
| expo-android-widgets | `expo/expo-android-widgets.skill` | android widgets |
| tauri | `rust-dev/tauri.skill` | tauri, rust desktop |
| vscode-extension | `editor-integration/vscode-extension.skill` | vscode extension, vsc |

### Backend Frameworks

| Skill | Path | Keywords |
|-------|------|----------|
| express | `backend-frameworks/express.skill` | express, node.js server |
| fastapi | `backend-frameworks/fastapi.skill` | fastapi, python api |
| trpc | `backend-frameworks/trpc.skill` | trpc, typescript rpc |

### TypeScript/JavaScript Tooling

| Skill | Path | Keywords |
|-------|------|----------|
| biome | `typescript-dev/biome.skill` | biome, lint, format |
| eslint | `typescript-dev/eslint.skill` | eslint, linting |
| typescript-best-practices | `typescript-dev/typescript-best-practices.skill` | typescript patterns |
| vite | `build-tools/vite.skill` | vite, build tool |
| zod | `typescript-dev/zod.skill` | zod, validation |

### Python Development

| Skill | Path | Keywords |
|-------|------|----------|
| mypy | `python-dev/mypy.skill` | mypy, type checking |
| pydantic-dev | `python-dev/pydantic-dev.skill` | pydantic, validation |
| pytest | `python-dev/pytest.skill` | pytest, testing |
| python-best-practices | `python-dev/python-best-practices.skill` | python patterns |
| ruff-dev | `python-dev/ruff-dev.skill` | ruff, lint, format |

### Other Languages

| Skill | Path | Keywords |
|-------|------|----------|
| go-best-practices | `go-dev/go-best-practices.skill` | go, golang |
| java-best-practices | `java-dev/java-best-practices.skill` | java |
| junit | `java-dev/junit.skill` | junit, java testing |
| rust-dev | `rust-dev/rust-dev.skill` | rust, cargo |
| wails | `go-dev/wails.skill` | wails, go desktop |

### Testing

| Skill | Path | Keywords |
|-------|------|----------|
| jest | `testing/jest.skill` | jest, js testing |
| playwright-cli | `testing/playwright-cli.skill` | playwright, e2e |
| vitest | `testing/vitest.skill` | vitest, vite testing |

### AI & LLM Integration

| Skill | Path | Keywords |
|-------|------|----------|
| claude-code-headless | `ai-llm-integration/claude-code-headless.skill` | claude code, headless |
| claude-code-hooks | `ai-llm-integration/claude-code-hooks-skill.skill` | hooks, automation |
| gemini-cli | `ai-llm-integration/gemini-cli.skill` | gemini, google ai |
| gemini-collaborate | `ai-llm-integration/gemini-collaborate.skill` | gemini collaboration |
| gemini-genkit | `ai-llm-integration/gemini-genkit.skill` | genkit, firebase ai |
| mcp-setup | `mcp/mcp-setup.skill` | mcp, model context |
| mcp-test-harness | `mcp/mcp-test-harness.skill` | mcp testing |
| mcp-typescript-sdk | `mcp/mcp-typescript-sdk.skill` | mcp sdk, typescript |
| sub-agent-creator | `ai-llm-integration/sub-agent-creator.skill` | agent creation |
| vercel-ai-sdk | `ai-llm-integration/vercel-ai-sdk.skill` | vercel ai, sdk |

### Code Quality

| Skill | Path | Keywords |
|-------|------|----------|
| best-practices | `code-quality/best-practices.skill` | best practices, solid, dry |
| code-cleanup-final-pass | `code-quality/code-cleanup-final-pass.skill` | cleanup, review |
| modern-frontend-design | `design/modern-frontend-design.skill` | frontend design |

### DevOps

| Skill | Path | Keywords |
|-------|------|----------|
| github-actions | `devops/github-actions.skill` | github actions, ci/cd |
| github-cli | `terminal-cli/github-cli.skill` | gh, github cli |

## Stack Detection Rules

### TypeScript/JavaScript Projects

Detect when: `package.json` exists with TypeScript or JavaScript

```
Always suggest:
- best-practices
- typescript-best-practices (if TS)

If react detected:
- react-19

If testing needed:
- vitest or jest

If linting needed:
- biome or eslint

If building:
- vite
```

### Python Projects

Detect when: `pyproject.toml`, `setup.py`, or `requirements.txt` exists

```
Always suggest:
- best-practices
- python-best-practices
- ruff-dev

If testing:
- pytest

If api:
- fastapi

If validation:
- pydantic-dev
```

### Go Projects

Detect when: `go.mod` exists

```
Always suggest:
- best-practices
- go-best-practices
```

### Rust Projects

Detect when: `Cargo.toml` exists

```
Always suggest:
- best-practices
- rust-dev
```

### Java Projects

Detect when: `pom.xml` or `build.gradle` exists

```
Always suggest:
- best-practices
- java-best-practices
- junit
```
