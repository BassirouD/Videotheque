from flask import Flask
import os
import json

app = Flask(__name__)

@app.route("/api/createVideotheque/<filename>")
def create_videotheque(filename):
    items ={'proprietaire': {"nom": "Diallo", "prenom": "Bassirou"}, 'films': []}
    with open(f'{filename}', 'w') as f:
        json.dump(items, f, indent=4)
    # file = open(f'{filename}', 'w')
    # file.writelines(items)
    return "<p>File Created and writed!</p>"

@app.route("/api/deleteVideotheque/<filename>")
def delete_videotheque(filename):
    os.remove(filename)
    return "<p>File Deleted!</p>"


@app.route("/api/getData/<filename>")
def get_data(filename):
    with open(f'{filename}', 'r') as f:
        data=json.load(f)
        print('-------------------------------------------')
        print(data)
        print('-------------------------------------------')
        for i in data:
            print(i)
    return "<p>File loaded!</p>"


@app.route("/api/addFilms/<filename>")
def add_data(filename):
    with open(f'{filename}', 'r') as f:
        data=json.load(f)
        print(data['films'])
    
    listFilms=data['films']
    films = {
        "titre" : "Fast and furious" ,
        "annee" : 1994 ,
        "realisateur" : {"nom" : "Tanrantino" , "prenom" : "Quentin" } ,
        "acteurs" : [
            {"nom" : "Chadwick" , "prenom" : "Boseman" },
            {"nom" : "Thurman" , "prenom" : "Uma" },
            {"nom" : "Jackson" , "prenom" : "Samuel L." }
        ]
    },
    print(type(listFilms))
    print(type(films))
    listFilms+=films

    with open(f'{filename}', 'w') as f:
        json.dump(data, f, indent=4)
        
    return "<p>Films added!</p>"




@app.route("/api/foundMovie/<filename>/<mouvie>")
def found_data(filename, mouvie):
    with open(f'{filename}', 'r') as f:
        data=json.load(f)
        print('-------------------------------------------')
        for i in data['films']:
            if i['titre'] == mouvie:
                print(data['films'][0])
                return "<p>Movie founded!</p>"
            else:
                return "<p>Movie not founded!</p>"