const REMOTE =
  "https://raw.githubusercontent.com/multilogin-labs/multilogin-labs/main/docs/api/endpoints.json";
const DOC_BASE =
  "https://github.com/multilogin-labs/multilogin-labs/blob/main/docs/api/endpoints/";

let endpoints = [];

async function load() {
  try {
    const cached = await chrome.storage.local.get("endpoints");
    if (cached.endpoints?.data && Date.now() - cached.endpoints.ts < 86400000) {
      endpoints = cached.endpoints.data;
      return;
    }
  } catch {}
  const res = await fetch(REMOTE);
  endpoints = await res.json();
  try {
    await chrome.storage.local.set({
      endpoints: { ts: Date.now(), data: endpoints },
    });
  } catch {}
}

function render(query) {
  const ul = document.getElementById("hits");
  ul.innerHTML = "";
  const q = (query || "").toLowerCase();
  const hits = endpoints.filter(
    (e) =>
      !q ||
      e.name.toLowerCase().includes(q) ||
      e.url.toLowerCase().includes(q) ||
      e.category.toLowerCase().includes(q),
  );
  for (const e of hits.slice(0, 30)) {
    const li = document.createElement("li");
    li.innerHTML = `<strong>${e.method}</strong> ${e.name}<div class="meta">${e.category}</div>`;
    li.onclick = () =>
      chrome.tabs.create({ url: DOC_BASE + e.slug + ".md" });
    ul.appendChild(li);
  }
}

(async () => {
  await load();
  render("");
  document.getElementById("q").addEventListener("input", (e) => render(e.target.value));
})();
