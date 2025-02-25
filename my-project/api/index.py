from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def index():
    title = os.getenv('PAGE_TITLE', 'Multiplication App')
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{{ title }}</title>
    </head>
    <body>
        <h1>{{ title }}</h1>
        <form>
            <label for="num1">Number 1:</label>
            <input type="number" id="num1"><br><br>
            <label for="num2">Number 2:</label>
            <input type="number" id="num2"><br><br>
            <button type="button" onclick="multiply()">Multiply</button>
        </form>
        <h2 id="result"></h2>
        <script>
            function multiply() {
                const num1 = document.getElementById('num1').value;
                const num2 = document.getElementById('num2').value;
                const result = num1 * num2;
                document.getElementById('result').innerText = "Result: " + result;
            }
        </script>
    </body>
    </html>
    """
    return render_template_string(html_template, title=title)

# Required for Vercel
def handler(event, context):
    return app(event, context)

# Run locally
if __name__ == "__main__":
    app.run(debug=True)
