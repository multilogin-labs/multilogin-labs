#!/usr/bin/env python3
"""Generate localized core guides for RU / TR / FR / AR."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GUIDES = ROOT / "docs" / "guides"
AFFILIATE = (
    "https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner"
    "&a_aid=saas&a_bid=f5fad549"
)

LANGS = {
    "ru": {
        "title": "Гайды Multilogin на русском",
        "items": [
            ("multilogin-chto-eto", "Что такое Multilogin? Обзор 2026", "antidetect cloud phone multilogin",
             "Multilogin — платформа мультиаккаунтинга: антидетект-браузеры (Mimic + Stealthfox), реальные облачные Android-устройства, встроенные прокси и 90 эндпоинтов API."),
            ("multilogin-tseni", "Сколько стоит Multilogin 2026 + промокоды",
             "multilogin tseni promo",
             "Pro 10 от ~$7,08/мес (год) — включая API, GB прокси и минуты cloud phone на Pro 50+. Используйте SAAS50 или MIN50 при оплате."),
            ("multilogin-ustanovka", "Установка Multilogin (Win/macOS/Linux)",
             "multilogin ustanovka",
             "Скачайте приложение, войдите по триалу $2/3 дня, проверьте Launcher на https://launcher.mlx.yt:45001."),
            ("multilogin-profil", "Как создать антидетект-профиль",
             "multilogin profil sozdat",
             "Каждый профиль изолирует fingerprint, cookies, прокси и локаль. Тегируйте профили для скриптовой автоматизации."),
            ("multilogin-tiktok", "Multilogin для TikTok в СНГ",
             "tiktok multilogin sng",
             "Реальный cloud phone Android + мобильный прокси целевой страны + 1 профиль = 1 аккаунт. Не меняйте IP внутри сессии."),
            ("multilogin-meta-ads", "Multilogin для Meta Ads (Facebook/Instagram)",
             "meta ads facebook multilogin",
             "Один BM = один профиль + резидентный прокси по стране карты. 2FA обязательно на каждом профиле."),
            ("multilogin-arbitrage", "Multilogin для арбитража трафика",
             "arbitrage multilogin",
             "Изоляция кабинетов Google/Meta/TikTok ads. Резидентные прокси, прогрев 3-7 дней перед запуском."),
            ("multilogin-api", "Гайд по Multilogin API",
             "multilogin api gid",
             "API Multilogin X содержит 90 эндпоинтов: Cloud (api.multilogin.com) + Launcher (launcher.mlx.yt:45001)."),
            ("multilogin-playwright", "Multilogin + Playwright (RU)",
             "playwright multilogin",
             "Запустите профиль через Launcher и подключите Playwright по CDP-порту."),
            ("multilogin-oshibki", "Частые ошибки Multilogin и фиксы",
             "multilogin oshibki 401 429",
             "401 = просрочен токен (refresh). 429 = лимит RPM (используйте automation token). Профиль не стартует: проверьте desktop-приложение и порт 45001."),
        ],
    },
    "tr": {
        "title": "Multilogin Türkçe rehberler",
        "items": [
            ("multilogin-nedir", "Multilogin nedir? 2026 genel bakış", "antidetect cloud phone multilogin",
             "Multilogin çoklu hesap platformu: antidetect tarayıcılar (Mimic + Stealthfox), gerçek bulut Android telefon, dahili proxy ve 90 API endpoint."),
            ("multilogin-fiyat", "Multilogin fiyatları 2026 + promosyon kodları",
             "multilogin fiyat promo",
             "Pro 10 ~$7,08/ay (yıllık) — API, proxy GB ve mobil dakika Pro 50+'da dahil. SAAS50 veya MIN50 kodları ödemede geçerli."),
            ("multilogin-kurulum", "Multilogin kurulumu (Win/macOS/Linux)",
             "multilogin kurulum",
             "Resmi uygulamayı indirin, $2 deneme ile giriş yapın, Launcher'ın https://launcher.mlx.yt:45001 üzerinde çalıştığını doğrulayın."),
            ("multilogin-profil", "Antidetect profili nasıl oluşturulur",
             "multilogin profil olustur",
             "Her profil; fingerprint, cookies, proxy ve dil ayarını izole eder. Otomasyon için etiket kullanın."),
            ("multilogin-tiktok", "Multilogin TikTok Türkiye",
             "tiktok multilogin turkiye",
             "Gerçek cloud phone + mobil proxy TR + 1 profil = 1 hesap. Oturum içinde IP değiştirmeyin."),
            ("multilogin-trendyol", "Multilogin Trendyol / Hepsiburada satıcı",
             "trendyol hepsiburada multilogin",
             "Mobil seller uygulamaları için cloud phone, web seller paneli için Mimic. Residential proxy TR."),
            ("multilogin-meta-ads", "Multilogin Meta Ads (FB/IG TR)",
             "meta ads facebook multilogin tr",
             "Bir BM = bir profil + ödeme yapılan ülkeye uygun residential proxy. Her profilde 2FA zorunlu."),
            ("multilogin-api", "Multilogin API rehberi (TR)",
             "multilogin api rehber",
             "Multilogin X API 90 endpoint içerir: Cloud (api.multilogin.com) + Launcher (launcher.mlx.yt:45001)."),
            ("multilogin-playwright", "Multilogin + Playwright (TR)",
             "playwright multilogin",
             "Profili Launcher ile başlatın ve dönen CDP portu üzerinden Playwright bağlayın."),
            ("multilogin-hatalar", "Sık karşılaşılan Multilogin hataları",
             "multilogin hata 401 429",
             "401 = token süresi doldu (refresh). 429 = RPM limiti (automation token kullanın). Profil başlamıyor: desktop app + port 45001 kontrol edin."),
        ],
    },
    "fr": {
        "title": "Guides Multilogin en français",
        "items": [
            ("multilogin-quest-ce-que", "Qu'est-ce que Multilogin ? Aperçu 2026", "antidetect cloud phone multilogin",
             "Multilogin est la plateforme multi-comptes : navigateurs antidetect (Mimic + Stealthfox), cloud phones Android réels, proxy intégré et 90 endpoints API."),
            ("multilogin-tarifs", "Tarifs Multilogin 2026 + codes promo",
             "multilogin tarifs prix promo",
             "Pro 10 dès ~$7,08/mois (annuel) — inclut API, Go de proxy et minutes mobile sur Pro 50+. Utilisez SAAS50 ou MIN50 au paiement."),
            ("multilogin-installation", "Installer Multilogin (Win/macOS/Linux)",
             "multilogin installation",
             "Téléchargez l'application officielle, connectez-vous avec l'essai $2, vérifiez le Launcher sur https://launcher.mlx.yt:45001."),
            ("multilogin-profil", "Comment créer un profil antidetect",
             "multilogin profil",
             "Chaque profil isole l'empreinte, les cookies, le proxy et la locale. Étiquetez vos profils pour l'automatisation."),
            ("multilogin-tiktok", "Multilogin pour TikTok (France/Afrique)",
             "tiktok multilogin france",
             "Cloud phone Android réel + proxy mobile pays cible + 1 profil = 1 compte. Pas de changement d'IP en cours de session."),
            ("multilogin-meta-ads", "Multilogin pour Meta Ads (FB/IG)",
             "meta ads facebook multilogin",
             "Un BM = un profil + proxy résidentiel aligné sur le pays de la carte. 2FA obligatoire sur chaque profil."),
            ("multilogin-amazon", "Multilogin pour Amazon Seller (FR/EU)",
             "amazon multilogin france",
             "Profil Mimic par compte vendeur, proxy ISP collant, IP cohérente avec le pays de paiement."),
            ("multilogin-api", "Guide de l'API Multilogin (FR)",
             "guide multilogin api",
             "L'API Multilogin X compte 90 endpoints répartis sur Cloud (api.multilogin.com) et Launcher (launcher.mlx.yt:45001)."),
            ("multilogin-playwright", "Multilogin + Playwright (FR)",
             "playwright multilogin francais",
             "Démarrez le profil via le Launcher puis connectez Playwright au port CDP retourné."),
            ("multilogin-erreurs", "Erreurs courantes Multilogin et corrections",
             "multilogin erreurs 401 429",
             "401 = token expiré (refresh). 429 = limite RPM (utilisez l'automation token). Profil ne démarre pas : vérifiez l'app desktop et le port 45001."),
        ],
    },
    "ar": {
        "title": "أدلة Multilogin بالعربية",
        "items": [
            ("multilogin-ma-howa", "ما هو Multilogin؟ نظرة 2026", "antidetect cloud phone multilogin",
             "Multilogin هو منصة متعددة الحسابات: متصفحات antidetect (Mimic + Stealthfox)، هواتف Android سحابية حقيقية، بروكسي مدمج، و 90 نقطة API."),
            ("multilogin-asaar", "أسعار Multilogin 2026 ورموز الخصم",
             "multilogin asaar promo",
             "Pro 10 من ~$7,08 شهرياً (سنوي) — يشمل API و GB من البروكسي ودقائق هاتف سحابي من Pro 50+. استخدم SAAS50 أو MIN50."),
            ("multilogin-tansib", "تثبيت Multilogin (Win/macOS/Linux)",
             "multilogin tansib",
             "حمّل التطبيق الرسمي، سجل بالتجربة $2/3 أيام، تأكد من تشغيل Launcher على https://launcher.mlx.yt:45001."),
            ("multilogin-profile", "كيفية إنشاء profile antidetect",
             "multilogin profile",
             "كل profile يعزل البصمة والكوكيز والبروكسي واللغة. استخدم الوسوم للأتمتة على نطاق واسع."),
            ("multilogin-tiktok", "Multilogin لتيك توك في MENA",
             "tiktok multilogin mena",
             "Cloud phone حقيقي + بروكسي محمول من البلد المستهدف + 1 profile = 1 حساب. لا تغيير لـ IP أثناء الجلسة."),
            ("multilogin-noon-amazon", "Multilogin لمتاجر Noon و Amazon SA",
             "noon amazon multilogin",
             "Profile Mimic لكل حساب بائع، بروكسي residential SA/AE، تطابق IP مع بلد الدفع."),
            ("multilogin-meta-ads", "Multilogin لإعلانات Meta",
             "meta ads facebook multilogin",
             "BM واحد = profile واحد + بروكسي residential متوافق مع بلد البطاقة. 2FA إلزامي."),
            ("multilogin-api", "دليل Multilogin API بالعربية",
             "dalil multilogin api",
             "API Multilogin X يحتوي على 90 نقطة: Cloud (api.multilogin.com) و Launcher (launcher.mlx.yt:45001)."),
            ("multilogin-playwright", "Multilogin + Playwright (AR)",
             "playwright multilogin",
             "ابدأ الـ profile عبر Launcher ثم اربط Playwright بمنفذ CDP المُعاد."),
            ("multilogin-akhtaa", "أخطاء Multilogin الشائعة وإصلاحاتها",
             "multilogin akhtaa 401 429",
             "401 = token منتهٍ (refresh). 429 = حد RPM (استخدم automation token). لا يبدأ الـ profile: تأكد من تطبيق desktop والمنفذ 45001."),
        ],
    },
}

TEMPLATE = """# {title}

> [Partner pricing →]({affiliate}) · **`SAAS50`** · **`MIN50`**

{intro}

## Step-by-step

1. Read [API CHEATSHEET](../../api/CHEATSHEET.md) for endpoint shape.
2. Use [Quick start](../../api/quick-start.md) to obtain a token.
3. Pick a [cookbook recipe](../../api/cookbook/README.md) (60 total) for your use case.

## Related

- [Cookbook ×60](../../api/cookbook/README.md) · [Swagger UI](../../api/swagger.html) · [Calculator](../../calculator.html)
- [Search](../../search.html) — full-text across the hub
- [Architecture diagrams](../../architecture.md)
- [English guides](../README.md)

**Keywords:** {keywords} · multilogin labs
"""


def main():
    total = 0
    for lang, cfg in LANGS.items():
        out = GUIDES / lang
        out.mkdir(parents=True, exist_ok=True)
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
            total += 1
            print(lang, slug)

        readme = out / "README.md"
        body = [
            f"# {cfg['title']}",
            "",
            f"> [Partner →]({AFFILIATE}) · **SAAS50** · **MIN50**",
            "",
            "| Guide | |",
            "|---|---|",
        ]
        for title, slug in [(t, s) for s, t, *_ in cfg["items"]]:
            body.append(f"| [{title}]({slug}.md) | |")
        body.append("")
        body.append("[All guides (EN)](../README.md) · [Hub](../../README.md)")
        readme.write_text("\n".join(body) + "\n", encoding="utf-8")
    print(f"locale guides v2: {total} new")


if __name__ == "__main__":
    main()
