import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import matplotlib.pyplot as plt
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
        Show column chart
        
        input:

            hid: display column name (Comfirmed,deaths,recovered)
            
        output: Column chart
        """
        fig = px.bar(self.df, x='Country', y=inf, color='Country', title="The graph shows the total number of infections in a country")
        return fig