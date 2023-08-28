from flask import Flask,render_template,request
app= Flask(__name__)
data={
    "saturday" :30 ,
    "sunday": 40 ,
    "monday": 35 ,
}
avg=0
week=["Saturday","sunday","monday","tuesday","wednesday","thursday","friday"]
# Home Page
@app.route("/",methods=["GET","POST"])
def start():
    return render_template("home.html",data=data)

@app.route("/add",methods=["GET","POST"])
def add():
    if request.method=="POST":
        day=request.form.get("name")
        temp=request.form.get("password")
        if day in data:
            return "sir day is in data please return and choose edit button"
        elif day not in week:
            return "Wrong day name "
        else:
            data[day]=temp
        return render_template("home.html",data=data)


    return render_template("add.html")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method=="POST":
        day=request.form.get("name")
        temp=request.form.get("password")
        if day in data:
            data[day]=temp
            return render_template("home.html",data=data)
        else:
            return "Error 404"


    return render_template("edit.html")







if __name__ == "__main__":
    app.run(debug=True)