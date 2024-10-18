from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'clave_secreta_12345'


usuarios = {
    'usuario1': '123',
    'usuario2': '456'
}

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasenia = request.form['contrasenia']
        
        if usuario in usuarios and usuarios[usuario] == contrasenia:
            session['usuario'] = usuario
            return redirect(url_for('inicio'))
        else:
            flash('Usuario o contraseña incorrectos')
    
    return render_template('login.html')

@app.route('/inicio')
def inicio():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('inicio.html', username=session['usuario'])

@app.route('/salir')
def salir():
    session.pop('usuario', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)