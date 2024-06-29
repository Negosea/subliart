from flask import Flask, render_template, request, redirect, url_for # type: ignore

app = Flask(__name__)

# Dados simulados para produtos
products = [
    {'id': 1, 'name': 'Caneca Personalizada 1', 'price': 19.99, 'description': 'Uma bela caneca personalizada.', 'image': 'caneca1.jpg'},
    {'id': 2, 'name': 'Caneca Personalizada 2', 'price': 21.99, 'description': 'Outra bela caneca personalizada.', 'image': 'caneca2.jpg'},
]

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html', products=products)

# Rota para a página do produto
@app.route('/product/<int:product_id>')
def product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    return render_template('product.html', product=product)

# Rota para o carrinho
@app.route('/cart')
def cart():
    return render_template('cart.html')

if __name__ == '__main__':
    app.run(debug=True)
