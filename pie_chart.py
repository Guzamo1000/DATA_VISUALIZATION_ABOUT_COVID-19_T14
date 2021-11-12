import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pandas import  DataFrame
import matplotlib.pyplot as plt
import streamlit as st



class pie:
    def __init__(self, dl,country) :
        self.dl = dl
        self.country = country
    def Pie_chart(self):
        confirmed_dl=self.dl.drop(columns=['Lat','Long','Province/State','Recovered','Deaths','Active'])
        deaths_dl=self.dl.drop(columns=['Lat','Long','Province/State','Confirmed','Recovered','Active'])
        recovered_dl=self.dl.drop(columns=['Lat','Long','Province/State','Confirmed','Deaths','Active'])


        confirmed_dl=confirmed_dl.groupby(by='Country').aggregate(np.sum).T
        confirmed_dl.index.name='Date'
        confirmed_dl = confirmed_dl.reset_index()
        deaths_dl=deaths_dl.groupby(by='Country').aggregate(np.sum).T
        deaths_dl.index.name='Date'
        deaths_dl = deaths_dl.reset_index()
        recovered_dl=recovered_dl.groupby(by='Country').aggregate(np.sum).T
        recovered_dl.index.name='Date'
        recovered_dl = recovered_dl.reset_index()

        confirmed_melt_dl=confirmed_dl.melt(id_vars='Date').copy()
        confirmed_melt_dl.rename(columns={'value':'Confirmed'}, inplace=True)
        deaths_melt_dl=deaths_dl.melt(id_vars='Date').copy()
        deaths_melt_dl.rename(columns={'value':'Deaths'}, inplace=True)
        recovered_melt_dl=recovered_dl.melt(id_vars='Date').copy()
        recovered_melt_dl.rename(columns={'value':'Recovered'}, inplace=True)

        A=confirmed_melt_dl.copy()
        A['Deaths']=deaths_melt_dl['Deaths']
        A['Recovered']=recovered_melt_dl['Recovered']
        A['% Confirmed']=(((A['Confirmed']-A['Deaths']-A['Recovered'])/A['Confirmed'])*100).round(2)
        A['% Deaths']=((A['Deaths']/A['Confirmed'])*100).round(2)
        A['% Recovered']=((A['Recovered']/A['Confirmed'])*100).round(2)
        list_pie = []
        # country = 'China' 
        for i in range(len(A)):
            if A['Country'][i] == self.country:
                list_pie.append(A['% Confirmed'][i]) 
                list_pie.append(A['% Deaths'][i])
                list_pie.append(A['% Recovered'][i])
    
        nhan=['% Confirmed','% Deaths','% Recovered']
        fig=px.pie(values=list_pie,names= nhan)
        return fig