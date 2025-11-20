import os
import sys

from prompt_toolkit import PromptSession
from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory



def get_completer():
    return NestedCompleter.from_nested_dict({
        'show': {
            'projects': None,
            'tasks': None,
            'users': None,
        },
        'create': {
            'project': None,
            'task': None,
            'user': None,
        },
        'delete': {
            'project': None,
            'task': None,
            'user': None,
        },
        'help': None,
        'exit': None,
    })


def main() -> None:
    history_file = os.path.join(os.getcwd(), '.my_app-history')
    session = PromptSession(
        history=FileHistory(history_file),
        auto_suggest=AutoSuggestFromHistory(),
        completer=get_completer(),
        complete_while_typing=True,
    )

    while True:
        try:
            text = session.prompt(HTML('<ansigreen>myapp</ansigreen> > '))

            if text.strip() == 'exit':
                break
            elif text.strip() == 'help':
                print("Available commands:")
                print("  show [projects|tasks|users]")
                print("  create [project|task|user]")
                print("  delete [project|task|user]")
                print("  help - Display this help")
                print("  exit - Exit the application")
            elif text.startswith('show'):
                parts = text.split()
                if len(parts) > 1:
                    print(f'Showing {parts[1]}...')
                else:
                    print("Please specify what to show")

        except KeyboardInterrupt:
            continue
        except EOFError:
            break


if __name__ == '__main__':
    print(f'Hello main from : {__file__} executed by {sys.executable}')
    print('Welcome to MyApp CLI. Type "help" for commands.')
    main()
    print('Goodbye!')
