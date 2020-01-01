from flask import *
from bs4 import BeautifulSoup
import requests

stuff = []


def gethtml(link):
    url = requests.get(link)
    new = BeautifulSoup(url.content, 'html.parser')

    new2 = new.find(class_='cmsmasters_text')

    new3 = new2.find_all('a')
    for item in new3:
        stuff.append(item)

gethtml('https://jfs.brent.sch.uk/pause-for-thought-december-2019/')

gethtml('https://jfs.brent.sch.uk/pause-for-thought-november-2019/')

gethtml('https://jfs.brent.sch.uk/pause-for-thought-october-2019-2/')

gethtml('https://jfs.brent.sch.uk/pause-for-thought-september-2019/')

gethtml('https://jfs.brent.sch.uk/pause-for-thought-july-2019/')

gethtml('https://jfs.brent.sch.uk/pause-for-thought-may2019/')

gethtml('https://jfs.brent.sch.uk/pause-for-thought-apr2019/')

gethtml('https://jfs.brent.sch.uk/pause-for-thought-mar2019/')

gethtml('https://jfs.brent.sch.uk/pause-for-thought-feb2019/')

gethtml('https://jfs.brent.sch.uk/pause-for-thought-jan2019/')

gethtml('https://jfs.brent.sch.uk/pause-for-thought-dec2018/')

gethtml('https://jfs.brent.sch.uk/pause-for-thought-nov2018/')

gethtml('https://jfs.brent.sch.uk/pause-for-thought-oct2018/')

gethtml('https://jfs.brent.sch.uk/pause-for-thought-sept2018/')

searcher = stuff

newest = searcher[0].get_text()

app = Flask(__name__)

person = ''
thelink = ''
together = []

@app.route('/')
def home():
    global person, thelink, together
    person = ''
    thelink = ''
    together = []
    return render_template('home.html')

@app.route('/name', methods=['POST', 'GET'])
def name():
    global person, thelink, together
    person = ''
    thelink = ''
    together = []
    if request.method == 'POST':
        search = request.form['thing']
        print(search)
        billy = False
        search2 = search.split(' ')
        search3 = []
        for item in search2:
            item2 = item[0].upper() + item[1:].lower()
            search3.append(item2)
        search4 = ' '.join(search3)
        for link in searcher:
            steve = link.get_text().index(':')
            bob = link.get_text().index('(')
            if search4 in link.get_text()[steve:bob]:
                person = link.get_text()
                thelink = link['href']
                together.append(person)
                together.append(thelink)
                billy = True
        if not (billy):
            return redirect(url_for('error'))
        return redirect(url_for('answer'))
    else:
        return render_template('name.html')

@app.route('/number', methods=['POST', 'GET'])
def number():
    global person, thelink, together
    person = ''
    thelink = ''
    together = []
    if request.method == 'POST':
        search = request.form['thing']
        print(search)
        for link in searcher:
            try:
                int(search) + 1
            except:
                return redirect(url_for('error'))
            if search != '' and (int(search) > 169 or int(search) < 149) and int(search) <= int(newest[7:10]) and int(
                    search) >= 1:
                if len(search) == 3:
                    if search in link.get_text()[0:10] and link.get_text()[10] == ':':
                        person = link.get_text()
                        thelink = link['href']
                        together.append(person)
                        together.append(thelink)
                        break
                elif len(search) == 2:
                    if search in link.get_text()[0:9] and link.get_text()[9] == ':':
                        person = link.get_text()
                        thelink = link['href']
                        together.append(person)
                        together.append(thelink)
                        break
                elif len(search) == 1:
                    if search in link.get_text()[0:8] and link.get_text()[8] == ':':
                        person = link.get_text()
                        thelink = link['href']
                        together.append(person)
                        together.append(thelink)
                        break
            else:
                return redirect(url_for('error'))
        return redirect( url_for('answer'))
    else:
        return render_template('number.html')

@app.route('/answer')
def answer():
    global together
    return render_template('final.html', together=together)

@app.route('/error')
def error():
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)

