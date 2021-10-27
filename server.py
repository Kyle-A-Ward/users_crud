from flask import Flask, render_template, redirect, request
from user import User
app = Flask(__name__)

@app.route('/')
def index():
    users = User.get_all()
    return render_template("create.html", all_users=users)
    
@app.route("/create_user", methods=["POST"])
def render_lists():
    data = {
        "firstname": request.form["firstname"],
        "lastname": request.form["lastname"],
        "email": request.form["email"]
    }
    user = User.save(data)
    return redirect("/read")

@app.route("/read")
def read():
    users = User.get_all()
    return render_template("read.html", all_users=users)

@app.route("/user/<int:id>")
def userinfo(id):
    #video 2hrs 30 mins
    data = {
        "id": id
    }
    user = User.get_user(data)
    return render_template("show.html", user=user)

@app.route("/edit/<int:id>")
def editinfo(id):
    data = {
        "id" : id
    }
    user = User.get_user(data)
    return render_template("edit.html", user=user)

@app.route("/edit_save/<int:id>", methods=["POST"])
def saveinfo(id):
    data = {
        "id" : id,
        "firstname": request.form["firstname"],
        "lastname": request.form["lastname"],
        "email": request.form["email"]
    }
    User.edit_user(data)
    return redirect("/read")

@app.route("/delete_user/<int:id>", methods=["POST"])
def deleteinfo(id):
    data = {
        "id" : id
    }
    user = User.delete_user(data)
    return redirect("/read")

if __name__ == "__main__":
    app.run(debug=True)