from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello_there():
    return "<p>Hello there</p>"



def main() -> None:
    print(f'Hello main from : {__file__}')
    app.run(debug=True)

if __name__ == '__main__':
    main()