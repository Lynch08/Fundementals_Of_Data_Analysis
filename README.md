
Assignment: Programming for Data Analysis, GMIT 2021  

![](https://upload.wikimedia.org/wikipedia/en/6/6b/GMIT_Logo_2011a.jpg)

Lecturer: Dr Ian Mcloughlin  

Author: Enda Lynch  
Github Username: Lynch08  
GMIT Email: G003987951@gmit.ie  
Personal Email: E.Lynch@Kostal.com  

This repository contains two jupter notebooks.    
This Readme will first address the parts of the repository that are common. Then outline some of the ways you can explore the notebook investigating the matplotlib.pyplot python package (pyplot.ipynb) and then the notebook andalysing the CAO points (cao.ipynb)


## Table of Contents
See pyplot.ipynb - main headings are hyperlinked.    
See cao.ipynb - main headings are hyperlinked.    

## Planned Project Outcomes
1. To break the project and assignment down into small manageable tasks
2. To gain an understanding of the matplotlib.pyplot package
3. To integrate the skills I had acquired so far in this course to visualise and analyse my "datasets", and display my findings
4. To expand my knowledge of the python libraries and tools to make the code as simple and readable as possible for the reader
5. To learn how to best optimise my time between research, programming, problem-solving and analysis.

## The Task and Expectations
[Assessment Sheet](https://github.com/Lynch08/Fundementals_Of_Data_Analysis/blob/main/Fundamentals%20of%20Data%20Analysis%20assessment%20sheet.pdf)

## The Repository Content 
 - 2 jupyter notebooks (pyplot.ipynb and cao.ipynb) that holds the explanation, code, visuals and citeations for the assignment and project.
 - The assignment and project details in PDF form from Dr. Ian Mcloughlin
 - A requirments.txt file that contains all of the dependancies required to run the both notebooks from the repository in the same environment
 - A readme file explaining the objectives, outcomes and instructions on how to view the notebook in both editable and static format.
 - A data_pyplot folder that contains nfl_2020_team_data.csv a csv file that I read in for one of my plots in pyplot.ipynb and irisdata.csv a csv file of the Iris data set for one of my plots in pyplot.ipynb
 - A data_cao folder that contains 2 edited CSV files (2019POINTS_20211104103000_edited.csv and ForExFix_comp.csv). I did some manual changes in excel to clean the data.

## View Notebook in Static Format(Online)
If you wish to view the pyplot.ipynb notebook in static (uneditable) format click here:  
[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/Lynch08/Fundementals_Of_Data_Analysis/blob/main/pyplot.ipynb)  

If you wish to view the cao.ipynb notebook in static (uneditable) format click here:   
[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/Lynch08/Fundementals_Of_Data_Analysis/blob/main/cao.ipynb) 

## How to download this repository (editable version)
Go to GitHub.com.
Go to my repository: https://github.com/Lynch08/Programming_For_Data_Analysis
Click the clone/download button.
Save the repository to a local folder location on your machine.
You will need to navigate to this folder location on the command line in order to run the program.
Details on how to run each individual script in this repository is included later in this Readme file.

### Python Dependancies 

I have a requirements.txt file that you can use to install all of the dependencies required to run the notebook in the exact same environment - however below are the main dependencies if you would like to do that manually. After cloning the repository navigate to the folder using the command prompt and use the ```pip install``` command if you want to use the requirments.txt file.
See this video for full instructions on how to install: https://www.youtube.com/watch?v=mBcmdcmZXJg 


**Required**
- Download Python environment - I recommend ([Anaconda](https://www.anaconda.com/products/individual)) 
    - Libraries to import within the python environment (all are linked to official documentation - **only first 4 required for pyplot.ipynb, all required for cao.ipynb**)
        - [Numpy](https://numpy.org/doc/)
        - [Pandas](https://pandas.pydata.org/docs/)
        - [matplotlib.pyplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html)
        - [Seaborn](https://seaborn.pydata.org/)
        - [Reg-Ex(Re)](https://docs.python.org/3/library/re.html)
        - [PyPDF2](https://pythonhosted.org/PyPDF2/PdfFileReader.html)
        - [Requests](https://docs.python-requests.org/en/latest/)
        - [urllib.request](urllib.request)
        - [Datetime](https://docs.python.org/3/library/datetime.html)

**Not required but helpful**  
cmder - this is a command line emulator that in my opinion is easier to use and cleaner than the windows cmd window. [Download Cmder Here](https://cmder.net/)


### Notebook Dependancies 

##### pyploy.ipynb
The irisdata.csv and nfl_2020_team_data.csv will need to be kept in the data_pyplot folder and left unedited for the pyplot.ipynb notebook to run the same as from the repo.  

irisdata.csv - a csv file of the Iris data set from https://www.kaggle.com/uciml/iris  
nfl_2020_team_data.csv - Added from https://www.pro-football-reference.com/years/2020/advanced.htm  

##### cao.ipynb
The ForExFix_comp.csv and 2019POINTS_20211104103000_edited.csv will need to be kept in the data_cao folder and left unedited for the cao.ipynb notebook to run the same as from the repo.   

2019POINTS_20211104103000_edited.csv - Manually edited to remove spurious data from df  
ForExFix_comp.csv - Manually edited to remove spurious data from df  

### Running the Jupyter Notebook
 - On the command line navigate to the folder location where the repository has been downloaded and saved to using the cd command to change directory.  
 - Type jupyter lab on the command line and press enter.  
 - After a short wait jupyter notebook will open in your web browser (I would suggest Chrome).  
 - Open the required notebook in the browser and the notebook containing the code and comments that I wrote for this assignment will be displayed.  
 - Before beginning I would suggest going to the Kernel option on the menu bar and if you want to run the notebook yourself choose "Restart Kernel and Clear Outputs". If you want the notebook to run automatically choose "Restart Kernel and Run All Cells".  
 - If you want to run the code in any particular cell, click into the cell, hold down the shift key, press enter and the command will run and the output wil be displayed in the next cell - please note the cells are not ready to be run so you cannot begin trying to run cells halfway down the note book.  
 - To change between edit and read mode at any time click into a cell and press the ESC key.  
 - When you have finished viewing the jupyter notebook close the web browser and return to the command line. Press Ctrl + C on the command line to kill the program.  



## Citations
All citations are at the end of the pyplot.ipynb notebook and refrence the section they citing.  
All citations are at the end of the cao.ipynb notebook and refrence the section they citing.



## pyplot.ipynb
![](https://upload.wikimedia.org/wikipedia/en/5/56/Matplotlib_logo.svg)  

This Repository contains an investigation into the the matplotlib.pyplot package (pyplot.ipynb) in a juypter notebook for the Fundamentals of Data Analysis Module(GMIT - Wimter 2021)

Link to the matplotlib.pyplot documentation
[Offical pyplot Documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html)

#### Explore
This notebook is very interactive.  
Especially in section 2. Functionality in pyplot. In this section I go through some of the customization and visualisation functions when making a plot.  
You can change the values for x and y. I used sine and cosine but you can plug in or generate your own values using [Numpy](https://numpy.org/doc/stable/reference/random/generator.html) to see how it effects the plot.

```python

# Generates an array of cos(x) values
# Creating an array with 100 values from 0 to 2pi
x = np.linspace(0,2*np.pi,100)

# An array with the sine of all the values in array x
y = np.sin(x)

# An array with the cos of all the values in array x
y1 = np.cos(x)
```
In the section below you can change the size of the plot, axis-labels, set axis limits, change the plot point symbol annd so on.  You can also go o the [pyplot documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html) where there are over 150 matplotlib.pyplot.X functions to choose from and play with. 

```python
# Produces the figure
plt.figure(figsize = (12,9))

# Adds a grid
plt.grid(True)

# Adds a title
plt.title("Plot of a sine and cosine function")

# Adds label for the x-axis
plt.xlabel("x")

# Defines a region along the x-axis to be displayed
plt.xlim(0,2*np.pi)

# Plots the sine function with red + signs and defines a legend label
plt.plot(x,y,'r+',label="sin(x)")

# Plots the cos function with green crosses and defines a legend label
plt.plot(x,y1,'gx',label="cos(x)")

# Adds a legend in the best position
plt.legend(loc='best')

```

In the 3 interesting plots section the first plot, section on Histograms is interactive but the rest of the graphs are based off static or scraped data so you will be able to interact with the customisation, but if you change the data input the results may differ greatly and the functionality will almost certainly not be as robust. 

## cao.ipynb
![](https://upload.wikimedia.org/wikipedia/commons/5/51/Central_Applications_Office.png)


This Repository contains an investigation into the the first round cao points for the last 3 years in a juypter notebook for the Fundamentals of Data Analysis Module(GMIT - Wimter 2021)

Link to the CAO website
[CAO Website](https://www.cao.ie/)

#### Explore

I would advise not to manipulat the code in section 2 "Scraping the Points" unless you are very familiar with scraping data as how the data is formatted is vital to how the code runs further down the notebook. 

In the analysis section you can do some limited manipulation.  
There is some oppertunitly to play with the graph visualisation by changing the amount of bins or the way the labels are set up on the axes, however no data manipulation.

```python
# Plot Size
plt.figure(figsize = (12, 8))

# Adds a grid
plt.grid(True, linestyle='--', linewidth=1)

# Type of plot, kde adds kde lin, bins determins number of bins
sns.histplot(z, kde = True, bins= 15)

# Get or set the current tick locations and labels of the x-axis
plt.xticks(np.arange(0, 1200, step=50))

# Get or set the current tick locations and labels of the y-axis
plt.yticks(np.arange(0, 400, step=50))

# Sets the title of the plot
plt.title('2019 CAO POINTS')
```

Here i created a new data frame by setting a condition on one of the columns in the original data frame

```python
# Bring all points back that show the course was not available in 2019
incr_ana = firstrndpts.loc[(firstrndpts['points_r1_2021'] >= 1)]
```

Below I added a new column (boolean) by setting conditions on two of the other columns, you can do this and even add more conditions - see this article in [ThisPointer.Com](https://thispointer.com/python-pandas-select-rows-in-dataframe-by-conditions-on-multiple-columns/) for ways in which to use this functionality to include and exclude data.

```python
# Add column that shows if there was an increase in points after first year
incr_ana_1['Increase after 1st year'] = incr_ana_1['points_r1_2021'] > incr_ana_1['points_r1_2020']
```
