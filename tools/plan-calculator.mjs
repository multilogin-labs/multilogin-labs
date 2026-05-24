#!/usr/bin/env node
/**
 * Recommend a Multilogin plan from profile count, team size, and mobile need.
 * Usage: npm run plan
 *        npm run plan -- --profiles 80 --team 5 --mobile
 */
import readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";
import { AFFILIATE_URL, PROMO_CODES } from "../lib/constants.mjs";

const PLANS = [
  { id: "trial", name: "Trial ($2 / 3 days)", profiles: 5, team: 1, mobile: true, annual: 2 },
  { id: "pro10", name: "Pro 10", profiles: 10, team: 2, mobile: true, annual: 7.08 },
  { id: "pro50", name: "Pro 50", profiles: 50, team: 999, mobile: true, annual: 19.17 },
  { id: "pro100", name: "Pro 100", profiles: 100, team: 999, mobile: true, annual: 26.67 },
  { id: "business", name: "Business 300+", profiles: 300, team: 999, mobile: true, annual: 57.08 },
];

function recommend({ profiles, team, mobile }) {
  if (profiles <= 5 && team <= 1) return PLANS[0];
  if (profiles <= 10 && team <= 2) return PLANS[1];
  if (profiles <= 50) return PLANS[2];
  if (profiles <= 100) return PLANS[3];
  return PLANS[4];
}

function parseArgs() {
  const args = process.argv.slice(2);
  const get = (flag) => {
    const i = args.indexOf(flag);
    return i >= 0 ? args[i + 1] : undefined;
  };
  const profiles = get("--profiles");
  const team = get("--team");
  if (profiles) {
    return {
      profiles: Number(profiles),
      team: Number(team ?? 1),
      mobile: args.includes("--mobile"),
    };
  }
  return null;
}

async function prompt() {
  const rl = readline.createInterface({ input, output });
  try {
    const profiles = Number(await rl.question("How many browser profiles? "));
    const team = Number(await rl.question("Team members (including you)? "));
    const mobileAns = await rl.question("Need cloud phone / mobile minutes? (y/n) ");
    return { profiles, team, mobile: /^y/i.test(mobileAns) };
  } finally {
    rl.close();
  }
}

async function main() {
  console.log("\n🐉 Multilogin Labs — Plan Calculator\n");

  const input = parseArgs() ?? (await prompt());
  const plan = recommend(input);

  console.log("\n--- Recommendation ---");
  console.log(`Plan:     ${plan.name}`);
  console.log(`From:     ~$${plan.annual}/mo (annual billing)`);
  console.log(`Profiles: up to ${plan.profiles}${plan.id === "business" ? "+" : ""}`);
  if (input.mobile && plan.id !== "trial") {
    console.log("Mobile:   minutes included on Pro 50+ (see pricing page)");
  }
  console.log(`\nCheckout: ${AFFILIATE_URL}`);
  console.log(`Promo:    ${PROMO_CODES.join(" or ")}\n`);
}

main().catch(console.error);
