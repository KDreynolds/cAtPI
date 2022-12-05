import os
import psycopg2
import random
from dotenv import load_dotenv
from flask import Flask, send_file


app = Flask(__name__)

def get_kitty():
    """
    Return a random image from the ones in the static/ directory
    """
    img_dir = "./kitties"
    img_list = os.listdir(img_dir)
    img_path = os.path.join(img_dir, random.choice(img_list))
    return img_path


@app.route('/')
def myapp():
    """
    Returns a random image directly through send_file
    """
    image = get_kitty()
    return send_file(image, mimetype='image/png')