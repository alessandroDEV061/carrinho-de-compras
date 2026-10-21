from flask import Flask, render_template, request

app = Flask(__name__)

lista_produtos = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        nome = request.form.get("nome")
        preco = request.form.get("preco")
        
        if nome and preco:
            novo_produto = {
                "nome": nome,
                "preco": float(preco)
            }
            lista_produtos.append(novo_produto)

    # Soma todos os preços presentes na lista de dicionários
    total = sum(item["preco"] for item in lista_produtos)

    return render_template("index.html", produtos=lista_produtos, total=total)

if __name__ == "__main__":
    app.run(debug=True)