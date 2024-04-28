from flask import Flask, render_template, request, jsonify
import numpy as np
from keras.models import load_model
import imageio

app = Flask(__name__)

# Cargar el modelo entrenado
model = load_model('mnist_cnn_model.h5')  # Asegúrate de que el modelo esté en el mismo directorio que este archivo

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Obtener la imagen enviada desde el frontend
    file = request.files['image']
    im = imageio.imread(file)  # Leer la imagen

    # Preprocesar la imagen
    gray = np.dot(im[..., :3], [0.299, 0.587, 0.114])
    if gray.shape != (28, 28):
        gray = gray[:28, :28]
    
    # Preparar la imagen para la predicción
    gray = gray.reshape(1, 28, 28, 1)
    gray = gray.astype('float32') / 255
    
    # Realizar la predicción
    prediction = model.predict(gray)
    predicted_number = prediction.argmax()

    # Devolver el resultado como JSON
    return jsonify({'predicted_number': str(predicted_number)})

if __name__ == '__main__':
    app.run(debug=True, port=8000)

