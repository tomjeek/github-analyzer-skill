#!/usr/bin/env python3
"""
GitHub Analyzer Skill Validation Script

Validates that the skill structure is correct and all required files are present.
"""

import os
import sys
import yaml
from pathlib import Path

def validate_skill(skill_path: str) -> tuple[bool, list[str], list[str]]:
    """
    Validate a skill directory structure.
    
    Args:
        skill_path: Path to the skill directory
        
    Returns:
        Tuple of (is_valid, errors, warnings)
    """
    errors = []
    warnings = []
    skill_dir = Path(skill_path)
    
    # Check if skill directory exists
    if not skill_dir.exists():
        errors.append(f"Skill directory does not exist: {skill_path}")
        return False, errors, warnings
    
    # Check SKILL.md
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        errors.append("SKILL.md not found")
    else:
        # Validate SKILL.md format
        try:
            content = skill_md.read_text()
            
            # Check for YAML frontmatter
            if not content.startswith("---"):
                errors.append("SKILL.md must start with YAML frontmatter (---)")
            else:
                # Parse YAML
                try:
                    frontmatter_end = content.find("---", 3)
                    if frontmatter_end == -1:
                        errors.append("SKILL.md YAML frontmatter not closed")
                    else:
                        yaml_content = content[3:frontmatter_end]
                        frontmatter = yaml.safe_load(yaml_content)
                        
                        # Check required fields
                        if "name" not in frontmatter:
                            errors.append("SKILL.md missing required field: name")
                        if "description" not in frontmatter:
                            errors.append("SKILL.md missing required field: description")
                            
                        # Validate name format
                        if "name" in frontmatter:
                            name = frontmatter["name"]
                            if not isinstance(name, str):
                                errors.append("SKILL.md 'name' must be a string")
                            elif not name.replace("-", "").replace("_", "").isalnum():
                                errors.append(f"SKILL.md 'name' contains invalid characters: {name}")
                                
                except yaml.YAMLError as e:
                    errors.append(f"SKILL.md YAML parsing error: {e}")
                    
        except Exception as e:
            errors.append(f"SKILL.md reading error: {e}")
    
    # Check agents/openai.yaml
    openai_yaml = skill_dir / "agents" / "openai.yaml"
    if not openai_yaml.exists():
        warnings.append("agents/openai.yaml not found (optional but recommended)")
    else:
        try:
            with open(openai_yaml, "r", encoding="utf-8") as f:
                openai_config = yaml.safe_load(f)
                
            # Check recommended fields
            if "display_name" not in openai_config:
                warnings.append("agents/openai.yaml missing recommended field: display_name")
            if "short_description" not in openai_config:
                warnings.append("agents/openai.yaml missing recommended field: short_description")
            if "default_prompt" not in openai_config:
                warnings.append("agents/openai.yaml missing recommended field: default_prompt")
                
        except yaml.YAMLError as e:
            warnings.append(f"agents/openai.yaml YAML parsing error: {e}")
        except Exception as e:
            warnings.append(f"agents/openai.yaml reading error: {e}")
    
    # Check for common issues
    # 1. No README.md in skill root
    if (skill_dir / "README.md").exists():
        warnings.append("README.md found in skill root (skills should not have README.md)")
    
    # 2. No extra documentation files
    extra_docs = [
        "INSTALLATION_GUIDE.md", 
        "QUICK_REFERENCE.md", 
        "CHANGELOG.md",
        "CONTRIBUTING.md"
    ]
    for doc in extra_docs:
        if (skill_dir / doc).exists():
            warnings.append(f"{doc} found in skill root (unnecessary for skills)")
    
    return len(errors) == 0, errors, warnings

def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python validate.py <skill-path>")
        sys.exit(1)
    
    skill_path = sys.argv[1]
    is_valid, errors, warnings = validate_skill(skill_path)
    
    # Print results
    if is_valid:
        print("✅ Skill validation passed!")
    else:
        print("❌ Skill validation failed!")
    
    if errors:
        print("\nErrors:")
        for error in errors:
            print(f"  ❌ {error}")
    
    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(f"  ⚠️  {warning}")
    
    if not errors and warnings:
        print("\n✅ Skill is valid (with warnings)")
    elif not errors:
        print("\n✅ Skill is valid")
    else:
        print(f"\n❌ Found {len(errors)} error(s)")
        sys.exit(1)

if __name__ == "__main__":
    main()