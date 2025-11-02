import click


@click.group()
def cli():
    """Project managment CLI tool"""
    pass


@click.command()
@click.argument('name')
@click.option('--files', default=3, help='Number of files to create.')
def create(name, files):
    click.echo(f'Creating project "{name}" with {files} files')

@click.command()
@click.argument('name')
@click.option('--all', is_flag=True, help='Delete all ')
def delete(name, all):
    click.echo(f'Deleting project "{name}" {"with all files" if all else ''}')


if __name__ == '__main__':
    cli()