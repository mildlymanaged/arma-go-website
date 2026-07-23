"""Run lightweight, dependency-free QA against the generated Astro site."""

from __future__ import annotations

import argparse
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


EXPECTED_MAILTO = {
    "mailto:hello@armago.me?subject=Arma%20Go%20Enquiry",
    "mailto:hello@armago.me?subject=Work%20Abroad%20Enquiry",
    "mailto:hello@armago.me?subject=Study%20Abroad%20Enquiry",
    "mailto:partnerships@armago.me?subject=Employer%20or%20Partner%20Enquiry",
}

EXPECTED_ROUTES = (
    "/",
    "/work-abroad/",
    "/study-abroad/",
    "/employers-partners/",
    "/how-it-works/",
    "/resources/",
    "/about/",
    "/contact/",
    "/faq/",
    "/privacy-policy/",
    "/terms-and-conditions/",
    "/refund-cancellation-policy/",
)

RESTRICTED_TERM = "path" + "way"

FORBIDDEN_BRAND_NAMES = (
    "Arma Go Internationals",
    "ArmaGo Internationals",
    "Arma Go International",
)


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.refs: list[tuple[str, str]] = []
        self.mailto: list[str] = []
        self.images: list[dict[str, str]] = []
        self.h1_count = 0
        self.meta: list[dict[str, str]] = []

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        values = {key: value or "" for key, value in attrs}
        if tag == "a" and values.get("href", "").startswith("mailto:"):
            self.mailto.append(values["href"])
        elif tag == "a" and "href" in values:
            self.refs.append(("href", values["href"]))
        if tag in {"img", "script", "link"}:
            ref = values.get("src") or values.get("href")
            if ref:
                self.refs.append(("asset", ref))
        if tag == "img":
            self.images.append(values)
        if tag == "h1":
            self.h1_count += 1
        if tag == "meta":
            self.meta.append(values)


def target_exists(dist: Path, target: str, base_path: str) -> bool:
    parsed = urlparse(target)
    if parsed.scheme or target.startswith("#"):
        return True
    path = unquote(parsed.path)
    prefix = base_path.rstrip("/")
    if prefix and path.startswith(f"{prefix}/"):
        path = path[len(prefix) :]
    relative = path.lstrip("/")
    if not relative:
        return (dist / "index.html").exists()
    candidate = dist / relative
    if path.endswith("/"):
        candidate = candidate / "index.html"
    return candidate.exists()


def check_site(dist: Path, base_path: str) -> list[str]:
    errors: list[str] = []
    html_files = sorted(dist.rglob("*.html"))
    seen_mailto: set[str] = set()
    if not html_files:
        return [f"No HTML files found under {dist}."]

    for route in EXPECTED_ROUTES:
        route_path = route.strip("/")
        target = dist / "index.html" if not route_path else dist / route_path / "index.html"
        if not target.exists():
            errors.append(f"Missing expected route {route}.")

    for html_file in html_files:
        source = html_file.read_text(encoding="utf-8")
        parser = PageParser()
        parser.feed(source)
        label = html_file.relative_to(dist)

        if parser.h1_count != 1:
            errors.append(f"{label}: expected one h1, found {parser.h1_count}.")

        for attribute, ref in parser.refs:
            if not target_exists(dist, ref, base_path):
                errors.append(f"{label}: broken {attribute} reference {ref!r}.")

        for href in parser.mailto:
            seen_mailto.add(href)
            if href not in EXPECTED_MAILTO:
                errors.append(f"{label}: unexpected mail link {href!r}.")

        for image in parser.images:
            if not image.get("alt"):
                errors.append(f"{label}: image is missing alt text.")
            if not image.get("width") or not image.get("height"):
                errors.append(
                    f"{label}: image {image.get('src')!r} is missing dimensions."
                )

        lower_source = source.lower()
        if re.search(rf"\b{RESTRICTED_TERM}s?\b", lower_source):
            errors.append(f"{label}: contains restricted public terminology.")
        if "x-frame-options" in lower_source:
            errors.append(f"{label}: contains an iframe-blocking header directive.")
        if "frame-ancestors 'none'" in lower_source:
            errors.append(f"{label}: contains a frame-ancestors restriction.")
        for forbidden in FORBIDDEN_BRAND_NAMES:
            if forbidden in source:
                errors.append(f"{label}: contains forbidden brand name {forbidden!r}.")

    for href in sorted(EXPECTED_MAILTO - seen_mailto):
        errors.append(f"Required mail link is missing: {href!r}.")

    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dist", default="dist")
    parser.add_argument("--base", default="")
    args = parser.parse_args()

    errors = check_site(Path(args.dist).resolve(), args.base)
    if errors:
        print("\n".join(errors))
        raise SystemExit(1)
    print("Static QA passed: routes, internal links, images, mail links and iframe rules.")


if __name__ == "__main__":
    main()
