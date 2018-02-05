

learningflask

for postgresql
https://community.c9.io/t/setting-up-postgresql/1573

PostgreSQL comes preinstalled on every Cloud9 workspace, yay! :tada: Here are a few basic commands to help out. The sudo sudo in each command is not a typo, you need to enter this or it will prompt for your ubuntu user password and break.

Start the PostgreSQL service
sudo service postgresql start
Connect to the service
psql
Create a PostgreSQL database
Make sure you have logged into the PostgreSQL terminal and then you can just run:

psql
postgres=# CREATE DATABASE "groceries";
List all databases
psql
postgres=# \list
Connecting with your language of choice
First you must set a password for your postgres user.

psql
postgres-# \password postgres
Enter new password: 
Then you can connect with username “ubuntu” and the password you set. Here’s an example in PHP:

<?php
$link = pg_connect("host=localhost dbname=groceries user=ubuntu password=cloud9isawesome");
?>

create a table:
CREATE TABLE users (
  id serial PRIMARY KEY,
  firstname varchar(100),
  middlename varchar(100),
  lastname varchar(100),
  email varchar(200),
  timestamp timestamp default current_timestamp
)














This was the old route for using sqlite
def index():
    #return 'Hello, World!'  # This return is what the person sees
    # you can put css in the quotes
    text = {'input':'Hello, this page cares how you are feeling'
            ,'input2':'Please tell me how you are feeling'
            ,'input3':'I really want to know'}
    if request.method == "POST":
        feeling = request.form['feeling'] # this is the name of the field in the form.
        text ={}
        conn = sqlite3.connect('test.sqlite')
        cur = conn.cursor()
        try:
            cur.execute('''INSERT
            --  OR IGNORE
            INTO feeling (feelings )  --if two, add ', field2' and (? , ?)
                VALUES ( ?  )''', ( feeling,  ) )  # and (field1, field2, ...)
        except:
            pass
        conn.commit()
        cur.execute(""" Select feelings from feeling limit 1000 """)
        allfeelings = cur.fetchall()
        return render_template("index.html", feeling =feeling, text = text, allfeelings = allfeelings)
            # because the index.html has two variabls (feeling and text),
            # I have to pass both variables
    return render_template("index.html",text=text,allfeelings = '')
    
    
for heroku:
https://devcenter.heroku.com/articles/heroku-postgresql