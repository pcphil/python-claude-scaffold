#!/usr/bin/env node
/**
 * validate-env.mjs
 *
 * Reads .env.example from the project root, identifies required variables
 * (lines of the form VAR= with no value), and checks that each one is set
 * in process.env.
 *
 * Exits 0 if all required variables are present.
 * Exits 1 if any required variables are missing, printing each missing name.
 */

import { readFileSync } from "node:fs";
import { resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const projectRoot = resolve(__dirname, "..", "..", "..");
const envExamplePath = resolve(projectRoot, ".env.example");

/** @param {string} filePath */
function parseRequiredVars(filePath) {
  let content;
  try {
    content = readFileSync(filePath, "utf8");
  } catch (err) {
    console.error(`validate-env: cannot read ${filePath}: ${err.message}`);
    process.exit(1);
  }

  const required = [];
  for (const line of content.split("\n")) {
    const trimmed = line.trim();
    // Skip comments and blank lines
    if (!trimmed || trimmed.startsWith("#")) continue;

    const eqIndex = trimmed.indexOf("=");
    if (eqIndex === -1) continue;

    const name = trimmed.slice(0, eqIndex).trim();
    const value = trimmed.slice(eqIndex + 1).trim();

    // A variable is required when the value is empty
    if (name && value === "") {
      required.push(name);
    }
  }
  return required;
}

const required = parseRequiredVars(envExamplePath);
const missing = required.filter((name) => !process.env[name]);

if (missing.length === 0) {
  console.log(`validate-env: OK — all ${required.length} required variable(s) are set.`);
  process.exit(0);
} else {
  console.error("validate-env: MISSING required environment variables:");
  for (const name of missing) {
    console.error(`  - ${name}`);
  }
  process.exit(1);
}
