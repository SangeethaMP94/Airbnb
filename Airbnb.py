import pandas as pd 
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import webbrowser 

st.set_page_config(page_title="AIRBNB-Analysis",layout="wide")

df = pd.read_csv(r"C:\Users\sangeetha\New folder\Airbnb.csv")
 
with st.sidebar:
    main = option_menu(None, ['Home','About','Explore Data','Overview'])

if main == "Home":
    st.title("AIRBNB ANALYSIS")
    st.write("This project aims to analyze Airbnb data using MongoDB Atlas, perform data cleaning and preparation, develop interactive geospatial visualizations, and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends.")
    
    
    st.text('''Technologies used:
                    *Python scripting
                    *Data Preprocessing
                    *Visualization
                    *EDA 
                    *Streamlit 
                    *MongoDb 
                    *PowerBI''')
    st.write("Email Id: sangeethamp94@gmail.com")
    st.write("Linkedin Id: https://www.linkedin.com/in/sangeetha-m-a66aa1251/")
      
 
if main == 'About':
    col1,col2 = st.columns(2)

    with col1:
        url = "https://www.theriver.asia/wp-content/uploads/2020/01/pngkey.com-airbnb-logo-png-605967.png"
        st.image(url)
        
    with col2:
      st.write("Airbnb is an American San Francisco-based company operating an online marketplace for short- and long-term homestays and experiences. The company acts as a broker and charges a commission from each booking. The company was founded in 2008 by Brian Chesky, Nathan Blecharczyk, and Joe Gebbia. Airbnb is a shortened version of its original name, AirBedandBreakfast.com. The company is credited with revolutionizing the tourism industry, while also having been the subject of intense criticism by residents of tourism hotspot cities like Barcelona and Venice for enabling an unaffordable increase in home rents, and for a lack of regulation.")


if main == 'Explore Data':
    
    option = st.selectbox("Select any one ",( "Based on Price","Based on availability","Based On Ratings","Based On Host"))
    country = st.sidebar.multiselect('Select a Country',sorted(df.country.unique()))
  
    if option == "Based on Price":
        
        query = f'country in {country}'
        
        con_df = df.groupby('country')['price'].mean().reset_index(name = 'Price')
        fig = px.scatter_geo(con_df,
                             locations = 'country',
                             color = 'Price',
                             title = 'Average price on each country in Geomap ',
                             hover_data = ['Price'],
                             locationmode = 'country names',
                             size = 'Price',
                             projection ='robinson')
        st.plotly_chart(fig)
        
        df0 = df.query(query).groupby("property_type")["price"].size().reset_index(name = "Price").sort_values(by='Price',ascending = True)[:10]
        fig = px.bar(df0,
                    title = "Property Type Based On Price",
                    x = 'property_type',
                    y = 'Price',
                    color = 'property_type')
      
        st.plotly_chart(fig)

        df1 = df.query(query).groupby("room_type")["price"].size().reset_index(name = "Price").sort_values(by='Price',ascending = True)[:10]
        fig = px.bar(df1,
                    title = "Room Type Based On Price ",
                    x = 'room_type',
                    y = 'Price',
                    color = 'room_type')
        st.plotly_chart(fig)

        df2 = df.query(query).groupby("bed_type")["price"].size().reset_index(name = 'Price')
        fig = px.bar(df2,
                      title = "Bed Type Based On Price",
                      x = 'bed_type',
                      y = 'Price',
                      color = 'bed_type')
        st.plotly_chart(fig)

    if option == "Based on availability":
        
        ava = st.sidebar.selectbox('select a availability',('availability_30','availability_60','availability_90','availability_365'))
        
        query = f'country in {country}' 

        if ava == 'availability_30':
            
            df3 = df.query(query).groupby("availability_30")["minimum_nights"].size().reset_index(name = "MinimumNights")
            df4 = df.query(query).groupby("availability_30")["maximum_nights"].size().reset_index(name = "MaximumNights")
            df5 = pd.merge(df3,df4,on='availability_30')
            fig = px.scatter(df5,
                            title = 'Based On Availability_30',
                            x = 'availability_30',
                            y = 'MaximumNights',
                            color = 'MinimumNights',
                            color_continuous_scale = px.colors.sequential.Agsunset)
            st.plotly_chart(fig)

        if ava == 'availability_60':
            
            df6 = df.query(query).groupby("availability_60")["minimum_nights"].size().reset_index(name = "MinimumNights")
            df7 = df.query(query).groupby("availability_60")["maximum_nights"].size().reset_index(name = "MaximumNights")
            df8 = pd.merge(df6,df7,on='availability_60')
            fig = px.scatter(df8,
                            title = 'Based On Availability_60',
                            x = 'availability_60',
                            y = 'MaximumNights',
                            color = 'MinimumNights',
                            color_continuous_scale = px.colors.sequential.Agsunset)
            st.plotly_chart(fig)

        if ava == 'availability_90':

            df9 = df.query(query).groupby("availability_90")["minimum_nights"].size().reset_index(name = "MinimumNights")
            df10 = df.query(query).groupby("availability_90")["maximum_nights"].size().reset_index(name = "MaximumNights")
            df11 = pd.merge(df9,df10,on='availability_90')
            fig = px.scatter(df11,
                            title = 'Based On Availability 90',
                            x = 'availability_90',
                            y = 'MaximumNights',
                            color = 'MinimumNights',
                            color_continuous_scale = px.colors.sequential.Agsunset)
            st.plotly_chart(fig)

        if ava == 'availability_365':    

            df12 = df.query(query).groupby("availability_365")["minimum_nights"].size().reset_index(name = "MinimumNights")
            df13 = df.query(query).groupby("availability_365")["maximum_nights"].size().reset_index(name = "MaximumNights")
            df14 = pd.merge(df12,df13,on='availability_365')
            fig = px.scatter(df14,
                            title = 'Based On Availability 365',
                            x = 'availability_365',
                            y = 'MaximumNights',
                            color = 'MinimumNights',
                            color_continuous_scale = px.colors.sequential.Agsunset)
            st.plotly_chart(fig)

    if option == "Based On Host":
        
        query = f'country in {country}' 

        df2 = df.query(query).groupby(["host_name"]).size().reset_index(name="Listings").sort_values(by='Listings',ascending=False)[:10]
        fig = px.bar(df2,
                      title='Top 10 Hosts with Highest number of Listings',
                      x='Listings',
                      y='host_name',
                      orientation='h',
                      color='host_name',
                      color_continuous_scale=px.colors.sequential.Agsunset)
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig,use_container_width=True)

    if option == "Based On Ratings":
        
        query = f'country in {country}'
        
        con_df = df.groupby('country')['review_scores'].mean().reset_index(name = 'Rate')
        fig = px.scatter_geo(con_df,
                             locations = 'country',
                             color = 'Rate',
                             title = 'Average rate on each country in Geomap ',
                             hover_data = ['Rate'],
                             locationmode = 'country names',
                             size = 'Rate',
                             projection ='robinson')
        st.plotly_chart(fig)
        
        df0 = df.query(query).groupby("property_type")["review_scores"].size().reset_index(name = "Rate").sort_values(by='Rate',ascending = True)[:10]
        fig = px.pie(df0,
                    title = "Property Type Based On Rate",
                    names = 'property_type',
                    values = 'Rate',
                    hole = 0.5)
        st.plotly_chart(fig)

        df1 = df.query(query).groupby("room_type")["review_scores"].size().reset_index(name = "Rate").sort_values(by='Rate',ascending = True)[:10]
        fig = px.pie(df0,
                    title = "Property Type Based On Rate",
                    names = 'property_type',
                    values = 'Rate',
                    hole = 0.5)
        st.plotly_chart(fig)

        df2 = df.query(query).groupby("bed_type")["review_scores"].size().reset_index(name = 'Rate')
        fig = px.pie(df2,
                      title = "Bed Type Based On Rate",
                      names = 'bed_type',
                      values = 'Rate',
                      hole = 0.5)
        st.plotly_chart(fig)

if main == 'Overview':
                
        st.subheader("Airbnb Analysis in Map view")
        df = df.rename(columns={"Latitude": "lat", "Longitude": "lon"})

        st.map(df)
