import streamlit as st
import streamlit as st
import numpy as np
import folium
import geopandas as gpd
from streamlit_option_menu import option_menu
from PIL import Image
from streamlit_folium import st_folium
from utils import popupTable
import branca
from pathlib import Path
import pandas as pd
from shapely.geometry import Point, Polygon
import geojson


def check_password():
    """Returns `True` if the user had a correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 User not known or password incorrect")
        return False
    else:
        # Password correct.
        return True
    
if check_password():
   # st.write("Here goes your normal Streamlit app...")
   
# Create a polygon object
# polygon = Polygon(polygon_coordinates)
    df = pd.read_csv('./static/WTGL-RK_names.csv')
    column1 = df['latitude']
    column2 = df['longitude']
    names = df['name']

    tuples = list(zip(column2,column1 ))

    # points_inside_polygon = []
    # for point in tuples:
        # Create a point object
        # point_object = Point(point[0], point[1])

        # # Check if the point is inside the polygon
        # if polygon.contains(point_object):
        #     points_inside_polygon.append(point)

    
    reversed_list = [t[::-1] for t in tuples]

    st.set_page_config(page_title='GalaxEye Space-Transmission Line Monitoring', page_icon='./static/galaxeye.png', layout="wide")




    with st.sidebar:
    
        
        choose = option_menu("GALAXEYE LIVE", ["Dashboard","Environmental Risk","Vegetation Risk","Asset Health Risk","Report Generation","Drone Services"],
                            icons=['graph-up','tree','cloud-upload','cloud-haze2','book'],
                            menu_icon="cast", default_index=0,orientation="horizontal",
                            styles={
            "container": {"padding": "10!important", "background-color": "#26272F","font-size": "20px"},
            "icon": {"color": "white", "font-size": "20px"}, 
            "nav-link": {"font-size": "20px", "text-align": "left", "margin":"10px", "--hover-color": "#0F1116"},
            "nav-link-selected": {"background-color": "#000000"},
        }
        )

    subVertices = [[22.52426667695317,72.75135939931562],
          [22.50143110346603,72.78637848267984],
          [22.497624820613293,72.87632945065815],
          [22.508090827123212,72.8922707189956],
          [22.50380894360244,72.90136881373117],
          [22.503491766651024,72.93810451420431],
          [22.507932248554848,72.9468592832535],
          [22.504760492884056,72.96042059371048],
          [22.501271478037076,72.97896010658636],
          [22.499209745734788,72.98737155230233],
          [22.500954292354166,72.99578299747132],
          [22.498099570545133,73.00093286241506],
          [22.498416766916737,73.01852823288108],
          [22.502624981631488,73.04740249396124],
          [22.52419183493881,73.09066135353656],
          [22.51562893178405,73.10679759685657],
          [22.50928570512058,73.19194202486985],
          [22.52197189211578,73.31965866490191],
          [22.524508994079532,73.45012190051801],
          [22.538462191186436,73.58058513615514],
          [22.52831455316309,73.70143529163948],
          [22.525777525064306,73.79756609695146],
          [22.54226735879663,73.85112468930868],
          [22.576509098350392,73.95824188642979],
          [22.582849282241813,74.0612391926503],
          [22.606939204923812,74.11067787159304],
          [22.625954553646952,74.19856889760656],
          [22.65130424995078,74.37847084152446],
          [22.63609496522175,74.4759749439179],
          [22.641164858934957,74.74514120660525],
          [22.61454554773528,74.83440552093332],
          [22.637362373074627,74.94289600996143],
          [22.684251776281048,74.94838921274732],
          [22.752656184477438,74.92366988169486],
          [22.71719152603556,74.82753906210375],
          [22.745057427765584,74.73278155686532],
          [22.727325288690224,74.5364000414469],
          [22.743790977632116,74.41005669451322],
          [22.723525285556672,74.19032912627254],
          [22.666511872449995,74.04063971758296],
          [22.674115036293244,73.99806750307376],
          [22.598064491831792,73.77284674927408],
          [22.610742508236562,73.57921183808153],
          [22.59806449141164,73.47621454512307],
          [22.57904538066069,73.30523899149597],
          [22.582849316259505,73.19194201765542],
          [22.57904529287275,73.07795832772774],
          [22.548937867733752,73.02473226627882],
          [22.542901503143586,72.94131527814841],
          [22.571436791417746,72.7675931738166]]

    dataframe = gpd.read_file("./static/map_adani.geojson")
    # lats = [20.83466574,20.83398309,20.76151577,20.80874355,20.83466517,20.81658646,20.71486564,20.8347532, 20.82000651,20.81548033]
    # lons = [80.46099093,80.4599096,80.37233492,80.42676978,80.46081031,80.43631223,80.29681496,80.46180345,80.44361421,80.43559392]
    # locations = list(zip(lats,lons ))
    locations = reversed_list
    vertices = [[22.78874298462253,72.75006444954514] ,
          [22.495624127393626,72.75006444954514 ],
          [22.495624127393626,74.95115298423937 ],
          [22.78874298462253,74.95115298423937 ],
          [22.78874298462253,72.75006444954514 ]]

    datastring = './static/adani_row.geojson'
    with open(datastring) as f:
        gj = geojson.load(f)

    verticestuple = gj['features'][0]['geometry']['coordinates'][0]

    verticesROW = [t[::-1] for t in verticestuple]
    logo = Image.open("./static/galaxeye.png")
    if choose =="Dashboard":

        col1,col2 = st.columns([0.94,0.06])
        with col1:
            st.markdown(""" <style> .fonty {
                font-size:95px ; font-family: 'Cooper Black'; color: #ffffff;} 
                </style> """, unsafe_allow_html=True)
            st.title("Transmission Line Risk Assessment")
        with col2:
            st.image(logo, width=130 )

    

        col1, col2 = st.columns( [0.9,0.1])
        with col1:               # To display the header text using css style
            st.markdown(""" <style> .font {
            font-size:35px ; font-family: 'Cooper Black'; color: #ffffff;} 
            </style> """, unsafe_allow_html=True)
            st.markdown('<p class="font">Area Of Interest</p>', unsafe_allow_html=True)    

        
            map = folium.Map(location=[22.606939204923812,74.11067787159304], zoom_start=9, scrollWheelZoom=True, tiles='Stamen Terrain')
            folium.TileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                        attr='ArcGIS',
                        name='Satellite',
                        overlay=True,
                        control=True).add_to(map)


            for l, row in enumerate(dataframe.iterrows()):
                    html = popupTable(dataframe, l)
                    iframe = branca.element.IFrame(html=html,width=700,height=600)
                    popup = folium.Popup(folium.Html(html, script=True), max_width=500)
                    folium.GeoJson(data=row[1][0], popup=popup).add_to(map)
            
            
            for i in range(len(locations)):
                        folium.Marker(location=locations[i],
                        icon= folium.Icon(color='blue',
                        icon_color='yellow',icon ="tower"),popup='Name : {} \n Coordinates: {}'.format(names[i],locations[i])).add_to(map)
            polygon = folium.Polygon(locations=verticesROW, color='black', fill_color=None, fill_opacity=1.0).add_to(map)
            st_map = st_folium(map, width=1100, height=550)
            st.image(Image.open("./static/Dashboard_legend.png"),width=300 )

        # with col2 :
        #     st.image(Image.open("./static/Dashboard_legend.png"))



        
    if choose =="Vegetation Risk":
        col1,col2 = st.columns([0.94,0.06])
        with col1:
            st.markdown(""" <style> .fonty {
                font-size:75px ; font-family: 'Cooper Black'; color: #ffffff;} 
                </style> """, unsafe_allow_html=True)
            st.title(choose)
        with col2:
            st.image(logo, width=130 )

        col1, col2= st.columns(2)
        with col1:
            
            option_3 = st.selectbox("Insight", ["Encroachment Hotspots", "Land Cover Map"])
        # with col2:
        #     Month = st.selectbox("Month", [ "Month"])
        # with col3:
            
            

        Year = "Year"
        
        col1, col2 = st.columns( [0.8, 0.2])
        with col1:               # To display the header text using css style
            st.markdown(""" <style> .font {
            font-size:35px ; font-family: 'Cooper Black'; color: #ffffff;} 
            </style> """, unsafe_allow_html=True)
            option_3_enc_text = "A Map with estimated height of vegetation in or around ROW is used to calculate the potential encroachment\
                                            hotspots. The legend shows the height of trees based on various thresholds in meters"
            option_3_LC_text = "A Land Classification map which shows the type of\
                                                vegetation cover(Trees, shrubs, crops, etc) in or around the ROW\
                                                region of the Transmission line."
            if option_3=="Encroachment Hotspots":
                st.markdown(f"<span style='font-size: 16px'>{option_3_enc_text}</span>", unsafe_allow_html=True)
            else:
                st.markdown(f"<span style='font-size: 16px'>{option_3_LC_text}</span>", unsafe_allow_html=True)

        

        col1, col2 = st.columns( [0.8, 0.2])
        with col1:               # To display the header text using css style
            map = folium.Map(location=[22.5391277778, 73.1608305556], zoom_start=14, scrollWheelZoom=True, tiles='Stamen Terrain')
        
            folium.TileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                    attr='ArcGIS',
                    name='Satellite',
                    overlay=True,
                    control=True).add_to(map)
            #folium.LayerControl().add_to(map)
            
            if option_3 =="Land Cover Map":
                img = folium.raster_layers.ImageOverlay(
                name= option_3,
                image="./static/2023lc.png" ,
                bounds=vertices,
                opacity=1.0,
                interactive=True,
                cross_origin=False,
                zindex=1,
                )

                img.add_to(map)
                for i in range(len(locations)):
                        folium.Marker(location=locations[i],
                        icon= folium.Icon(color='blue',
                        icon_color='yellow',icon ="tower"),popup='Name : {} \n Coordinates: {}'.format(names[i],locations[i])).add_to(map)
            
                    #folium.Marker(location=locations[i],radius=2,color='black').add_to(map)
                polygon = folium.Polygon(locations=verticesROW, color='black', fill_color=None, fill_opacity=1.0).add_to(map)

                st_map = st_folium(map, width=1100, height=550)
                folium.LayerControl().add_to(map)
            
            else:
                img = folium.raster_layers.ImageOverlay(
                name= option_3,
                image="./static/tch_adani.png",
                bounds=vertices,
                opacity=1.0,
                interactive=True,
                cross_origin=False,
                zindex=1,
                )

                img.add_to(map)
                for i in range(len(locations)):
                        folium.Marker(location=locations[i],
                        icon= folium.Icon(color='blue', 
                        icon_color='yellow',icon ="tower"),popup='Name : {} \n Coordinates: {}'.format(names[i],locations[i])).add_to(map)
            
                    #folium.Marker(location=locations[i],radius=2,color='black').add_to(map)
                polygon = folium.Polygon(locations=verticesROW, color='black', fill_color=None, fill_opacity=1.0).add_to(map)

                st_map = st_folium(map, width=1100, height=550)
                folium.LayerControl().add_to(map)

    
        with col2:   
            
            if option_3 =="Land Cover Map":
                st.image(Image.open("./static/LandCover_legend.png"))
            else:
                st.image(Image.open("./static/tch_legend.png"))
                val = "The map here, shows sparse tree cover, because of which this line has low vegetation risk."
                st.markdown(f"<span style='font-size: 13px'>{val}</span>", unsafe_allow_html=True)


    elif choose =="Asset Health Risk":
        col1,col2 = st.columns([0.94,0.06])
        with col1:
            st.markdown(""" <style> .fonty {
                font-size:75px ; font-family: 'Cooper Black'; color: #ffffff;} 
                </style> """, unsafe_allow_html=True)
            st.title(choose)
        with col2:
            st.image(logo, width=130 )

        radio_style = "<style>div.row-widget.stRadio > div{flex-direction:row;font-size:70px;}</style>"
        
    # Display the radio buttons with the custom CSS style
        st.markdown(radio_style, unsafe_allow_html=True)
    
        #structural = st.radio("",["Land Subsidence","Potential Fouling Zones"])
        col1, col2= st.columns(2)
        with col1:
            
            structural = st.selectbox("Insight", ["Land Subsidence", "Potential Fouling Zones","Atmospheric Corrosion"])
        if structural =="Land Subsidence":
            col1, col2 = st.columns( [0.9, 0.1])
            with col1:               # To display the header text using css style
                st.markdown(""" <style> .font {
                font-size:30px ; font-family: 'Cooper Black'; color: #ffffff;} 
                </style> """, unsafe_allow_html=True)
                st.markdown('<p class="font">{}</p>'.format(structural), unsafe_allow_html=True)   
                selected_ground_option_text = "The generated susceptibility map of land subsidence intensities can be used\
                                                to predict the high-susceptibility areas of different land subsidence\
                                                intensities along transmission lines ROW, which is important to the\
                                                planning, design, protection, and operations management of transmission\
                                                line towers.Transmission towers require a solid foundation to support their\
                                            weight and withstand external forces such as wind and seismic activity. \
                                                Foundation problems, such as settling or shifting, can cause towers to\
                                                become unstable and potentially collapse.\
                                                The movement of Towers causes seismic vibrations and it is important to \
                                                monitor the vibrations and take appropriate measures to reduce their impact on nearby structures."
                
                
                st.markdown(f"<span style='font-size: 16px'>{selected_ground_option_text}</span>", unsafe_allow_html=True)

                val = "This is a 1 year displacement map for 2022'March to 2023'March."
                st.markdown(f"<span style='font-size: 12px'>{val}</span>", unsafe_allow_html=True)

                
            

            # col1,col2 = st.columns( [0.7, 0.3])
            # with col1 : 
                #disp = st.selectbox("Displacement Range", ["Entire", "-0.109 to -0.054","-0.054 to 0.001","0.001 to 0.055", "0.055 to 0.11"])
                #dict_ls = {"Entire":"indiGrid","-0.109 to -0.054":'first',"-0.054 to 0.001":'sec',"0.001 to 0.055":'third',"0.055 to 0.11":'four'}
            # with col2:               # To display brand log
            #     st.write(" ")
            #     st.write(" ")
            col1,col2 = st.columns( [0.8, 0.2])

            with col2:
                if structural == "Land Subsidence":
                    st.image(Image.open("./static/ls_legend.png"))
                        
            col1, col2 = st.columns( [0.85, 0.15])
            with col1:               # To display the header text using css style
                map = folium.Map(location=[22.606939204923812,74.11067787159304], zoom_start=11, scrollWheelZoom=True, tiles='Stamen Terrain')
            
                folium.TileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                        attr='ArcGIS',
                        name='Satellite',
                        overlay=True,
                        control=True).add_to(map)
                #folium.LayerControl().add_to(map)
                
                img = folium.raster_layers.ImageOverlay(
                name= structural,
                image="./static/ls_{}.png".format('adani'),
                bounds=subVertices,
                opacity=1.0,
                interactive=True,
                cross_origin=False,
                zindex=1,
                )

                img.add_to(map)
                for i in range(len(locations)):
                    # if locations[i]==(20.71486564, 80.29681496):
                    #     folium.CircleMarker(location=locations[i],radius=30,color='red',line_width=40, opacity=5).add_to(map)
                    folium.Marker(location=locations[i],
                        icon= folium.Icon(color='blue',
                        icon_color='yellow',icon ="tower"),popup='Name : {} \n Coordinates: {}'.format(names[i],locations[i])).add_to(map)
                polygon = folium.Polygon(locations=verticesROW, color='black', fill_color=None, fill_opacity=1.0).add_to(map)

                st_map = st_folium(map, width=1100, height=550)
                folium.LayerControl().add_to(map)
            
            with col2:               # To display brand log

                if structural == "Land Subsidence":
               
                    val = "The positive value means downward displacement and the negative value means upward displacement. Yellow zones are more neutral, whereas darker the shade of blue or red, more displacement is observed"
                    st.markdown(f"<span style='font-size: 13px'>{val}</span>", unsafe_allow_html=True) 
                
         
        
        elif structural == "Potential Fouling Zones":
            col1, col2 = st.columns( [0.7, 0.3])
            with col1:               # To display the header text using css style
                st.markdown(""" <style> .font {
                font-size:30px ; font-family: 'Cooper Black'; color: #ffffff;} 
                </style> """, unsafe_allow_html=True)
                st.markdown('<p class="font">{}</p>'.format(structural), unsafe_allow_html=True)   
                selected_ground_option_text = "An accurate PDM(pollution Distribution Maps) can help in optimising the\
                                            arrangement of monitoring points and promptly clean the more seriously\
                                            fouled insulators to ensure stable equipment operation."
                

                st.markdown(f"<span style='font-size: 16px'>{selected_ground_option_text}</span>", unsafe_allow_html=True)
                val = "The Transmission Towers in the region with high industrial Pollution value are more susceptible to\
                        flash-overs caused by fouling those regions are in yellow - red range"
                st.markdown(f"<span style='font-size: 12px'>{val}</span>", unsafe_allow_html=True)

        
            

            col1, col2 = st.columns( [0.8, 0.2])
            with col1:               # To display the header text using css style
                map = folium.Map(location=[22.606939204923812,74.11067787159304], zoom_start=11, scrollWheelZoom=True, tiles='Stamen Terrain')
            
                folium.TileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                        attr='ArcGIS',
                        name='Satellite',
                        overlay=True,
                        control=True).add_to(map)
                #folium.LayerControl().add_to(map)
                
                img = folium.raster_layers.ImageOverlay(
                name= structural,
                image="./static/{}_adani.png".format("PDM"),
                bounds=vertices,
                opacity=1.0,
                interactive=True,
                cross_origin=False,
                zindex=1,
                )

                img.add_to(map)
                for i in range(len(locations)):
                    if locations[i]==(20.82000651, 80.44361421) or locations[i]==(20.83398309, 80.4599096):
                        folium.CircleMarker(location=locations[i],radius=30,color='red',line_width=50, opacity=5).add_to(map)
                        folium.Marker(location=locations[i],
                            icon= folium.Icon(color='blue',
                            icon_color='yellow',icon ="tower"),popup='Name : {} \n Coordinates: {}'.format(names[i],locations[i])).add_to(map)
                    else:
                        folium.Marker(location=locations[i],
                            icon= folium.Icon(color='blue',
                            icon_color='yellow',icon ="tower"),popup='Name : {} \n Coordinates: {}'.format(names[i],locations[i])).add_to(map)
                polygon = folium.Polygon(locations=verticesROW, color='black', fill_color=None, fill_opacity=1.0).add_to(map)
                

                st_map = st_folium(map, width=1100, height=550)
                folium.LayerControl().add_to(map)
            
                
            with col2:               # To display brand log
                val = "The PDM is in mol/meter-square"
                st.markdown(f"<span style='font-size: 16px'>{val}</span>", unsafe_allow_html=True)
                st.image(Image.open("./static/pdm_leg.png"))
                val = "More susceptible regions are in yellow - red range"
                st.markdown(f"<span style='font-size: 13px'>{val}</span>", unsafe_allow_html=True)


        elif structural == "Atmospheric Corrosion":
            col1, col2 = st.columns( [0.8, 0.2])
            with col1:               # To display the header text using css style
                st.markdown(""" <style> .font {
                font-size:30px ; font-family: 'Cooper Black'; color: #ffffff;} 
                </style> """, unsafe_allow_html=True)
                st.markdown('<p class="font">{}</p>'.format(structural), unsafe_allow_html=True)   
                selected_ground_option_text = "Corrosion is the process of slow eating up \
                    of a metal by the gasses and water vapours present in the air due to the formation of\
                          certain chemical compounds. Polluted air and humid climate can speed up the corrosion process\
                            We try to find the rate of corrosion emperically by combining these factors, namely\
                                humidity, temperature and certain gases like Sulphur Dioxide"
                

                st.markdown(f"<span style='font-size: 16px'>{selected_ground_option_text}</span>", unsafe_allow_html=True)
                val = "The green region have relatively low corrosion rate whereas yellow-red region have higher corrosion rates"
                st.markdown(f"<span style='font-size: 12px'>{val}</span>", unsafe_allow_html=True)

            col1, col2 = st.columns( [0.5, 0.5])
            with col1:
                month = st.selectbox("Months", ["month 1", "month 2","month 3"])


            

            col1, col2 = st.columns( [0.8, 0.2])
            with col1:               # To display the header text using css style
                map = folium.Map(location=[22.606939204923812,74.11067787159304], zoom_start=11, scrollWheelZoom=True, tiles='Stamen Terrain')
            
                folium.TileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                        attr='ArcGIS',
                        name='Satellite',
                        overlay=True,
                        control=True).add_to(map)
                #folium.LayerControl().add_to(map)
                
                img = folium.raster_layers.ImageOverlay(
                name= structural,
                image="./static/{}_corr.png".format(month.split(' ')[1]),
                bounds=vertices,
                opacity=1.0,
                interactive=True,
                cross_origin=False,
                zindex=1,
                )

                img.add_to(map)
                for i in range(len(locations)):
                    if locations[i]==(20.82000651, 80.44361421) or locations[i]==(20.83398309, 80.4599096):
                        folium.CircleMarker(location=locations[i],radius=30,color='red',line_width=50, opacity=5).add_to(map)
                        folium.Marker(location=locations[i],
                            icon= folium.Icon(color='blue',
                            icon_color='yellow',icon ="tower"),popup='Name : {} \n Coordinates: {}'.format(names[i],locations[i])).add_to(map)
                    else:
                        folium.Marker(location=locations[i],
                            icon= folium.Icon(color='blue',
                            icon_color='yellow',icon ="tower"),popup='Name : {} \n Coordinates: {}'.format(names[i],locations[i])).add_to(map)
                polygon = folium.Polygon(locations=verticesROW, color='black', fill_color=None, fill_opacity=1.0).add_to(map)
                

                st_map = st_folium(map, width=1100, height=550)
                folium.LayerControl().add_to(map)
            
                
            with col2:               # To display brand log
                # val = "The PDM is in mol/meter-square"
                # st.markdown(f"<span style='font-size: 16px'>{val}</span>", unsafe_allow_html=True)
                st.image(Image.open("./static/corr_leg.png"))
                val = "More susceptible regions are in yellow - red range"
                st.markdown(f"<span style='font-size: 13px'>{val}</span>", unsafe_allow_html=True)



    elif choose == "Environmental Risk":
        col1,col2 = st.columns([0.94,0.06])
        with col1:
            st.markdown(""" <style> .fonty {
                font-size:75px ; font-family: 'Cooper Black'; color: #ffffff;} 
                </style> """, unsafe_allow_html=True)
            st.title(choose)
        with col2:
            st.image(logo, width=130 )

        col1, col2= st.columns(2)
        # with col1:
        #     Year = st.selectbox("Year", ["Year"])
        # with col2:
        #     Month = st.selectbox("Month", ["Month"])
        with col1:
            
            option_3 = st.selectbox("Insight", ["Temperature", "Moisture Index","Fire Hotspots"])

        col1, col2 = st.columns( [0.8, 0.2])
        with col1:               # To display the header text using css style
            st.markdown(""" <style> .font {
            font-size:35px ; font-family: 'Cooper Black'; color: #ffffff;} 
            </style> """, unsafe_allow_html=True)
            FireHotspots_text= "This map is used to identify drought conditions that pose a fire risk by correlating the\
                                vegetation and soil Moisture Index and the surface Temperature. The heat from the fire around the\
                                    region causes damage to the transmission line."
            LandSurfaceTemperature_text = "The Surface Temperature map here demonstrates the heat dispersion over the ROW, with a higher value \
                                            recorded when the intensity of radiation is higher. This is useful for identifying the\
                                                greenhouse effect in the area. A rise in Surface Temperature could lead to dry conditions."
            VegetationMoistureIndex_text = "The water content is calculated by NDMI, and water stress is indicated by the negative\
                                            values as they go closer to -1 and waterlogging as they get closer to +1. Thus, a\
                                                region's agronomic situation is addressed."

            if option_3 == "Fire Hotspots":
                option_3text = FireHotspots_text
            elif option_3 == "Temperature":
                option_3text = LandSurfaceTemperature_text
            elif option_3 == "Moisture Index":
                option_3text = VegetationMoistureIndex_text
                
        
            st.markdown(f"<span style='font-size: 16px'>{option_3text}</span>", unsafe_allow_html=True)
            


        

        col1, col2 = st.columns( [0.8, 0.2])
        with col1:               # To display the header text using css style
            if option_3 == "Temperature":
                map = folium.Map(location=[22.606939204923812,74.11067787159304], zoom_start=11, scrollWheelZoom=True, tiles='Stamen Terrain')
            
                folium.TileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                        attr='ArcGIS',
                        name='Satellite',
                        overlay=True,
                        control=True).add_to(map)
                #folium.LayerControl().add_to(map)
                
                img = folium.raster_layers.ImageOverlay(
                name= option_3,
                image="./static/hotspot2.png",
                bounds=vertices,
                opacity=1.0,
                interactive=True,
                cross_origin=False,
                zindex=1,
                )

                img.add_to(map)
                for i in range(len(locations)):
                        folium.Marker(location=locations[i],
                        icon= folium.Icon(color='blue',
                        icon_color='yellow',icon ="tower"),popup='Name : {} \n Coordinates: {}'.format(names[i],locations[i])).add_to(map)
            
                polygon = folium.Polygon(locations=verticesROW, color='black', fill_color=None, fill_opacity=1.0).add_to(map)

                st_map = st_folium(map, width=1100, height=550)
                folium.LayerControl().add_to(map)
                
            
            elif option_3 == "Moisture Index":
                map = folium.Map(location=[22.606939204923812,74.11067787159304], zoom_start=11, scrollWheelZoom=True, tiles='Stamen Terrain')
            
                folium.TileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                        attr='ArcGIS',
                        name='Satellite',
                        overlay=True,
                        control=True).add_to(map)
                #folium.LayerControl().add_to(map)
                
                img = folium.raster_layers.ImageOverlay(
                name= option_3,
                image="./static/NDMIApril1.png",
                bounds=vertices,
                opacity=1.0,
                interactive=True,
                cross_origin=False,
                zindex=1,
                )

                img.add_to(map)
                for i in range(len(locations)):
                        folium.Marker(location=locations[i],
                        icon= folium.Icon(color='blue',
                        icon_color='yellow',icon ="tower"),popup='Name : {} \n Coordinates: {}'.format('name',locations[i])).add_to(map)
            
                polygon = folium.Polygon(locations=verticesROW, color='black', fill_color=None, fill_opacity=1.0).add_to(map)

                st_map = st_folium(map, width=1100, height=550)
                folium.LayerControl().add_to(map)

            elif option_3 == "Fire Hotspots":
                # val = "The environmental fire prone areas are marked here with yellow circles"
                # st.markdown(f"<span style='font-size: 12px'>{val}</span>", unsafe_allow_html=True)
                map = folium.Map(location=[22.606939204923812,74.11067787159304], zoom_start=11, scrollWheelZoom=True, tiles='Stamen Terrain')
            
                folium.TileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                        attr='ArcGIS',
                        name='Satellite',
                        overlay=True,
                        control=True).add_to(map)
                
                img = folium.raster_layers.ImageOverlay(
                name= option_3,
                image="./static/fireHotspots.png",
                bounds=vertices,
                opacity=1.0,
                interactive=True,
                cross_origin=False,
                zindex=1,
                )
                firespots = [(20.83541042217368,80.46141244556767),
                    # (20.823537708019863,80.43961145069463),
                    # (20.807652478456497,80.4353199162708),
                    (20.775876998861502,80.39223291065557),
                    # (20.76053615415873,80.34218411021307),
                    (20.71282003372299,80.2982933534056)]
            
                
                img.add_to(map)
                # for i in range(len(firespots)):
        
                #     folium.CircleMarker(location=firespots[i],radius=15,color='yellow',line_width=50, opacity=5).add_to(map)

                for i in range(len(locations)):
                    folium.Marker(location=locations[i],
                    icon= folium.Icon(color='blue',
                    icon_color='yellow',icon ="tower"),popup='Name : {} \n Coordinates: {}'.format(names[i],locations[i])).add_to(map)
            
                    folium.Marker(location=locations[i],radius=2,color='black').add_to(map)
                polygon = folium.Polygon(locations=verticesROW, color='black', fill_color=None, fill_opacity=1.0).add_to(map)

                st_map = st_folium(map, width=1100, height=550)
                folium.LayerControl().add_to(map)

            
            

        with col2:   
            
            if option_3 == "Fire Hotspots":
                st.image(Image.open("./static/try.png"))


            elif option_3 =="Temperature":
                st.image(Image.open("./static/temp_leg.png"))
               # st.markdown(f"<span style='font-size: 16px'>{selected_ground_option_text}</span>", unsafe_allow_html=True)
                val = "The yellow region shows average temperature, blue region are relatively colder and red regions have the maximum\
                    temperature in this ROW. This thresholding of temperature will vary from region to region as average temperature \
                        is region dependent as well."
                st.markdown(f"<span style='font-size: 12px'>{val}</span>", unsafe_allow_html=True)

                # st.markdown(f"<span style='font-size: 14px'>The mean LST for this area</span>", unsafe_allow_html=True)
                # meanval = "30.091 C"
                # st.markdown(f"<span style='font-size: 35px'>{meanval}</span>", unsafe_allow_html=True)
            elif option_3 =="Moisture Index":
                st.image(Image.open("./static/NDMI_legend.png"))
                # st.markdown(f"<span style='font-size: 14px'>The mean Vegetation Moisture for this area</span>", unsafe_allow_html=True)
                # meanval = "0.042"
                # st.markdown(f"<span style='font-size: 35px'>{meanval}</span>", unsafe_allow_html=True)

                

        
    elif choose =="Drone Services":
        col1,col2 = st.columns([0.94,0.06])
        with col1:
            st.markdown(""" <style> .fonty {
                font-size:75px ; font-family: 'Cooper Black'; color: #ffffff;} 
                </style> """, unsafe_allow_html=True)
            st.title("GalaxEye DROVCO")
        with col2:
            st.image(logo, width=130 )

        radio_style = "<style>div.row-widget.stRadio > div{flex-direction:row;font-size:70px;}</style>"
        
    # Display the radio buttons with the custom CSS style
        st.markdown(radio_style, unsafe_allow_html=True)
    
        drone = st.radio("",["Vegetation Monitoring","Transmission Line Sagging"])
        if drone =="Vegetation Monitoring":
            col1,col2 = st.columns([0.85,0.15])
            with col1:
                st.markdown(""" <style> .font {
                font-size:30px ; font-family: 'Cooper Black'; color: #ffffff;} 
                </style> """, unsafe_allow_html=True)
                st.markdown('<p class="font">{}</p>'.format("3D Point Cloud"), unsafe_allow_html=True) 
                pt_cloud = Image.open("./static/3d_pc.png")
                video_file = open('./static/drone.webm', 'rb')
                video_bytes = video_file.read()
                drone = st.video(video_bytes)

                an = st.button('Show Analysis')
                #vid = st.button('3D point cloud')
                if an:
                    
                    drone.empty()
                
                    pt = st.image(pt_cloud, caption='3D Encraochment analysis',use_column_width=True)
                    
                    an = st.button('Back to 3D point cloud video')
                    if an:
                        video_file = open('./static/drone.webm', 'rb')
                        video_bytes = video_file.read()
                        drone = st.video(video_bytes)
                    with col2 : 
                        st.markdown(" ")
                        st.markdown(" ")
                        st.markdown(" ")
                        st.markdown(" ")
                        st.markdown(" ")
                        st.markdown(" ")
                        st.markdown(" ")
                        st.markdown(" ")
                        st.markdown(" ")
                        st.markdown(" ")
                        st.markdown(f"<span style='font-size: 18px'>Mean Height</span>", unsafe_allow_html=True)
                        meanval = "6.54 m"
                        st.markdown(f"<span style='font-size: 35px'>{meanval}</span>", unsafe_allow_html=True)
                        st.markdown("""-------------------""")
                        st.markdown(f"<span style='font-size: 18px'>Highest Tree</span>", unsafe_allow_html=True)
                        meanval = "8.32 m"
                        st.markdown(f"<span style='font-size: 35px'>{meanval}</span>", unsafe_allow_html=True)

            

        
            # with col2:
        elif drone =="Transmission Line Sagging":
            col1,col2 = st.columns([0.8,0.2])
            with col1:
                st.markdown(""" <style> .font {
                font-size:30px ; font-family: 'Cooper Black'; color: #ffffff;} 
                </style> """, unsafe_allow_html=True)
                st.markdown('<p class="font">{}</p>'.format("Radar Image for Transmission Lines"), unsafe_allow_html=True) 
                radar = Image.open("./static/sagging_indiG.png")
                st.image(radar, width=1000)

            

        # st.markdown(""" <style> .font {
        # font-size:30px ; font-family: 'Cooper Black'; color: #ffffff;} 
        # </style> """, unsafe_allow_html=True)
        # st.markdown('<p class="font">{}</p>'.format("3D Point Cloud"), unsafe_allow_html=True) 
        # video_file = open('./static/drone.webm', 'rb')
        # video_bytes = video_file.read()
        # drone = st.video(video_bytes)

        # st.markdown(""" <style> .font {
        # font-size:30px ; font-family: 'Cooper Black'; color: #ffffff;} 
        # </style> """, unsafe_allow_html=True)
        # st.markdown('<p class="font">{}</p>'.format("Radar Image for Transmission Lines"), unsafe_allow_html=True) 
        # radar = Image.open("./static/dronesar.png")
        # st.image(radar, width=1000)




    elif choose =="Report Generation":
        col1,col2 = st.columns([0.94,0.06])
        df = pd.read_csv('./static/adani_report.csv')
        measure = st.selectbox("Insight", ["Temperature", "Vegetation encroachment","Land Subsidence","Potential Fouling","Corrosion"])
        if measure =="Temperature":
            df_temp = df[['latitude', 'longitude', 'name','Temperature']]
            df_temp = df_temp.loc[df_temp['Temperature'] == 1]
            df_temp["tuple"] = df_temp[["latitude","longitude"]].apply(tuple, axis=1)
            map = folium.Map(location=[22.606939204923812,74.11067787159304], zoom_start=11, scrollWheelZoom=True, tiles='Stamen Terrain')
            
            folium.TileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                        attr='ArcGIS',
                        name='Satellite',
                        overlay=True,
                        control=True).add_to(map)
            #st.map(data=df_temp)
            poly = folium.Polygon(locations=verticesROW, color='black', fill_color=None, fill_opacity=1.0).add_to(map)
            locs = list(df_temp['tuple'])
            names = list(df_temp['name'])
            for i in range(len(locs)):
                
                folium.CircleMarker(location=locs[i],radius=2,color='red',line_width=50, opacity=5,popup='Name : {} \n Coordinates: {}'.format(names[i],locs[i])).add_to(map)
                # folium.Marker(location=locations[i],
                #     icon= folium.Icon(color='blue',
                #     icon_color='yellow',icon ="tower"),popup='Name : {} \n Coordinates: {}'.format(names[i],locations[i])).add_to(map)


        elif measure =="Vegetation encroachment":
            df_temp = df[['latitude', 'longitude','name', 'Vegetation encroachment']]
            df_temp = df_temp.loc[(df_temp['Vegetation encroachment'] == 'low') | (df_temp['Vegetation encroachment'] == 'Moderate') | (df_temp['Vegetation encroachment'] == 'high')]
            df_temp["tuple"] = df_temp[["latitude","longitude"]].apply(tuple, axis=1)
            map = folium.Map(location=[22.606939204923812,74.11067787159304], zoom_start=11, scrollWheelZoom=True, tiles='Stamen Terrain')
            
            folium.TileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                        attr='ArcGIS',
                        name='Satellite',
                        overlay=True,
                        control=True).add_to(map)
            #st.map(data=df_temp)
            poly = folium.Polygon(locations=verticesROW, color='black', fill_color=None, fill_opacity=1.0).add_to(map)
            locs = list(df_temp['tuple'])
            names = list(df_temp['name'])
            for i in range(len(locs)):
                
                folium.CircleMarker(location=locs[i],radius=2,color='green',line_width=50, opacity=5,popup='Name : {} \n Coordinates: {}'.format(names[i],locs[i])).add_to(map)

        elif measure =="Land Subsidence":
            df_temp = df[['latitude', 'longitude', 'name','Land Subsidence']]
            df_temp =df_temp.loc[(df_temp['Land Subsidence'] == 'low') | (df_temp['Land Subsidence'] == 'Moderate') | (df_temp['Land Subsidence'] == 'high')]
            df_temp["tuple"] = df_temp[["latitude","longitude"]].apply(tuple, axis=1)
            map = folium.Map(location=[22.606939204923812,74.11067787159304], zoom_start=11, scrollWheelZoom=True, tiles='Stamen Terrain')
            
            folium.TileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                        attr='ArcGIS',
                        name='Satellite',
                        overlay=True,
                        control=True).add_to(map)
            #st.map(data=df_temp)
            poly = folium.Polygon(locations=verticesROW, color='black', fill_color=None, fill_opacity=1.0).add_to(map)
            locs = list(df_temp['tuple'])
            names = list(df_temp['name'])
            for i in range(len(locs)):
                
                folium.CircleMarker(location=locs[i],radius=2,color='blue',line_width=50, opacity=5,popup='Name : {} \n Coordinates: {}'.format(names[i],locs[i])).add_to(map)
            

        elif measure =="Potential Fouling":
            df_temp = df[['latitude', 'longitude','name', 'Potential Fouling']]
            df_temp =df_temp.loc[(df_temp['Potential Fouling'] == 'low') | (df_temp['Potential Fouling'] == 'Moderate') | (df_temp['Potential Fouling'] == 'high')]
            df_temp["tuple"] = df_temp[["latitude","longitude"]].apply(tuple, axis=1)
            map = folium.Map(location=[22.606939204923812,74.11067787159304], zoom_start=11, scrollWheelZoom=True, tiles='Stamen Terrain')
            
            folium.TileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                        attr='ArcGIS',
                        name='Satellite',
                        overlay=True,
                        control=True).add_to(map)
            #st.map(data=df_temp)
            poly = folium.Polygon(locations=verticesROW, color='black', fill_color=None, fill_opacity=1.0).add_to(map)
            locs = list(df_temp['tuple'])
            names = list(df_temp['name'])
            for i in range(len(locs)):
                
                folium.CircleMarker(location=locs[i],radius=2,color='orange',line_width=50, opacity=5,popup='Name : {} \n Coordinates: {}'.format(names[i],locs[i])).add_to(map)


        elif measure =="Corrosion":
            df_temp = df[['latitude', 'longitude', 'name','Corrosion']]
            df_temp =df_temp.loc[(df_temp['Corrosion'] == 'low') | (df_temp['Corrosion'] == 'Moderate') | (df_temp['Corrosion'] == 'high')]
            df_temp["tuple"] = df_temp[["latitude","longitude"]].apply(tuple, axis=1)
            map = folium.Map(location=[22.606939204923812,74.11067787159304], zoom_start=11, scrollWheelZoom=True, tiles='Stamen Terrain')
            
            folium.TileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                        attr='ArcGIS',
                        name='Satellite',
                        overlay=True,
                        control=True).add_to(map)
            #st.map(data=df_temp)
            poly = folium.Polygon(locations=verticesROW, color='black', fill_color=None, fill_opacity=1.0).add_to(map)
            locs = list(df_temp['tuple'])
            names = list(df_temp['name'])
            for i in range(len(locs)):
                
                folium.CircleMarker(location=locs[i],radius=2,color='white',line_width=50, opacity=5,popup='Name : {} \n Coordinates: {}'.format(names[i],locs[i])).add_to(map)

        st_map = st_folium(map, width=1100, height=550)
            # st.map(data=df_temp)
        with col1:
            st.markdown(""" <style> .fonty {
                font-size:75px ; font-family: 'Cooper Black'; color: #ffffff;} 
                </style> """, unsafe_allow_html=True)
            st.title("Generate Report")
        with col2:
            st.image(logo, width=130 )

        # col1, col2 = st.columns(2)
        # with col1:
            
        #     Year = st.selectbox("Year", ["Year"])
        # with col2:
        #     Month = st.selectbox("Month", ["Month"])

        
    
        with open("./static/satelliteReport.xlsx", "rb") as template_file:
            template_byte = template_file.read()

        st.download_button(label="Download report",
                            data=template_byte,
                            file_name="./static/satellite_Report.xlsx",
                            mime='application/octet-stream')
        
