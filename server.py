from flask import Flask,request,jsonify
from chat import chatBot
import json
app = Flask(__name__)

@app.route("/bot",methods=['GET'])
def bot():
    if(request.args.get('query') != ''):
        ans = chatBot(request.args.get('query'))
        return json.loads(ans)
    else:
        return jsonify("Empty")
    

if __name__=="__main__":
    app.run(debug=True,port="4000")