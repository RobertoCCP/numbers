from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from PIL import Image

app = Flask(__name__)

# Cargar el modelo Keras
model = load_model('model.h5')
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

@app.route('/')
def home():
    return "Servicio activo"

@app.route('/predict', methods=['POST'])
def predict():
    # Verificar que se haya enviado un archivo
    if 'file' not in request.files:
        return jsonify({'error': 'No se encontró ningún archivo en la solicitud'}), 400
    
    # Leer el archivo de imagen
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Nombre de archivo vacío'}), 400
    
    try:
        # Abrir la imagen
        im = Image.open(file.stream)
        
        # Preprocesar la imagen
        im = im.resize((128, 128))
        im = img_to_array(im)
        im = np.expand_dims(im, axis=0)
        
        # Realizar la predicción
        prediction = model.predict(im)
        predicted_class = np.argmax(prediction)
        
        return jsonify({'predicted_class': int(predicted_class)}), 200
    except Exception as e:
        return jsonify({'error': f'Error al procesar la imagen: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
