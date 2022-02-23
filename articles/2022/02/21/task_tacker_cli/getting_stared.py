import typer

from rich.console import Console
from rich.table import Table

from todo_model import Todo
from db_handling import insert_todo, get_all_todos, delete_todo, update_todo, complete_todo

app = typer.Typer()

console = Console()

@app.command(short_help='adds an item')
def add(task: str, category: str):
    typer.echo(f"adding {task}, {category}")
    todo = Todo(task, category)
    insert_todo(todo)
    show()

@app.command()
def delete(position: int):
    typer.echo(f"deleting {position}")
    delete_todo(position - 1) # indexing in db starts from 0
    show()

@app.command()
def update(position: int, task: str = None, category: str = None):
    typer.echo(f"updating {position}")
    update_todo(position - 1, task, category)
    show()

@app.command()
def complete(postion: int):
    typer.echo(f"complete {postion}")
    complete_todo(postion - 1)
    show()

@app.command()
def show():
    # typer.echo(f"Todos")
    # tasks = [("My firs TOTO", "Study"), ("My second TODO", "Sports")]
    tasks = get_all_todos()

    console.print("[bold magenta]TODOS[/bold magenta]", "💻")

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("TODO", width=20)
    table.add_column("Category", min_width=12, justify="right")
    table.add_column("Done", min_width=12, justify="right")

    def get_category_color(category):
        COLORS = {'Learn': 'cyan', 'YouTube': 'red', 'Sports': 'cyan', 'Study': 'green'}
        if category in COLORS:
            return COLORS[category]
        return 'white'
    
    for idx, task in enumerate(tasks, start=1):
        c = get_category_color(task.category)
        status = task.status
        is_done_str = '✅' if status else '❌'
        table.add_row(str(idx), task.task, f'[{c}]{task.category}[/{c}]', is_done_str)
    console.print(table)


def main():
    print('Hello main')
    app()

if __name__ == '__main__':
    main()
