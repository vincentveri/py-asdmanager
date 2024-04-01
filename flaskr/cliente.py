from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from sqlalchemy import update as upd

from flaskr import db
from flaskr.auth import login, login_required
from flaskr.models import Cliente


bp = Blueprint('cliente', __name__, url_prefix='/cliente')


@bp.route('/')
def index():
    clienti = db.session.execute(db.select(Cliente).order_by(Cliente.cognome)).scalars()
    return render_template("cliente/index.html", clienti=clienti)


@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        cognome = request.form['cognome']
        nome = request.form['nome']
        codice_fiscale = request.form['codice_fiscale']

        error = None

        if not cognome or not nome:
            error = 'Lastname and name are required'

        if error is None:
            cliente = Cliente(
                nome=nome,
                cognome=cognome,
                codice_fiscale=codice_fiscale,
            )
            db.session.add(cliente)
            db.session.commit()

    return render_template('cliente/create.html')


@bp.route('/<int:id>', methods=('GET', 'POST'))
@login_required
def update(id):
    cliente = db.get_or_404(Cliente, id)

    # Effettua refactor con
    # https://docs.sqlalchemy.org/en/20/tutorial/orm_data_manipulation.html
    if request.method == 'POST':
        cognome = request.form['cognome']
        nome = request.form['nome']
        codice_fiscale = request.form['codice_fiscale']

        error = None

        if not cognome or not nome:
            error = 'Lastname and name are required'
            flash(error)

        if error is None:

            db.session.execute(
                upd(Cliente),
                [
                    {"id": id, "cognome": cognome, "nome": nome, "codice_fiscale": codice_fiscale}
                ]
            )
            db.session.commit()

            flash("Cliente salvato", "success")
            return redirect(url_for('cliente.index'))

    return render_template('cliente/update.html', cliente=cliente)
