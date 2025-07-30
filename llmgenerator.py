#!/usr/bin/env python3
import feedparser
import requests
from datetime import datetime
import os

RSS_URL = "https://carlosdelfino.eti.br/atom.xml"
OUTPUT = "llm.txt"
SITE_TITLE = "carlosdelfino.eti.br"
SITE_DESC = "Artigos sobre engenharia elétrica, teologia islâmica e marketing digital."

def fetch_feed(url):
    return feedparser.parse(url)

def build_llm_txt(feed):
    lines = []
    lines.append(f"# {SITE_TITLE}")
    lines.append(f"> {SITE_DESC}")
    lines.append("")
    lines.append("## Conteúdo Principal")
    for entry in feed.entries:
        title = entry.get("title", "Sem título")
        link = entry.get("link", "#")
        pub = entry.get("published", "")
        date = ""
        if pub:
            try:
                date = datetime(*entry.published_parsed[:6]).strftime("%Y-%m‑%d")
            except:
                date = pub
        lines.append(f"- [{title}]({link}) — {date}")
    return "\n".join(lines)

def save_file(content, path):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf‑8") as f:
        f.write(content)
    os.replace(tmp, path)

def main():
    feed = fetch_feed(RSS_URL)
    if not feed.entries:
        print("Feed vazio ou inacessível.")
        return
    content = build_llm_txt(feed)
    save_file(content, OUTPUT)
    print(f"{OUTPUT} atualizado com {len(feed.entries)} itens.")

if __name__ == "__main__":
    main()
