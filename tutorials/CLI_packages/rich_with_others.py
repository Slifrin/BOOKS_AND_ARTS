import argparse
from rich.console import Console
from rich.progress import track
from rich.syntax import Syntax
from rich.panel import Panel
import time
import random

console = Console()


def process_file(filename):
    for _ in track(range(100), description=f'Processing {filename}...'):
        time.sleep(0.02)

    # Display file content with syntax highlighting
    code = f'def hello():\n    print("Processed {filename}")\n\nhello()'
    syntax = Syntax(code, 'python', theme='monokai', line_numbers=True)
    console.print(Panel(syntax, title=filename, border_style='green'))

def main() -> None:
    parser = argparse.ArgumentParser(description='File processor with rich output')
    parser.add_argument('files', nargs='+', help='Files to process')

    args = parser.parse_args()

    console.print("[bold blue]Starting file processing...[/bold blue]")
    
    for file in args.files:
        process_file(file)

    console.print("[bold green]All files processed successfully![/bold green]")

if __name__ == '__main__':
    main()