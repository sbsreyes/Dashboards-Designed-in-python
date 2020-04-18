import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(56)

x_values = np.linspace(0,1,100)
y_values = np.random.randn(100)

trace0 = go.Scatter(x = x_values, y = y_values+5,
                   mode = 'markers', name = 'markers')

trace1=go.Scatter(x = x_values, y = y_values,
                  mode = 'lines', name = 'My Lines')#names puede ser el nombre que yo quiera
                                 #name es el nombre del label del grafico
trace2 = go.Scatter(x = x_values, y = y_values-5,
                   mode = 'lines+markers', name = 'my favorite')

data0= [trace0] #Esta es una opcion para dibujar un solo grafico

data  = [trace0, trace1, trace2]

layout = go.Layout(title='Line Char')

fig = go.Figure(data = data, layout = layout)

pyo.plot(fig, filename = 'index.html')
