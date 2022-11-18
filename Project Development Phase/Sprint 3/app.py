import bcrypt
import ibm_db
from flask import Flask, redirect, render_template, request, session, url_for

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=b70af05b-76e4-4bca-a1f5-23dbb4c6a74e.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32459;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=bbw69807;PWD=JT6D7cbbvyMNhIQk",'','')



app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/",methods=['GET'])
def home():
    if 'email' not in session:
      return redirect(url_for('index'))
    return render_template('index.html',name='Home')
@app.route("/index")
def index():
  return render_template('index.html')
@app.route("/index1")
def index1():
  return render_template('index1.html')

@app.route("/addcategory")
def  addcategory():
  return render_template('addcategory.html')


@app.route("/addcustomer")
def  addcustomer():
  return render_template('addcustomer.html')

@app.route("/addproduct")
def  addproduct():
   return render_template('addproduct.html')

@app.route("/addpurchase")
def  addpurchase():

  return render_template('addpurchase.html')
   
@app.route("/addsupplier")
def  addsupplier():
  return render_template('addsupplier.html')

@app.route("/categorylist")
def categorylist():
  return render_template('categorylist.html')

@app.route("/customerlist")
def customerlist():
  return render_template('customerlist.html')

@app.route("/importpurchase")
def importpurchase():
  return render_template('importpurchase.html')

@app.route("/home")
def home():
  return render_template('home.html')

@app.route("/register")
def register():
  return render_template('register.html')

@app.route("/productlist")
def productlist():
  return render_template('productlist.html')

@app.route("/purchaselist")
def purchaselist():
  return render_template('purchaselist.html')

@app.route("/supplierlist")
def supplierlist():
  return render_template('supplierlist.html')

@app.route("/homepage")
def homepage():
  return render_template('homepage.html')






@app.route("/register",methods=['GET','POST'])
def register():
  if request.method == 'POST':
  
   
    email = request.form['email']
    psw = request.form['psw']

    if  not email or  not psw:
      return render_template('register.html',error='Please fill all fields')
    hash=bcrypt.hashpw(psw.encode('utf-8'),bcrypt.gensalt())
    query = "SELECT * FROM form WHERE email=? OR psw=?"
    stmt = ibm_db.prepare(conn, query)
    ibm_db.bind_param(stmt,1,email)
    ibm_db.bind_param(stmt,2,phn)
    ibm_db.execute(stmt)
    print(stmt)
    isUser = ibm_db.fetch_assoc(stmt)
    if not isUser:
      insert_sql = "INSERT INTO user_detail(email, psw) VALUES (?,?)"
      prep_stmt = ibm_db.prepare(conn, insert_sql)
  
      ibm_db.bind_param(prep_stmt, 2, email)
      ibm_db.bind_param(prep_stmt, 3, psw)

      ibm_db.execute(prep_stmt)
      return render_template('register.html',success="You can login")
    else:
      return render_template('register.html',error='Invalid Credentials')

  return render_template('register.html',name='Home')



@app.route("/home",methods=['GET','POST'])
def login():
    if request.method == 'POST':
      email = request.form['email']
      psw = request.form['psw']

      if not email or not psw:
        return render_template('home.html',error='Please fill all fields')
      query = "SELECT * FROM form WHERE email=?"
      stmt = ibm_db.prepare(conn, query)
      ibm_db.bind_param(stmt,1,email)
      ibm_db.execute(stmt)
      isUser = ibm_db.fetch_assoc(stmt)
      print(isUser,psw)

      if not isUser:
        return render_template('home.html',error='Invalid Credentials')
      
      isPasswordMatch = bcrypt.checkpw(psw.encode('utf-8'),isUser['PSW'].encode('utf-8'))

      if not isPasswordMatch:
        return render_template('home.html',error='Invalid Credentials')

      session['email'] = isUser['EMAIL']
      return redirect(url_for('home'))

    return render_template('home.html',name='Home')



if __name__ == "__main__":
    app.run(debug=True)
