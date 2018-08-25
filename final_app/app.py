import numpy as np
import pandas as pd
import pickle
import os
import json
from flask import (
    Flask,
    render_template,
    jsonify,
    request)

from flask_sqlalchemy import SQLAlchemy

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################
#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite"

#db = SQLAlchemy(app)


#class WOSO(db.Model):
    #__tablename__ = 'stats'

    #shots = db.Column(db.Integer)
    #GK_SOG_Faced = db.Column(db.Integer)
    #assists = db.Column(db.Integer)
    #pass_comp_pct = db.Column(db.Integer)
    #big_chances = db.Column(db.Integer)
    #key_passes = db.Column(db.Integer)
    #take_ons = db.Column(db.Integer)
    #ad_win_pct = db.Column(db.Integer)
    #gk_overall_pass_comp_pct = db.Column(db.Integer)

    #def __repr__(self):
        #return '<Pet %r>' % (self.nickname)


#@app.before_first_request
#def setup():
    # Recreate database each time for demo
 #   db.drop_all()
    #db.create_all()


#################################################
# Routes
#################################################

@app.route("/send", methods=["GET", "POST"])
def send():
    #if request.method == "POST":
        #shots = request.form["shots"]
        #GK_SOG_Faced = request.form["GK_SOG_Faced"]
        #assists = request.form["assists"]
        #pass_comp_pct = request.form["pass_comp_pct"]
        #big_chances = request.form["big_chances"]
        #key_passes = request.form["key_passes"]
        #take_ons = request.form["take_ons"]
        #ad_win_pct = request.form["ad_win_pct"]
        #gk_overall_pass_comp_pct = request.form["gk_overall_pass_comp_pct"]

        #new_stats = New_Stats(shots=shots,GK_SOG_Faced=GK_SOG_Faced,assists=assists,pass_comp_pct=pass_comp_pct,big_chances=big_chances,key_passes=key_passes,take_ons=take_ons,ad_win_pct=ad_win_pct,gk_overall_pass_comp_pct=gk_overall_pass_comp_pct)
        #print(new_stats)
        ##db.session.add(new_stats)
        ##db.session.commit()

        #return "Thanks for the form data!"

    return render_template("form.html")

@app.route('/get_prediction', methods=["POST", "GET"])
def get_table():

   for i in request.json:
       print(i["name"])
       if i["name"] == "Shots":
           Shots=i["value"]
       elif i["name"] == "assists":
           Assists=i["value"]
       elif i["name"] == "fwPass.Comp.Pct":
           fwPass=i["value"]
       elif i["name"] == "Cross.Comp.Pct":
           crossInput=i["value"]
       elif i["name"] == "Big.Chances":
           BigChancesInput=i["value"]
       elif i["name"] == "AD.Win.Pct":
           AdWinInput=i["value"]

   model_file=os.path.join("static","woso_finalized_model.sav")
   loaded_model = pickle.load(open(model_file, 'rb'))

   print(loaded_model)
   test_dict={"Shots":Shots,"Assists":Assists,"fwPass.Comp.Pct":fwPass,"Cross.Comp.Pct":crossInput,"Big.Chances":BigChancesInput,"AD.Win.Pct":AdWinInput}

   data=pd.DataFrame(test_dict,index=[0])
   result = loaded_model.predict(data)
   result=str(result)
   return result

@app.route("/")
def home():
    return render_template ('index.html')


if __name__ == "__main__":
    app.run()
