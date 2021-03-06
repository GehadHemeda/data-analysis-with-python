Bike Share Data
Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, you will use data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. You will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.

The Datasets<br>
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:<br>

Start Time (e.g., 2017-01-01 00:07:57)<br>
End Time (e.g., 2017-01-01 00:20:53)<br>
Trip Duration (in seconds - e.g., 776)<br>
Start Station (e.g., Broadway & Barry Ave)<br>
End Station (e.g., Sedgwick St & North Ave)<br>
User Type (Subscriber or Customer)<br>
The Chicago and New York City files also have the following two columns:<br>

Gender<br>
Birth Year<br>

![image](https://user-images.githubusercontent.com/91467768/135971351-9e1d6852-4c88-4437-98cd-7a794dead4bd.png)
Data for the first 10 rides in the new_york_city.csv file<br>

The original files are much larger and messier, and you don't need to download them, but they can be accessed here if you'd like to see them (Chicago, New York City, Washington). These files had more columns and they differed in format in many cases. Some data wrangling has been performed to condense these files to the above core six columns to make your analysis and the evaluation of your Python skills more straightforward. In the Data Wrangling course that comes later in the Data Analyst Nanodegree program, students learn how to wrangle the dirtiest, messiest datasets, so don't worry, you won't miss out on learning this important skill!<br>

Statistics Computed<br><br>
You will learn about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics. In this project, you'll write code to provide the following information:<br>

#1 Popular times of travel (i.e., occurs most often in the start time)

most common month <br>
most common day of week <br>
most common hour of day <br>

#2 Popular stations and trip<br>

most common start station<br>
most common end station<br>
most common trip from start to end (i.e., most frequent combination of start station and end station)<br>

#3 Trip duration<br>

total travel time<br>
average travel time<br>

#4 User info<br>

counts of each user type<br>
counts of each gender (only available for NYC and Chicago)<br>
earliest, most recent, most common year of birth (only available for NYC and Chicago)<br>


The Files<br>
To answer these questions using Python, you will need to write a Python script. To help guide your work in this project, a template with helper code and comments is provided in a bikeshare.py file, and you will do your scripting in there also. You will need the three city dataset files too:

chicago.csv
new_york_city.csv
washington.csv
