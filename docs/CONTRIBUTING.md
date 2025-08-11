# Contributing to 90-Day SRE Journey

## Commit Message Convention

This project follows the [Conventional Commits](https://www.conventionalcommits.org/) specification.

### Format
```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Types
- **feat**: New features
- **fix**: Bug fixes  
- **docs**: Documentation changes
- **style**: Code style changes (formatting, semicolons, etc)
- **refactor**: Code refactoring (no functional changes)
- **test**: Adding or updating tests
- **chore**: Maintenance tasks, dependency updates
- **ci**: CI/CD pipeline changes
- **build**: Build system changes
- **perf**: Performance improvements
- **revert**: Revert previous commits

### Examples
```bash
feat: add automated progress tracking system
fix(scripts): resolve progress calculation bug
docs: update README with setup instructions
ci: add commit message validation workflow
chore: update dependencies to latest versions
```

### Enforcement
- **Local**: Git hook validates commit messages
- **CI/CD**: GitHub Actions validates on pull requests
- **Tools**: VS Code extensions provide autocomplete

### Setup
1. Install recommended VS Code extensions
2. Git hooks are automatically active
3. Follow the format for all commits

---

*This ensures consistent, readable commit history for the project.*
