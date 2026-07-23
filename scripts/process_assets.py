"""Prepare supplied Arma Go logos and generated editorial imagery for the site."""

from pathlib import Path

from PIL import Image, ImageChops


ROOT = Path(__file__).resolve().parents[1]
BRAND = ROOT / "src" / "assets" / "brand"
OUTPUT = ROOT / "public" / "images"

GENERATED = {
    "og-card.webp": Path(
        "/Users/abby/.codex/generated_images/019f8fb4-480c-7570-8781-2551429fe2a7/"
        "exec-bc4e20cd-4c10-4a78-ad48-c76f77c70094.png"
    ),
    "home-guidance.webp": Path(
        "/Users/abby/.codex/generated_images/019f8fb4-480c-7570-8781-2551429fe2a7/"
        "exec-e2299d4a-ae34-48d8-9d55-48fa820e6095.png"
    ),
    "home-guidance-v2.webp": Path(
        "/Users/abby/.codex/generated_images/019f8fb4-480c-7570-8781-2551429fe2a7/"
        "call_RzQrTU0RYeFmIesV74oi0v41.png"
    ),
    "home-guidance-v3.webp": ROOT
    / "src"
    / "assets"
    / "editorial"
    / "home-hero-dark-source.png",
    "work-abroad-v2.webp": ROOT
    / "src"
    / "assets"
    / "editorial"
    / "work-abroad-professions-source.png",
    "work-abroad.webp": Path(
        "/Users/abby/.codex/generated_images/019f8fb4-480c-7570-8781-2551429fe2a7/"
        "exec-db21a7e0-0a3f-4515-8554-cb390f371292.png"
    ),
    "study-abroad.webp": Path(
        "/Users/abby/.codex/generated_images/019f8fb4-480c-7570-8781-2551429fe2a7/"
        "exec-e4f0531a-cc9e-462b-bb3d-dbaf7312a01d.png"
    ),
    "employers-partners.webp": Path(
        "/Users/abby/.codex/generated_images/019f8fb4-480c-7570-8781-2551429fe2a7/"
        "exec-cabbcda2-79d2-40ed-9a6b-c0137feb8e84.png"
    ),
    "how-it-works.webp": Path(
        "/Users/abby/.codex/generated_images/019f8fb4-480c-7570-8781-2551429fe2a7/"
        "exec-fcf2b445-6e88-4dba-b914-e2d9f3f77a14.png"
    ),
    "about-architecture.webp": Path(
        "/Users/abby/.codex/generated_images/019f8fb4-480c-7570-8781-2551429fe2a7/"
        "exec-32c64ff5-52ba-4803-9042-99fc25bafc8c.png"
    ),
    "resources-still-life.webp": Path(
        "/Users/abby/.codex/generated_images/019f8fb4-480c-7570-8781-2551429fe2a7/"
        "exec-fd88b53a-98f7-4148-b308-17d7e0a08582.png"
    ),
}


def contain(image: Image.Image, max_size: int) -> Image.Image:
    output = image.copy()
    output.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
    return output


def prepare_generated_images() -> None:
    for filename, source in GENERATED.items():
        image = Image.open(source).convert("RGB")
        if filename == "og-card.webp":
            target_ratio = 1200 / 630
            source_ratio = image.width / image.height
            if source_ratio > target_ratio:
                crop_width = round(image.height * target_ratio)
                left = (image.width - crop_width) // 2
                image = image.crop((left, 0, left + crop_width, image.height))
            else:
                crop_height = round(image.width / target_ratio)
                top = (image.height - crop_height) // 2
                image = image.crop((0, top, image.width, top + crop_height))
            image = image.resize((1200, 630), Image.Resampling.LANCZOS)
        else:
            image = contain(image, 1800)
        image.save(OUTPUT / filename, "WEBP", quality=82, method=6)


def transparent_symbol(source: Image.Image) -> Image.Image:
    rgba = source.convert("RGBA")
    pixels = []
    for red, green, blue, _ in rgba.getdata():
        distance_from_white = 255 - min(red, green, blue)
        alpha = max(0, min(255, (distance_from_white - 5) * 12))
        pixels.append((red, green, blue, alpha))
    rgba.putdata(pixels)
    bbox = rgba.getchannel("A").getbbox()
    if bbox:
        rgba = rgba.crop(bbox)
    return contain(rgba, 800)


def prepare_logo_assets() -> None:
    full = Image.open(BRAND / "arma-go-full.png").convert("RGB")
    symbol_source = Image.open(BRAND / "arma-go-symbol-source.png").convert("RGB")
    horizontal = Image.open(BRAND / "arma-go-horizontal-source.png").convert("RGBA")
    background = full.getpixel((0, 0))

    contain(full, 1000).save(OUTPUT / "arma-go-logo.png", "PNG", optimize=True)

    horizontal_bbox = horizontal.getchannel("A").getbbox()
    if not horizontal_bbox:
        raise RuntimeError("Could not locate the horizontal logo artwork.")
    horizontal = horizontal.crop(horizontal_bbox)
    horizontal.save(
        OUTPUT / "arma-go-logo-horizontal.png",
        "PNG",
        optimize=True,
    )

    symbol = transparent_symbol(symbol_source)
    symbol.save(OUTPUT / "arma-go-symbol.png", "PNG", optimize=True)

    mono = Image.new("RGBA", symbol.size, (255, 255, 255, 0))
    mono.putalpha(symbol.getchannel("A"))
    mono.save(OUTPUT / "arma-go-logo-white.png", "PNG", optimize=True)

    favicon = Image.new("RGB", (128, 128), background)
    favicon_symbol = contain(symbol, 92)
    favicon.alpha_composite(
        favicon_symbol,
        ((128 - favicon_symbol.width) // 2, (128 - favicon_symbol.height) // 2),
    ) if favicon.mode == "RGBA" else favicon.paste(
        favicon_symbol,
        ((128 - favicon_symbol.width) // 2, (128 - favicon_symbol.height) // 2),
        favicon_symbol,
    )
    favicon.save(OUTPUT / "favicon.png", "PNG", optimize=True)

    background_image = Image.new("RGB", full.size, background)
    difference = ImageChops.difference(full, background_image).convert("L")
    content_mask = difference.point(lambda value: 255 if value > 10 else 0)

    symbol_bbox = content_mask.crop((0, 100, full.width, 1050)).getbbox()
    lower = full.crop((0, 1000, full.width, 1400))
    white_mask = lower.convert("L").point(lambda value: 255 if value > 235 else 0)
    word_bbox = white_mask.getbbox()
    if not symbol_bbox or not word_bbox:
        raise RuntimeError("Could not locate the logo artwork.")

    symbol_bbox = (
        symbol_bbox[0],
        symbol_bbox[1] + 100,
        symbol_bbox[2],
        symbol_bbox[3] + 100,
    )
    word_bbox = (
        word_bbox[0],
        word_bbox[1] + 1000,
        word_bbox[2],
        word_bbox[3] + 1000,
    )
    symbol_lockup = full.crop(symbol_bbox)
    word_lockup = full.crop(word_bbox)
    symbol_lockup.thumbnail((250, 250), Image.Resampling.LANCZOS)
    word_lockup.thumbnail((760, 130), Image.Resampling.LANCZOS)

    compact = Image.new("RGB", (1100, 300), background)
    compact.paste(symbol_lockup, (24, (300 - symbol_lockup.height) // 2))
    compact.paste(word_lockup, (300, (300 - word_lockup.height) // 2))
    compact.save(OUTPUT / "arma-go-logo-compact.png", "PNG", optimize=True)


if __name__ == "__main__":
    OUTPUT.mkdir(parents=True, exist_ok=True)
    prepare_generated_images()
    prepare_logo_assets()
