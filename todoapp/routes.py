import os
from flask import render_template, url_for, flash, redirect, request
from todoapp import app, db
from todoapp.models import Todo


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    tasks = Todo.query.filter_by(complete=False)
    return render_template('home.html', title='Home', tasks=tasks)


@app.route("/task/<int:id>/completed", methods=['POST'])
def task_completed(id):
    task = Todo.query.get_or_404(id)
    task.complete = True
    db.session.add(Todo)
    db.session.commit()
    flash('You Completed The Task', 'success')
    return redirect(url_for('completed'))


@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        flash('Your Task is deleted', 'success')
        return redirect(url_for('home'))

    except:
        return 'Error'


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            flash('Your Task is edited', 'success')
            return redirect(url_for('home'))
        except:
            return 'Error'

    else:
        return render_template('update.html', task=task)














