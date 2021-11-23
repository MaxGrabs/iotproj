from flask import Flask, request, jsonify, render_template
from IPython.display import display
import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
host= "iotpython.mysql.database.azure.com",
user= "dmitry@iotpython",
password= "IOTpassword!",
database= "iotpython",)


mycursorone = mydb.cursor()
mycursorone.execute("SELECT * FROM sensor_one_data")
myresultone = mycursorone.fetchall()

mycursortwo = mydb.cursor()
mycursortwo.execute("SELECT * FROM sensor_two_data")
myresulttwo = mycursortwo.fetchall()

# t = PrettyTable(['ID', 'Date/Time', 'Temperature', 'Humid'])
# t2 = PrettyTable(['ID', 'Date/Time', 'Temperature', 'Humid'])

# from_db = []
# from_db2 = []

temp =''
for x in myresultone:
    temp+=str(list(x))
    # x = list(x)
    # from_db.append(x)

# columns = ['ID', 'Date/Time', 'Temperature', 'Humid']
# df = pd.DataFrame(from_db, columns=columns)
# df.set_index(['ID'], inplace=True)
# df.name=None

temp2 =''
for x in myresulttwo:
    temp2+=str(list(x))
    # x = list(x)
    # from_db2.append(x)

# df2 = pd.DataFrame(from_db2, columns=columns)
# df2.set_index(['ID'], inplace=True)
# df2.index.name=None

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def hello_world():
    return temp + '                 ' +temp2
    # render_template('view.html',tables=[df.to_html(classes='female'), df2.to_html(classes='male')])


mycursorone.close()
mycursortwo.close()
mycursortwo.close()
