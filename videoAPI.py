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
    fims = {
        "titre" : "Pulp fiction" ,
        "annee" : 1994 ,
        "realisateur" : {"nom" : "Tanrantino" , "prenom" : "Quentin" } ,
        "acteurs" : [
            {"nom" : "Travolta" , "prenom" : "John" },
            {"nom" : "Thurman" , "prenom" : "Uma" },
            {"nom" : "Jackson" , "prenom" : "Samuel L." }
        ]
    },
    listFilms.append(fims)

    with open(f'{filename}', 'w') as f:
        json.dump(data,f, indent=4)
        
    return "<p>Films added!</p>"