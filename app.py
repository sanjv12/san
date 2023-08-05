from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def calculate_flames(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

    for char in name1:
        if char in name2:
            name1 = name1.replace(char, "", 1)
            name2 = name2.replace(char, "", 1)

    combined_names = name1 + name2
    flames_result = flames[len(combined_names) % len(flames)]
    flames_abbr = flames_result[0].upper()  # Use abbreviation

    return flames_result, flames_abbr

def get_relation_emoji(result):
    emoji_dict = {
        'Friends': '🕺',
        'Love': '💕',
        'Affection': '😍',
        'Marriage': '💍',
        'Enemy': '🤬',
        'Siblings': '👫'
    }
    return emoji_dict.get(result, '')

def get_emoji_animation(result):
    if result in ['Friends', 'Love', 'Marriage']:
        return 'bounce'
    elif result in ['Affection', 'Siblings']:
        return 'rotate'
    else:
        return ''

def get_relation_quote(result):
    quotes = {
        'Friends': 'True friends are never apart; maybe in distance, but never in heart.',
        'Love': 'Love is not about how many days, months, or years you have been together. Love is about how much you love each other every single day.',
        'Affection': 'Affection is when you see someone\'s strengths, love is when you accept someone\'s flaws.',
        'Marriage': 'A successful marriage requires falling in love many times, always with the same person.',
        'Enemy': 'The greatest good you can do for another is not just to share your riches but to reveal to him his own.',
        'Siblings': 'Siblings are the people we practice on, the people who teach us about fairness and cooperation and kindness and caring – quite often the hard way.'
    }
    return quotes.get(result, '')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name1 = request.form['name1']
        name2 = request.form['name2']
        return redirect(url_for('result', name1=name1, name2=name2))
    return render_template('index.html')

@app.route('/result', methods=['GET'])
def result():
    if request.method == 'GET':
        name1 = request.args.get('name1', '')
        name2 = request.args.get('name2', '')
        result, flames_abbr = calculate_flames(name1, name2)
        emoji = get_relation_emoji(result)
        emoji_animation = get_emoji_animation(result)
        quote = get_relation_quote(result)

        # Map result to a CSS class for background color
        result_category = result.lower().replace(" ", "-")

        return render_template('result.html', name1=name1, name2=name2, result=result, result_label='FLAMES Result', flames_abbr=flames_abbr, emoji=emoji, emoji_animation=emoji_animation, quote=quote, result_category=result_category)
    else:
        return redirect(url_for('index'))

@app.route('/try-again', methods=['GET'])
def try_again():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
