#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const os = require('os');

const args = process.argv.slice(2);
const isGlobal = args.includes('--global') || args.includes('-g');

const sourceSkillsDir = path.join(__dirname, '../skills');

let targetSkillsDir;
if (isGlobal) {
  targetSkillsDir = path.join(os.homedir(), '.gemini', 'antigravity', 'skills');
} else {
  targetSkillsDir = path.join(process.cwd(), 'skills');
}

const targetOpencodeAgentsDir = path.join(process.cwd(), '.opencode', 'agents');

if (path.resolve(sourceSkillsDir) === path.resolve(targetSkillsDir)) {
  console.log('\n💡 Info: You are running installation inside the repository itself.');
  console.log('No copying needed as files are already in place.');
  
  // Generate OpenCode agents even when running inside repo
  try {
    generateOpencodeAgents();
  } catch (e) {
    console.error('⚠️  Failed to generate OpenCode agents:', e.message);
  }
  
  process.exit(0);
}

console.log('🔄 Installing Trading AI Agent Skills...');
console.log(`📂 Source: ${sourceSkillsDir}`);
console.log(`📂 Target: ${targetSkillsDir}`);

try {
  if (!fs.existsSync(targetSkillsDir)) {
    fs.mkdirSync(targetSkillsDir, { recursive: true });
  }

  if (fs.existsSync(sourceSkillsDir)) {
    fs.cpSync(sourceSkillsDir, targetSkillsDir, { recursive: true });
    console.log('\n✅ Success! All Trading AI Agent Skills installed.');
    if (isGlobal) {
      console.log('💡 Global Install: Accessible across all agent workspaces.');
    } else {
      console.log('💡 Local Install: Active for current workspace.');
    }
    
    // Generate OpenCode v2 custom agents
    try {
      generateOpencodeAgents();
    } catch (e) {
      console.error('⚠️  Failed to generate OpenCode agents:', e.message);
    }
  } else {
    console.log('\n⚠️ Notice: Source skills directory is currently being populated.');
  }
} catch (error) {
  console.error('\n❌ Installation failed:', error.message);
  process.exit(1);
}

function generateOpencodeAgents() {
  // Only generate for local install (not global) or always for cwd
  const agentsDir = targetOpencodeAgentsDir;
  
  if (!fs.existsSync(agentsDir)) {
    fs.mkdirSync(agentsDir, { recursive: true });
  }
  
  const skills = fs.readdirSync(sourceSkillsDir).filter(item => {
    return fs.statSync(path.join(sourceSkillsDir, item)).isDirectory();
  });
  
  let generated = 0;
  for (const skill of skills) {
    const skillMdPath = path.join(sourceSkillsDir, skill, 'SKILL.md');
    if (fs.existsSync(skillMdPath)) {
      try {
        const content = fs.readFileSync(skillMdPath, 'utf8');
        const agentContent = convertSkillToAgent(skill, content);
        const agentPath = path.join(agentsDir, `${skill}.md`);
        fs.writeFileSync(agentPath, agentContent);
        generated++;
      } catch (e) {
        console.error(`  ⚠️  Failed to convert ${skill}:`, e.message);
      }
    }
  }
  
  if (generated > 0) {
    console.log(`\n🤖 OpenCode v2: Generated ${generated} custom agents in .opencode/agents/`);
    console.log('💡 You can now use @<skill-name> in OpenCode v2');
  }
}

function convertSkillToAgent(skillName, skillContent) {
  // Extract description from frontmatter
  const descMatch = skillContent.match(/description:\s*(.+?)(?:\n|\r)/);
  const description = descMatch ? descMatch[1].trim().replace(/^["']|["']$/g, '') : `Trading AI Agent Skill: ${skillName}`;
  
  // Remove frontmatter if exists
  let body = skillContent;
  if (body.startsWith('---')) {
    const end = body.indexOf('---', 3);
    if (end !== -1) {
      body = body.substring(end + 3).trim();
    }
  }
  
  // Build OpenCode agent format
  return `---
description: ${escapeYaml(description)}
---

# ${skillName}

You are the **${skillName}** agent from the Trading AI Agent Skills Suite.

${body}
`;
}

function escapeYaml(str) {
  return str.replace(/:/g, '\\:').replace(/\n/g, ' ');
}
