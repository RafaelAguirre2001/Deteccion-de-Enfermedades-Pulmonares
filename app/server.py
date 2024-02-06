from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import prediction
import os

app = Flask("__main__", template_folder="templates")
Uploaded_images = "C:/Users/jesus/Desktop/CovidNet-Peru-master/Interfaz_predict-main/Diagnosticc-main/Diagnosticc-main/Uploaded_images"

app.config['Uploaded_images'] = Uploaded_images

@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'GET':
        return render_template('index.html')
    # Aquí puedes añadir lógica para manejar el método POST si es necesario
    # messages = ['Covid 19', 'Normal', 'Opacidad Pulmonar']
    # return random.choice(messages)

@app.route('/getFile', methods=['POST'])
def getOutput():
    output = ""
    if request.method == 'POST':
        myimage = request.files.get('myfile')
        imgname = secure_filename(myimage.filename)
        imgpath = os.path.join(app.config["Uploaded_images"], imgname)
        myimage.save(os.path.join(app.config["Uploaded_images"], imgname))
        output = prediction.prediction(imgpath)
        print(output)
    return output

if __name__ == '__main__':
    app.run(port=3000)
