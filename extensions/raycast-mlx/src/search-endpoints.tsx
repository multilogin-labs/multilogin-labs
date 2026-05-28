import { ActionPanel, Action, List, Icon } from "@raycast/api";
import { useEffect, useState } from "react";

type Endpoint = {
  category: string;
  name: string;
  method: string;
  url: string;
  slug: string;
};

const REMOTE_INDEX =
  "https://raw.githubusercontent.com/multilogin-labs/multilogin-labs/main/docs/api/endpoints.json";

export default function Command() {
  const [items, setItems] = useState<Endpoint[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(REMOTE_INDEX)
      .then((r) => r.json())
      .then((data) => {
        setItems(data);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  return (
    <List isLoading={loading} searchBarPlaceholder="Search 90 Multilogin endpoints…">
      {items.map((e) => (
        <List.Item
          key={`${e.method}-${e.slug}`}
          icon={Icon.Globe}
          title={`${e.method} ${e.name}`}
          subtitle={e.category}
          accessories={[{ text: e.url }]}
          actions={
            <ActionPanel>
              <Action.OpenInBrowser
                url={`https://github.com/multilogin-labs/multilogin-labs/blob/main/docs/api/endpoints/${e.slug}.md`}
              />
              <Action.CopyToClipboard content={e.url} title="Copy URL" />
              <Action.OpenInBrowser
                title="Open Swagger UI"
                url="https://multilogin-labs.github.io/multilogin-labs/api/swagger.html"
              />
              <Action.OpenInBrowser
                title="Partner pricing (SAAS50 / MIN50)"
                url="https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549"
              />
            </ActionPanel>
          }
        />
      ))}
    </List>
  );
}
