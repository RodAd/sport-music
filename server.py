from bottle import run, route, get, post, request, redirect
import webbrowser, pyaudio, wave
import subprocess


@route('/init')
def init():
    file = open("data.txt", "w")
    file.write("100\n6")
    file.close()

    redirect("/play-music?tempo=100&energy=6")


@route('/change-tempo')
def changeTempo():
    deltaTempo = int(request.query.deltaTempo)
    file = open("data.txt", "r")
    currentTempo = int(file.readline()[:-1])
    currentEnergy = int(file.readline())
    file.close()
    newTempo = currentTempo + deltaTempo
    file = open("data.txt", "w")
    file.write(str(newTempo) + "\n" + str(currentEnergy))
    file.close()

    redirect("/play-music?tempo=" + str(newTempo) + "&energy=" + str(currentEnergy))


@route('/change-energy')
def changeEnergy():
    deltaEnergy = int(request.query.deltaEnergy)
    file = open("data.txt", "r")
    currentTempo = int(file.readline()[:-1])
    currentEnergy = int(file.readline())
    file.close()
    newEnergy = currentEnergy + deltaEnergy
    file = open("data.txt", "w")
    file.write(str(currentTempo) + "\n" + str(newEnergy))
    file.close()

    redirect("/play-music?tempo=" + str(currentTempo) + "&energy=" + str(newEnergy))


@route('/play-music')
def playMusic():
    tempo = int(request.query.tempo)
    energy = int(request.query.energy)

    dicMusic = {(100,6):"https://open.spotify.com/track/4irvUT0wvFBq7hm1EwFg2O",
                (100,10):"https://open.spotify.com/track/4fCcieEzqWWc8DfeH6JOuy",
                (140,6):"https://open.spotify.com/track/4E9CSPZLNKqpkqsv8UMMuT",
                (140,10):"https://open.spotify.com/track/4Pf4iGABgMW0BA7fHhTbfa",
                (180,6):"https://open.spotify.com/track/2VfEcR59Czu8ii3u6kKeP8",
                (180,10):"https://open.spotify.com/track/4qPnE8jBZN3wmgGxspsOcP"
                }

    return subprocess.check_output(['music.exe', dicMusic[(tempo,energy)] ], shell=True)


@route('/stop')
def stop():
    return subprocess.check_output(['no-music.exe'], shell=True)


run(host='localhost', port=80, debug=True)

