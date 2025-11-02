import sys
import time
import typer
from rich.console import Console
from rich.table import Table
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

app = typer.Typer()
console = Console()


@app.command()
def analyze(file: str, interactive: bool = False):
    with console.status(f'Analyzing {file}...', spinner='dots'):
        time.sleep(2)

    table = Table(title=f'Analysis Results: {file}')
    table.add_column('Metric')
    table.add_column('Value')
    table.add_row('Size', '1.2 MB')
    table.add_row('Line', '2,430')
    table.add_row('Functions', '143')
    console.print(table)

    if interactive:
        actions = ['export', 'clean', 'optimize', 'exit']
        completer = WordCompleter(actions)

        console.print("\n[bold]Interactive Mode[/bold]")
        while True:
            action = prompt('Action > ', completer=completer)
            if action == 'exit':
                break
            elif action in actions:
                console.print(f"Performing: [bold]{action}[/bold]")
            else:
                console.print("[red]Unknown action[/red]")


def main() -> None:
    print(f'Hello main from : {__file__} executed by {sys.executable}')


if __name__ == '__main__':
    app()