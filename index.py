from flask import Flask, render_template, request
import sqlite3, os

from models import db, Feelings
from forms import FeelingsForm

app = Flask(__name__)
try:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL'] #'postgresql:///learningflask'
except:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///learningflask'  # this works on c9
    # to use database url I had to run      heroku pg:promote ___________     where ______ = my heroku database's path
    # I also pushed my existing db to heroku
    #app.config['SQLALCHEMY_DATABASE_URI'] = 
    #db = SQLAlchemy(app)  # I mgiht need this
db.init_app(app)


# for wtforms 
app.secret_key = "development-key"


#doing it with sqlite
##conn = sqlite3.connect(":memory:", check_same_thread = False)
#conn = sqlite3.connect('test.sqlite')
#cur = conn.cursor()


# Make some fresh tables using executescript()
createtable = '''
CREATE TABLE IF NOT EXISTS feeling (
    --id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    feelings    TEXT,
    --url  TEXT UNIQUE,
        -- because I made this unique, it won't allow dupes later
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
'''
#cur.executescript(createtable)


@app.route('/', methods=['GET','POST'])
def feelsubmit():
    form = FeelingsForm()

    if request.method == "POST":
        if form.validate() == False:
            return render_template('index.html', form=form)
        else:
          newfeeling= Feelings(form.feeling.data)
          db.session.add(newfeeling)
          db.session.commit()
          
          print(form.feeling.data)
          newfeelingtext = form.feeling.data
          #for a in newfeeling:
          #    print(a)   -- new feelings is not iterable
          a = Feelings.query.all()   #.order_by(Feelings.timestamp).
          print(a)
            
          
          return render_template('index.html', form=form, newfeelingtext=newfeelingtext, allfeelings = a)
        
    elif request.method == "GET":
        return render_template('index.html', form=form, newfeelingtext='')


# if not in c9
#if __name__ == "__main__":  # This says only run the app if this is your main file
#    app.run(debug=True)


#if on c9: 
#DATABASE = 'test.sqlite'  # this didn't work to get the command to work , app.logger.info("Database on: %s", app.config['DATABASE'])
#if __name__ == "__main__":
#    app.debug = True
#    
#    host = os.environ.get('IP', '0.0.0.0')
#    port = int(os.environ.get('PORT', 8080))
#    app.logger.info("Starting flask app on %s:%s", host, port)
   # app.logger.info("Database on: %s", app.config['DATABASE'])
    
#    app.run(host=host, port=port)

#  heroku
if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)



# testing the doc

print('sucks')

#this is how to use dictionaries
# keys have to be unique
text = {'input':'Hello, this is the first'
    ,'input2':'This is the second'
    ,'input3':'This is the thirdd'}
for k,v in text.items():
    print(k, v)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

#cur.execute(""" Select rowid, name, url from Artist order by name limit 10 """)
#cur.execute(""" Select * from feeling limit 10 """)
#print(cur.fetchall())
