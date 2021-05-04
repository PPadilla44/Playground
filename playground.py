from flask import Flask, render_template
app = Flask(__name__)
@app.route("/play")
def play():
    return render_template("index.html", page = "play")
@app.route("/play/<number>")
def play_mult(number):
    return render_template("index.html", page = "play_mult", number = int(number))
@app.route("/play/<number>/<color_pick>")
def num_and_color(number, color_pick):
    return render_template("index.html", page = "color", number = int(number), color_pick = str(color_pick))
if __name__ == "__main__":
    app.run(debug=True)