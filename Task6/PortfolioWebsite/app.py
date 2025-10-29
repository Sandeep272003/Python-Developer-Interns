from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key' 

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        if not name or not email or not message:
            flash("Please fill in all fields", "error")
        else:
            # In real app, save message or send email here
            flash("Thank you for contacting me!", "success")
            return redirect(url_for('index'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
