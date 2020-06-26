### Date created
This project has been created during June 2020.

### Project Title
**Explore US bikeshare data**

### Description
The project consists in creating a tool by using **Python** to explore data related to bike share systems for three major cities in the United States:
* Chicago
* New York City
* Washington

The datasets used in the project have been provided by [*Motivate*](https://www.motivateco.com/), a bike share system provider for many major cities in the United States, to uncover bike share usage patterns.

The purpose of this project has been to learn how to code in **Python**, as well as to use some essential libraries for Data Science, such as **NumPy** and **Pandas**.

Essentially, I have created a program to import the data and answer interesting questions about it by computing descriptive statistics. It also includes a script that takes in raw input to create an interactive experience in the terminal to present these statistics.

#### The datasets

Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six columns:
* Start Time (e.g., 2017-01-01 00:07:57)
* End Time (e.g., 2017-01-01 00:20:53)
* Trip Duration (in seconds - e.g., 776)
* Start Station (e.g., Broadway & Barry Ave)
* End Station (e.g., Sedgwick St & North Ave)
* User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:
* Gender
* Birth Year

#### Statistics computed

1. **Popular times of travel**
    * most common month
    * most common day of the week
    * most common hour of day


2. **Popular stations and trip**
    * most common start station
    * most common end station
    * most common trip from start to end


3. **Trip duration**
    * total travel time
    * average travel time


4. **User info**
    * counts of each type
    * counts of each gender (only available for *NYC* and *CHI*)
    * earliest, most recent and most common year of birth (only available for *NYC* and *CHI*)


### Files used
The project has been developed in the file **bikeshare.py**.

This file makes use of the following three city dataset files:
* __chicago.csv__
* __new_york_city.csv__
* __washington.csv__


### Credits
In order to complete the project, I have made use of the resources listed below:

* [The Python Standard Library](https://docs.python.org/3/library/index.html)
* [pandas documentation](https://pandas.pydata.org/docs/#)
* [GeeksforGeeks](https://www.geeksforgeeks.org/)
* [Stack Overflow](https://stackoverflow.com/)
* [Programiz](https://www.programiz.com/python-programming)
