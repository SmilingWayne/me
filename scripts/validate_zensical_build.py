from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
DOCS = ROOT / "docs"


def require_file(relative_path: str) -> str:
    path = SITE / relative_path
    if not path.is_file():
        raise SystemExit(f"Missing generated file: {path}")
    return path.read_text(encoding="utf-8")


def require_text(content: str, expected: str, context: str) -> None:
    if expected not in content:
        raise SystemExit(f"Missing {expected!r} in {context}")


def main() -> None:
    index = require_file("index.html")
    deep_page = require_file("Philosophy/Foucault/Verite/index.html")
    tags_page = require_file("Website/tags/index.html")
    mermaid_page = require_file("Study/TextEdit/Markdown/Mkdocs_Tutorials1/index.html")
    math_page = require_file("Study/TextEdit/LaTeX/pieces/index.html")
    require_file("search.json")

    markdown_count = sum(1 for _ in DOCS.rglob("*.md"))
    html_count = sum(1 for _ in SITE.rglob("*.html"))
    if html_count < markdown_count:
        raise SystemExit(
            f"Generated HTML count {html_count} is below Markdown count {markdown_count}"
        )

    require_text(index, "data-md-color-scheme", "index.html")
    require_text(index, "stylesheets/extra.css", "index.html")
    require_text(index, "https://vercount.one/js", "index.html")
    require_text(index, "页面修改记录", "index.html")
    require_text(index, "页面源码", "index.html")
    require_text(deep_page, "页面修改记录", "deep page")
    require_text(tags_page, "Website/tags.md?plain=1", "tags page")
    require_text(mermaid_page, '<pre class="mermaid">', "Mermaid page")
    require_text(math_page, 'class="arithmatex"', "math page")
    require_text(math_page, 'class="admonition ', "admonition page")

    print(
        f"Validated {html_count} generated HTML files for "
        f"{markdown_count} Markdown sources."
    )


if __name__ == "__main__":
    main()
