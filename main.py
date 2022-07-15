from flask import Flask
from utils import get_all, get_by_pk, get_by_skill
app = Flask(__name__)

@app.route('/')
def head_page():
    return f"<pre>{get_all()}</pre>"

@app.route('/candidates/<int:pk>')
def candidates_by_pk_page(pk):
    by_pk_list, url_image = get_by_pk(pk)
    return f"<img src={url_image}></br><pre>{by_pk_list}</pre>"

@app.route('/skills/<skill_name>')
def candidates_by_skill_page(skill_name):
    by_skill_list = get_by_skill(skill_name)
    return f"<pre>{by_skill_list}</pre>"

app.run()