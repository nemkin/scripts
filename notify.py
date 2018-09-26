#/usr/bin/python3

from flask import Flask
from flask import request
from subprocess import Popen, PIPE

app = Flask(__name__)

@app.route("/")
def notify():
    msg = request.args.get('msg')

    rc = 0
    while rc == 0:
        p = Popen(['zenity', '--info', '--title=Ricsi', '--text='+msg], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate()
        rc = p.returncode

    p = Popen(['zenity', '--entry', '--title=Ricsi valasz', '--text='+msg], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    return output

if __name__ == "__main__":
    app.run(host='0.0.0.0')
