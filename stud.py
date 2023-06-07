from flask import Flask, render_template, request
from DBConnection import Db
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/add_stud')
def add_stud():
    return render_template('add_stud.html')

@app.route('/add_studpost', methods=['POST'])
def add_studpost():
    name = request.form['n1']
    dob = request.form['n2']
    gender = request.form['n3']
    email = request.form['n4']
    db = Db()
    qry = "INSERT INTO `stud`(`name`,`gender`,`email`,`dob`) VALUES('"+name+"','"+gender+"','"+email+"','"+dob+"')"
    res = db.insert(qry)
    return add_stud()



@app.route('/view_stud')
def view_stud():
    db = Db()
    qry = "select * from stud"
    res = db.select(qry)
    return render_template('view Studend.html',data=res)


@app.route('/add_mark/<id>')
def add_mark(id):
    db = Db()
    qry = "select * from stud where roll_no='"+str(id)+"'"
    res = db.selectOne(qry)
    return render_template('add_mark.html',data=res)


@app.route('/mark_post', methods=['POST'])
def mark_post():
    id = request.form['h1']
    mark = request.form['m1']
    db = Db()
    qry = "INSERT INTO `mark`(`stud_id`,`mark`) VALUES('"+str(id)+"','"+str(mark)+"')"
    res = db.insert(qry)
    return view_stud()



@app.route('/view_mark/<id>')
def view_mark(id):
    db = Db()
    qry = "SELECT * FROM mark INNER JOIN `stud` ON `stud`.`roll_no`=`mark`.`stud_id` WHERE `stud`.`roll_no`='"+str(id)+"'"
    res = db.selectOne(qry)
    return render_template('view_mark.html',data=res)


@app.route('/view_result')
def view_result():
    db = Db()
    qry = "SELECT * FROM mark INNER JOIN `stud` ON `stud`.`roll_no`=`mark`.`stud_id`"
    res = db.select(qry)

    return render_template('view result.html', data=res)

if __name__ == '__main__':
    app.run()
