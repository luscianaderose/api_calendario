from flask import Flask
import requests
import calendar
from datetime import date
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

calendario = calendar.Calendar()


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
    
@app.route('/feriados/ano/<int:ano>/mes/<int:mes>')
def feriados_mes(ano, mes):
    resposta = requests.get(f'https://brasilapi.com.br/api/feriados/v1/{ano}')
    if resposta.status_code == 200:
        feriado_mes = []
        for data in resposta.json():
            if f'{ano}-{mes:02d}' in data['date']:
                feriado_mes.append(data)
        return feriado_mes
    else:
        return f'Erro na requisição: {resposta.status_code}'

@app.route('/calendario/ano/<int:ano>/mes/<int:mes>')
def calendario_mes(ano, mes):
    cal_mes = list(calendario.itermonthdates(int(ano), int(mes)))
    lista_dias_mes = []
    dias_semana = ['S', 'T', 'Q', 'Q', 'S', 'S', 'D']
    feriados = feriados_mes(ano, mes)
    feriados_formato2 = {}
    for feriado in feriados:
        data = feriado['date']
        feriados_formato2[data] = feriado['name']
    for dia_mes in cal_mes:
        if dia_mes.month == mes:  # Verificar se o dia pertence ao mês corrente
            dia_data = dia_mes.strftime("%Y-%m-%d")
            dia_info = {
                'dia_mes': dia_mes.day,
                'dia_semana': dia_mes.weekday(),
                'dia_semana_display': dias_semana[dia_mes.weekday()],
                'tem_feriado': dia_data in feriados_formato2.keys(),
                'feriado': feriados_formato2.get(dia_data),
            }
            lista_dias_mes.append(dia_info)
    return lista_dias_mes

@app.route('/calendario/ano/<ano>')
def calndario(ano):
    meses_do_ano = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
    calendario_ano = {}
    for i,mes in enumerate(meses_do_ano):
        calendario_ano[i] = {"mes_display":mes, "dias":calendario_mes(ano, i+1)}
    return calendario_ano


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
