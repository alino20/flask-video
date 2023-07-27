from flask import Flask
from os import listdir
import webvtt

app = Flask(__name__)

video_files = [
    f for f in listdir("static/videos") if f.endswith(".mkv") or f.endswith("mp4")
]

srt_files = [
    f for f in listdir("static/videos") if f.endswith("srt")
]

for f in srt_files:
    webvtt.from_srt("static/videos/"+f).save()

sub_files = [f for f in listdir("static/videos") if f.endswith(".vtt")]


@app.route("/")
def hello():
    html = ""
    html += '<video src="/static/videos/{}" controls>'.format(video_files[0])

    for sub in sub_files:
        html += '<track label="English" kind="subtitles" srclang="en" src="/static/videos/{}" default/>'.format(
            sub
        )
    html += "</video>"

    return html
