import plotly.plotly as py
import plotly
import pandas as pd
import os

df = pd.read_excel("dude.xlsx")

df['text'] = ''

scl = [[0, "rgb(248, 67, 41)"], [.1, "rgb(248, 67, 41)"], [.2, "rgb(248, 67, 41)"], [0.3, "rgb(248, 67, 41)"],
       [.4, "rgb(248, 67, 41)"], [.5, "rgb(248, 67, 41)"], [.6, "rgb(45, 230, 67)"], [.7, "rgb(45, 230, 67)"],
       [.8, "rgb(45, 230, 67)"], [.9, "rgb(45, 230, 67)"], [1, "rgb(45, 230, 67)"]]

data = [ dict(
        type = 'scattergeo',
        locationmode = 'USA-states',
        lat= df['longitude'],
        lon = df['latitude'],
        text = df['text'],
        mode = 'markers',
        marker = dict(
            size = 4,
            sizeref = 2. * 5000 / (8 ** 2),
            opacity = 0.5,
            reversescale = True,
            autocolorscale = False,
            symbol = 'circle',
            colorscale = scl
        ))]

layout = dict(
        title = '"dude" Usage Locations',
        colorbar = True,
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5
        ),
    )

fig = dict(data=data, layout=layout)
plotly.offline.plot(fig, validate=False, filename='dude_locations.html')