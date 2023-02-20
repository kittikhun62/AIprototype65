from flask import Flask, request, render_template, make_response 
import json
# import pandas as pd

app = Flask(__name__)

@app.route("/")  
def helloworld():
    return "Hello, World!"

@app.route("/name")  
def hellotohn():
    return "Hello, Tohn!"

##api
#api เว็บเชอร์วิส api 
@app.route('/getrequest',methods=['GET']) #methon เป็น http โปรโตคอล 
def request_detail():

    getmsg = request.args.get('msg1')
    print(getmsg)
    return "received"   

#api เว็บเชอร์วิส api    
@app.route('/postrequest',methods=['POST']) #methon เป็น http โปรโตคอล 
def post_request_detail():
    # payload = request.data.decode("utf-8") # รับของที่ส่งมาให้เรา ข้อความ
    # inmessage = json.loads(payload) #ข้อความที่ส่งปกติมักจะเป็น json 

    # print(inmessage) 

    # json_data = json.dumps({'y': 'received!'})
    return 'received'

##webapp 
# @app.route("/home", methods=['POST','GET'])
# def home():
    
#     if request.method == "POST":
#         dbpd = pd.read_csv('db.csv')
#         # getting input with name = fname in HTML form
#         first_name = request.form.get("fname")
#         # getting input with name = lname in HTML form 
#         last_name = request.form.get("lname") 

#         dbpd = dbpd.append({'name': first_name,'lastname' : last_name}, ignore_index=True)
#         dbpd.to_csv('db.csv',index=False)

#         resp = make_response(render_template("home.html",name = f"{first_name} {last_name}", fav =""))
#         resp.set_cookie('firstname', first_name)
        
#         return resp

#     if request.method == "GET":
#         getval = request.args
#         print(getval)
#         print(getval.get('name'))
        

#     return render_template("home.html",name = 'Tohn', fav ="")

@app.route("/home")
def home():
#     print('we are in home2')
#     # getting input with name = fname in HTML form
#     name = request.form['fav_language']
#     print(name)
#     #return render_template("home.html",name = f"{first_name} {last_name}")


    return render_template("home.html",name="kittikhun")
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=5001)#host='0.0.0.0',port=5001