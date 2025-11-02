import typer

app = typer.Typer(help='Project managment CLI tool.')


@app.command()
def create(name: str, files: int = 3):
    typer.echo(f'Creating project {name} with files {files}')


@app.command()
def delete(name: str, all:bool = False):
    typer.echo(f'Deleting project "{name}" {"with all files" if all else ""}')

if __name__ == '__main__':
    app()