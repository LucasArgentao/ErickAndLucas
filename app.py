import cloudpickle
from flask import Flask, render_template, request

with open('model.pkl', 'rb') as file_in:
  model = cloudpickle.load(file_in)

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', nome='Fulano')

@app.route('/predicao', methods=['POST'])
def predicao():
  Age = int(request.form['Age'])
  Type_of_Travel = int(request.form['Type_of_Travel'])
  Customer_Type = int(request.form['Customer_Type'])
  Class = int(request.form['Class'])
  
  Flight_Distance = int(request.form['Flight_Distance'])
  Inflight_wifi_service = int(request.form['Inflight_wifi_service'])
  Departure_Arrival_time_convenient = int(request.form['Departure_Arrival_time_convenient'])
  Ease_of_Online_booking = int(request.form['Ease_of_Online_booking'])
  
 
  predicao = model.predict([[Age,Type_of_Travel,Customer_Type,Class,Flight_Distance,Inflight_wifi_service,Departure_Arrival_time_convenient,Ease_of_Online_booking]])
  return render_template('resposta.html', predicao=predicao[0])

app.run(debug=True)

# pip install -r requirements.txt (instala as bibliotecas)
# python app.py (para executar)
# git add .
# git commit -m "nomenovo"
# git push