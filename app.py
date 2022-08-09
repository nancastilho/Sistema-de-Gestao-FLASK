import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'your secret key'


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        buscar = request.form['buscar']
        conn = get_db_connection()
        print(buscar)
        posts = conn.execute(
            "SELECT * FROM posts WHERE status=? or id=? or departamentos=? or title=?", (buscar, buscar, buscar, buscar,)).fetchall()
        conn.close()
        return render_template('index.html', posts=posts)
        
    
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()

    return render_template('index.html', posts=posts)


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        conclusao = request.form['conclusao']
        departamentos = request.form['departamentos']
        status = request.form['status']
        anexos = request.form['anexos']

        if not title:
            flash('É necessário ter um título!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content, conclusao, departamentos, status, anexos) VALUES (?, ?, ?, ?, ?, ?)',
                         (title, content, conclusao, departamentos, status, anexos))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        conclusao = request.form['conclusao']
        departamentos = request.form['departamentos']
        status = request.form['status']
        anexos = request.form['anexos']

        if not title:
            flash('É necessário ter um título!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?, conclusao = ?, departamentos = ?, status = ?, anexos = ?'
                         ' WHERE id = ?',
                         (title, content, conclusao, departamentos, status, anexos, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" deletado com sucesso'.format(post['title']))
    return redirect(url_for('index'))