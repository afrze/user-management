from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
db = SQLAlchemy(app)

class Users(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(200), nullable=False)
  date_created =  db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self):
     return '<User Created %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
      from_user_input = request.form['user']
      new_user =  Users(name=from_user_input) 
      
      try:
        db.session.add(new_user)
        db.session.commit()
        return redirect('/')
      except:
        return "There was an issues adding the user"
    
    else:
      users = Users.query.order_by(Users.date_created).all()
      return render_template('index.html', users=users)
    
@app.route('/delete/<int:id>')
def deleteUser(id):
  user_to_delete = Users.query.get_or_404(id)
  try:
    db.session.delete(user_to_delete)
    db.session.commit()
    return redirect('/')
  except:
    return 'There was an issue deleting the user'
  

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def updateUser(id):
  user_to_update = Users.query.get_or_404(id)

  if request.method == 'POST':
    user_to_update.name = request.form['user']

    try:
      db.session.commit()
      return redirect('/')
    except:
      return 'There was an issue updating the user'

  else: 
    return render_template('update.html', user=user_to_update)

if __name__ == "__main__":
  app.run(debug=True)