from bottle import run, route, get, post, request, redirect
import webbrowser, pyaudio, wave
import subprocess

@route('/init')
def init():
    file = open("data.txt", "w")
    file.write("100\r")
    file.close()

    redirect("/play-music?tempo=" + "100")


@route('/play-music')
def playMusic():
    tempo = int(request.query.tempo)

    dicMusic = {100:"https://open.spotify.com/track/0vFahN7YciXucZseX61eSa"}

    return subprocess.check_output(['music.exe', dicMusic[100] ], shell=True)

run(host='localhost', port=80, debug=True)

