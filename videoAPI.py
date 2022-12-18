from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)

@app.route("/api/createVideotheque", methods=['POST'])
def create_videotheque():
    try:
        filename=request.json['filename']
        prenomP=request.json['prenomP']
        nomP=request.json['nomP']
        items ={'proprietaire': {"nom": nomP, "prenom": prenomP}, 'films': []}
        with open(f'{filename}', 'w') as f:
            json.dump(items, f, indent=4)
        # file = open(f'{filename}', 'w')
        # file.writelines(items)
        return jsonify({'Sucess': 'File Created and writed!'})
    except Exception as e:
        return jsonify({'Error': 'Invalid request'})

@app.route("/api/deleteVideotheque", methods=['DELETE'])
def delete_videotheque():
    try:
        filename=request.json['filename']
        os.remove(filename)
        return "<p>File Deleted!</p>"
    except Exception as e:
        return jsonify({'Error': 'Invalid request'})


@app.route("/api/getAllMovies/<filename>", methods=['GET'])
def get_data(filename):
    with open(f'{filename}', 'r') as f:
        data=json.load(f)
        print('-------------------------------------------')
        print(data)
        print('-------------------------------------------')
        for i in data:
            print(i)
    return data


@app.route("/api/addFilms/<filename>", methods=['POST'])
def add_data(filename):
    try:
        titre=request.json['titre']
        annee=request.json['annee']
        nomR=request.json['nomR']
        prenomR=request.json['prenomR']
        acteurs=request.json['acteurs']
        with open(f'{filename}', 'r') as f:
            data=json.load(f)
            print(data['films'])
        
        listFilms=data['films']
        films = {
            "titre" : titre ,
            "annee" : annee ,
            "realisateur" : {"nom" : nomR, "prenom" : prenomR} ,
            "acteurs" : acteurs
        },
        listFilms+=films

        with open(f'{filename}', 'w') as f:
            json.dump(data, f, indent=4)
            
        return jsonify({'Sucess': 'Movie added'})
    except Exception as e:
        return jsonify({'Error': 'Invalid request'})



@app.route("/api/foundMovie/<filename>", methods=['GET'])
def found_movie(filename):
    try:
        mouvie=request.json['mouvie']
        with open(f'{filename}', 'r') as f:
            data=json.load(f)
            return [i for i in data['films'] if i['titre'] == mouvie][0]
    except Exception as e:
        return jsonify({'Error': 'Invalid request'})

        

@app.route("/api/deleteMovie/<filename>", methods=['DELETE'])
def delete_movie(filename):
    try:
        titre=request.json['titre']
        if titre!="":
            with open(f'{filename}', 'r') as f:
                data=json.load(f)
            f.close()
            listFilms=data['films']

            deletedict = [i for i in listFilms if not (i['titre'] == titre)]

            data['films']=deletedict

            print(deletedict)

            with open(f'{filename}', 'w') as f:
                json.dump(data, f, indent=4)

            return jsonify({'Success': 'Movie deleted'})
        else:
            return jsonify({'Error': 'Champ ne doit pas être vide'})
    except Exception as e:
        return jsonify({'Error': 'Invalid request'})

        