# Wine Recommendations

by Zachary Greenberg

<p align="center"><img src="https://github.com/zachagreenberg/Wine_Recommendations/blob/main/Images/Banner.jpg" width="400" height="250" /></p>


# Overview
When it comes to selecting a wine, there are many choices. Having recommendations is helpful, as it will educate customers about new bottles and wineries alike. With the help of Data Science, I have generated a content based recommender system to identify wines that are similar to ones we already enjoy. I have additionally run a MultiNomial Bayes to assess the quality of the data.

# Business Problem
If we can identify wines that are similar to ones we already enjoy, we can have an easier time selecting new wines with this new information.  

# Data
The data for this recommender system was scraped from Vivino.com, a website which houses information and reviews on wines. A total of 1200 wines were extracted. With each of these wines, the following information was provided:

-*winery*: str, the winery that makes that specific wine  
-*wine_name*: str, the name of the wine  
-*wine_type*: str, the classification of the wine (ie red, white)  
-*wine_country*: str, the country in which the wine was made  
-*average_rating*: float, the average rating of the wine on Vivino.com  
-*num_of_ratings*: int, the number of ratings for that wine  
-*wine_price*: float, the price per bottle  
-*grapes*: str, the grapes utilized in the wine  
-*alcohol_content*: the percent alcohol in the wines  
-*reviews*: str, descriptive text reviews of the wine

**IMPORTANT NOTE: Due to the updates of Vivino.com, the scraping process cannot be replicated. Additionally there are frequent repeats of wines with further scrolling down the webpage. 

# Exploratory Data Analysis
My process began by looking at the distribution of wine types from my scraped data:

<p align="center"><img src="https://github.com/zachagreenberg/Wine_Recommendations/blob/main/Images/wine_graphs.png" width="400" height="250" /></p>


One of my focuses was specifically the text reviews. I performed NLP techniques on them and generated word clouds for each of the types of wine. 

<p align="center"><img src="https://github.com/zachagreenberg/Wine_Recommendations/blob/main/Images/Redcloud.png" width="400" height="250" /></p>

<p align="center"><img src="https://github.com/zachagreenberg/Wine_Recommendations/blob/main/Images/Whitecloud.png" width="400" height="250" /></p>

<p align="center"><img src="https://github.com/zachagreenberg/Wine_Recommendations/blob/main/Images/Sparklingcloud.png" width="400" height="250" /></p>

<p align="center"><img src="https://github.com/zachagreenberg/Wine_Recommendations/blob/main/Images/Rosecloud.png" width="400" height="250" /></p>

<p align="center"><img src="https://github.com/zachagreenberg/Wine_Recommendations/blob/main/Images/Fortifiedcloud.png" width="400" height="250" /></p>

<p align="center"><img src="https://github.com/zachagreenberg/Wine_Recommendations/blob/main/Images/Dessertcloud.png" width="400" height="250" /></p>




# Modeling
Before I created my recommender system, I put the parsed review text data into a classification algorithm to assess their ability to predict the type of wine.

With the utilization of MultiNomial Naive Bayes, the textual data had a 78% accuracy rate of correctly identifying the types of wine. This allowed me to validate the reviews as helpful bits of information in generating content based recommendations.

<p align="center"><img src="https://github.com/zachagreenberg/Wine_Recommendations/blob/main/Images/Matrix.png" width="400" height="250" /></p>

I then created 2 recommender systems using Cosine Similarity and Euclidean Distance as metrics. 

<p align="center"><img src="https://github.com/zachagreenberg/Wine_Recommendations/blob/main/Images/EuclideanModelOutput.png" width="400" height="250" /></p>


# Evaluation & Next Steps
The success of my rec systems output is more subject to opinion due to the nature of content based recommendations. I called on the help of my wine drinking friends to try out the results, and they all agreed the Euclidean Distance model seemed most logical.
I was pleased to achieve 78% accuracy in the MultiNomial Bayes test I ran on the text data. This makes me feel more sure of my result. 

Some of the next steps I would like to take include:
- Adding more wines to the roster
- Using LDA for topic modeling to make the search for wines by the descriptions
- Create an interface for user interaction

-----------------------------------------------
## Repository Structure

├── Data
├── Images
├── .gitignore
├── Wine_Recommendations.pdf
├── Project_Notebook.ipynb
└── README.md
