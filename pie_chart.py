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
        """
        Create pie chart

        input: country
        
        ounput: fig (Pie chart)
        """
        self.dl=self.dl.drop(columns=['Lat','Long','Province/State','Active'])
        self.dl=self.dl.groupby(by='Country').aggregate(np.sum)
        self.dl.index.name='Country'
        self.dl = self.dl.reset_index()
        A=self.dl.copy()      
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