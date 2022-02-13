""" flask_example.py
    Required packages:
    - flask
    - folium
    Usage:
    Start the flask server by running:
        $ python flask_example.py
    And then head to http://127.0.0.1:5000/ in your browser to see the map displayed
"""
import os
from flask import Flask
import folium
import requests
import json
from Station_VLille import Station_VLille
app = Flask(__name__)
@app.route('/')
def index():
    path="https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&q=&facet=libelle&facet=nom&facet=commune&facet=etat&facet=type&facet=etatconnexion&rows=500"
    rep=requests.get(path,verify=False)  # Appel API temps réel de la MEL pour les stations V'Lille
    assert rep.status_code == 200 , rep.status_code
    re=json.loads(rep.content)
    stations=[] # la listes de toutes les stations V'Lille
    for i in range(len(re["records"])):
        stations.append(Station_VLille(re["records"][i]))
    loc=[50.65, 3.07] # centre de la carte
    map = folium.Map(location=loc,zoom_start=14) # création de la carte
    for station in stations:  # markers des stations V'Lille
        folium.Marker(station.geo,popup=station.pop(),icon=folium.Icon(color=station.color_marker)).add_to(map)
    folium.Marker([50.687,3.075],popup="Aérodrome LFQQ").add_to(map)  # marker de aérodrome Lille-Marcq
    map.save("map.html")  # sauvegarde du fichier html contenant la carte
    return map._repr_html_() # affichage de la carte par Flask
if __name__=='__main__':
    app.run(debug=True,host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT',80))) # lancement du serveur Flask