
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Armazenamento simples para clientes
clientes = []

@app.route('/')
def index():
    return render_template('index.html', clientes=clientes)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        idade = request.form.get('idade')
        objetivo = request.form.get('objetivo')
        # Adiciona o novo cliente à lista
        clientes.append({'nome': nome, 'idade': idade, 'objetivo': objetivo})
        return redirect(url_for('index'))
    return render_template('cadastro.html')

@app.route('/prescricao/<int:index>')
def prescricao(index):
    cliente = clientes[index]
    return render_template('prescricao.html', cliente=cliente)

if __name__ == '__main__':
    app.run(debug=True)

