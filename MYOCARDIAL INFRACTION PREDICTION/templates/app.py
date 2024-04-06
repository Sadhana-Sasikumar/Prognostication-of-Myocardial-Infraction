from flask import Flask, render_template, request
import pickle

app = Flask(_name_)

def predict_heart(sex, age_category, had_angina, had_stroke, had_diabetes, tetanus_last_10_tdap,
       had_asthma, blind_or_vision_difficulty, deaf_or_hard_of_hearing,
        difficulty_concentrating, smoking_status, bmi, cholesterol, bp):

    # Convert 'yes' and 'no' to 1 and 0
    convert_to_numeric = lambda x: 1 if x.lower() == 'yes' else 0

    had_angina = convert_to_numeric(had_angina)
    had_stroke = convert_to_numeric(had_stroke)
    had_diabetes = convert_to_numeric(had_diabetes)
    tetanus_last_10_tdap = convert_to_numeric(tetanus_last_10_tdap)
    had_asthma = convert_to_numeric(had_asthma)
    blind_or_vision_difficulty = convert_to_numeric(blind_or_vision_difficulty)
    deaf_or_hard_of_hearing = convert_to_numeric(deaf_or_hard_of_hearing)
    difficulty_concentrating = convert_to_numeric(difficulty_concentrating)

    predss = [[sex, age_category, had_angina, had_stroke, had_diabetes, tetanus_last_10_tdap,
               had_asthma, blind_or_vision_difficulty, deaf_or_hard_of_hearing,
               difficulty_concentrating, smoking_status, bmi, cholesterol, bp]]

    with open('heart.pkl', 'rb') as our_model:
        for_pred_model = pickle.load(our_model)

    predicted = for_pred_model.predict(predss)

    return predicted

@app.route('/')
def home():
    return render_template('myocardial_infraction_form.html')

@app.route('/predict', methods=['POST'])
def predict():

    sex = request.form['sex']
    age_category = request.form['AgeCategory']
    had_angina = request.form['HadAngina']
    had_stroke = request.form['HadStroke']
    had_diabetes = request.form['HadDiabetes']
    tetanus_last_10_tdap = request.form['TetanusLast10Tdap']
    had_asthma = request.form['HadAsthma']
    blind_or_vision_difficulty = request.form['BlindOrVisionDifficulty']
    deaf_or_hard_of_hearing = request.form['DeafOrHardOfHearing']
    difficulty_concentrating = request.form['DifficultyConcentrating']
    smoking_status = request.form['SmokingStatus']
    bmi = request.form['BMI']
    cholesterol = request.form['Cholesterol']
    bp = request.form['BP']

    prediction = predict_heart(sex, age_category, had_angina, had_stroke, had_diabetes, tetanus_last_10_tdap,
       had_asthma, blind_or_vision_difficulty, deaf_or_hard_of_hearing,
        difficulty_concentrating, smoking_status, bmi, cholesterol, bp)

    return render_template('myocardial_infraction_result.html', prediction=prediction)

if _name_ == '_main_':
    app.run()