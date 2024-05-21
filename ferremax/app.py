from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Reemplaza 'YOUR_API_KEY' con tu clave de API real
API_URL = " https://si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx?user=123456789&pass=tuPassword&firstdate=YYYY-MM-DD&lastdate=YYYY-MM-DD&timeseries=codigodeserie&function=GetSeries"

@app.route('/convert', methods=['GET'])
def convert():
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    amount = float(request.args.get('amount'))

    response = requests.get(API_URL)
    data = response.json()

    if from_currency not in data['rates'] or to_currency not in data['rates']:
        return jsonify({"error": "Invalid currency code"}), 400

    from_rate = data['rates'][from_currency]
    to_rate = data['rates'][to_currency]

    converted_amount = (amount / from_rate) * to_rate

    return jsonify({
        "from": from_currency,
        "to": to_currency,
        "amount": amount,
        "converted_amount": converted_amount
    })

if __name__ == '__main__':
    app.run(debug=True)
