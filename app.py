from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html", title="כסף חכם")

@app.route('/budget', methods=['GET', 'POST'])
def budget():
    result = None
    if request.method == 'POST':
        income = float(request.form.get('income', 0))
        expenses = float(request.form.get('expenses', 0))
        result = income - expenses
    return render_template("budget.html", title="ניהול תקציב", result=result)

@app.route('/invest')
def invest():
    return render_template("invest.html", title="השקעות בסיסיות")

@app.route('/tips')
def tips():
    return render_template("tips.html", title="טיפים לחיסכון")

@app.route('/game', methods=['GET', 'POST'])
def game():
    message = None
    if request.method == 'POST':
        action = request.form.get('action')
        balance = int(request.form.get('balance', 1000))
        if action == 'invest':
            balance += 200
            message = "השקעת חכם! קיבלת 200 ש"ח נוספים."
        elif action == 'spend':
            balance -= 300
            message = "בזבזת 300 ש"ח. כדאי לחשוב שוב בפעם הבאה."
        return render_template("game.html", title="משחק כלכלי", balance=balance, message=message)
    return render_template("game.html", title="משחק כלכלי", balance=1000)

if __name__ == "__main__":
    app.run(debug=True)
