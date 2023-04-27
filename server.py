from flask import Flask, render_template,session, redirect

app = Flask(__name__)

app.secret_key = "riffdini"

@app.route('/')
def clientVisit():
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] += 1
    return render_template("index.html")


@app.route('/destroy_session')
def destroySession():
    session.pop("count", None)
    return redirect('/')


@app.route('/double_btn')
def doubleIncreament():
    session["count"] += 1
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port = 5001)