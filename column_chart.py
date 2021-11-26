import pandas as pd #pip install pandas
import numpy as np #pip install numpy
#pip install plotly==5.4.0
import plotly.express as px 
import plotly.graph_objects as go 
import streamlit as st #pip install streamlit
import matplotlib.pyplot as plt #pip install matplotlib 
import folium #pip install folonum


class Column:
    def __init__(self,df):
        self.df = df
        self.country=None
    def choose_chart_column(self):
        """
        Select the country to display the column chart

        input: country

        output: list country
        """
        d_country= self.df['Country'].unique().tolist()
        self.country=st.multiselect('Choose country:',d_country)
    def Data_preprocessing(self):
        """
        Process data into transpose

        input: data

        output: data has been transposed
        """
        self.df=self.df.drop(columns=['Province/State','Lat','Long'])
        self.df=self.df.groupby(by='Country').aggregate(np.sum)
        self.df.index.name='Country'
        self.df = self.df.reset_index()
        self.df=self.df[self.df['Country'].isin(self.country)]
    def cl_chart(self,inf):
        """
        Column chart by feature
        
        input:

            hid: display column name (Comfirmed,deaths,recovered)
            
        output: Column chart by feature
        """
        fig = px.bar(self.df,
                    x='Country',
                    y=inf, 
                    title="The graph shows the total number of infections in a country",
                    color='Country',
                    height=400
                    )
        return fig
    def cl(self):
        """
        Column chart showing all features
        """
        fig=go.Figure(data=[
            go.Bar(name='Confirmed',x=self.country,y=self.df['Confirmed']),
            go.Bar(name='Deaths',x=self.country,y=self.df['Deaths']),
            go.Bar(name='Recovered',x=self.country,y=self.df['Recovered'])
        ])
        fig.update_layout(barmode='group')
        return fig
    