from flask import Flask
import requests
import calendar
from datetime import date

app = Flask(__name__)

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
        dia_data = dia_mes.strftime("%Y-%m-%d")
        print('dia_data ', dia_data, '\n\n')
        dia_info = {
            'dia_mes': dia_mes.day,
            'dia_semana': dia_mes.weekday(),
            'dia_semana_display': dias_semana[dia_mes.weekday()],
            'tem_feriado': dia_data in feriados_formato2.keys(),
            'feriado': feriados_formato2.get(dia_data),
        }
        lista_dias_mes.append(dia_info)
    print('calendario ', calendario, '\n\n')
    print('cal_mes ', cal_mes, '\n\n')
    print('lista_dias_mes', lista_dias_mes, '\n\n')
    print('dias_semana', dias_semana, '\n\n')
    print('feriados', feriados, '\n\n')
    print('feriados_formato2', feriados_formato2, '\n\n')
    return lista_dias_mes

@app.route('/calendario/ano/<ano>')
def calndario(ano):
    meses_do_ano = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
    calendario_ano = {}
    for mes in meses_do_ano:
        cal_mes = list(calendario.itermonthdates(int(ano), int(mes)))
        mes_indice = meses_do_ano.index(mes)
        calendario_ano[mes] = {}
        for dia in cal_mes:
            calendario_ano[mes][dia] = dia.day
    return calendario_ano


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)




