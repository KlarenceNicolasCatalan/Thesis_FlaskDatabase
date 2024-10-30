from flask import Flask, jsonify, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os
import json
from flask import (Flask, send_file, url_for, jsonify, render_template)

#CNN imports
import cv2
import numpy as np
from matplotlib import pyplot as plt
import shutil
from matplotlib.pyplot import figure
import librosa
import numpy
import skimage.io
import tensorflow as tf
from flask import Flask
from flask import render_template
from flask import request
import sqlite3
from datetime import datetime
import pandas as pd

app = Flask(__name__)
@app.route("/")
def home():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT rowid, * FROM bird")

    rows_list = cur.fetchall()
    con.close()

    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT EnglishName, COUNT(*) FROM bird GROUP BY EnglishName")

    rows_species = cur.fetchall()

    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Asian_Glossy_Starling'")
    Asian_Glossy_Starling = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Barn_Swallow'")
    Barn_Swallow = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Black-Crowned_Night_Heron'")
    BlackCrowned_Night_Heron = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Black-headed_Gull'")
    Blackheaded_Gull = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Black-Tailed_Godwit'")
    BlackTailed_Godwit = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Black-Winged_Stilt'")
    BlackWinged_Stilt = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Blue-tailed_Bee-eater'")
    Bluetailed_Beeeater = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Clamorous_Reed_Warbler'")
    Clamorous_Reed_Warbler = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Common_Greenshank'")
    Common_Greenshank = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Common_Kingfisher'")
    Common_Kingfisher = cur.fetchone()[0]

    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Common_Pochard'")
    Common_Pochard = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Common_Redshank'")
    Common_Redshank = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Common_Sandpiper'")
    Common_Sandpiper = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Common_Snipe'")
    Common_Snipe = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Common_Tern'")
    Common_Tern = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Eastern_Yellow_Wagtail'")
    Eastern_Yellow_Wagtail = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Eurasian_Coot'")
    Eurasian_Coot = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Eurasian_Moorhen'")
    Eurasian_Moorhen = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Eurasian_Tree_Sparrow'")
    Eurasian_Tree_Sparrow = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Eurasian_Wigeon'")
    Eurasian_Wigeon = cur.fetchone()[0]

    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Gadwall'")
    Gadwall = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Garganey'")
    Garganey = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Golden-headed_Cristicola'")
    Goldenheaded_Cristicola = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Gray_Heron'")
    Gray_Heron = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Great_Egret'")
    Great_Egret = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Greater_White-fronted_Goose'")
    Greater_Whitefronted_Goose = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Kentish_Plover'")
    Kentish_Plover = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Large-billed_Crow'")
    Largebilled_Crow = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Lesser_Coucal'")
    Lesser_Coucal = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Little_Egret'")
    Little_Egret = cur.fetchone()[0]

    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Little_Grebe'")
    Little_Grebe = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Little_Ringed_Plover'")
    Little_Ringed_Plover = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Little_Tern'")
    Little_Tern = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Marsh_Sandpiper'")
    Marsh_Sandpiper = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Northern_Pintail'")
    Northern_Pintail = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Northern_Shoveler'")
    Northern_Shoveler = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Oriental_Reed_Warbler'")
    Oriental_Reed_Warbler = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Oriental_Skylark'")
    Oriental_Skylark = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Pacific_Golden-Plover'")
    Pacific_GoldenPlover = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Paddyfield_Pipit'")
    Paddyfield_Pipit = cur.fetchone()[0]

    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Philippine_Pied-Fantail'")
    Philippine_PiedFantail = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Purple_Heron'")
    Purple_Heron = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Rock_Pigeon'")
    Rock_Pigeon = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Scaly-breasted_Munia'")
    Scalybreasted_Munia = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Spotted_Dove'")
    Spotted_Dove = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Striated_Grassbird'")
    Striated_Grassbird = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Striated_Heron'")
    Striated_Heron = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Swinhoe_s_Snipe'")
    Swinhoe_s_Snipe = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Tawny_Grassbird'")
    Tawny_Grassbird = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Tufted_Duck'")
    Tufted_Duck = cur.fetchone()[0]

    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Watercock'")
    Watercock = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Whiskered_Tern'")
    Whiskered_Tern = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'White-breasted_Waterhen'")
    Whitebreasted_Waterhen = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'White-shouldered_Starling'")
    Whiteshouldered_Starling = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'White-winged_Tern'")
    Whitewinged_Tern = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Wood_Sandpiper'")
    Wood_Sandpiper = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Yellow-vented_Bulbul'")
    Yellowvented_Bulbul = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Zebra_Dove'")
    Zebra_Dove = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where EnglishName = 'Zitting_Cisticola'")
    Zitting_Cisticola = cur.fetchone()[0]

    data_species = {'EnglishName' : 'Count', 'Asian_Glossy_Starling' : Asian_Glossy_Starling, 'Barn_Swallow' : Barn_Swallow, 'Black-Crowned_Night_Heron' : BlackCrowned_Night_Heron,
            'Black-headed_Gull' : Blackheaded_Gull, 'Black-Tailed_Godwit' : BlackTailed_Godwit, 'Black-Winged_Stilt' : BlackWinged_Stilt,
            'Blue-tailed_Bee-eater' : Bluetailed_Beeeater, 'Clamorous_Reed_Warbler' : Clamorous_Reed_Warbler, 'Common_Greenshank' : Common_Greenshank,
            'Common_Kingfisher' : Common_Kingfisher, 'Common_Pochard' : Common_Pochard, 'Common_Redshank' : Common_Redshank, 'Common_Sandpiper' : Common_Sandpiper,
            'Common_Snipe' : Common_Snipe, 'Common_Tern' : Common_Tern, 'Eastern_Yellow_Wagtail' : Eastern_Yellow_Wagtail, 'Eurasian_Coot' : Eurasian_Coot,
            'Eurasian_Moorhen' : Eurasian_Moorhen, 'Eurasian_Tree_Sparrow' : Eurasian_Tree_Sparrow, 'Eurasian_Wigeon' : Eurasian_Wigeon,
            'Gadwall' : Gadwall, 'Garganey' : Garganey, 'Golden-headed_Cristicola' : Goldenheaded_Cristicola, 'Gray_Heron' : Gray_Heron, 'Great_Egret' : Great_Egret,
            'Greater_White-fronted_Goose' : Greater_Whitefronted_Goose, 'Kentish_Plover' : Kentish_Plover, 'Large-billed_Crow' : Largebilled_Crow,
            'Lesser_Coucal' : Lesser_Coucal, 'Little_Egret' : Little_Egret,
            'Little_Grebe' : Little_Grebe, 'Little_Ringed_Plover' : Little_Ringed_Plover, 'Little_Tern' : Little_Tern, 'Marsh_Sandpiper' : Marsh_Sandpiper,
            'Northern_Pintail' : Northern_Pintail, 'Northern_Shoveler' : Northern_Shoveler, 'Oriental_Reed_Warbler' : Oriental_Reed_Warbler,
            'Oriental_Skylark' : Oriental_Skylark, 'Pacific_Golden-Plover' : Pacific_GoldenPlover, 'Paddyfield_Pipit' : Paddyfield_Pipit,
            'Philippine_Pied-Fantail' : Philippine_PiedFantail, 'Purple_Heron' : Purple_Heron, 'Rock_Pigeon' : Rock_Pigeon, 'Scaly-breasted_Munia' : Scalybreasted_Munia,
            'Spotted_Dove' : Spotted_Dove, 'Striated_Grassbird' : Striated_Grassbird, 'Striated_Heron' : Striated_Heron, 'Swinhoe_s_Snipe' : Swinhoe_s_Snipe,
            'Tawny_Grassbird' : Tawny_Grassbird, 'Tufted_Duck' : Tufted_Duck,
            'Watercock' : Watercock, 'Whiskered_Tern' : Whiskered_Tern, 'White-breasted_Waterhen' : Whitebreasted_Waterhen, 'White-shouldered_Starling' : Whiteshouldered_Starling,
            'White-winged_Tern' : Whitewinged_Tern, 'Wood_Sandpiper' : Wood_Sandpiper, 'Yellow-vented_Bulbul' : Yellowvented_Bulbul, 'Zebra_Dove' : Zebra_Dove, 'Zitting_Cisticola' : Zitting_Cisticola}

    con.close()

    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT Class, COUNT(*) FROM bird GROUP BY Class")

    rows_class = cur.fetchall()

    cur.execute("SELECT  COUNT(*) FROM bird where Class = 'ardeidae'")
    ardeidae = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where Class = 'anatidae'")
    anatidae = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where Class = 'columbidae'")
    columbidae = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where Class = 'sturnidae'")
    sturnidae = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where Class = 'hirundinidae'")
    hirundinidae = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where Class = 'laridae'")
    laridae = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where Class = 'scolopacidae'")
    scolopacidae = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where Class = 'recurvirostridae'")
    recurvirostridae = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where Class = 'meropidae'")
    meropidae = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where Class = 'acrocephalidae'")
    acrocephalidae = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where Class = 'alcedinidae'")
    alcedinidae = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where Class = 'motacillidae'")
    motacillidae = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where Class = 'rallidae'")
    rallidae = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where Class = 'nectariniidae'")
    nectariniidae = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where Class = 'cisticolidae'")
    cisticolidae = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where Class = 'charadriidae'")
    charadriidae = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where Class = 'corvidae'")
    corvidae = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where Class = 'cuculidae'")
    cuculidae = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where Class = 'podicipedidae'")
    podicipedidae = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where Class = 'alaudidae'")
    alaudidae = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where Class = 'rhipiduridae'")
    rhipiduridae = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where Class = 'estrildidae'")
    estrildidae = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where Class = 'locustellidae'")
    locustellidae = cur.fetchone()[0]
    cur.execute("SELECT  COUNT(*) FROM bird where Class = 'dicaeidae'")
    dicaeidae = cur.fetchone()[0]

    data_class = {'Class' : 'Count', 'Anatidae' : anatidae, 'Ardeidae' : ardeidae, 'Columbidae' : columbidae, 'Sturnidae' : sturnidae,
            'Hirundinidae' : hirundinidae, 'Laridae' : laridae, 'Scolopacidae' : scolopacidae, 'Recurvirostridae' : recurvirostridae,
            'Meropidae' : meropidae, 'Acrocephalidae' : acrocephalidae, 'Alcedinidae' : alcedinidae, 'Motacillidae' : motacillidae,
            'Rallidae' : rallidae, 'Nectariniidae' : nectariniidae, 'Cisticolidae' : cisticolidae, 'Charadriidae' : charadriidae,
            'Corvidae' : corvidae, 'Podicipedidae' : podicipedidae, 'Cuculidae' : cuculidae, 'Alaudidae' : alaudidae,
            'Rhipiduridae' : rhipiduridae, 'Estrildidae' : estrildidae, 'Locustellidae' : locustellidae, 'Dicaeidae' : dicaeidae}

    con.close()

    return render_template("home.html",rows_list=rows_list,rows_species=rows_species,data_species=data_species,rows_class=rows_class,data_class=data_class )

@app.route("/export", methods=['POST','GET'])
def export():
    conn = sqlite3.connect("database.db", isolation_level=None,
                       detect_types=sqlite3.PARSE_COLNAMES)
    db_df = pd.read_sql_query("SELECT * FROM bird", conn)
    _time = datetime.date
    timeprint = str(_time)
    _output = 'database_' + timeprint +'.csv'
    db_df.to_csv("database_exported.csv", index=False)

    path = 'database_exported.csv'
    return send_file(path, as_attachment=True)

    #return render_template('result.html',msg="Successfully exported the database! Check your Flask app's root folder.")

@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if(request.method == "POST"):
        soundFile = request.files['image']
        longitude = request.form['1']
        latitude = request.form['2']
        authStatus = request.form['auth']
        filename = secure_filename(soundFile.filename)
        soundFile.save(filename)
        print("HI")
        prediction_value = spectrogramMaking(filename)
        class_name, scientific_name = determine_classandscientific(prediction_value)
        if (authStatus == "Verified" and prediction_value !="Unknown"):
            try:
                with sqlite3.connect('database.db') as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO bird (EnglishName, ScientificName, Class, Time, longitude, latitude) VALUES (?,?,?,?,?,?)",(prediction_value, scientific_name, class_name, datetime.now(), longitude, latitude))

                    con.commit()
            except:
                con.rollback()

            finally:
                con.close()
            os.remove(filename)
            return jsonify({'message': prediction_value})
        else:
            os.remove(filename)
            return jsonify({'message': prediction_value})
    else:
        return jsonify({'message': prediction_value})

    #modelPrediction()

@app.route('/auth', methods=['POST', 'GET'])
#methods=['POST', 'GET']
def auth():
    if(request.method == "POST"):
        user = request.form['user']
        password = request.form['pass']
        con = sqlite3.connect('database.db')
        #con = con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("SELECT Username FROM users WHERE Username = ? AND Password = ? ", (user,password))
        con.commit()
        if cur.fetchall():
            msg = "Verified"
        else:
            msg = "Not Verified"

        con.close()
        return jsonify({'message': msg})
    else:
        return "nope"

#---------------------------------------------------------------------------------------
def determine_classandscientific(_value):
    anatidae = ["Common_Pochard", "Eurasian_Wigeon","Gadwall","Garganey","Greater_White-fronted_Goose", "Northern_Pintail",
                "Northern_Shoveler", "Tufted_Duck",]
    sturnidae = ["Asian_Glossy_Starling","White-shouldered_Starling",]
    hirundinidae = ["Barn_Swallow",]
    ardeidae = ["Black-Crowned_Night_Heron","Gray_Heron","Great_Egret","Little_Egret","Purple_Heron","Striated_Heron",]
    laridae = ["Black-headed_Gull","Common_Tern","Little_Tern","Whiskered_Tern","White-winged_Tern",]
    scolopacidae = ["Black-Tailed_Godwit", "Common_Greenshank","Common_Redshank","Common_Sandpiper","Common_Snipe","Marsh_Sandpiper",
                    "Swinhoe_s_Snipe","Wood_Sandpiper",]
    recurvirostridae = ["Black-Winged_Stilt",]
    meropidae = ["Blue-tailed_Bee-eater",]
    acrocephalidae = ["Clamorous_Reed_Warbler","Oriental_Reed_Warbler",]
    alcedinidae = ["Common_Kingfisher",]
    motacillidae = ["Eastern_Yellow_Wagtail","Paddyfield_Pipit",]
    rallidae = ["Eurasian_Coot","Eurasian_Moorhen","Watercock","White-breasted_Waterhen",]
    nectariniidae = ["Eurasian_Tree_Sparrow",]
    cisticolidae = ["Golden-headed_Cristicola","Zitting_Cisticola"]
    charadriidae = ["Kentish_Plover","Little_Ringed_Plover","Pacific_Golden-Plover",]
    corvidae = ["Large-billed_Crow",]
    cuculidae = ["Lesser_Coucal",]
    podicipedidae = ["Little_Grebe",]
    alaudidae = ["Oriental_Skylark",]
    rhipiduridae = ["Philippine_Pied-Fantail",]
    columbidae = ["Rock_Pigeon","Spotted_Dove","Zebra_Dove",]
    estrildidae = ["Scaly-breasted_Munia",]
    locustellidae = ["Striated_Grassbird","Tawny_Grassbird",]
    dicaeidae = ["Yellow-vented_Bulbul",]

    class_name = ""
    scientific_name = ""

    if (_value in anatidae):
        class_name = "anatidae"
    elif (_value in sturnidae):
        class_name = "sturnidae"
    elif (_value in hirundinidae):
        class_name = "hirundinidae"
    elif (_value in ardeidae):
        class_name = "ardeidae"
    elif (_value in laridae):
        class_name = "laridae"
    elif (_value in scolopacidae):
        class_name = "scolopacidae"
    elif (_value in recurvirostridae):
        class_name = "recurvirostridae"
    elif (_value in meropidae):
        class_name = "meropidae"
    elif (_value in acrocephalidae):
        class_name = "acrocephalidae"
    elif (_value in alcedinidae):
        class_name = "alcedinidae"
    elif (_value in motacillidae):
        class_name = "motacillidae"
    elif (_value in rallidae):
        class_name = "rallidae"
    elif (_value in nectariniidae):
        class_name = "nectariniidae"
    elif (_value in cisticolidae):
        class_name = "cisticolidae"
    elif (_value in charadriidae):
        class_name = "charadriidae"
    elif (_value in corvidae):
        class_name = "corvidae"
    elif (_value in cuculidae):
        class_name = "cuculidae"
    elif (_value in podicipedidae):
        class_name = "podicipedidae"
    elif (_value in alaudidae):
        class_name = "alaudidae"
    elif (_value in rhipiduridae):
        class_name = "rhipiduridae"
    elif (_value in columbidae):
        class_name = "columbidae"
    elif (_value in estrildidae):
        class_name = "estrildidae"
    elif (_value in locustellidae):
        class_name = "locustellidae"
    elif (_value in dicaeidae):
        class_name = "dicaeidae"

    if (_value == "Asian_Glossy_Starling"):
        scientific_name = "Aplonis panayensis"
    elif (_value == "Barn_Swallow"):
        scientific_name = "Hirundo rustica"
    elif (_value == "Black-Crowned_Night_Heron"):
        scientific_name = "Nycticorax nycticorax"
    elif (_value == "Black-headed_Gull"):
        scientific_name = "Chroicocephalus ridibundus"
    elif (_value == "Black-Tailed_Godwit"):
        scientific_name = "Limosa limosa"
    elif (_value == "Black-Winged_Stilt"):
        scientific_name = "Himantopus himantopus"
    elif (_value == "Blue-tailed_Bee-eater"):
        scientific_name = "Merops philippinus"
    elif (_value == "Clamorous_Reed_Warbler"):
        scientific_name = "Acrocephalus stentoreus"
    elif (_value == "Common_Greenshank"):
        scientific_name = "Tringa nebularia"
    elif (_value == "Common_Kingfisher"):
        scientific_name = "Alcedo atthis"
    elif (_value == "Common_Pochard"):
        scientific_name = "Aythya ferina"
    elif (_value == "Common_Redshank"):
        scientific_name = "Tringa totanus"
    elif (_value == "Common_Sandpiper"):
        scientific_name = "Actitis hypoleucos"
    elif (_value == "Common_Snipe"):
        scientific_name = "Gallinago gallinago"
    elif (_value == "Common_Tern"):
        scientific_name = "Sterna hirundo"
    elif (_value == "Eastern_Yellow_Wagtail"):
        scientific_name = "Motacilla tschutschensis"
    elif (_value == "Eurasian_Coot"):
        scientific_name = "Fulica atra"
    elif (_value == "Eurasian_Moorhen"):
        scientific_name = "Gallinula chloropus"
    elif (_value == "Eurasian_Tree_Sparrow"):
        scientific_name = "Passer montanus"
    elif (_value == "Eurasian_Wigeon"):
        scientific_name = "Mareca penelope"
    elif (_value == "Gadwall"):
        scientific_name = "Mareca strepera"
    elif (_value == "Garganey"):
        scientific_name = "Spatula querquedula"
    elif (_value == "Golden-headed_Cristicola"):
        scientific_name = "Cisticola exilis"
    elif (_value == "Gray_Heron"):
        scientific_name = "Ardea cinerea"
    elif (_value == "Great_Egret"):
        scientific_name = "Ardea alba"
    elif (_value == "Greater_White-fronted_Goose"):
        scientific_name = "Anser albifrons"
    elif (_value == "Kentish_Plover"):
        scientific_name = "Charadrius alexandrinus"
    elif (_value == "Large-billed_Crow"):
        scientific_name = "Corvus macrorhynchos"
    elif (_value == "Lesser_Coucal"):
        scientific_name = "Centropus bengalensis"
    elif (_value == "Little_Egret"):
        scientific_name = "Egretta garzetta"
    elif (_value == "Little_Grebe"):
        scientific_name = "Tachybaptus ruficollis"
    elif (_value == "Little_Ringed_Plover"):
        scientific_name = "Charadrius dubius"
    elif (_value == "Little_Tern"):
        scientific_name = "Sternula albifrons"
    elif (_value == "Marsh_Sandpiper"):
        scientific_name = "Tringa stagnatilis"
    elif (_value == "Northern_Pintail"):
        scientific_name = "Anas acuta"
    elif (_value == "Northern_Shoveler"):
        scientific_name = "Spatula clypeata"
    elif (_value == "Oriental_Reed_Warbler"):
        scientific_name = "Acrocephalus orientalis"
    elif (_value == "Oriental_Skylark"):
        scientific_name = "Alauda gulgula"
    elif (_value == "Pacific_Golden-Plover"):
        scientific_name = "Pluvialis fulva"
    elif (_value == "Paddyfield_Pipit"):
        scientific_name = "Anthus rufulus"
    elif (_value == "Philippine_Pied-Fantail"):
        scientific_name = "Rhipidura nigritorquis"
    elif (_value == "Purple_Heron"):
        scientific_name = "Ardea purpurea"
    elif (_value == "Rock_Pigeon"):
        scientific_name = "Columba livia"
    elif (_value == "Scaly-breasted_Munia"):
        scientific_name = "Lonchura punctulata"
    elif (_value == "Spotted_Dove"):
        scientific_name = "Spilopelia chinensis"
    elif (_value == "Striated_Grassbird"):
        scientific_name = "Megalurus palustris"
    elif (_value == "Striated_Heron"):
        scientific_name = "Butorides striata"
    elif (_value == "Swinhoe_s_Snipe"):
        scientific_name = "Gallinago megala"
    elif (_value == "Tawny_Grassbird"):
        scientific_name = "Megalurus timoriensis"
    elif (_value == "Tufted_Duck"):
        scientific_name = "Aythya fuligula"
    elif (_value == "Watercock"):
        scientific_name = "Gallicrex cinerea"
    elif (_value == "Whiskered_Tern"):
        scientific_name = "Chlidonias hybrida"
    elif (_value == "White-breasted_Waterhen"):
        scientific_name = "Amaurornis phoenicurus"
    elif (_value == "White-shouldered_Starling"):
        scientific_name = "Sturnia sinensis"
    elif (_value == "White-winged_Tern"):
        scientific_name = "Chlidonias leucopterus"
    elif (_value == "Wood_Sandpiper"):
        scientific_name = "Tringa glareola"
    elif (_value == "Yellow-vented_Bulbul"):
        scientific_name = "Pycnonotus goiavier"
    elif (_value == "Zebra_Dove"):
        scientific_name = "Geopelia striata"
    elif (_value == "Zitting_Cisticola"):
        scientific_name = "Cisticola juncidis"

    return class_name, scientific_name


def get_pixel(img, center, x, y):

	new_value = 0

	try:
		# If local neighbourhood pixel
		# value is greater than or equal
		# to center pixel values then
		# set it to 1
		if img[x][y] >= center:
			new_value = 1

	except:
		# Exception is required when
		# neighbourhood value of a center
		# pixel value is null i.e. values
		# present at boundaries.
		pass

	return new_value

# Function for calculating LBP
def lbp_calculated_pixel(img, x, y):

	center = img[x][y]

	val_ar = []

	# top_left
	val_ar.append(get_pixel(img, center, x-1, y-1))

	# top
	val_ar.append(get_pixel(img, center, x-1, y))

	# top_right
	val_ar.append(get_pixel(img, center, x-1, y + 1))

	# right
	val_ar.append(get_pixel(img, center, x, y + 1))

	# bottom_right
	val_ar.append(get_pixel(img, center, x + 1, y + 1))

	# bottom
	val_ar.append(get_pixel(img, center, x + 1, y))

	# bottom_left
	val_ar.append(get_pixel(img, center, x + 1, y-1))

	# left
	val_ar.append(get_pixel(img, center, x, y-1))

	# Now, we need to convert binary
	# values to decimal
	power_val = [1, 2, 4, 8, 16, 32, 64, 128]

	val = 0

	for i in range(len(val_ar)):
		val += val_ar[i] * power_val[i]

	return val

def scale_minmax(X, min=0.0, max=1.0):
    X_std = (X - X.min()) / (X.max() - X.min())
    X_scaled = X_std * (max - min) + min
    return X_scaled

def spectrogram_image(y, sr, out, hop_length, n_mels):
    mels = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels,
                                            n_fft=hop_length*2, hop_length=hop_length)
    mels = numpy.log(mels + 1e-9)
    img = scale_minmax(mels, 0, 255).astype(numpy.uint8)
    img = numpy.flip(img, axis=0) # put low frequencies at the bottom in image
    img = 255-img # invert. make black==more energy

    # save as PNG
    skimage.io.imsave(out, img)


def spectrogramMaking(_filename):
    # settings
    print("Spectrogram making started")
    hop_length = 512
    n_mels = 128
    time_steps = 384

    copyPaste = _filename

    # load audio. Using example from librosa
    #os.listdir can be changed into whatever directory depending on the data needed
    path = copyPaste
    export_path = "./Spectrogram"
    export_path2 = "./Spectrogram"
    for file in os.listdir():
      if (file == _filename):
        sample_path2 = file
        path = (sample_path2)
        y, sr = librosa.load(path, offset=1.0, duration=10.0, sr=22050)
        out = '3-' + file + '.png'
        print("Spectrogram making is processing")

        # extract a fixed length window
        start_sample = 0 # starting at beginning
        length_samples = time_steps*hop_length
        window = y[start_sample:start_sample+length_samples]

        # convert to PNG
        spectrogram_image(window, sr=sr, out=out, hop_length=hop_length, n_mels=n_mels)
        print('wrote file', out)

        img_bgr = cv2.imread(out, 1)
        height, width, _ = img_bgr.shape
        img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
        img_lbp = np.zeros((height, width), np.uint8)

        for i in range(0, height):
          for j in range(0, width):
            img_lbp[i, j] = lbp_calculated_pixel(img_gray, i, j)
        figure(figsize=(1, 2), dpi=80)
        plt.imshow(img_lbp, cmap='gray')
        plt.axis('off')
        #plt.show
        plt.savefig(file + "_LBP.png", transparent=True, pad_inches=0, bbox_inches='tight')
        print(out + " LBP Program is finished")

        LBP = file + "_LBP.png"
        prediction_value = modelPredicting(LBP)
        shutil.move(out, export_path)
        shutil.move(file + "_LBP.png", export_path2)

        return prediction_value

def modelPredicting(_LBP):
    # categories = ["Asian_Glossy_Starling","Barn_Swallow","Black-Crowned_Night_Heron","Black-headed_Gull",
    #           "Black-Tailed_Godwit","Black-Winged_Stilt","Blue-tailed_Bee-eater","Clamorous_Reed_Warbler",
    #           "Common_Greenshank","Common_Kingfisher","Common_Pochard","Common_Redshank","Common_Sandpiper","Common_Snipe","Common_Tern",
    #           "Eastern_Yellow_Wagtail","Eurasian_Coot","Eurasian_Moorhen","Eurasian_Tree_Sparrow","Eurasian_Wigeon","Gadwall","Garganey","Golden-headed_Cristicola",
    #           "Gray_Heron","Great_Egret","Greater_White-fronted_Goose","Kentish_Plover","Large-billed_Crow","Lesser_Coucal",
    #           "Little_Egret","Little_Grebe","Little_Ringed_Plover","Little_Tern","Marsh_Sandpiper",
    #           "Northern_Pintail","Northern_Shoveler","Oriental_Reed_Warbler","Oriental_Skylark","Pacific_Golden-Plover",
    #           "Paddyfield_Pipit","Philippine_Pied-Fantail","Purple_Heron",
    #           "Rock_Pigeon","Scaly-breasted_Munia","Silence","Spotted_Dove","Striated_Grassbird","Striated_Heron","Swinhoe_s_Snipe",
    #           "Tawny_Grassbird","Tufted_Duck","Watercock","Whiskered_Tern","White-breasted_Waterhen",
    #           "White-shouldered_Starling","White-winged_Tern","Wood_Sandpiper","Yellow-vented_Bulbul","Zebra_Dove","Zitting_Cisticola"]
    # img_height = 80
    # img_width = 120
    # img_array = cv2.imread(_LBP, cv2.IMREAD_GRAYSCALE)
    # new_array = cv2.resize(img_array, (img_width, img_height))
    # #new_array = new_array.shape[1:]
    # #new_array = new_array.reshape(0, img_width, img_height, 1)
    # new_array = np.array(new_array)
    # new_array = new_array/255
    # #new_array = new_array.shape[1:]
    # #new_array = tf.expand_dims(new_array, axis=0)

    # print(new_array)

    path_training = _LBP
    categories = ["Barn_Swallow",
              "Common_Greenshank","Common_Sandpiper","Eurasian_Tree_Sparrow","Garganey","Great_Egret","Little_Egret","Purple_Heron",
              "Rock_Pigeon","Silence","Zitting_Cisticola"]
    #path_test = "Bird_LBPs_test"
    image_width = 80
    image_height = 120
    training_data = []
    #testing_data = []
    print(len(categories))

    for category in categories:
        path = path_training
        class_num = categories.index(category)
        try:
            try:
                image_array = cv2.imread(path)
                image_array2 = cv2.resize(image_array,(image_width, image_height))
                training_data.append([image_array2, class_num])
            except Exception as e:
                pass
        except Exception as e:
            pass
    print(len(training_data))

    x_train = []
    y_train = []

    for features, label in training_data:
        x_train.append(features)
        y_train.append(label)

    #x_train = np.array(x_train).reshape(-1, image_width, image_height, 1)
    #y_train = np.array(y_train).reshape(-1, 1)
    x_train = np.array(x_train)
    y_train = np.array(y_train)
    x_train = x_train/255

    bird_model = tf.keras.models.load_model('bird_sound_detector.keras')
    #results = bird_model.predict_classes(X_test, batch_size=4)
    #y_prob = bird_model.predict(x_train)
    #y_classes = y_prob.argmax(axis=-1)
    #y_prob = bird_model.predict(x_train)
    y_prob = bird_model.predict(x_train)
    #y_classes = y_prob.argmax(axis=-1)
    #y_classes2 = y_prob.max(axis=-1)
    y_classes = y_prob.argmax(axis=-1)
    #y_classes = np.where(y_prob > 0.85, 1, 0)
    #print(y_prob)

    #print(y_classes2)
    print(y_classes)
    #print(y_classes2 < y_classes)
    #print(categories[y_classes[0]])
    #prediction_value = "test"
    prediction_value = categories[y_classes[0]]
    if (y_classes[0] == 5 or y_classes[0] == 6 or y_classes[0] == 8):
        prediction_value = "Unknown"
    print(prediction_value)
    return prediction_value
#---------------------------------------------------------------------------------------

if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=5000, debug=True)
    app.run(debug=True)
