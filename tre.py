from flask import Flask, render_template, request
import math 
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def calcoloGeo():
  return render_template("tre_3.html", methods = ['GET']) 

@app.route('/risultato',methods=['get'])
def risultato():
    latoQ = float(request.args.get('latoQ'))
    tipo = int(request.args.get('primo'))

    def doppietta(a):
        if tipo == 0:
             calcolo = a * a
        elif tipo == 1:
            calcolo = math.sqrt(2)*a
            
        return calcolo

    return render_template('tre_3Risultato.html',calcolo=doppietta(latoQ))
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)