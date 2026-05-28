import { Bot, InlineKeyboard } from "grammy";

const TOKEN = process.env.TELEGRAM_BOT_TOKEN;
const PARTNER =
  "https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549";
const REMOTE =
  "https://raw.githubusercontent.com/multilogin-labs/multilogin-labs/main/docs/api/endpoints.json";

if (!TOKEN) {
  console.error("Set TELEGRAM_BOT_TOKEN");
  process.exit(1);
}

const bot = new Bot(TOKEN);
let endpoints = [];
let lastFetch = 0;

async function ensureIndex() {
  if (Date.now() - lastFetch < 60 * 60 * 1000 && endpoints.length) return;
  endpoints = await fetch(REMOTE).then((r) => r.json());
  lastFetch = Date.now();
}

bot.command("start", (ctx) => {
  ctx.reply(
    `Multilogin Labs bot · 90 API endpoints in your pocket.\n\nCommands:\n/search <terms> — find endpoints\n/cheatsheet — one-page API\n/plan — how to pick a plan\n/trial — partner pricing & promo codes`,
    {
      reply_markup: new InlineKeyboard()
        .url("Trial $2", PARTNER)
        .row()
        .url("Swagger UI", "https://multilogin-labs.github.io/multilogin-labs/api/swagger.html")
        .url("Hub", "https://github.com/multilogin-labs/multilogin-labs"),
    },
  );
});

bot.command("trial", (ctx) =>
  ctx.reply(`Partner pricing: ${PARTNER}\nCodes: SAAS50 · MIN50`),
);

bot.command("cheatsheet", (ctx) =>
  ctx.reply(
    "https://github.com/multilogin-labs/multilogin-labs/blob/main/docs/api/CHEATSHEET.md",
  ),
);

bot.command("plan", (ctx) =>
  ctx.reply(
    "Plan calculator: https://multilogin-labs.github.io/multilogin-labs/calculator.html",
  ),
);

bot.command("search", async (ctx) => {
  await ensureIndex();
  const q = ctx.match.toLowerCase().trim();
  if (!q) return ctx.reply("Usage: /search profile start");
  const hits = endpoints
    .filter(
      (e) =>
        e.name.toLowerCase().includes(q) ||
        e.url.toLowerCase().includes(q) ||
        e.category.toLowerCase().includes(q),
    )
    .slice(0, 8);
  if (!hits.length) return ctx.reply("No matches.");
  ctx.reply(
    hits
      .map(
        (e) =>
          `*${e.method}* \`${e.name}\`\n${e.url}\nDocs: https://github.com/multilogin-labs/multilogin-labs/blob/main/docs/api/endpoints/${e.slug}.md`,
      )
      .join("\n\n"),
    { parse_mode: "Markdown", disable_web_page_preview: true },
  );
});

bot.start();
console.log("mlx-telegram-bot running");
