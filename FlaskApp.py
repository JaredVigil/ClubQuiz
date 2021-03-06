from flask import Flask, render_template, request, flash, url_for, redirect
import sqlite3 as sql
from qClass import question

app = Flask(__name__)
app.config.from_object('config')

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/index')
def home():
	return render_template('index.html')

@app.route('/enternew')
def new_student():
	return render_template('student.html')
	

@app.route('/newUser')
def new_user():
	return render_template('addUser.html')


@app.route('/enternewrequest')
def new_request():
	return render_template('request.html')


@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
	message = "Before record insertion"
	if request.method == 'POST':
		try:
			nm = request.form['nm']
			addr = request.form['add']
			city = request.form['city']
			descrp = request.form['descrp']
			Type = request.form['Type']
			aid = request.form['aid']
			with sql.connect("database.db") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO allItems (name,addr,city,descrp,Type,aid) VALUES (?,?,?,?,?,?)",(nm,addr,city,descrp,Type,aid)
)
				con.commit()
				message = "Record successfully added"
			with sql.connect("database.db") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO "+Type+" (name,addr,city,descrp,Type,aid) VALUES (?,?,?,?,?,?)",(nm,addr,city,descrp,Type,aid))
				con.commit()
				message = "Record successfully added into "+Type
		except:
			con.rollback()
			message = "Error in insert operation"

		finally:
			return render_template("result.html", msg = message)
			con.close()
			
@app.route('/adduser',methods = ['POST', 'GET'])
def adduser():
	message = "Before record insertion"
	if request.method == 'POST':
		try:
			wn = request.form['wNum']
			name = request.form['name']
			uName = request.form['userName']
			password = request.form['password']
			clubAS = 0;
			clubBS = 0;
			with sql.connect("database.db") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO userId (wNum,name,username,password,clubA,clubB) VALUES (?,?,?,?,?,?)",(wn,name,uName,password,clubAS,clubBS))
				con.commit()
				message = "Record successfully added"
		except:
			con.rollback()
			message = "Error in insert operation"

		finally:
			return render_template("result.html", msg = message)
			con.close()


@app.route('/listdonations')
def listdonations():
	con = sql.connect("database.db")
	con.row_factory = sql.Row
	cur = con.cursor()
	cur.execute("select * from food  WHERE aid = 'donation'")
	foodRows = cur.fetchall()
	cur.execute("select * from hygiene  WHERE aid = 'donation'")
	hygieneRows = cur.fetchall()
	cur.execute("select * from jobs  WHERE aid = 'donation'")
	jobsRow = cur.fetchall()
	cur.execute("select * from clothes  WHERE aid = 'donation'")
	clothesRows = cur.fetchall()
	cur.execute("select * from shelter  WHERE aid = 'donation'")
	shelterRows = cur.fetchall()
	cur.execute("select * from transportation  WHERE aid = 'donation'")
	transportationRows = cur.fetchall()
	donDict ={};
	donDict['foodRows'] = foodRows;
	donDict['foodRowsSize'] = len(foodRows);
	donDict['hygieneRows'] = hygieneRows;
	donDict['hygieneRowsSize'] = len(hygieneRows);
	donDict['jobsRow'] = jobsRow;
	donDict['jobsRowSize'] = len(jobsRow);
	donDict['clothesRows'] = clothesRows;
	donDict['clothesRowsSize'] = len(clothesRows);
	donDict['shelterRows'] = shelterRows;
	donDict['shelterRowsSize'] = len(shelterRows);
	donDict['transportationRows'] = transportationRows;
	donDict['transportationRowsSize'] = len(transportationRows);
	title = "All the Donations"


	rows = cur.fetchall()
	return render_template('listAll.html', donDict = donDict,title=title)

@app.route('/listrequests')
def listrequests():
      con = sql.connect("database.db")
      con.row_factory = sql.Row
      cur = con.cursor()
      cur.execute("select * from food  WHERE aid = 'request'")
      foodRows = cur.fetchall()
      cur.execute("select * from hygiene  WHERE aid = 'request'")
      hygieneRows = cur.fetchall()
      cur.execute("select * from jobs  WHERE aid = 'request'")
      jobsRow = cur.fetchall()
      cur.execute("select * from clothes  WHERE aid = 'request'")
      clothesRows = cur.fetchall()
      cur.execute("select * from shelter  WHERE aid = 'request'")
      shelterRows = cur.fetchall()
      cur.execute("select * from transportation  WHERE aid = 'request'")
      transportationRows = cur.fetchall()
      donDict ={}
      donDict['foodRows'] = foodRows
      donDict['foodRowsSize'] = len(foodRows)
      donDict['hygieneRows'] = hygieneRows
      donDict['hygieneRowsSize'] = len(hygieneRows)
      donDict['jobsRow'] = jobsRow
      donDict['jobsRowSize'] = len(jobsRow)
      donDict['clothesRows'] = clothesRows
      donDict['clothesRowsSize'] = len(clothesRows)
      donDict['shelterRows'] = shelterRows
      donDict['shelterRowsSize'] = len(shelterRows)
      donDict['transportationRows'] = transportationRows
      donDict['transportationRowsSize'] = len(transportationRows)
      title = "All the Requests"
      return render_template('listAll.html', donDict = donDict,title=title)

@app.route('/Donate')
def Donate():
    return render_template('donate.html')

@app.route('/Receive')
def Receive():
    return render_template('receive.html')

@app.route('/Tutorial')
def Tutorial():
    return render_template('tutorial.html')

@app.route('/Question')
def Question():
	qlist = []
	o1 = []
	o1 = question.make_optionArry("Blue","o1a","ClubA","Red","o1b","ClubB","Green","o1c","ClubA","Yellow","o1d","ClubA")
	q1 = question("what color do you like better",1,o1)
	o2 = question.make_optionArry("a","o2a","ClubA","b","o2b","ClubB","c","o2c","ClubA","d","o2d","ClubA")
	q2 = question("This is a test",2,o2)
	qlist.append(q1)
	qlist.append(q2)
	return render_template('questionTemp.html',qList = qlist)
	
@app.route('/results',methods = ['POST', 'GET'])
def results():	
	text = request.form.get('1')
	quizR = (str(text))
	return render_template('quizResults.html',quizR = quizR)

@app.route('/Signup')
def Signup():
    return render_template('signup.html')
@app.route('/showFood')
def showFood():

      aid = request.args.get('aid', None)
      con = sql.connect("database.db")
      con.row_factory = sql.Row
      cur = con.cursor()
      cur.execute("select * from food WHERE aid = '"+aid+"'")
      title = ""
      rows = cur.fetchall()
      if(aid == "donation"):
            title = "Donations for All Food"
      else:
            title = "Request for All Food"
      return render_template('list.html',  rows = rows,aid=aid, title=title)

@app.route('/item')
def item():
    fileid = request.args.get('fileid', None)
    tableType = request.args.get('type', None)

    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM "+tableType+" WHERE  fileid=?",[fileid])
    info = cur.fetchall()
    idTable = info[0]
    return render_template('item.html',info = idTable)

@app.route('/delete')
def delete():
    fileid = request.args.get('fileid', None)
    tableType = request.args.get('type', None)

    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("DELETE FROM "+tableType+" WHERE  fileid=?",[fileid])
    con.commit()
    message = "you have deleted the item from the database"
    return render_template("result.html", msg = message)
    con.close()



@app.route('/showHygiene')
def showHygiene():

	aid = request.args.get('aid', None)
	con = sql.connect("database.db")
	con.row_factory = sql.Row

	cur = con.cursor()
	cur.execute("select * from hygiene WHERE aid = '"+aid+"'")

	rows = cur.fetchall()
	if(aid == "donation"):
            title = "Donations for All Hygiene"
	else:
            title = "Request for All Food"
	return render_template('list.html',  rows = rows,aid=aid,title = title)

@app.route('/showOddjobs')
def showOddjobs():
	aid = request.args.get('aid', None)
	con = sql.connect("database.db")
	con.row_factory = sql.Row

	cur = con.cursor()
	cur.execute("select * from jobs WHERE aid = '"+aid+"'")

	rows = cur.fetchall()
	if(aid == "donation"):
            title = "Donations for All Odd Jobs"
	else:
            title = "Request for All Odd Jobs"
	return render_template('list.html',  rows = rows,aid=aid,title = title)
@app.route('/showClothes')
def showClothes():
	aid = request.args.get('aid', None)
	con = sql.connect("database.db")
	con.row_factory = sql.Row

	cur = con.cursor()
	cur.execute("select * from clothes WHERE aid = '"+aid+"'")

	rows = cur.fetchall()
	if(aid == "donation"):
            title = "Donations for All Clothes"
	else:
            title = "Request for All Clothes"
	return render_template('list.html',  rows = rows,aid=aid,title = title)

@app.route('/showShelter')
def showShelter():
	aid = request.args.get('aid', None)
	con = sql.connect("database.db")
	con.row_factory = sql.Row

	cur = con.cursor()
	cur.execute("select * from shelter WHERE aid = '"+aid+"'")

	rows = cur.fetchall()
	if(aid == "donation"):
            title = "Donations for All Shelter"
	else:
            title = "Request for All Shelter"
	return render_template('list.html',  rows = rows,aid=aid,title = title)

@app.route('/showTransportation')
def showTransportation():
	aid = request.args.get('aid', None)
	con = sql.connect("database.db")
	con.row_factory = sql.Row

	cur = con.cursor()
	cur.execute("select * from transportation WHERE aid = '"+aid+"'")

	rows = cur.fetchall()
	if(aid == "donation"):
            title = "Donations for All Transportation"
	else:
            title = "Request for All Transportation"
	return render_template('list.html',  rows = rows,aid=aid,title = title)

if __name__ == "__main__":
    app.run(debug = True)
