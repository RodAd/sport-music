from bottle import run, route, get, post, request, redirect
import webbrowser, pyaudio, wave

@route('/init')
def init():
    file = open("data.txt", "w")
    file.write("100\r")
    file.close()

    redirect("/play-music?tempo=" + "100")


@route('/play-music')
def playMusic():
    tempo = request.query.tempo

    # init chunk
    CHUNK = 1024

    # open wave file
    wf = wave.open('Electro-punk.wav', 'rb')

    # instantiate PyAudio (1)
    p = pyaudio.PyAudio()

    # open stream (2)
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # read data
    data = wf.readframes(CHUNK)

    print("I'm playing music!")
    # play stream (3)
    for i in range(200):
        stream.write(data)
        data = wf.readframes(CHUNK)

    # stop stream (4)
    stream.stop_stream()
    stream.close()

    # close PyAudio (5)
    p.terminate()
    print("Stop playing music")


# def process(path):
#     if path == "init":
#         return subprocess.check_output(['python', 'init.py', ], shell=True)
#     else:
#         return subprocess.check_output(['python', path + '.py'], shell=True)


run(host='localhost', port=8080, debug=True)

