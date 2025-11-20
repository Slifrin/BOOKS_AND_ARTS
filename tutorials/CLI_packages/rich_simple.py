from rich.console import Console
from rich.table import Table


console = Console()


def display_projects(projects):
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("ID", style="dim")
    table.add_column("Name")
    table.add_column("Status", justify="right")

    for p_id, name, status in projects:
        color = "gree" if status == "active" else "red"
        table.add_row(str(p_id), name, f'[{color}]{status}[/{color}]')

    console.print(table)


projects = [
    (1, "Web API", "active"),
    (2, "Database Migration", "inactive"),
    (3, "Frontend", "active"),
]


console.print("[bold]Project Management System[/bold]", justify="center")


if __name__ == "__main__":
    display_projects(projects)
