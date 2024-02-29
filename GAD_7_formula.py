from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Calculate the GAD-7 score based on user responses
        gad_7_score = calculate_gad_7_score(request.form)
        return render_template('result.html', gad_7_score=gad_7_score)
    return render_template('index.html')

def calculate_gad_7_score(form_data):
    # Mapping radio button values to scores
    score_mapping = {
        'Not_at_all': 0,
        'At_several_days': 1,
        'More_than_half_the_days': 2,
        'Nearly_everyday': 3
    }

    total_score = 0

    # Calculate total score based on form data
    for question in range(1, 8):
        question_key = f'Q{question}_PHQ'
        selected_value = form_data.get(question_key, 'Not_at_all')
        total_score += score_mapping[selected_value]

    return total_score

if __name__ == '__main__':
    app.run(debug=True)
