import { Client, GatewayIntentBits, EmbedBuilder } from "discord.js";

const TOKEN = process.env.DISCORD_BOT_TOKEN;
const PARTNER =
  "https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549";
const REMOTE =
  "https://raw.githubusercontent.com/multilogin-labs/multilogin-labs/main/docs/api/endpoints.json";

if (!TOKEN) {
  console.error("Set DISCORD_BOT_TOKEN");
  process.exit(1);
}

const client = new Client({
  intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent],
});

let endpoints = [];
let lastFetch = 0;
async function ensureIndex() {
  if (Date.now() - lastFetch < 60 * 60 * 1000 && endpoints.length) return;
  endpoints = await fetch(REMOTE).then((r) => r.json());
  lastFetch = Date.now();
}

client.on("ready", () => console.log(`Logged in as ${client.user.tag}`));

client.on("messageCreate", async (msg) => {
  if (msg.author.bot) return;
  const content = msg.content.trim();

  if (content === "!mlx" || content === "!mlx help") {
    await msg.reply(
      `**Multilogin Labs bot**\n\`!mlx search <terms>\` · \`!mlx trial\` · \`!mlx cheatsheet\` · \`!mlx plan\``,
    );
    return;
  }

  if (content === "!mlx trial") {
    await msg.reply(`Partner: ${PARTNER}\nCodes: \`SAAS50\` · \`MIN50\``);
    return;
  }

  if (content === "!mlx cheatsheet") {
    await msg.reply(
      "https://github.com/multilogin-labs/multilogin-labs/blob/main/docs/api/CHEATSHEET.md",
    );
    return;
  }

  if (content === "!mlx plan") {
    await msg.reply(
      "https://multilogin-labs.github.io/multilogin-labs/calculator.html",
    );
    return;
  }

  if (content.startsWith("!mlx search ")) {
    await ensureIndex();
    const q = content.slice("!mlx search ".length).toLowerCase();
    const hits = endpoints
      .filter(
        (e) =>
          e.name.toLowerCase().includes(q) ||
          e.url.toLowerCase().includes(q) ||
          e.category.toLowerCase().includes(q),
      )
      .slice(0, 5);
    if (!hits.length) {
      await msg.reply("No matches.");
      return;
    }
    const embed = new EmbedBuilder()
      .setColor(0x0066ff)
      .setTitle("Multilogin X · search results")
      .setDescription(
        hits
          .map(
            (e) =>
              `**${e.method}** ${e.name}\n${e.url}\n[docs](https://github.com/multilogin-labs/multilogin-labs/blob/main/docs/api/endpoints/${e.slug}.md)`,
          )
          .join("\n\n"),
      )
      .setURL("https://github.com/multilogin-labs/multilogin-labs");
    await msg.reply({ embeds: [embed] });
  }
});

client.login(TOKEN);
