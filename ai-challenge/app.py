import tensorflow as tf

model = tf.keras.models.load_model('../data_project_model.h5')


from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.json  # Get the input data from the request body
    prediction = model.predict(input_data)  # Make a prediction using the model
    return jsonify(prediction.tolist())  # Send the prediction back as JSON

# Start the server
if __name__ == '__main__':
    app.run(debug=True, port=3000)