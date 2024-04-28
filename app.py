from flask import Flask, render_template, request, jsonify
import numpy as np
from keras.models import load_model
from keras.optimizers import Adam  
from PIL import Image

app = Flask(__name__)

# Cargar el modelo entrenado y compilarlo
model = load_model('mnist_cnn_model.h5')
model.compile(loss='categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Leer la imagen y convertirla a escala de grises
        img = Image.open(request.files['image']).convert('L').resize((28, 28))
        
        # Preparar la imagen para la predicción
        img_array = np.array(img).reshape(1, 28, 28, 1).astype('float32') / 255
        
        # Realizar la predicción
        prediction = model.predict(img_array)
        predicted_number = np.argmax(prediction)
        
        # Devolver el resultado como JSON
        return jsonify({'predicted_number': str(predicted_number)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8000)

