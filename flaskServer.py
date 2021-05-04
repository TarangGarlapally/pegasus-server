# pip install syft,torch==1.7.1,flask

import syft as sy
import asyncio
import os
from flask import Flask, render_template, url_for

#original flask server

app = Flask(__name__)

#when the client lanches duet, implicitly a get request will be sent to the path '/join' invoking the below function
@app.route("/join")
def welcome():
    os.environ["SYFT_USE_EVENT_LOOP_THREAD"] = "0"
    loop = asyncio.new_event_loop()
    asyncio._set_running_loop(loop)
    duet = sy.join_duet(loopback=True)
    return "Hello"
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run()