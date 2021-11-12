from Layout import Layout as ly
from mapword import Map
import streamlit as st
import pandas as pd
from streamlit_folium import folium_static
from column_chart import Column as c
from chart_line import Line as l
from Statistics import Statistical_data_visualization as S
from pie_chart import pie as p
 # chart column
def char_column(data_maps):
    """Create column chart"""
    st.header("Overall chart for 1 country")
    cl=c(data_maps.copy())
    cl.choose_chart_column()
    col=st.radio('Type:',('Comfirmed', 'Deaths', 'Recovered'))
    cl.Data_preprocessing()
    if st.button('Show',key="1"):
        if col == 'Comfirmed':
            st.plotly_chart(cl.cl_chart('Confirmed'))
        elif col=='Deaths':
            st.plotly_chart(cl.cl_chart('Deaths'))
        elif col=='Recovered':
            st.plotly_chart(cl.cl_chart('Recovered'))
        else: st.caption('No style selected')


#Line Chart
def Line_chart(df):
    """Create Line chart"""
    
    country=st.text_input('Name country') 
    date_first,date_last=ly.run_time()
    df=df.drop(columns=['Province/State','Lat','Long'])
    # st.pyplot(Line.chart_line())
    if st.button('Performances'):
        if str(date_first)>str(date_last):
            st.text('Invalid date')
        else:
            Line=l(df,country,str(date_first),str(date_last))
            # Line.Data_preprocessing()
            d=Line.chart_line()
            if d is not None:
                st.plotly_chart(Line.chart_line())
    else: st.info("Please select the country and time period you want to show")
    



#map word
def map_word(data_maps):
    """Create map word"""
    st.header("Map of infection distribution")
    df=data_maps
    date=ly.time()  
    maps=Map(data_maps,str(date))
    m=maps.datamap()
    if st.button('Show maps'):
        if m==0: st.error('Date not in data')
        else:
            folium_static(m)
    else: st.warning('No date selected')

def pie_chart(df):
    d_country=df['Country'].unique().tolist()
    country=st.selectbox("Country",tuple(d_country))
    if st.button("Filter"):
        pie=p(df,country)
        st.plotly_chart(pie.Pie_chart())
    else: st.warning("Please select a country")
#Statistics
def statistics(dt):
    """Statistics data"""
    Sta=S(dt)
    c,d=Sta.Data_preprocessing()
    #country
    country_max_comfirmed  , number_country_max_comfirmed , country_min_comfirmed, number_country_min_comfirmed = Sta.By_country(c,inf='Confirmed')
    country_max_deaths , number_country_max_deaths, country_min_deaths  , number_country_min_deaths = Sta.By_country(c,inf='Deaths')
    country_max_recovered  , number_country_max_recovered, country_min_recovered , number_country_min_recovered = Sta.By_country(c,inf='Recovered')
    #date
    days_ave_confirmed, days_max_confirmed, days_min_confirmed, date_max_confirmed, date_min_confirmed=Sta.Date_handling(d,inf='Confirmed')
    days_ave_deaths, days_max_deaths, days_min_deaths, date_max_deaths, date_min_deaths=Sta.Date_handling(d,inf='Deaths')
    days_ave_recovered, days_max_recovered, days_min_recovered, date_max_recovered, date_min_recovered=Sta.Date_handling(d,inf='Recovered')
    total_country_confirmed=Sta.total_country(c)
    st.markdown(f'Number of countries with Covid-19 cases: {total_country_confirmed}/195')
    op=st.radio("object selection",('None','Country','Word'))
    if op == 'Country':
        d_country= dt['Country'].unique().tolist() 
        p=st.selectbox('Choose country',d_country)
        if st.button("Filter"):
            date_max_confirmed,date_min_confirmed,days_max_confirmed,days_min_confirmed,avg_confirmed=Sta.by_country(p,'Confirmed')
            date_max_deaths,date_min_deaths,days_max_deaths,days_min_deaths,avg_deaths=Sta.by_country(p,'Deaths')
            date_max_recovered,date_min_recovered,days_max_recovered,days_min_recovered,avg_recorered=Sta.by_country(p,'Recovered')
            col1,col2,col3=st.columns(3)
            with col1: 
                st.subheader("Comfirmed")
                st.caption(f"Average in National: {avg_confirmed}")
                st.caption(f"Total date max: {days_max_confirmed}({date_max_confirmed})")
                st.caption(f"Total date min: {days_min_confirmed}({date_min_confirmed})")                
            with col2:
                st.subheader("Deaths")
                st.caption(f"Average in National: {avg_deaths}")
                st.caption(f"Total date max: {days_max_deaths}({date_max_deaths})")
                st.caption(f"Total date min: {days_min_deaths}({date_min_deaths})")
            with col3:
                st.subheader("Recovered")
                st.caption(f"Average in National: {avg_recorered}")
                st.caption(f"Total date max: {days_max_recovered}({date_max_recovered})")
                st.caption(f"Total date min: {days_min_recovered}({date_min_recovered})")

    elif op == 'Word':
        if st.button('filter'):
            col1,col2,col3=st.columns(3)
            with col1:
                
            
                st.subheader('Confirmed by country: ')
                st.caption(f"Country max: {country_max_comfirmed}({number_country_max_comfirmed})")
                st.caption(f"Country min: {country_min_comfirmed}({number_country_min_comfirmed})")
                st.subheader('Confirmed by date: ')
                st.caption(f'Avegare in word: {days_ave_confirmed}')
                st.caption(f'Day max: {date_max_confirmed}({days_max_confirmed})')
                st.caption(f'Day min: {date_min_confirmed}({days_min_confirmed})')
                
            with col2:
                st.subheader('Deaths by country')
                st.caption(f"Country max: {country_max_deaths}({number_country_max_deaths})")
                st.caption(f"Country min: {country_min_deaths}({number_country_min_deaths})")
                st.subheader('Deaths by date: ')
                st.caption(f'Avegare in word: {days_ave_deaths}')
                st.caption(f'Day max: {date_max_deaths}({days_max_deaths})')
                st.caption(f'Day min: {date_min_deaths}({days_min_deaths})')
            
            with col3:
                st.subheader('Recovered by country')
                st.caption(f"Country max: {country_max_recovered}({number_country_max_recovered})")
                st.caption(f"Country min: {country_min_recovered}({number_country_min_recovered})")
                st.subheader('Recovered by date: ')
                st.caption(f'Avegare in word: {days_ave_recovered}')
                st.caption(f'Day max: {date_max_recovered}({days_max_recovered})')
                st.caption(f'Day min: {date_min_recovered}({days_min_recovered})')
def main():
    st.title("Data visualization about covid-19")
    ly.Title()
    upload_file_maps=None,None,None,None

    upload_file_maps=ly.upload_data()

    global data_maps
    if upload_file_maps is not None: 
        #read data
        data_maps=pd.read_csv(upload_file_maps)

        st.sidebar.text('Choose a representative number')
        st.sidebar.text('1. Column chart')
        st.sidebar.text('2. Line chart')
        st.sidebar.text('3. Map word')
        st.sidebar.text("4. Pie chart")
        st.sidebar.text("5. Statistics")
        option = None
        option = st.sidebar.number_input('Insert a number',step=1)
        if option is not None:
            if option == 1:
                char_column(data_maps.copy())
            elif option==2:
                Line_chart(data_maps.copy())
            elif option == 3:
                map_word(data_maps.copy())
            elif option == 4:
                # st.header('None')
                pie_chart(data_maps.copy())
            elif option == 5:
                st.title('Statistics')
                statistics(data_maps.copy())
            elif option>5: 
                st.sidebar.warning("Please select only 1 to 5")
if __name__=="__main__":
    main()



   
   
    