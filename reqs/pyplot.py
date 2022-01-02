#!/usr/bin/env python
# coding: utf-8

# # An In-depth Analysis of the Matplotlib.Pyplot Package for Python
# 
# **Module:** Fundementals of Data Analysis, GMIT 2021  
# 
# **Lecturer:** Dr Ian McLoughlin  
# 
# **Author:** Enda Lynch   
# **Github Username:** Lynch08  
# **GMIT Email:** G003987951@gmit.ie  
# **Personal Email:** E.Lynch@Kostal.com 
#     
#     
# View this notebook in static format:  
# [![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/Lynch08/numpy-random-investigation/blob/86648f030548ae171d294aa48f19e1ac12f80650/numpy-random.ipynb)
# 
# [Offical Documentation](https://matplotlib.org/)

# ### Table of Contents
# The main headings and distributions are hyperlinked to make it easier to navigate to certain parts of the notebook if required

# **[1. What is in this Notebook](#What_is_this_Notebook)**  
# 1.1 Introduction to Pyplot    
# 1.2 Plots in Data Analysis  
# 1.3 Data Generation  
# 
# **[2. Importing Libraries for this notebook](#Importing_Libs)**  
# 
# **[3. Functionality in pyplot](#First_plot)**    
# 3.1 Creating data for x and y  
# 3.2 A very basic plot  
# 3.3 Customising the plot  
# 3.4 Plotting more data on the same Axis  
# 3.5 Using multiple axis  
# 
# **[4. 2D Plots](#2d_plot)**   
# 
# **[5. Three interesting plots](#three_plot)**  
# 5.1 Plot 1 - The Histogram  
# 5.2 Plot 2 - Diverging Bar Charts  
# 5.3 Plot 3 - Scatterplot and Annotation  
# 5.4 Plot 4 - Bonas Plot with Seaborn - Heatmaps and Corrolations  
# 
# **[6. Conclusion](#conclu)**    
# 

# <a id='What_is_this_Notebook'></a>
# 
# ### What is in this Notebook?

# This notebook is aimed as a presentation to the class - I am going to give a brife introduction with my own thoughts on the matplotlib.pyplot library. Then discuss plots and data generation - before moving on to a demo of how to crate a simple plot or plots using pseudo random data.  
# I will then go through my 3 interesting plots (this is actually 4). I took a bit of a gamble here and instead of discussing plot types such as box plot, histogram and scatter, I chose one plot type, one specific plot where I discuss its pros and cons, and for the third I created 3
# plots of one plot type using data I find interesting for analysis. Then I do a little bonas plot using another library built on matplotlib.pyplot.
# 
# The first is a plot type - I took the histogram as it is one of the most common plots and in this I show the difference between normal and uniform distributions. Not very inventive but it was my first one.  
# The second is a data set I found in a github repository (related to vehicle fuel efficiency - miles per gallon) when reading a blog on the the different types of plots in matplotlib. For this plot I discuss the advantages of diverging bar charts and how cusimization of a chart can lead to intentional or unintentional bias.  
# Third is  on a sport I have followed from the last number of years, NFL (or American) Football.  I downloaded some CSV data and attempted to make some assumptions based on each teams offensive data by using scatter plots to show their effiency.   
# Finally I will use a data set that is extremly well known and has been used multiple times in this course, the Iris data set - to generate a heatmap using pyplot and another python library that is based on matplotlib - seaborn. For this I will look at the corrolations between variables and how removing a variable can impact the dataset

# ### 1.1 Introduction to Pyplot
# Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.[[1]](https://matplotlib.org/)
# That is the one line explaination for the Matplotlib Package from the offical website and honestly I find it a little boring and does not do the package or its power in data analysis justice.
# I was first introduced to the Matplotlib package in Feb 2021 towards the beginning of my Programming and Scripting module for this course. At this time I was introduced to a number of packages such as [Numpy](https://numpy.org/), [Pandas](https://pandas.pydata.org/) and [Math](https://docs.python.org/3/library/math.html). The size and initial complexity of these packages was a little daunting at the beginning, however once I began to understand that the aim of these packages was to try and take the complexity out of writing code, I became much more grateful and impressed by their rationale. I began to see examples of, and write, basic scripts in other languages such as BASH in my Computer Architecture module and I had been exposed to limited SQL and C# from my work. From this I could see how these packages were allowing the author of code to condense and simplify both the reading and writing of code in the Python environment.
# 
# Pyplot offers an easy to use interface while at the same time, it also allows to control all aspects of plotting for advanced visualizations through its main object-oriented interface, which facilitates the creation of maintainable, modular code. It is particularly powerful if you want to do some exploratory data analysis or scientific plotting.  
# Matplotlib’s strength in exploratory data analysis comes from the pyplot interface where you can generate a variety of plots with a small number of keystrokes and interactively augment existing figures with new data. Additionally, the seaborn library built on top of matplotlib provides even more visualizations with some basic data analysis, such as linear regression or kernel density estimation, built in.  https://www.kite.com/blog/python/matplotlib-tutorial/
# 
# This notebook will investigate and discuss some of the features that are available in the Matplotlib Package in an attempt to to deliver a a clear and concise overview of the package.
# I will use multiple plots from the matplotlib.pyplot Python package to illiustrate the overview. I hope to use a mix of static and random data to give the author of this notebook a glimpse into the power of Matplotlib.
# 

# ### 1.2 Plots in Data Analysis
# In my opinion data plots are one of the most valuable tools for any data analyst. They not only give the reader a visualisation of sometimes obscure, unreadable data, they also sometimes give us the ability to make assumptions and decisions based off that data.[[2]](https://livebook.manning.com/book/data-science-bookcamp/chapter-2/v-4/1) Now, from my limited experience, I have found it is extreamly helpful if not essential that the analyser does have a strong grasp of the structure of the underlying data, such as knowing what kind of data is being used, strings, integers, floting points, what shape is the data? 1d or 2d arrey,  and how is it being stored (csv, json, .txt) in order to generate accurate and insightful plots from the matplotlib package.
# 
# 

# ### 1.3 Data Generation
# There are countless ways and forms in which data can be collected and stored.  
# In my introduction I use the numpy mathamathical functionality to generate data for me (pi, sin, cosine).  
# Then, to generate the data for my first **"interesting plot"** example, I am again going to use the numpy package but this time I will use a "random" number generator (rng) to generate two types of random distributions - normal and uniform.  
# This data will change every time the programme is run (I could change this by seeding the rng - see numpy seeding documentation)- however for the purpose of displaying some of the more basic plots like as is in my case, a histogram, that will not be a problem.
# 
# For the more complex and detailed plots I am going to import static data from downloaded csv files.  

# <a id='Importing_Libs'></a>
# 
# # 2. Importing Libraries for this notebook
# 
# I will be importing a number of Python Libraries to use in this notebook - I have gone into a little more detail on each in the readme if you would like to learn some more about them. 

# In[1]:


# efficent numerical arreys
import numpy as np

# Plotting
import matplotlib.pyplot as plt

# To read in data
import pandas as pd

# High-level interface for drawing attractive and informative statistical graphics
import seaborn as sns


# <a id='First_plot'></a>
# 
# ### 3. Functionality in pyplot
# 
# As an introduction I will generate some basic plots below and do some customisation to give examples of the funtionality available in the pyplot package.   
# This is of course only the beginning but hopfully this will give you a glimpse into some of the possibilities that are available when you use pyplot.  
# 
# This introduction was adapted from a towardsdatascience blog.
# 
# https://towardsdatascience.com/an-introduction-to-plotting-with-matplotlib-in-python-6d983b9ba081

# The first thing we need to do, before we create any plots, is to actually create data that we will use to plot. For this I will use the Numpy library and its mathematical functionality to create data that I want to plot.

# ##### 3.1 Creating data for x and y

# In[2]:


# Creating an array with 100 values from 0 to 2pi
x = np.linspace(0,2*np.pi,100)
# An array with the sine of all the values in array x
y = np.sin(x)


# ##### 3.2 A very basic plot

# In[3]:


# Produces the figure
plt.figure()
# Jupyter seems to add the grid automatically
# So I am removeing to show the bareness of the plot so far
plt.grid(False)
# Plots the sine function
plt.plot(x,y)


# Above you can see how with just a couple of lines of code I was able to generate a nice clean plot where the y value peaks at 1 and bottoms out at -1 and we could more accurately read of data in relation to where we are on the x and y value. However even though the plot makes sense to the reader of this notebook as I am explaining the code, for someone who is just looking at the image it does not give them any indication of what they are looking at - for this we will have to do a little customization, which is only a few short lines of code away in pyplot.

# ##### 3.3 Customising the plot

# In[4]:


# Changing style to ggplot
plt.style.use('ggplot')

# Produces the figure - figsize sets plot size
plt.figure(figsize = (8, 6))

# Adds a grid
plt.grid(True)

# Adds a title
plt.title("Plot of a sine function", fontsize = 20, pad = 15)

# Adds label for the x-axis
plt.xlabel("x", fontsize = 15, labelpad = 20)

# Adds label for the y-axis
plt.ylabel("sin(x)", fontsize = 15, labelpad = 15)

# Plots the sine function with yellow + signs
plt.plot(x,y,'y+')


# Now you can see I changed the style of the plot to 'ggplot' - this is more just to show the funtionality here - in practice this may not be what you want (I personally like the dark background styles)- but you can get a list of the stylesheets available in pyplot by using ```plt.style.available```.
# You can also see I was able to give more information on my plot by adding a title and labels to the x and y axis, resizing it using figsize and plotting it with these funky yellow plus signs that gives the plot a little more pop. Also adding the grid if it does not come in automatically gives the viewer far more readability.
# 
# I have also specified fontsize to dictate the size of the font used on the labels and labelpad and pad to move the labels away from the axis so that they become clearer to read. 
# 

# In[5]:


# List of style sheets in pyplot
plt.style.available


# ##### 3.4 Plotting more data on the same Axis
# 
# Although we have now created an nice clean, descriptive plot, what if we would like to add more data. This can be done by simply reusing the same axis and plotting the new data.
# We have plotted the sine wave previously, now lets plot the cosine wave (Cos in Mathamatics)

# In[6]:


# Generates an array of cos(x) values
y1 = np.cos(x)

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


# Above you can see I simply added the cosine data to the same axis and plotted along them so we can now visualise the similarities and differences of the sine and cosine waves.
# You may also have noticed that a legend was added in the bottom left hand corner - this is a really handy little function ```plt.legend()``` and is really important to a plots readability when you are visualising mulitple distinct data points on the same axis - NB pyplot is smart and can sometimes guess what the legend should be, but if it cannot, you need to specify a label by passing in the label argument to the ```plt.legend```function, as I did above.  
# I also used the ```plt.xlim``` function to get rid of any excess whitespace on the plot by limiting the x-axis so that I only show where values are actually plotted. This can also be done on the y-axis using ```plt.ylim```.

# ##### 3.5 Using multiple axis
# 
# Above we have looked at the basic plotting functionality of pyplot and how we can generate and visualise data using some simple commands to the numpy and pyplot library, we have even seen how to add data to existing axis.  
# Now we will look at generating more than one set of axis - this is extremly usesful and powerful from both a visualisation and analyicital standpoint. Depending on the datasets or maybe the "story" you are trying to tell, or point you are trying to emphasise with your data, you may want or need more than one set of axis.  
# 
# This can be done by creating what are called subplots in pyplot.  
# This can be done in two ways.
# 1. Create a Base figure (we have done this above) and use the ```fig.add_subplot(1,2,1)``` where the first two numbers indicate the size of the array created (here 1 row and 2 columns), while the third number indicates which subplot this will be. We can assign this back to a variable to create it as an axis. The only difference here between what we previously did and here is now we have an axis where instead of using ```fig.title``` or ```fig.xlabel``` we now have to use ```ax.set_title``` and ```ax.set_xlabel``` . You can see this method below under: **Using a Base Figure**
# 2. We can also use ```fig, ax = plt.subplots(1,2, figsize = (10,5))``` to specify straight away that we are creating subplots where fig is our base axis and ax is an array of axis which we can access just a we would a list or an array. We can thus plot the same information as have done previously. You can see this method below under: **Specifying number of Subplots**
# 
# You will see below that we can generate the same subplots using slightly different methods - I would suggest using the second method as standard practice, simply because it is slighly more flexable from a programming standpoint in my opinion. You can change and add subplots easily if you notice something else you would like to visualise from your data set, or if you are adding data to your existing dataset.

# ##### Using a Base Figure

# In[7]:


# Defines a variable for your array of subplots
fig = plt.figure(figsize=(20,10))

# Adds a subplot to the array
ax1 = fig.add_subplot(1,2,1)

#Plot 1
# Plots the sine function on the first subplot
ax1.plot(x,y,'r')
ax1.set_title("Sine function")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.grid(True)

# Plot 2
# Plots the cosine function on the second subplot
# Adds second subplot to the array
ax2 = fig.add_subplot(1,2,2)
ax2.plot(x,y1,'g')
ax2.set_title("Cosine function")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.grid(True)

# Ensure no overlapping
plt.tight_layout()


# ##### Specifying number of Subplots

# In[8]:


# Specifying number of plots required and their size
fig, ax = plt.subplots(1,2, figsize = (20,10))

# Plots the sine function on the first subplot
ax[0].plot(x,y,'r')
ax[0].set_title("Sine function")
ax[0].set_xlabel("x")
ax[0].set_ylabel("y")
ax[0].grid(True)

# Plots the cosine function on the second subplot
ax[1].plot(x,y1,'g')
ax[1].set_title("Cosine function")
ax[1].set_xlabel("x")
ax[1].set_ylabel("y")
ax[1].grid(True)

#to ensure no overlapping
plt.tight_layout()


# ##### Other Simple Examples
# 
# Matplotlib.pyplot can do a lot more than I have demonstrated so far but I think displaying some of the "simpler" functions where the benifit is a more obvious (for example the legend, label and tight_layout functions) is a good way to get comfortable and see how pyplot is trying to make life easier for the programmer and the reader.
# We can also specify the types of plots we would like to generate based on our understanding of the data set, would a 2d plot be better here?? - sometimes a scatter plot, box plot, histogram, matrix plot, radar plot or heatmap may be more suitable - I will give a few short examples of some 2D plots before diving into my three interesting plots. 

# <a id='2d_plot'></a>
# ### 4. 2D Plots 

# ##### matplotlib.pyplot.imshow
# 
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html

# In[9]:


# Changing back to default style
plt.style.use('default')

# Creates a 10x10 array of random integers from 1 (inclusive) to 10 (exclusive)
two_d = np.random.randint(1,11, (10,10))


# In[10]:


# Plots array x 
plt.imshow(two_d,cmap='cividis',extent=(20,80,20,80))

# Print numerical arrey
print(two_d)

# Adds title
plt.title("A bunch of random numbers")

# Axes labels
plt.xlabel("x")
plt.ylabel("y")

# Generates a scale
plt.colorbar()


# If you look at the corrolation from the 2d numerical array to the plot, you wll be able  to see that the numbers match the key from the colour bar

# ##### matplotlib.pyplot.matshow
# 
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.matshow.html

# In[11]:


# a 2D array with linearly increasing values on the diagonal 0 (inclusive) to 10 (exclusive)
a = np.diag(range(10))
print(a)

# generate plot
plt.matshow(a)

# add title 
plt.title('Matrix Plot')

# Axes labels
plt.xlabel("x")
plt.ylabel("y")

# Generates a scale
plt.colorbar()
 


# Once again if you look at the corrolation from the 2d numerical array to the plot, you wll be able to see that the numbers match the key from the colour bar.  
# I found this really good to help me visualise what this plot was showing me about the data.

# <a id='three_plot'></a>
# # 5. Three interesting plots

# ### 5.1 Plot 1 - The Histogram
# 
# ##### An Introduction
# A histogram is a graphical representation that organizes a group of data points into user-specified ranges. Similar in appearance to a bar graph, the histogram condenses a data series into an easily interpreted visual by taking many data points and grouping them into logical ranges or bins.[3](https://www.investopedia.com/terms/h/histogram.asp)
# 
# A histogram is one of the more plain but effective visualisations in data analysis.
# Here is a link to a short youtube video I found extremly useful. It explains what a histogram is trying to show the reader, and shows some of the things to watch out for to generate the most effective analyicital data from the visualisation.[StatQuest:Histograms Clearly Explained](https://www.youtube.com/watch?v=qBigTkBLU6g). 
# 
# From the video we can see a histogram is a bar graph-like representation of data that buckets a range of outcomes into columns along the x-axis. The y-axis represents the number count or percentage of occurrences in the data for each column and can be used to visualize data distributions.[4](https://www.investopedia.com/terms/h/histogram.asp)
# 
# The histograms below are generated usung random data from the numpy package.
# They are not "interesting" in the classical sense of the word - but however, what is interesting is what we learn from the the two plots.
# 

# ### Histograms: 2D Data Representation

# In[12]:


#change default style sheet
plt.style.use('dark_background')

#Change default figure size
plt.rcParams['figure.figsize'] = [25,5]


# In[13]:


# plt.subplot - to generate the plots side by side
plt.subplot(1, 2, 1)
x = np.random.normal(0.0, 1.0, 10000)
plt.hist(x, bins = 20)
plt.title('random.normal')

plt.subplot(1, 2, 2)
x = np.random.uniform(-3.0, 3.0, 10000)
plt.hist(x, bins = 20)
plt.title('random.uniform')

plt.show()


# ### Analysis of the Plots
# 
# As you can see from the plots they each tell a very different story regarding distribution.
# 
# In the first plot we can see that the "Random" data generates the data unevenly, as the you approch 0 on the x-axis the frequency becomes higher and higher.
# In the second plot howver the distribution is spread much more evenly across the plot. This is due to the way I have requested the data sing the numpy package - the titles of the plots indicate the type of "Random" data I have requested.
# 

# 
# The normal distribution and uniform distribution share the following similarity:
# 
# Both distributions are symmetrical. That is, if we were to draw a line down the center of the distribution, the left and right sides of the distribution would perfectly mirror each other:
# However, the two distributions have the following difference:
# 
# The distributions have different shapes.
# The normal distribution is bell-shaped, which means value near the center of the distribution are more likely to occur as opposed to values on the tails of the distribution.
# The uniform distribution is rectangular-shaped, which means every value in the distribution is equally likely to occur.
# 

# ### 5.2 Plot 2 - Diverging Bar Charts

# ##### Diverging barcharts
# Diverging Bar Charts are used to ease the comparison of multiple groups. Its design allows us to compare numerical values in various groups. It also helps us to quickly visualize the favorable and unfavorable or positive and negative responses. The bar chart consisted of a combination of two horizontal bars starting from the middle - one bar extends out from right to left and the other extends out from left to right. The length of the bar is corresponding to the numerical value it represents.[[5]](https://www.geeksforgeeks.org/diverging-bar-chart-using-python/)
# Although this is not a partgicularly complex chart, I have found from my work (that sometimes constists of proof-reading and editing these types of charts for a wider audience),  that charts that easily distingusish between the negative and positive are extremly useful and impactful in presentations and training. Of course not all data analysis is so clear cut and we often have to dig our way out of the grey, especially of you are using bigger or "messier" datasets, but if possible I have found that having the data tell a clear easy to read story, is often far more impactful than showing off how you can combine lots of data types and make a big crowded complex chart  
# 
# The Code for this plot was taken from [MachineLearningPlus.com](https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/#10.-Diverging-Bars).

# In[14]:


# Prepare Data
#Read in data
df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mtcars.csv")
x = df.loc[:, ['mpg']]


# In[15]:


# Peek at the structure of the data 
df.head()


# In[16]:


# Peek at x - make sure it is MPG
x.head()


# In[17]:


# Define second dataframe
# coefficient of variation expresses the relative variation of MPG
df['mpg_z'] = (x - x.mean())/x.std()

# Define colors of bars based on less than or greater than 0
df['colors'] = ['red' if x < 0 else 'green' for x in df['mpg_z']]

#Sort the values and reset the dataframe so the headers and colums are in place
# inplace = True , the data is modified in place, which means it will return nothing and the dataframe is now updated
df.sort_values('mpg_z', inplace=True)
df.reset_index(inplace=True)


# In[18]:


#change default style sheet
plt.style.use('classic')


# In[19]:


# Draw plot
plt.figure(figsize=(14,14), dpi= 80)
plt.hlines(y=df.index, xmin=0, xmax=df.mpg_z)
for x, y, tex in zip(df.mpg_z, df.index, df.mpg_z):
    t = plt.text(x, y, round(tex, 2), horizontalalignment='right' if x < 0 else 'left', 
                 verticalalignment='center', fontdict={'color':'red' if x < 0 else 'green', 'size':14})
# Decorations
plt.yticks(df.index, df.cars, fontsize=12)
plt.title('Diverging Text Bars of Car Mileage', fontdict={'size':20})
plt.grid(linestyle='--', alpha=0.5)
plt.xlim(-2.5, 2.5)
plt.show()


# ##### Examining the plot - Visualisation
# As you can see the code above has produced a very clear and consise chart based on the fuel effiency data of each of the car types listed.  
# Althogh what the plot is telling us may be 'interesting' to some people (I dont think I could afford 90% of the cars listed so the list would be much shorter for me), for the purpose of this notebook it is the intriguing visualisation that I would like to discuss.
# 
# Firstly the red and green is always a strong indicator of good/bad or stop/go. In this plot I believe it is used to bias the reader into thinking the 'good' numbers are the green ones - in terms of fuel effiency they are probaby right....but the cars at the other end of the list, the Maserati, Camaro, Cadillac would be considered much more exclusive brands than Toyota, Fiat or Honda. So depending on what you are trying to  show or highlight, colour-code accordingly.  
# Second when you are using the data of well known brand names I find it is always useful to try and display those names on your plot(unless you connot because of bias or security). It will draw the readers eye to familiar words - in the case above i found myself looking for my car model (its not there - Nissan didnt seem to make the cut) and then subconsciously looking at the models I knew and checking where they fell on the list. The creator of this plot had managed to get me to interact with the data without any explaination - that in my opinion is the key to a good informative plot.
# Finally the clear title and especially the perferated lines to help readability are the icing on the cake. I have expierenced many presentations where if I am not sitting directly in front of the presenter I sometimes find the slides can become meaningless espically if I have to struggle to follow along the with the data - here the plotter is guiding you to the information that they think you need wherever they can.  
# To bring this back to pyplot, what I am trying to convey here is that almost all of these little features are flexible in pyplot and although numbers dont lie, how the numbers are presented can sometimes be more impactful than the truth behind them, and pyplot has dozens of these tools to help you target that impact.

# ### 5.3 Plot 3 - Scatterplot and Annotation

# ##### Scatter Plots
# 
# Scatter plots have always been one of my 'favourite' plot types - simply because I could understand and read them pretty easily. Also they can give surprising insights that you may miss from the typical bar chart or histogram as it can clearly show you the relationship between two variables, and more importantly you can see that relationship even if it is a non-linear pattern.
# What is also a factor is that it is one of the easier plots to code - however this did not all go as plan for me.

# ##### Raw Data
# For this section I used some data that interests me.  
# I used the NFL team data for the 2020 regualar season from: https://www.pro-football-reference.com/years/2020/advanced.htm   
# 
# Steps to reproduce raw data:
#  - Go to https://www.pro-football-reference.com/years/2020/advanced.htm   
#  - Download Advanced Passing - Air Yards for the 2020 season as Excel workbook from the "Share & Export" drop down 
#  - Download Team Advanced Rushing for the 2020 season as Excel workbook from the "Share & Export" drop down 
#  - I did a little manual work here - as the data was sorted by the the Team Names I simply copied the columns I needed from the Team Advanced Rushing workbook and saved them into the Advanced Passing notebook and saved as total workbook in CSV format. 
#  - Save raw data CSV to preferred location
# 
#  
# 

# In[20]:


# Data downloaded in CSV Format from: https://www.pro-football-reference.com/years/2020/advanced.htm 
nflCsv = pd.read_csv('data_pyplot/nfl_2020_team_data.csv')


# In[21]:


# Take a peek at the data
# Used raw data to do a check here to make sure the ray data matched the DF 
print(nflCsv.head())


# In[22]:


# Crete df with columns I want to use
nfl2020team = nflCsv[['Tm','P-Cmp','P-Att','P-Yds','R-Att','Yds']]


# In[23]:


# put data into pandas dataframe
# this stopped me getting the really annoying indexing errors later
nfl2020team = pd.DataFrame(nfl2020team)


# In[24]:


#Create Columns for total offense
# Passing Yards + Rushing Yards = Total Yards
# Passing Attempts + Rushing Attempts = Total Attempts

nfl2020team['Tot-yds'] = nfl2020team['P-Yds'] + nfl2020team['Yds']
nfl2020team['Tot-att'] = nfl2020team['P-Att'] + nfl2020team['R-Att']


# In[25]:


# Take a peek at the data
# You can also do a quick spot check here at this point using the raw data to make sure you are correct
nfl2020team.head()


# In[26]:


#change default style sheet
plt.style.use('bmh')


# In[27]:



# plot for Total Offence
fig, ax = plt.subplots(figsize=(20, 8))
x = nfl2020team['Tot-att'].values
y = nfl2020team['Tot-yds'].values
t = nfl2020team['Tm'].values
ax.scatter(x, y)
ax.set_xlabel('Total Attmpts', fontname="Arial", fontsize=20)
ax.set_ylabel('Total Yards', fontname="Arial", fontsize=20)
ax.set_title('Total Offence 2020', fontname='Comic Sans MS',fontsize=50 )
ax.set_facecolor('g')
for i, txt in enumerate(t):
    ax.annotate(txt, xy=(x[i], y[i]), xytext=(x[i], y[i]+0.5), ha='center', weight = 'bold')

# plot for Total Passing Offence
fig, ax = plt.subplots(figsize=(20, 8))
x = nfl2020team['P-Att'].values
y = nfl2020team['P-Yds'].values
t = nfl2020team['Tm'].values
ax.scatter(x, y)
ax.set_xlabel('Pass Att', fontname="Arial", fontsize=20)
ax.set_ylabel('Pass Yds', fontname="Arial", fontsize=20)
ax.set_title('Pass Attempts vs Pass Yards 2020', fontname='Comic Sans MS',fontsize=50 )
ax.set_facecolor('skyblue')
for i, txt in enumerate(t):
    ax.annotate(txt, xy=(x[i], y[i]), xytext=(x[i], y[i]+0.5), ha='center', weight = 'bold')
    
    
# plot for Total Rushing Offence
fig, ax = plt.subplots(figsize=(20, 8))
x = nfl2020team['R-Att'].values
y = nfl2020team['Yds'].values
t = nfl2020team['Tm'].values
ax.scatter(x, y)
ax.set_xlabel('Rush Att', fontname="Arial", fontsize=20)
ax.set_ylabel('Rush Yds', fontname="Arial", fontsize=20)
ax.set_title('Rush Attempts vs Rush Yards 2020', fontname='Comic Sans MS',fontsize=50 )
ax.set_facecolor('c')
for i, txt in enumerate(t):
    ax.annotate(txt, xy=(x[i], y[i]), xytext=(x[i], y[i]+0.5), ha='center', weight = 'bold')

plt.show()


# Here I gatherd the offensive statistical data for all 32 NFL teams for the 2020 season and broke down the data into 3 catogries - Passing Data, Rusing Data and Total Offence Data(Passing + Rushing).  I will say I am a little disappointed at how this turned out.  Although the plots do make a lot of sense to me as I watched the season and followed along I was unable to really display all I had wanted to.
# I had visions of the plots being much cleaner - maybe even with some interaction where if you clicked on the team name it would bring you to the team website, or the team logo would pop up if you hovered over the name - but some of that was just a step too far for me at the moment - also jupyter doent seem to allow some of the animation/interaction I got to work on visual studios.  
# So in all, even though I was a little disappointed in my customization and visualisation the data told me the story I was expecting - kind of.
# 
# Two things stood out to me - in the Passing and Rush plots the Baltimore Ravens are at polar opposites in both attempts and yards gained - now I know Baltimore had a relitively good season - however it surprised me that a team could be so poor in the passing aspect of the game and still have such a successful season (Finished 4th or 5th overall).  
# Second - in the Total Offence plot - the Houston Texans - who were one of the worst 3 teams in the entire league that year, were actually pretty efficent when they did have the ball - they had the least offensive attempts, but were top 12 in yards gained. Now knowing the game, this is probably a really bad look for their defence as it means they were not able to get back the ball, and because of this they were probably really far behind towards the end of the game so some of their statistiacs are flawed (garbage-time stats). However if I was the manager of this team it is at least pointing me in a direction that deserves furter investigation.  
# Honestly I really enjoyed my messing about with this but I spent a huge amount of time on it (I must have started 10 differnt nfl .ipynb's and installed multiple nfl data libraries). That was really not helpful to the rest of the project grade. However I think it may be something I come back to as a summer project before the new season though.

# ### 5.4 Plot 4 - Bonas Plot with Seaborn - Heatmaps and Corrolations

# For my final plot I will be using seaborn to generate it, a python library built on matplotlib.pyplot. 
# This actually comes from a part of a project I did last year in my programming and scripting module - but it was my first time using a heat map and i was surprised at how it made me look at the data differently.  
# I used a heat map to help me with analysing the correlations between the variables. Although the data is duplicated on this map I found an extremely helpful visualisation tool and easy to read. Where the correlation is 1 or 'reddest' we can see that the variable data will be the same so the correlation will match - the further the figure is away from 1 (going from red to blue to purple), the less correlation there is.  
# 

# In[28]:


# Read in the data
irisCsv = pd.read_csv('data_pyplot/irisdata.csv')

#Give column names
irisCsv.columns = ['sepal length', 'sepal width', 'petal length' , 'petal width', 'species']
grouped = irisCsv.groupby('species')

#test - compare with file
print (grouped.first())


# In[29]:


# Heatmap for the entire data set
sns.heatmap(irisCsv.corr(),annot=True,cmap='rainbow', linewidths=.5)


# The least correlation happens between petal values and sepal width (-.42 and -.36). We can see the highest correlation between the between petal length and width (.96) - this tells us as one gets larger, so does the other, and this number is so close to 1 I began to assume this is the case across all species. Surprisingly to me, there was a high correlation between the petal values and the sepal length (.87 and .82, petal length and width respectively) This correlation was surprising as it was so low with the sepal width. I was able to conclude from this data that the sepal width did not strongly correlate with any of the other variables.
# 
# However because my interest was now peaked by the fact the sepal variables did not strongly correlate, I I decided to generate one for each species. The combination of the text summary and the heat maps, led to some very interesting findings.

# In[30]:


# Use groupby to gather the data each column for plotting
irisCsv_set = grouped.get_group('Iris-setosa')
irisCsv_ver = grouped.get_group('Iris-versicolor')
irisCsv_vir = grouped.get_group('Iris-virginica')


# In[31]:


# Heatmap for Setsosa
sns.heatmap(irisCsv_set.corr(), annot=True, cmap='rainbow') 
plt.title('Iris-Setsosa')
plt.show()

# Heatmap for Versicolor
sns.heatmap(irisCsv_ver.corr(), annot=True, cmap='rainbow') 
plt.title('Iris-Versicolor')
plt.show()

# Heatmap for Virginica
sns.heatmap(irisCsv_vir.corr(), annot=True, cmap='rainbow') 
plt.title('Iris-Virginica')
plt.show()


# Firstly the correlations that I had found with the overall dataset did not seem to carry over to the correlations of the grouped species.
# 
# Specifically while the overall data set showed correlation between the petal length and width, this was not reflected when broken down by species - it dropped below the overall number of .96 in all cases. Secondly, the weakest variable for correlation of the overall data set, the Sepal width, went from being negative to positive across all species, most notably with the Iris-Setsosa. This trend continued across almost all variables where the inital correlations from the overall dataset were remarkably different to correlations of the variables when analysed by species.  
# 
# From my research I found that this was a known phenomenon with the dataset, and many other datasets called Simpsons Paradox. Simpson’s paradox, also called Yule-Simpson effect, in statistics, an effect that occurs when the marginal association between two categorical variables is qualitatively different from the partial association between the same two variables after controlling for one or more other variables. This was interesting and led me to reading up more on Simpsons Paradox. It was a good learning experience as it taught me not to take for granted the relationship between two variables if there was one or more other variable in the dataset. My further research on this informed me that this was not a particularly rare occurrence in the world of Data Analysis.

# <a id='conclu'></a>
# # 6. Conclusion

# In conclusion, pyplot is an extremly valuable and "easyish" library to use. My rookie programming levels not withstanding, it was an extremly interesting project and I learned alot about matplotlib.pyplot and its sister libraries, seaborn, numpy and pandas.  
# When I started this project, as usual, I got extremly overwhelemed and anxious about all of the information that was available about pyplot. The sheer volume made me a bit uneasy as I was wondering how I was going to whittle it all down to something susscinct.  
# Also the "read the docs" mantra that is in the programming world makes perfect sense, and I think I have gotten better at it, but knowning what docs you are looking for  and then understanding what you are reading in the docs, is an absolute skill in itself, one I hope to improve as it kills my time management.   
# However once I had read a few blogs and perused through a sea of tutorials on youtube I began to realise, it was mostly the same tutorial, with slight variations here and there. This helped me to focus in on the fundementals of the package and begin from there. That is why I chose to do a brife demo showing some of its functionality before diving into the 3 plots section of the notebook. 
#   
# I also gained some insight into customisation and how valuable it is for the creator to use the customisation functions to tell the story of the data as you want it told. Now in python terms pyplot is one of the older libraries so some of the add on or sister libraries such as seaborn may be better if you are looking for all the "bells and whistles",
# I ran into plenty of problems and frustrations that had me usually figurativly but sometimes literally pulling my hair out, however getting through them and seeing the final result was rewarding - even if i did not always manage to fulfill the visualisation I had created in my mind.

# # END
