from flask import Flask
import requests
import calendar
from datetime import date

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
    cal_mes = list(calendario.itermonthdates(int(ano), int(mes)))
    lista_dias_mes = []
    dias_semana = ['S', 'T', 'Q', 'Q', 'S', 'S', 'D']
    feriados = feriados_mes(ano, mes)
    feriados_datas = []
    for feriado in feriados:
        feriados_datas.append(feriado['date'])
    for dia_mes in cal_mes:
        dia_data = ano + '-' + mes + '-' + str(dia_mes.day)
        tem_feriado = dia_data in feriados_datas
        if tem_feriado:
            for feriado in feriados:
                print(dia_data, feriado['date'], feriado['date'] == dia_data)
                if feriado['date'] == dia_data:
                    feriado = feriado['name']
        else:
            feriado = None
        print(feriado)
        dia_info = {
            'dia_mes': dia_mes.day,
            'dia_semana': dia_mes.weekday(),
            'dia_semana_display': dias_semana[dia_mes.weekday()],
            'tem_feriado': dia_data in feriados_datas,
            'feriado': feriado,
        }
        lista_dias_mes.append(dia_info)
    return lista_dias_mes


# 'dia_semana': 'Mon',
# 'dia_mes': 29,


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)




