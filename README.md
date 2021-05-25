# Wine Recommendations

by Zachary Greenberg

<p align="center"><img src="https://github.com/zachagreenberg/Wine_Recommendations/blob/main/Images/Banner.png" width="600" height="250" /></p>


# Overview
When it comes to selecting a wine, there are many choices. Having recommendations is helpful, as it will educate customers about new bottles and wineries alike. With the help of Data Science, I have generated a content based recommender system to identify wines that are similar to ones we already enjoy. To be sure of the quality of the data, I have run a MultiNomial Bayes to assess the provided textual reviews of each wine. Additionally, I have created a simple front end of the finished recommender system using Streamlit.

# Business Problem
If we can identify wines that are similar to ones we already enjoy, we can have an easier time selecting new wines with this new information. Additionally, wineries can use this algorithm to recommend other wines in their roster. 

# Data
The data for this recommender system was scraped from [Vivino.com](https://www.vivino.com/), a website which houses information and reviews on wines. A total of 1800 wines were extracted. With each of these wines, the following information was provided:

-**winery**: str, the winery that makes that specific wine  
-**wine_name**: str, the name of the wine  
-**wine_type**: str, the classification of the wine (ie red, white)  
-**wine_country**: str, the country in which the wine was made  
-**average_rating**: float, the average rating of the wine on Vivino.com  
-**num_of_ratings**: int, the number of ratings for that wine  
-**wine_price**: float, the price per bottle  
-**grapes**: str, the grapes utilized in the wine  
-**alcohol_content**: the percent alcohol in the wines  
-**reviews**: str, descriptive text reviews of the wine

**IMPORTANT NOTE: Due to the updates of Vivino.com, the scraping process cannot be replicated. Additionally there are frequent repeats of wines with further scrolling down the webpage. I would suggest putting the links into a set() to accomodate for this. 

# Exploratory Data Analysis
My process began by looking at the distribution of wine types from my scraped data:

<p align="center"><img src="https://github.com/zachagreenberg/Wine_Recommendations/blob/main/Images/wine_graphs.png" width="1000" height="380" /></p>

The distribution of wines was fairly even amongst the 6 types. It was also not surprising that the top 3 countries represented from these wines were France, the US, and Italy. 


One of my focuses was specifically the text reviews. I performed NLP techniques on them and generated word clouds for each of the types of wine. (All of the clouds are available in the image folder, I condensed it here down to 4 of the 6 to save space.) 

<p float="left">
  <img src="https://github.com/zachagreenberg/Wine_Recommendations/blob/main/Images/Redcloud.png" width="300" height="300" />
  <img src="https://github.com/zachagreenberg/Wine_Recommendations/blob/main/Images/Whitecloud.png" width="300" height="300" /> 
</p>

<p float="left">
  <img src="https://github.com/zachagreenberg/Wine_Recommendations/blob/main/Images/Dessertcloud.png" width="300" height="300" />
  <img src="https://github.com/zachagreenberg/Wine_Recommendations/blob/main/Images/Fortifiedcloud.png" width="300" height="300" /> 
</p>

We can see from these wordclouds that the reviews seem to characterize the profiles of the wines pretty well. 




# Modeling
Before I created my recommender system, I put the parsed review text data into a classification algorithm to assess their ability to predict the type of wine.

With the utilization of MultiNomial Naive Bayes, the textual data had an 83% accuracy rate of correctly identifying the types of wine. This allowed me to validate the reviews as helpful bits of information in generating content based recommendations.

<p align="center"><img src="https://github.com/zachagreenberg/Wine_Recommendations/blob/main/Images/Matrix.png" width="500" height="350" /></p>

I then created variations of recommender systems using Cosine Similarity and Euclidean Distance as metrics. The variations included a general wine recommender and even recommendatons by winery. 

<p align="center"><img src="https://github.com/zachagreenberg/Wine_Recommendations/blob/main/Images/Model_comparison.png" width="550" height="100" /></p>

This image is a comparison of the two models for a general wine recommender. Each of the models returned 10 wines using the 1000 Stories Chardonnay 2018 as a base for recommendations. 


# Evaluation
The output of my rec system is difficult to interpret numerically. According the comparison of 'average_rating' and 'wine_price' in the models, the Euclidean model seemed a bit more probable, as the averages were closer to the input wine. The true success of it, I believe, is more subject to opinion due to the nature of content based recommendations. I called on the help of my wine drinking friends to try out the results, and they all agreed the Euclidean Distance model seemed most logical.


I was pleased to achieve 83% accuracy in the MultiNomial Bayes test I ran on the text data. This makes me feel more sure of my results. 

# Streamlit

I was able to take my recommender system and create a basic front end for user interaction using streamlit:

<p align="center"><img src="https://github.com/zachagreenberg/Wine_Recommendations/blob/main/Images/Demo.gif" width="600" height="400" /></p>

Using this interactive recommender, the user can select up to 25 wines to be recommended!


# Next Steps
Some of the next steps I would like to take include:
- Adding more wines to the roster
- Using LDA for topic modeling to supplement the search features for the models
- Enhancing my Streamlit app

-----------------------------------------------
## Repository Structure

|_ data
|_ images
|_ streamlit
|_ .gitignore
|_ EDA_Modeling_Eval.ipynb
|_ README.md
|_ Wine_Rec_Presentation.pdf

