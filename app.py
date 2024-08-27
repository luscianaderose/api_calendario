from flask import Flask
import requests
import calendar

app = Flask(__name__)

@app.route('/')
def home():
    return 'API Calendário OK'

@app.route('/feriados/ano/<ano>')
def feriados(ano):
    resposta = requests.get('https://brasilapi.com.br/api/feriados/v1/' + ano)
    if resposta.status_code == 200:
        return resposta.json()
    elif not resposta:
        return []
    else:
        return f'Erro na requisição: {resposta.status_code}'
    
@app.route('/feriados/ano/<ano>/mes/<mes>')
def feriados_mes(ano, mes):
    resposta = requests.get('https://brasilapi.com.br/api/feriados/v1/' + ano)
    if resposta.status_code == 200:
        feriado_mes = []
        for data in resposta.json():
            #print('data', data)
            #print('ano + mês:', ano + '-' + mes in data['date'])
            if ano + '-' + mes in data['date']:
                feriado_mes.append(data)
        return feriado_mes
        # return resposta.json()
    else:
        return f'Erro na requisição: {resposta.status_code}'

@app.route('/calendario/ano/<ano>/mes/<mes>')
def calendario(ano, mes):
    calendario = calendar.Calendar()
    print(list(calendario.itermonthdates(int(ano), int(mes))))
    return ''




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)




