from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

tiposIndicador = ['Estrés hídrico', 'Nitrógeno foliar', 'Índice cosecha', 'Densidad volumétrica radial']

@app.route("/crearIndicador", methods=['GET'])
def crearIndicador():
    return render_template('CrearIndicador.html', listaTipos = tiposIndicador)

@app.route("/listarIndicadores", methods=['GET'])
def listarIndicadores():
    lista_indicadores = requests.get('https://api-evergreen-391.azurewebsites.net/indicadores').json()
    return render_template('ListarIndicadores.html', lista = lista_indicadores)

@app.route("/guardarIndicador", methods=['POST'])
def guardarIndicador():
    indicador = dict(request.values)
    indicador['prioridad'] = int(indicador['prioridad'])
    indicador['codigo'] = int(indicador['codigo'])
    requests.post('https://api-evergreen-391.azurewebsites.net/indicadores', json=indicador)
    return(crearIndicador())

