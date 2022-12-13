import rss
import typer

app = typer.Typer()
app.add_typer(rss.app, name="rss")


def main(name: str):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
