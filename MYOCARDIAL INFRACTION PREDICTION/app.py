from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

def predict_heart(input_data):
    # Use the provided input_data directly
    predss = [input_data]

    with open('heart.pkl', 'rb') as our_model:
        for_pred_model = pickle.load(our_model)

    predicted = for_pred_model.predict(predss)

    return predicted

@app.route('/')
def home():
    return render_template('myocardial_infraction_form.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Use the provided input_data
    #input_data = (1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1)
    input_data = (0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0)
    prediction = predict_heart(input_data)

    return render_template('myocardial_infraction_result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
