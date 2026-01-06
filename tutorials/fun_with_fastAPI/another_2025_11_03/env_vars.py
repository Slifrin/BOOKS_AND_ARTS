import os

name = os.environ.get('MY_NAME', 'World')

print(f"Hello {name} from Python")
