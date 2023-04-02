import tensorflow as tf
import pandas as pd

model = tf.keras.models.load_model('../data_project_model.h5')


from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.json  # Get the input data from the request body
    new_data = summarizingData(input_data)
    prediction = model.predict(new_data)  # Make a prediction using the model
    return jsonify(prediction.tolist())  # Send the prediction back as JSON



def summarizingData(input_data):
    # term
    input_data['term'] = input_data['term'][:3]

    # sub_grade
    subgrade_dummies = pd.get_dummies(input_data['sub_grade'], prefix='sub_grade', drop_first=True)

    input_data = pd.concat([input_data.drop('sub_grade', axis=1), subgrade_dummies], axis=1)
    
    # 'verification_status','purpose','initial_list_status','application_type'
    dummies = pd.get_dummies(data['verification_status','purpose','initial_list_status','application_type'], drop_first=True)
    input_data = data.drop(column_name, axis=1)
    input_data = pd.concat([data, dummies], axis=1)

    # adresse
    input_data['zip_code'] = input_data['address'][-5:]

    # earliest_cr_year
    input_data['earliest_cr_year'] = input_data['earliest_cr_line'][-4:]

    return input_data



# Start the server
if __name__ == '__main__':
    app.run(debug=True, port=3000)