"""
    https://www.youtube.com/watch?v=UcKkmwaRbsQ
"""
from pathlib import Path
from os import chdir

def check_settings_file():
    path = Path.cwd() / 'settings.yaml'
    print(path.exists())
    with path.open() as file:
        print(file.read())

    # or

    print(path.read_text())

def other_settings_operation():
    path = Path('settings.yaml')
    print(path)
    print(path.resolve())
    full_path = path.resolve()
    print(f"Parent: {full_path.parent}")
    print(f"Parent: {full_path.name}")
    print(f"Parent: {full_path.stem}")
    print(f"Parent: {full_path.suffix}")

    print(f"Is directory: {full_path.is_dir()}")
    print(f"Is file: {full_path.is_file()}")
 
def check_new_file():
    new_file = Path.cwd() / "new_file.txt"
    new_file.touch()
    new_file.write_text("Hello")
    # new_file.unlink()

def check_new_dir():
    new_dir = Path.cwd() / "new_dir"
    if not new_dir.exists():
        new_dir.mkdir()
    new_dir.mkdir(exist_ok=True)
    chdir(new_dir)
    print(f"Current working directory {Path.cwd()}")
    new_dir.rmdir()

def main() -> None:
    print(f'Hello main from : {__file__}')
    print(f"Current working directory {Path.cwd()}")
    print(f"Home directory: {Path.home()} ")

    path = Path("/usr/bin/python3")
    print(path.exists())
    path = Path("/usr") /"bin" /"python3"
    print(path.exists())

    check_settings_file()
    other_settings_operation()

    check_new_file()
    check_new_dir()

if __name__ == '__main__':
    main()