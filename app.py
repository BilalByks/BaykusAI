from flask import Flask, request, render_template_string

app = Flask(__name__)

hafiza = {
    "selam": "Selam 😄",
    "merhaba": "Merhaba 👋",
    "naber": "İyiyim, sen nasılsın?",
    "oyunlar": "Oyunlar: Valorant, GTA, FIFA, Minecraft 🎮"
}

html = """
<!doctype html>
<title>BaykusAI</title>
<h1>🦉 BaykusAI</h1>

<form method="POST">
  <input name="mesaj" placeholder="Bir şey yaz..." style="width:300px">
  <button type="submit">Gönder</button>
</form>

<p><b>Sen:</b> {{soru}}</p>
<p><b>BaykusAI:</b> {{cevap}}</p>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    soru = ""
    cevap = ""

    if request.method == "POST":
        soru = request.form["mesaj"].lower()

        if soru.startswith("öğret "):
            try:
                _, key, value = soru.split(" ", 2)
                hafiza[key] = value
                cevap = f"Tamam öğrendim 👍 ({key})"
            except:
                cevap = "Format: öğret kelime cevap"

        else:
            cevap = hafiza.get(soru, "Bunu bilmiyorum 😅 Bana 'öğret ...' ile öğretebilirsin")

    return render_template_string(html, soru=soru, cevap=cevap)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)