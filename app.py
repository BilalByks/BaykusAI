from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🦉 BaykusAI</h1>
    <h2>İlk web sitem çalışıyor!</h2>
    <p>Merhaba Bilal 😄</p>
    """

if __name__ == "__main__":
    app.run(debug=True)