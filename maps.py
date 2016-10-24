# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:19:48 2016

@author: Eric
"""

import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('E:/Users/Eric/Documents/ENGL 317/prj3/col_adjusted_salary.csv')

df['Wage dif'] = df['Wage dif'].apply(lambda x: x*100)
df['COL dif'] = df['COL dif'].apply(lambda x: x*100)

for col in df.columns:
    df[col] = df[col].astype(str)

df['text_sal'] = df['state'] + '<br>' +\
                'Annual Median Wage $'+df['Annual median wage']+'<br>'+\
                'dif '+df['Wage dif']+'%'
df['text_col'] = df['state'] + '<br>' +\
                'Annual Mean Cost of Living $'+df['Mean COL']+'<br>'+\
                'dif '+df['COL dif']+'%'

df['text_cpi'] = df['state'] + '<br>' +\
            'Annual Median Wage $'+df['Annual median wage']+'<br>'+\
            'dif '+df['Wage dif']+'%'+'<br>'+\
            'Mean Cost of Living $'+df['Mean COL']+'<br>'+\
            'dif '+df['COL dif'] + '%'

    
    
# SALARY DATA    
scl_sal = [[0.0, 'rgb(242,240,247)'],[1.0, 'rgb(0,0,255)']]
             
data_sal = [ dict(
        type='choropleth',
        colorscale = scl_sal,
        autocolorscale = False,
        locations = df['code'],
        z = df['Annual median wage'].astype(float),
        locationmode = 'USA-states',
        text = df['text_sal'],
        marker = dict(
            line = dict (
                color = 'rgb(255,255,255)',
                width = 2
            ) ),
        colorbar = dict(
            title = "Median Salary")
        ) ]

layout_sal = dict(
        title = '2015 Median Salary for Electrical Engineers, USD<br>(Hover for more info)',
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showlakes = True,
            lakecolor = 'rgb(255, 255, 255)'),
             )
        
fig_sal = dict(data=data_sal,layout=layout_sal)
        
# COST OF LIVING
scl_col = [[0.0, 'rgb(242,240,247)'],[1.0, 'rgb(255, 0, 0)']]

data_col = [ dict(
        type='choropleth',
        colorscale = scl_col,
        autocolorscale = False,
        locations = df['code'],
        z = df['Mean COL'].astype(float),
        locationmode = 'USA-states',
        text = df['text_col'],
        marker = dict(
            line = dict (
                color = 'rgb(255,255,255)',
                width = 2
            ) ),
        colorbar = dict(
            title = "Mean Cost of Living")
        ) ]

layout_col = dict(
        title = '2015 Mean Cost of Living, USD<br>(Hover for more info)',
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showlakes = True,
            lakecolor = 'rgb(255, 255, 255)'),
             ) 

fig_col = dict(data=data_col,layout=layout_col)
        
# EFFECTIVE SALARY RATIO
scl_cpi = [[0.0, 'rgb(242,240,247)'],[1.0, 'rgb(0, 153, 7)']]
            
data_cpi = [ dict(
        type='choropleth',
        colorscale = scl_cpi,
        autocolorscale = False,
        locations = df['code'],
        z = df['Mean CPI'].astype(float),
        locationmode = 'USA-states',
        text = df['text_cpi'],
        marker = dict(
            line = dict (
                color = 'rgb(255,255,255)',
                width = 2
            ) ),
        colorbar = dict(
            title = "Effective Salary to CoL Ratio")
        ) ]
        
layout_cpi = dict(
        title = '2015 Salary to Cost of Living for Electrical Engineers<br>(Hover for more info)',
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showlakes = True,
            lakecolor = 'rgb(255, 255, 255)'),
             )    
fig_cpi = dict(data=data_cpi,layout=layout_cpi)

df_cpi_asc = df.sort('Mean CPI', ascending=1)
df_cpi_des = df.sort('Mean CPI', ascending=0)

bestx = df_cpi_des['code'][0:5]
besty = df_cpi_des['Mean CPI'][0:5]
worstx = df_cpi_asc['code'][0:5]
worsty = df_cpi_asc['Mean CPI'][0:5]

name = 'Ratio'

databest = [go.Bar(
            x=bestx,y=besty,
            marker=dict(
                color='rgb(0,128,0)',
                line=dict(
                    color='rgb(8,48,107)',
                    width=1.5),
            ),
            opacity=0.6
        )]

layoutbest = go.Layout(
    title='5 Best States to live in for ratio of median salary to mean CoL',
    annotations=[
        dict(x=xi,y=yi,
             text=str(yi),
             xanchor='center',
             yanchor='bottom',
             showarrow=False,
        ) for xi, yi in zip(bestx, besty)]
)
        
dataworst = [go.Bar(
            x=worstx,y=worsty,
            marker=dict(
                color='rgb(220,20,60)',
                line=dict(
                    color='rgb(8,48,107)',
                    width=1.5),
            ),
            opacity=0.6
        )]

layoutworst = go.Layout(
    title='5 Worst States to live in for ratio of median salary to mean CoL',
    annotations=[
        dict(x=xi,y=yi,
             text=str(yi),
             xanchor='center',
             yanchor='bottom',
             showarrow=False,
        ) for xi, yi in zip(worstx, worsty)]
)

figbest = go.Figure(data=databest, layout=layoutbest)
figworst = go.Figure(data=dataworst, layout=layoutworst)
py.iplot(figbest, filename='best_ratio')
py.iplot(figworst, filename='worst_ratio')


#py.iplot(fig_sal, filename='engl317-sal')
#py.iplot(fig_col, filename='engl317-col')
#py.iplot(fig_cpi, filename='engl317-cpi')