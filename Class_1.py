#basic py
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)
#this information is in order to create new scatter plot
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

data = [go.Scatter(x= random_x,
                   y = random_y,
                   mode= 'markers',
                   marker = dict(
                    size = 12,
                    color ='rgb(51,204,153)',
                    symbol = 'circle',
                    line = dict(width = 2)
                   ),)]#remove maker only to see what happens

layout = go.Layout(title = 'Hello first plot', xaxis = {'title':'My random X Axis'},
                                               yaxis= dict(title = "My random Y Axis"),
                                               hovermode = 'closest')

fig = go.Figure(data = data, layout=layout)

pyo.plot(fig, filename='index.html')
