import typer
from typing import Optional
from time import sleep

app = typer.Typer()


@app.command()
def process(file: str, force: bool = False):
    if not force and not typer.confirm(f"Are you sure you want to process {file}?"):
        typer.echo("Operation canceled.")
        raise typer.Exit()

    with typer.progressbar(range(100)) as progress:
        for i in progress:
            sleep(0.05)


if __name__ == "__main__":
    app()
