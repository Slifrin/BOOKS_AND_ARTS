from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.styles import Style
from pygments.lexers.python import PythonLexer



python_completer = WordCompleter([
    'print', 'def', 'class', 'import', 'if', 'else', 'elif', 'for', 
    'while', 'try', 'except', 'finally', 'with', 'return', 'yield'
])


style = Style.from_dict(
    {
        'completion-menu.completion': 'bg:#008888 #ffffff',
        'completion-menu.completion.current': 'bg:#00aaaa #000000',
    }
)


def main() -> None:
    while True:
        try:
            user_input = prompt(
                'Python> ',
                lexer=PygmentsLexer(PythonLexer),
                completer=python_completer,
                style=style,
                include_default_pygments_style=False,
            )

            if user_input.strip() == 'exit':
                break

            try:
                # result = eval(user_input)
                result = exec(user_input)
                print(f'Result: {result}')

            except Exception as err:
                print(f'Error: {err}')

        except KeyboardInterrupt:
            continue
        except EOFError:
            break

if __name__ == '__main__':
    print('Interactive python CLI (type "exit" to quit)')

    main()
    print('Goodbye!')