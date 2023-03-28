import pandas as pd
import plotly.express as px

#Access token to mapbox declared here
token = 'pk.eyJ1IjoiYWFyb25icnVudCIsImEiOiJjbGQ3MmNtbjMxaTJmM3hvZzRnYnZtZnloIn0.xw5Va9Qk5DvxlXa5CEC-zQ'

#Declare file directory and file name
file_dir = "C:/Users/Azzla/Downloads/"
file_name = "StadiumsExVFLAFL.csv"

#Open csv filename and put data into dataframe
ex_vfl_afl_stadia = pd.read_csv(file_dir + file_name)

#Add new column to determine marker sizes to the dataframe
#First find number of rows/stadia
num_stadia = ex_vfl_afl_stadia.shape[0]
# Declare a list that is to be converted into a column
marker_sizes = []

#Populate that list with the marker size as many times as there are venues/stadia (size for each stadia)
i = 0
while i < num_stadia:
    marker_sizes.append(5)
    i += 1
  
# Using 'MarkerSize' as the column name
# and equating it to the list
ex_vfl_afl_stadia['MarkerSize'] = marker_sizes

#Declare data to be displayed when you hover over the point
#Columns in order are...
#ID, latitude, longitude, Name, First Match, Last Match, Games Played, Record Attendance, MarkerSize
data_to_display = {}
data_to_display['ID']=False
data_to_display[' latitude']=False
data_to_display['longitude']=False
data_to_display['Name']=True
data_to_display['First Match']=True
data_to_display['Last Match']=True
data_to_display['Games Played']=True
data_to_display['Record Attendance']=False
data_to_display['MarkerSize']=False


#Plot the stadia on a map
fig = px.scatter_mapbox(ex_vfl_afl_stadia, lat=" latitude", lon="longitude", size='MarkerSize', hover_name="Name", hover_data=data_to_display,
                        color_discrete_sequence=["red"], center=dict(lat=-26,lon=135), zoom=3, title='Former VFL/AFL Venues', height=500, width=600)

#Update the map so that the basemap is satellite, which requires your mapbox token
#You will need a mapbox account to do this
fig.update_layout(mapbox_style="satellite", mapbox_accesstoken=token)

#Update the map so that the margins right, top, left and bottom are zero
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

#Show the map which will open up a new tab in your default internet browser
fig.show()

#Export to HTML
filename = file_dir + "Former_VFLAFL_Venues.html"
fig.write_html(filename)
