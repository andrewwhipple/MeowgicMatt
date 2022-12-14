import typer
from models import (
    CATEGORY_SUBCATEGORY_TREE,
    Channel,
    ITunesCategory,
    ITunesSubcategory,
    Owner,
)
from rich import print

app = typer.Typer()


def get_category_from_prompt(prompt_text: str = "Podcast category") -> ITunesCategory:
    category_prompt = typer.prompt(prompt_text)
    if not category_prompt:
        return None

    category_prompt = category_prompt.replace("&", "&amp;")

    try:
        return ITunesCategory(name=category_prompt)
    except:
        try:
            return ITunesSubcategory(name=category_prompt)
        except:
            print(
                "[bold red]Error:[/bold red] category prompt is not a valid category or subcategory"
            )
            return get_category_from_prompt(prompt_text=prompt_text)


def get_category_from_subcategory(subcategory: ITunesSubcategory):
    for category_name in CATEGORY_SUBCATEGORY_TREE.keys():
        if subcategory.name in CATEGORY_SUBCATEGORY_TREE[category_name]:
            return ITunesCategory(name=category_name, subcategories=[subcategory])


def format_category_list(
    category1: ITunesCategory or ITunesSubcategory,  # type: ignore
    category2: ITunesCategory or ITunesSubcategory or None,  # type: ignore
):
    if not category2 or category1 == category2:
        if isinstance(category1, ITunesCategory):
            # make it a category
            return [category1]
        else:
            # make it a subcategory
            main_category = get_category_from_subcategory(category1)
            return [main_category]

    main_category1 = category1
    main_category2 = category2

    if isinstance(category1, ITunesSubcategory):
        main_category1 = get_category_from_subcategory(category1)
    if isinstance(category2, ITunesSubcategory):
        main_category2 = get_category_from_subcategory(category2)

    if main_category1.name == main_category2.name:
        if main_category1.subcategories:
            main_category1.subcategories = (
                main_category1.subcategories + main_category2.subcategories
            )
        else:
            main_category1.subcategories = main_category2.subcategories
        return [main_category1]

    return [main_category1, main_category2]


def build_feed() -> Channel:
    title = typer.prompt("Podcast title")
    link = typer.prompt("Podcast link")
    language = typer.prompt("Podcast language (leave blank for en-us)") or "en-us"
    itunes_subtitle = typer.prompt("Podcast subtitle")
    itunes_author = typer.prompt("Podcast author")
    description = typer.prompt("Podcast description")
    itunes_summary = (
        typer.prompt("iTunes Summary (leave blank to re-use description)")
        or description
    )
    itunes_image = typer.prompt("Url for podcast logo image")
    copyright = typer.prompt("Podcast copyright notice")

    category1 = get_category_from_prompt()
    category2 = get_category_from_prompt("Podcast category 2 (optional)")

    category_list = format_category_list(category1, category2)

    itunes_owner_name = typer.prompt("iTunes owner name")
    itunes_owner_email = typer.prompt("iTunes owner email")

    itunes_explicit = typer.confirm("Explicit?")

    # Improve the error handling and re-prompting

    feed = Channel(
        title=title,
        link=link,
        language=language,
        itunes_subtitle=itunes_subtitle,
        itunes_author=itunes_author,
        description=description,
        itunes_summary=itunes_summary,
        itunes_image=itunes_image,
        copyright=copyright,
        itunes_owner=Owner(
            itunes_name=itunes_owner_name,
            itunes_email=itunes_owner_email,
        ),
        itunes_categories=category_list,
        itunes_explicit=itunes_explicit,
    )

    return feed


def edit_channel():
    pass


def create_item():
    pass


def edit_item():
    pass


def delete_item():
    pass


@app.command()
def create_feed(filename: str):
    """
    Notes: take the feed, save it as an XML file with the given filename
    """
    if not filename.endswith(".xml"):
        print(f"[bold red]Error:[/bold red] file name must end with .xml")
        raise typer.Exit()

    feed = build_feed()

    try:
        with open(filename, "w") as file:
            file.write(feed.to_xml())
    except:
        print(f"[bold red]Error:[/bold red] writing to file {filename}")


if __name__ == "__main__":
    app()
