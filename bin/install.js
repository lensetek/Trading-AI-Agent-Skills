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

if (path.resolve(sourceSkillsDir) === path.resolve(targetSkillsDir)) {
  console.log('\n💡 Info: You are running installation inside the repository itself.');
  console.log('No copying needed as files are already in place.');
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
  } else {
    console.log('\n⚠️ Notice: Source skills directory is currently being populated.');
  }
} catch (error) {
  console.error('\n❌ Installation failed:', error.message);
  process.exit(1);
}
