from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://sql9242941:pbc1ShuFGU@sql9.freemysqlhosting.net/sql9242941'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    comment = db.Column(db.String(1000))

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        print(request)
        print(request.headers)
        print(request.form)
        print(request.data)
        name = request.form['name']
        comment = request.form['comment']

        signature = Comments(name=name, comment=comment)
        db.session.add(signature)
        db.session.commit()
    mycomments = Comments.query.all()
    return render_template("index.html", comments=mycomments)


if __name__ == '__main__':
    app.run(debug = True)
