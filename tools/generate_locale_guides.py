#!/usr/bin/env python3
"""Generate localized core guides for additional languages."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GUIDES = ROOT / "docs" / "guides"
AFFILIATE = (
    "https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner"
    "&a_aid=saas&a_bid=f5fad549"
)

LANGS = {
    "pt-br": {
        "title": "Guias Multilogin em português",
        "items": [
            ("multilogin-o-que-e", "O que é Multilogin? Visão geral 2026", "antidetect cloud phone multilogin",
             "Multilogin é a plataforma de multi-conta com navegadores antidetect (Mimic + Stealthfox), cloud phones Android reais, proxy integrado e 90 endpoints de API."),
            ("multilogin-precos", "Quanto custa Multilogin? Preços 2026 e cupons",
             "multilogin precos planos cupons",
             "Pro 10 a partir de ~$7,08/mês (anual) — inclui API, proxy GB e minutos mobile no Pro 50+. Use SAAS50 ou MIN50 no checkout."),
            ("multilogin-instalar", "Como instalar Multilogin (Win/macOS/Linux)",
             "multilogin instalar baixar",
             "Baixe o app, faça login com a conta de teste $2 e confirme que o Launcher local responde em https://launcher.mlx.yt:45001."),
            ("multilogin-perfil", "Como criar um perfil antidetect",
             "criar perfil antidetect",
             "Cada perfil isola fingerprint, cookies, proxy e idioma. Use tags para automação em escala."),
            ("multilogin-tiktok", "Multilogin para TikTok no Brasil",
             "tiktok multilogin brasil",
             "Cloud phone Android real + proxy mobile BR + 1 perfil = 1 conta. Sem mistura de IP entre sessões."),
            ("multilogin-mercado-livre", "Multilogin para Mercado Livre / Shopee BR",
             "mercado livre shopee multilogin brasil",
             "Cloud phone para apps de seller, perfil Mimic para painel web. Proxy residencial BR."),
            ("multilogin-meta-ads", "Multilogin para Meta Ads (Facebook/Instagram BR)",
             "meta ads facebook multilogin brasil",
             "Um BM = um perfil + proxy residencial alinhado ao país do cartão. 2FA obrigatório."),
            ("multilogin-api", "Guia da API Multilogin em português",
             "multilogin api guia",
             "API Multilogin X possui 90 endpoints divididos entre Cloud (api.multilogin.com) e Launcher (launcher.mlx.yt:45001)."),
            ("multilogin-playwright", "Multilogin + Playwright em português",
             "playwright multilogin",
             "Inicie o perfil pelo Launcher → conecte o Playwright via CDP usando a porta retornada."),
            ("multilogin-erros-comuns", "Erros comuns Multilogin e como corrigir",
             "multilogin erro 401 429 timeout",
             "401 = token expirou (refresh). 429 = limite RPM (use automation token). Perfil não inicia: verifique o app desktop e a porta 45001."),
        ],
    },
    "id": {
        "title": "Panduan Multilogin Bahasa Indonesia",
        "items": [
            ("multilogin-apa-itu", "Apa itu Multilogin? Tinjauan 2026",
             "antidetect cloud phone multilogin",
             "Multilogin adalah platform multi-akun: browser antidetect (Mimic + Stealthfox), cloud phone Android nyata, proxy bawaan, dan 90 endpoint API."),
            ("multilogin-harga", "Berapa harga Multilogin 2026 + kode promo",
             "harga multilogin promo",
             "Pro 10 mulai ~$7,08/bulan (tahunan) — termasuk API, proxy GB, dan menit mobile mulai Pro 50+. Pakai SAAS50 atau MIN50 saat checkout."),
            ("multilogin-instalasi", "Instal Multilogin di Windows/macOS/Linux",
             "instal multilogin",
             "Unduh app resmi, login dengan trial $2, pastikan Launcher lokal siap di https://launcher.mlx.yt:45001."),
            ("multilogin-buat-profil", "Cara membuat profil antidetect",
             "buat profil antidetect",
             "Tiap profil mengisolasi fingerprint, cookies, proxy, dan bahasa. Gunakan tag untuk otomasi skala besar."),
            ("multilogin-tiktok", "Multilogin TikTok Indonesia",
             "tiktok multilogin indonesia",
             "Cloud phone Android nyata + proxy mobile ID + 1 profil = 1 akun. Jangan tukar proxy di tengah sesi."),
            ("multilogin-shopee-tokopedia", "Multilogin untuk Shopee & Tokopedia",
             "shopee tokopedia multilogin",
             "Cloud phone untuk app seller mobile, profil Mimic untuk seller center web. Proxy residential ID."),
            ("multilogin-meta-ads", "Multilogin untuk Meta Ads (FB/IG Indonesia)",
             "meta ads facebook multilogin indonesia",
             "Satu BM = satu profil + proxy residential cocok dengan negara kartu pembayaran. 2FA wajib."),
            ("multilogin-api", "Panduan Multilogin API",
             "panduan multilogin api",
             "API Multilogin X memiliki 90 endpoint dalam dua bagian: Cloud (api.multilogin.com) dan Launcher (launcher.mlx.yt:45001)."),
            ("multilogin-playwright", "Multilogin + Playwright (Indonesia)",
             "playwright multilogin",
             "Jalankan profil via Launcher, lalu hubungkan Playwright melalui CDP port yang dikembalikan."),
            ("multilogin-error-umum", "Error umum Multilogin dan cara perbaikan",
             "error multilogin 401 429",
             "401 = token kedaluwarsa (refresh). 429 = batas RPM (pakai automation token). Profil tidak start: cek desktop app & port 45001."),
        ],
    },
    "es": {
        "title": "Guías Multilogin en español",
        "items": [
            ("multilogin-que-es", "¿Qué es Multilogin? Visión 2026",
             "antidetect cloud phone multilogin",
             "Multilogin es la plataforma multicuenta: navegadores antidetect (Mimic + Stealthfox), cloud phones Android reales, proxy integrado y 90 endpoints de API."),
            ("multilogin-precio", "Precios Multilogin 2026 + códigos promocionales",
             "multilogin precio planes promo",
             "Pro 10 desde ~$7,08/mes (anual) — incluye API, proxy GB y minutos móvil en Pro 50+. Usa SAAS50 o MIN50 al pagar."),
            ("multilogin-instalacion", "Instalar Multilogin en Windows/macOS/Linux",
             "instalar multilogin",
             "Descarga la app oficial, inicia sesión con la prueba de $2, confirma que el Launcher local responde en https://launcher.mlx.yt:45001."),
            ("multilogin-crear-perfil", "Cómo crear un perfil antidetect",
             "crear perfil antidetect",
             "Cada perfil aísla fingerprint, cookies, proxy y locale. Etiqueta los perfiles para automatizar en escala."),
            ("multilogin-tiktok", "Multilogin para TikTok en LATAM",
             "tiktok multilogin latam",
             "Cloud phone Android real + proxy móvil de país objetivo + 1 perfil = 1 cuenta. No intercambies IP en mitad de sesión."),
            ("multilogin-mercado-libre", "Multilogin para Mercado Libre",
             "mercado libre multilogin",
             "Cloud phone para apps de seller, Mimic para el centro web. Proxy residencial alineado al país de la tienda."),
            ("multilogin-meta-ads", "Multilogin para Meta Ads (Facebook/Instagram)",
             "meta ads facebook multilogin",
             "Un BM = un perfil + proxy residencial alineado con la tarjeta. 2FA obligatorio en cada perfil."),
            ("multilogin-api", "Guía de la API Multilogin en español",
             "guia multilogin api",
             "La API Multilogin X tiene 90 endpoints divididos en Cloud (api.multilogin.com) y Launcher (launcher.mlx.yt:45001)."),
            ("multilogin-playwright", "Multilogin + Playwright (español)",
             "playwright multilogin espanol",
             "Inicia el perfil por el Launcher y conecta Playwright al puerto CDP devuelto."),
            ("multilogin-errores", "Errores comunes Multilogin y cómo solucionarlos",
             "errores multilogin 401 429",
             "401 = token caducado (refresh). 429 = límite RPM (usa token de automation). Perfil no inicia: revisa la app de escritorio y el puerto 45001."),
        ],
    },
}

TEMPLATE = """# {title}

> [Pricing partner →]({affiliate}) · **`SAAS50`** · **`MIN50`**

{intro}

## Step-by-step

1. Read [API CHEATSHEET](../../api/CHEATSHEET.md) for endpoint shape.
2. Use [Quick start](../../api/quick-start.md) to obtain a token.
3. Pick a [cookbook recipe](../../api/cookbook/README.md) for your use case.

## Related

- [Cookbook ×60](../../api/cookbook/README.md) · [Swagger UI](../../api/swagger.html) · [Calculator](../../calculator.html)
- [SEARCH](../../search.html) — full-text across the hub
- [Architecture diagrams](../../architecture.md)
- [English guides](../README.md)

**Keywords:** {keywords} · multilogin labs
"""


def main():
    total = 0
    for lang, cfg in LANGS.items():
        out = GUIDES / lang
        out.mkdir(parents=True, exist_ok=True)
        rows = []
        for slug, title, kw, intro in cfg["items"]:
            path = out / f"{slug}.md"
            if path.exists():
                continue
            path.write_text(
                TEMPLATE.format(
                    title=title,
                    affiliate=AFFILIATE,
                    intro=intro,
                    keywords=kw,
                ),
                encoding="utf-8",
            )
            rows.append((title, slug))
            total += 1
            print(lang, slug)

        readme = out / "README.md"
        body = [f"# {cfg['title']}", "", f"> [Partner →]({AFFILIATE}) · **SAAS50** · **MIN50**", "", "| Guide | |", "|---|---|"]
        for title, slug in [(t, s) for s, t, *_ in cfg["items"]]:
            body.append(f"| [{title}]({slug}.md) | |")
        body.append("")
        body.append("[All guides (EN)](../README.md) · [Hub](../../README.md)")
        readme.write_text("\n".join(body) + "\n", encoding="utf-8")
    print(f"locale guides: {total} new")


if __name__ == "__main__":
    main()
