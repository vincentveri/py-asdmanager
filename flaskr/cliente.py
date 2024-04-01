from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

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


def get_cliente(id, check_author=True):
    post = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post



@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_cliente(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            flash("Messaggio salvato", "success")
            return redirect(url_for('invoice.index'))

    return render_template('invoice/update.html', post=post)
