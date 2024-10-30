from flask import Flask, jsonify, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os
import json

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
    return render_template("home.html")

# Route to form used to add a new student to the database
@app.route("/showclass")
def showclass():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT Class, COUNT(*) FROM bird GROUP BY Class")

    rows = cur.fetchall()
    con.close()
    # Send the results of the SELECT to the list.html page
    return render_template("class.html",rows=rows)

@app.route("/showspecies")
def showspecies():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT EnglishName, COUNT(*) FROM bird GROUP BY EnglishName")

    rows = cur.fetchall()
    con.close()
    # Send the results of the SELECT to the list.html page
    return render_template("species.html",rows=rows)

# Route to SELECT all data from the database and display in a table
@app.route('/list')
def list():
    # Connect to the SQLite3 datatabase and
    # SELECT rowid and all Rows from the students table.
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT rowid, * FROM bird")

    rows = cur.fetchall()
    con.close()
    # Send the results of the SELECT to the list.html page
    return render_template("list.html",rows=rows)

# Route that will SELECT a specific row in the database then load an Edit form
@app.route("/edit", methods=['POST','GET'])
def edit():
    if request.method == 'POST':
        try:
            # Use the hidden input value of id from the form to get the rowid
            id = request.form['id']
            # Connect to the database and SELECT a specific rowid
            con = sqlite3.connect("database.db")
            con.row_factory = sqlite3.Row

            cur = con.cursor()
            cur.execute("SELECT rowid, * FROM students WHERE rowid = " + id)

            rows = cur.fetchall()
        except:
            id=None
        finally:
            con.close()
            # Send the specific record of data to edit.html
            return render_template("edit.html",rows=rows)

@app.route("/export", methods=['POST','GET'])
def export():
    conn = sqlite3.connect("database.db", isolation_level=None,
                       detect_types=sqlite3.PARSE_COLNAMES)
    db_df = pd.read_sql_query("SELECT * FROM bird", conn)
    _time = datetime.date
    timeprint = str(_time)
    _output = 'database_' + timeprint +'.csv'
    db_df.to_csv("database_exported.csv", index=False)

    return render_template('result.html',msg="Successfully exported the database! Check your Flask app's root folder.")

@app.route("/delete", methods=['POST','GET'])
def delete():
    if request.method == 'POST':
        try:
             # Use the hidden input value of id from the form to get the rowid
            rowid = request.form['id']
            # Connect to the database and DELETE a specific record based on rowid
            with sqlite3.connect('database.db') as con:
                    cur = con.cursor()
                    cur.execute("DELETE FROM students WHERE rowid="+rowid)

                    con.commit()
                    msg = "Record successfully deleted from the database"
        except:
            con.rollback()
            msg = "Error in the DELETE"

        finally:
            con.close()
            # Send the transaction message to result.html
            return render_template('result.html',msg=msg)


@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if(request.method == "POST"):
        soundFile = request.files['image']
        longitude = request.form['1']
        latitude = request.form['2']
        filename = secure_filename(soundFile.filename)
        soundFile.save(filename)
        print("HI")
        prediction_value = spectrogramMaking(filename)
        class_name, scientific_name = determine_classandscientific(prediction_value)
        try:
            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO bird (EnglishName, ScientificName, Class, Time, longitude, latitude) VALUES (?,?,?,?,?,?)",(prediction_value, scientific_name, class_name, datetime.now(), longitude, latitude))

                con.commit()
        except:
            con.rollback()

        finally:
            con.close()
        return jsonify({'message': prediction_value})
    else:
        return jsonify({'message': prediction_value})

    #modelPrediction()


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

def lbp_calculated_pixel(img, x, y):
	center = img[x][y]
	val_ar = []

	val_ar.append(get_pixel(img, center, x-1, y-1))
	val_ar.append(get_pixel(img, center, x-1, y))
	val_ar.append(get_pixel(img, center, x-1, y + 1))
	val_ar.append(get_pixel(img, center, x, y + 1))
	val_ar.append(get_pixel(img, center, x + 1, y + 1))
	val_ar.append(get_pixel(img, center, x + 1, y))
	val_ar.append(get_pixel(img, center, x + 1, y-1))
	val_ar.append(get_pixel(img, center, x, y-1))

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
    img = numpy.flip(img, axis=0)
    img = 255-img # invert. make black==more energy

    # save as PNG
    skimage.io.imsave(out, img)


def spectrogramMaking(_filename):
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
        start_sample = 0
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

    path_training = _LBP
    categories = ["Asian_Glossy_Starling","Barn_Swallow","Black-Crowned_Night_Heron","Black-headed_Gull",
                "Black-Tailed_Godwit","Black-Winged_Stilt","Blue-tailed_Bee-eater","Clamorous_Reed_Warbler",
                "Common_Greenshank","Common_Kingfisher","Common_Pochard","Common_Redshank","Common_Sandpiper","Common_Snipe","Common_Tern",
                "Eastern_Yellow_Wagtail","Eurasian_Coot","Eurasian_Moorhen","Eurasian_Tree_Sparrow","Eurasian_Wigeon","Gadwall","Garganey","Golden-headed_Cristicola",
                "Gray_Heron","Great_Egret","Greater_White-fronted_Goose","Kentish_Plover","Large-billed_Crow","Lesser_Coucal",
                "Little_Egret","Little_Grebe","Little_Ringed_Plover","Little_Tern","Marsh_Sandpiper",
                "Northern_Pintail","Northern_Shoveler","Oriental_Reed_Warbler","Oriental_Skylark","Pacific_Golden-Plover",
                "Paddyfield_Pipit","Philippine_Pied-Fantail","Purple_Heron",
                "Rock_Pigeon","Scaly-breasted_Munia","Spotted_Dove","Striated_Grassbird","Striated_Heron","Swinhoe_s_Snipe",
                "Tawny_Grassbird","Tufted_Duck","Watercock","Whiskered_Tern","White-breasted_Waterhen",
                "White-shouldered_Starling","White-winged_Tern","Wood_Sandpiper","Yellow-vented_Bulbul","Zebra_Dove","Zitting_Cisticola"]
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

    x_train = np.array(x_train)
    y_train = np.array(y_train)
    x_train = x_train/255

    bird_model = tf.keras.models.load_model('bird_sound_detector.keras')
    y_prob = bird_model.predict(x_train)
    y_classes = y_prob.argmax(axis=-1)
    print(y_prob)
    print(categories[y_classes[0]])
    prediction_value = categories[y_classes[0]]
    return prediction_value
#---------------------------------------------------------------------------------------

if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=5000, debug=True)
    app.run(debug=True)
