# sqlalchemychallenge
*For this assignment we had to analyse weather data from the state of Hawaii. 

*In the ipynb file, we created and engine and session to connect the sql lite files which had Hawaii's weather data. The two classes of data were 'Measurement' and 'Station'.
*First we used a query to find the most recent date in the data set, which was August 23, 2017. Then we designed a query to retrieve the precipitation data from the last twelve months. Then we plotted this data on a graph with the dates on the x-axis, and inches of precipitation on the y-axis. After this, we used pandas to generate precipitation statistics such as mean, max, and standard deviation. 
We then designed two queries for the weather stations. The first query counted the number of stations, the second ordered the stations from most active to least active. Then we calculated the minimum temp, maximum temp, and average temp for the most active station (USC00519281). Lastly, we queried the temperature data for the last 12 months in station USC00519281, and plotted the results on a histogram. The histogram has temperature on the x-axis, and frequency on the y-axis. The last cell is our session close.

*In the app.py file, we created a Flask API for the Hawaii climate data. 
*First, the imports were added (Flask, json, sqlalchemy etc.). After the imports we created a database session. We then retrieved the last 12 months precipitation data and made a dictionary. Imports for stations and most active stations were added. Lastly, we added the mininum, maximim, and average in the last 12 months for the most active station.
