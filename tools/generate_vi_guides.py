#!/usr/bin/env python3
"""Generate Vietnamese versions of core guides."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "guides" / "vi"
OUT.mkdir(parents=True, exist_ok=True)

AFFILIATE = (
    "https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner"
    "&a_aid=saas&a_bid=f5fad549"
)

GUIDES = [
    (
        "multilogin-la-gi",
        "Multilogin là gì? Tổng quan 2026",
        "antidetect browser cloud phone multilogin",
        "Multilogin là nền tảng quản lý đa tài khoản: browser antidetect (Mimic + Stealthfox), cloud phone Android thật, proxy tích hợp và **API 90 endpoint** phục vụ automation.",
        [
            "Tạo profile trình duyệt riêng biệt — fingerprint khác nhau, không bị link account.",
            "Cloud phone Android phần cứng thật cho TikTok, Instagram, WhatsApp, Telegram.",
            "Proxy residential/mobile bundled trong gói Pro.",
            "API + Postman collection cho Playwright, Puppeteer, Selenium.",
        ],
    ),
    (
        "multilogin-gia-bao-nhieu",
        "Multilogin giá bao nhiêu? Bảng giá 2026 + mã giảm",
        "multilogin gia bang gia",
        "Pro 10 từ ~**$7.08/tháng** (trả năm) — bao gồm API, proxy GB và mobile minutes ở Pro 50+. Mã **SAAS50** / **MIN50** giảm thêm khi checkout.",
        [
            "Trial $2 / 3 ngày — 5 profile, đủ test API và proxy.",
            "Pro 10: solo / freelancer.",
            "Pro 50: team 5–10 người, agency nhỏ.",
            "Pro 100 + Business 300+: agency, dropship, MMO scale lớn.",
        ],
    ),
    (
        "multilogin-cai-dat",
        "Cài đặt Multilogin trên Windows / macOS / Linux",
        "cai dat multilogin install",
        "Tải app từ trang chính thức, đăng nhập bằng tài khoản partner ($2 trial), kiểm tra Launcher chạy ở `https://launcher.mlx.yt:45001`.",
        [
            "Windows: tải `.exe`, cài bình thường, mở app, login.",
            "macOS: `.dmg`, cấp quyền Accessibility nếu app yêu cầu.",
            "Linux: hỗ trợ Ubuntu/Debian; có thể chạy trên VPS với GUI hoặc Xvfb.",
            "Sau khi login, mở [docs/api/quick-start](../../api/quick-start.md) để lấy token.",
        ],
    ),
    (
        "multilogin-tao-profile",
        "Cách tạo profile trình duyệt antidetect",
        "tao profile antidetect multilogin",
        "Profile = một danh tính trình duyệt độc lập (fingerprint, cookies, proxy, ngôn ngữ).",
        [
            "Mở app → Folders → tạo folder theo client/dự án.",
            "New profile → chọn Mimic (Chrome) hoặc Stealthfox (Firefox).",
            "Gán proxy phù hợp với quốc gia mục tiêu.",
            "Đặt tag (`tiktok`, `warmup`, `client-x`) để dễ search và filter API.",
            "Quick profile dùng cho phiên một lần — xem [cookbook 02](../../api/cookbook/02-quick-profile-scrape.md).",
        ],
    ),
    (
        "multilogin-tiktok-mmo",
        "Multilogin nuôi nick TikTok 2026",
        "tiktok multilogin nuoi nick mmo",
        "Stack tốt nhất: cloud phone Android thật + proxy mobile + một profile = một tài khoản.",
        [
            "Match GPS với proxy trước khi cài app TikTok.",
            "Warmup 3–5 ngày: xem, like, follow — không gắn link.",
            "Một số điện thoại = một danh tính, không đổi proxy giữa phiên.",
            "Tham khảo [TikTok playbook](../../platforms/tiktok.md).",
        ],
    ),
    (
        "multilogin-shopee-lazada",
        "Multilogin chạy nhiều shop Shopee / Lazada",
        "shopee lazada multilogin",
        "Cloud phone cho app seller mobile, Mimic profile cho seller center web. Proxy khớp quốc gia (VN/ID/PH/TH).",
        [
            "Một shop = một profile = một số ĐT (nếu cần).",
            "Warmup bằng đơn organic trước khi chạy ads.",
            "Xem playbook [Vietnam](../../playbooks/vietnam.md), [Indonesia](../../playbooks/indonesia.md).",
        ],
    ),
    (
        "multilogin-facebook-ads",
        "Multilogin chạy Facebook Ads nhiều BM",
        "facebook ads multilogin bm",
        "Mỗi BM/agency account = một Mimic profile + proxy residential cùng quốc gia thẻ thanh toán.",
        [
            "Không share cookie giữa các BM khác nhau.",
            "Bật 2FA, lưu backup code an toàn.",
            "Tag profile: `fb-bm`, `client-slug`.",
            "Xem [Meta playbook](../../platforms/facebook-meta.md).",
        ],
    ),
    (
        "multilogin-api-tieng-viet",
        "Hướng dẫn Multilogin API tiếng Việt",
        "multilogin api huong dan",
        "API Multilogin X có 90 endpoint, chia 2 phần: Cloud (`api.multilogin.com`) và Launcher (`launcher.mlx.yt:45001`).",
        [
            "Lấy token: [authentication](../../api/authentication.md).",
            "Start profile: `GET /api/v2/profile/f/{folder_id}/p/{profile_id}/start`.",
            "Stop profile: `GET /api/v1/profile/stop?profile_id=...`.",
            "Khám phá API: [Swagger UI](../../api/swagger.html), [Cheatsheet](../../api/CHEATSHEET.md), [Cookbook](../../api/cookbook/).",
        ],
    ),
    (
        "multilogin-playwright",
        "Multilogin + Playwright tiếng Việt",
        "playwright multilogin tu dong",
        "Start profile qua Launcher → kết nối Playwright bằng CDP qua port trả về.",
        [
            "Cài: `npm i playwright`.",
            "Tham khảo [scripts/playwright/connect-profile.mjs](../../../scripts/playwright/connect-profile.mjs).",
            "Cookbook đầy đủ: [01-playwright-full-session](../../api/cookbook/01-playwright-full-session.md).",
        ],
    ),
    (
        "multilogin-so-sanh",
        "So sánh Multilogin với 16 tool antidetect",
        "multilogin vs adspower gologin",
        "Bảng one-page và bài chi tiết cho từng đối thủ.",
        [
            "[Comparison matrix](../../comparisons/comparison-matrix.md) — 16 tool.",
            "[vs AdsPower](../../comparisons/multilogin-vs-adspower.md), [vs GoLogin](../../comparisons/multilogin-vs-gologin.md).",
            "[vs Dolphin](../../comparisons/multilogin-vs-dolphin-anty.md), [vs Octo](../../comparisons/multilogin-vs-octo-browser.md).",
        ],
    ),
    (
        "multilogin-loi-thuong-gap",
        "Lỗi Multilogin thường gặp + cách fix",
        "multilogin loi 401 429 timeout",
        "Tổng hợp lỗi 401, 429, profile không khởi động, proxy timeout.",
        [
            "401: token hết hạn — refresh hoặc dùng automation token.",
            "429: vượt rate limit — automation token cho RPM cao hơn.",
            "Profile không start: kiểm tra Multilogin desktop, port 45001, [troubleshooting](../../troubleshooting.md).",
        ],
    ),
    (
        "multilogin-mmo-vietnam",
        "Multilogin cho dân MMO Việt Nam",
        "multilogin mmo viet nam",
        "Use case phổ biến: TikTok Shop VN, Shopee VN, Facebook Ads, Affiliate, airdrop, Amazon FBA.",
        [
            "[Vietnam playbook](../../playbooks/vietnam.md) — proxy, plan, platform.",
            "Mã đối tác: **SAAS50** / **MIN50**.",
            f"[Đăng ký trial $2]({AFFILIATE}).",
        ],
    ),
]

TEMPLATE = """# {title}

> [Giá đối tác →]({affiliate}) · **`SAAS50`** · **`MIN50`**

{intro}

## Các bước

{steps}

## Liên quan

- [Tất cả guide tiếng Việt](README.md)
- [Hub tài liệu](../../README.md) · [SEARCH_INDEX](../../SEARCH_INDEX.md)
- [API cheatsheet](../../api/CHEATSHEET.md) · [So sánh tool](../../comparisons/comparison-matrix.md)
- [Tính plan](../../calculator.html)

**Keywords:** {keywords} · multilogin tiếng việt · multilogin labs
"""


def main():
    rows = []
    for slug, title, kw, intro, steps in GUIDES:
        path = OUT / f"{slug}.md"
        if path.exists():
            continue
        bullets = "\n".join(f"{i+1}. {s}" for i, s in enumerate(steps))
        path.write_text(
            TEMPLATE.format(
                title=title,
                affiliate=AFFILIATE,
                intro=intro,
                steps=bullets,
                keywords=kw,
            ),
            encoding="utf-8",
        )
        rows.append((title, slug))
        print("vi", slug)

    readme = OUT / "README.md"
    body = ["# Hướng dẫn Multilogin tiếng Việt", "",
            f"> [Giá đối tác →]({AFFILIATE}) · **`SAAS50`** · **`MIN50`**",
            "", "| Bài | Mô tả |", "|---|---|"]
    for title, slug in (rows or [(t, s) for s, t, *_ in GUIDES]):
        body.append(f"| [{title}]({slug}.md) | {title} |")
    body.append("")
    body.append("[All guides (EN)](../README.md) · [Hub](../../README.md)")
    readme.write_text("\n".join(body) + "\n", encoding="utf-8")
    print(f"vi guides: {len(rows)} new")


if __name__ == "__main__":
    main()
