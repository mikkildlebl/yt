from flask import Flask, render_template, request, url_for
import json

app = Flask(__name__)

recent_videos = []

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/', methods = ['POST']) 
def get_data(): 
    link = request.form['link']

    if request.method == 'POST': 
        #with open('data.txt', 'w') as f:
        #     f.write("\n" + str(link))
        #     f.close()
        pass

    recent_videos.append(link)
    print(recent_videos)
    items = len(recent_videos)
    if items > 19:
        print(items)
        
    return render_template("index.html", link=link, recent_videos=recent_videos) 