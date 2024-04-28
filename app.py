from flask import Flask, render_template, request, jsonify
import numpy as np
from keras.models import load_model
from keras.optimizers import Adam  # Importa el optimizador que usaste durante el entrenamiento
from PIL import Image

app = Flask(__name__)

# Cargar el modelo entrenado
model = load_model('mnist_cnn_model.h5')  # Asegúrate de que el modelo esté en el mismo directorio que este archivo

# Compila el modelo después de cargarlo
optimizer = Adam()  # Configura el optimizador
model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Obtener la imagen enviada desde el frontend
    file = request.files['image']
    
    try:
        # Leer la imagen y convertirla a escala de grises
        im = Image.open(file).convert('L')
        im = im.resize((28, 28))  # Asegúrate de que la imagen tenga las dimensiones correctas
        im = np.array(im)
        
        # Preparar la imagen para la predicción
        gray = im.reshape(1, 28, 28, 1)
        gray = gray.astype('float32') / 255
        
        # Realizar la predicción
        prediction = model.predict(gray)
        predicted_number = np.argmax(prediction)
        
        # Devolver el resultado como JSON
        return jsonify({'predicted_number': str(predicted_number)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8000)
