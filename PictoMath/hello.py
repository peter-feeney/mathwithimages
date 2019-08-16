from flask import Flask, render_template
from PIL import Image
import numpy as np


app = Flask(__name__, static_url_path='/static')

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/hello")
def hello():
    return "Hello World!"



@app.route("/transpose")
def transpose():
    input_img = request.args.get("input")

    img_mat = np.asarray(input_img, dtype=np.uint8)
    img_mat = np.rot90(img_mat, k = -1)
    img = Image.fromarray(img_mat)

    return img

@app.route("/members")
def members():
    return "Members"

if __name__ == "__main__":
    app.run()