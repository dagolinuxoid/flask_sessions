from flask import Flask, render_template, redirect, url_for, request, session, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# LOL
def main():
    @app.route('/', methods=['GET', 'POST'])
    def index():
        # set second argument = None to behave silently instead of rising Keyerrror
        session.pop('user', None)
        if request.method == 'POST':
            if request.form['userpassword'] == request.form['username']:
                session['user'] = request.form['username']
                flash('your username and password are the same go agead to the /protected page')
            else: 
                flash('you have messed up')
        return render_template('index.html')

    @app.route('/protected')
    def protected():
        if 'user' in session:
            return render_template('protected.html')
        return redirect(url_for('index'))
        
if __name__ == '__main__':
    main()

app.run(debug=True) # facepalm
