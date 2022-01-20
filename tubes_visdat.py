# -*- coding: utf-8 -*-
"""Tubes_Visdat.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OO1zmjSOrtfQZk6gUmzdY7L8k9h4JDOm
"""

pip install bokeh

import pandas as pd
from bokeh.plotting import figure, show
from bokeh.io import curdoc
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.models import CategoricalColorMapper
from bokeh.palettes import Spectral11
from bokeh.layouts import widgetbox, row, gridplot
from bokeh.models import Slider, Select
from bokeh.io import output_file, output_notebook
from bokeh.models.widgets import Tabs, Panel

ds1 = pd.read_csv("DataSet1.csv", parse_dates=['date'])
ds1.head()

ds1["Name"] = "DataCovid"
ds1

ds1['Name'].unique()

newDS1 = ds1
newDS1 = newDS1.sort_values(['date', 'Name'])
newDS1.head()

DataCovid = newDS1[newDS1['Name'] == 'DataCovid']

output_notebook()

DataCovid

output_file('index.html',
            title='data terkonfirmasi positif berdasarkan kurun waktu')
dt_covid = ColumnDataSource(DataCovid)

tooltips = [('Name', '@Name'), ('acc_confirmed', '@acc_confirmed'), ('new_confirmed', '@new_confirmed'),('acc_negative', '@acc_negative')]

covidFig = figure(x_axis_type= 'datetime',
                  plot_height=500, plot_width=1000,
                  title='data covid', 
                  x_axis_label='Tanggal', y_axis_label='acc confirmed',  tooltips=tooltips)

covidFig2 = figure(x_axis_type= 'datetime',
                  plot_height=500, plot_width=1000,
                  title='data covid', 
                  x_axis_label='Tanggal', y_axis_label='new confirmed',  tooltips=tooltips)

covidFig3 = figure(x_axis_type= 'datetime',
                  plot_height=500, plot_width=1000,
                  title='data covid', 
                  x_axis_label='Tanggal', y_axis_label='acc negative',  tooltips=tooltips)

covidFig.line('date', 'acc_confirmed', 
         color='red', legend_label='DataCovid',
         line_width=1, 
         source=dt_covid)

covidFig2.line('date', 'new_confirmed', 
         color='red', legend_label='DataCovid',
         line_width=1, 
         source=dt_covid)

covidFig3.line('date', 'acc_negative', 
         color='red', legend_label='DataCovid',
         line_width=1, 
         source=dt_covid)

covidFig.legend.location = 'top_left'
covidFig2.legend.location = 'top_left'
covidFig3.legend.location = 'top_left'

covidFig.legend.click_policy = 'hide'
covidFig2.legend.click_policy = 'hide'
covidFig3.legend.click_policy = 'hide'

cv = Panel(child= covidFig, title='acc_confirmed')
cv2 = Panel(child= covidFig2, title='new_confirmed')
cv3 = Panel(child= covidFig3, title='acc_negative')

tabs = Tabs(tabs=[cv, cv2, cv3])
show(tabs)