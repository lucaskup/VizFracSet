# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 16:01:46 2020

@author: LKUPSSINSKU
"""

import plotly.express as px
import plotly.graph_objects as go
fig = go.Figure()

#N fractures
data = [5,9,6,10,18,16,15,8,7,5,2,12]

#total size
data = [84.93,102.29,70.73,85.02,261.43,142.66,110.5,74.42,57.38,33.72,17.27,168.76]
#mean size
#data = [16.986,11.36555556,11.78833333,8.502,14.52388889,8.91625,7.366666667,9.3025,8.197142857,6.744,8.635,14.06333333]
#N weight lenght
#data = [35.12,76.14,35.1,70.32,389.19,188.78,137.08,49.24,33.22,13.94,2.86,167.49]




_theta = []
size = 180//len(data)
for i in range(len(data)):
    _theta.append(size/2 + size * (i))
_width = [size]*len(_theta)


N_data = data[0:2] + data[-2:]
N_theta = _theta[0:2] + _theta[-2:]

NE_data = data[2:4] 
NE_theta = _theta[2:4]

E_data = data[4:8] 
E_theta = _theta[4:8]

SE_data = data[8:10] 
SE_theta = _theta[8:10] 

def add_trace(r,theta,size,name,color):

    fig.add_trace(go.Barpolar(
        r=r,
        theta = theta,
        width=[size]*len(theta),
        name=name,
        marker_color=color,
        marker_line_color="black",
        marker_line_width=1,
        opacity=0.8
    ))
    
#"#E4FF87", '#709BFF', '#709BFF', '#FFAA70', '#FFAA70', '#FFDF70', '#B6FFB4'
add_trace(N_data*2,N_theta + [x+180 for x in N_theta],size,'North','#FFDF70')
add_trace(NE_data*2,NE_theta + [x+180 for x in NE_theta],size,'North-East','#709BFF')
add_trace(E_data*2,E_theta+ [x+180 for x in E_theta],size,'East','#B6FFB4')
add_trace(SE_data*2,SE_theta + [x+180 for x in SE_theta],size,'South-East','#FFAA70')

# fig.add_trace(go.Barpolar(
#     r=[15,8,7,5,2,13,5,9,6,10,18],
#     theta= _theta[:-1],
#     width=_width[:-1],
#     #name='11-14 m/s',
#     marker_color='rgb(106,81,163)'
# ))

fig.update_layout(
    #template=None,
    #title='Wind Speed Distribution in Laurel, NE',
    font_size=16,
    #legend_font_size=16,
    #polar_radialaxis_ticksuffix='%',
    #polar_angularaxis_rotation=-90,
    polar = dict(
        radialaxis = dict(showticklabels=False, ticks=''),
        angularaxis = dict(direction = "clockwise"),
        )
)
#fig.show()
fig.write_html('first_figure.html', auto_open=True)