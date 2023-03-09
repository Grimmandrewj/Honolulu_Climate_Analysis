# Goal
- I was tasked with completing a climate analysis about Honolulu, HI in preparation for a long holiday trip
- Part 1 of the assignment was to analyze and explore the climate data in the provided datasets and display the data in DataFrames and plot them 
- Part 2 of the assignment was to create a Climate App from which users can access the queried information and pull API to obtain the data in JSON format

# Method
- Part 1 - Analysis and Exploration
  - To complete this task, I created an engine to connect to the dataset, reflected the       database into a new model, reflected the tables, and set variables for each table
  - I then created a session/link to the database
  - I created queries to display the data in the tables, found the most recent date in       the dataset, retrieved the last twelve months of precipitation data starting with the     most recent date, calculate one year back from that date, sort the data by date, and     plot the data into a line plot:

![image](https://user-images.githubusercontent.com/120341249/223899461-cf326ff9-420c-42f8-a93a-0c750ae46a0d.png)

  - I then calculated the summary statistics for the precipitation data I queried:

![image](https://user-images.githubusercontent.com/120341249/223899613-9db24833-7179-4fb7-9309-e4b1984cecb2.png)

  - I then created queries to determine the number of weather stations in the dataset,       found the most active station with the most temp measurements, calculated the             minimum, maximum, and average temperature in the dataset for that station, queried       the last twelve months of temperature readings for that station, and plotted the         results in a histogram:
 
 ![image](https://user-images.githubusercontent.com/120341249/223899950-477b9c8e-3527-404d-b909-4ddf19432b98.png)

- Part 2 - Climate App
  - To complete this task, I imported the necessary dependencies, set up the database and     established the connection to the database, set up Flask, and created the routes
  - The routes I was to create included:<br/>
    <ins>/api/v1.0/precipitation</ins> (displaying 12 months of precipitation data),                 
    <ins>/api/v1.0/stations</ins> (displaying list of weather station locations and IDs),           
    <ins>/api/v1.0/tobs</ins> (displaying 12 months of temperature measurements for the   most active weather station),<br/> 
    <ins>/api/v1.0/start</ins> (displaying minimum, maximum, and average temps for dates equal     to and greater than date entered by user), and <br/>
    <ins>/api/v1.0/start/end</ins> (displaying minimum, maximum, and average temps for dates     between start date and end date entered by user, inclusive of end date).
  
# Summary and Results
- The Analysis can be found in the Jupyter Notebook titled climate_analysis.ipynb
- The Climate App is titled app.py
- As demonstrated, there is no discernible pattern with levels of precipitation by date according to the provided dataset (with high levels appearing in ~September 2016, ~February 2017, and ~April 2017), suggesting some variability with the potential for rain.  Also, the temperatures measured with the highest frequency were between 70 and 80 (ideal temperatures for comfort on a long holiday).
