# from flask import Flask, jsonify
# import requests
# import calendar
# from datetime import date
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# calendario = calendar.Calendar()

# @app.route('/')
# def home():
#     return 'API Calendário OK'

# @app.route('/feriados/ano/<ano>')
# def feriados(ano):
#     resposta = requests.get('https://brasilapi.com.br/api/feriados/v1/' + ano)
#     if resposta.status_code == 200:
#         return jsonify(resposta.json())
#     else:
#         return f'Erro na requisição: {resposta.status_code}'

# @app.route('/feriados/ano/<int:ano>/mes/<int:mes>')
# def feriados_mes(ano, mes):
#     resposta = requests.get(f'https://brasilapi.com.br/api/feriados/v1/{ano}')
#     if resposta.status_code == 200:
#         feriados = resposta.json()
#         feriado_mes = [data for data in feriados if f'{ano}-{mes:02d}' in data['date']]
#         return jsonify(feriado_mes)
#     else:
#         return f'Erro na requisição: {resposta.status_code}'

# @app.route('/calendario/ano/<int:ano>/mes/<int:mes>')
# def calendario_mes(ano, mes):
#     cal_mes = list(calendario.itermonthdays(ano, mes))
#     lista_dias_mes = []
#     dias_semana = ['S', 'T', 'Q', 'Q', 'S', 'S', 'D']
    
#     try:
#         feriados = feriados_mes(ano, mes).json()
#         feriados_formato2 = {feriado['date']: feriado['name'] for feriado in feriados}
        
#         for dia in cal_mes:
#             if dia == 0:
#                 continue
#             dia_data = date(ano, mes, dia).strftime("%Y-%m-%d")
#             dia_info = {
#                 'dia_mes': dia,
#                 'dia_semana': date(ano, mes, dia).weekday(),
#                 'dia_semana_display': dias_semana[date(ano, mes, dia).weekday()],
#                 'tem_feriado': dia_data in feriados_formato2,
#                 'feriado': feriados_formato2.get(dia_data),
#             }
#             lista_dias_mes.append(dia_info)

#         return jsonify(lista_dias_mes)
#     except Exception as e:
#         return str(e), 500

# @app.route('/calendario/ano/<ano>')
# def calendario_ano(ano):
#     meses_do_ano = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
#     calendario_ano = {}
#     for i, mes in enumerate(meses_do_ano):
#         calendario_ano[i] = {"mes_display": mes, "dias": calendario_mes(int(ano), i + 1)}
    
#     return jsonify(calendario_ano)

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)



















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
            #print('data', data)
            #print('ano + mês:', ano + '-' + mes in data['date'])
            if f'{ano}-{mes:02d}' in data['date']:
                feriado_mes.append(data)
        return feriado_mes
        # return resposta.json()
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
            #print('dia_data ', dia_data, '\n\n')
            dia_info = {
                'dia_mes': dia_mes.day,
                'dia_semana': dia_mes.weekday(),
                'dia_semana_display': dias_semana[dia_mes.weekday()],
                'tem_feriado': dia_data in feriados_formato2.keys(),
                'feriado': feriados_formato2.get(dia_data),
            }
            lista_dias_mes.append(dia_info)
    # print('calendario ', calendario, '\n\n')
    # print('cal_mes ', cal_mes, '\n\n')
    # print('lista_dias_mes', lista_dias_mes, '\n\n')
    # print('dias_semana', dias_semana, '\n\n')
    # print('feriados', feriados, '\n\n')
    # print('feriados_formato2', feriados_formato2, '\n\n')
    return lista_dias_mes

@app.route('/calendario/ano/<ano>')
def calndario(ano):
    meses_do_ano = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
    calendario_ano = {}
    for i,mes in enumerate(meses_do_ano):
        calendario_ano[i] = {"mes_display":mes, "dias":calendario_mes(ano, i+1)}
        #print('i,mes', i+1,mes)
    return calendario_ano


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)




