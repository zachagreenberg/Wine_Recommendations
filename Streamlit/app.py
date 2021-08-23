"""This is the code for my simple Streamlit app."""



#importing libraries
import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import euclidean_distances


#importing datasets
information = pd.read_csv('https://raw.githubusercontent.com/zachagreenberg/Wine_Recommendations/main/Streamlit/df.csv')
vectorized_data = pd.read_csv('https://raw.githubusercontent.com/zachagreenberg/Wine_Recommendations/main/Streamlit/scale_model_data.csv', index_col = ['title'])


#renaming the columns
information.rename(columns = {'title':'Wine Name', 'wine_type': 'Wine Type', 'wine_country': 'Wine Country',
                             'grapes': 'Grapes', 'average_rating': 'Average Rating', 'wine_price': 'Wine Price'}, inplace = True)
information.set_index('Wine Name', inplace = True)


#making containers
header = st.beta_container()
about = st.beta_container()
recommender = st.beta_container()

with header:
    st.title('Wine Recommender System')
    st.text('By: Zachary Greenberg')
       
    from PIL import Image
    image = Image.open('https://github.com/zachagreenberg/Wine_Recommendations/blob/main/Images/App.png') 
    st.image(image) 
       

with about:
    st.title('About')
    st.write('Welcome to the page for my wine recommender system! This is my capstone project at Flatiron School\'s Data Science Immersive Bootcamp. \nThe data for this wine recommender comes from [Vivino.com](https://www.vivino.com). Users can select from a variety \nof 1800 wines scraped from the site. These wines are of different varieties from wineries all around the world. The user can choose the amount of recommendations they would like in a range of 1 to 25. The recommendations will show you the wine names as well as other information including the type of wine, country in which the wine was made, grapes the wine was made with, average rating (from a scale of 1-5 on Vivino.com), as well as the wine price in USD. The recommender system will generate it\'s recommendations based on the selection using Euclidean Distance, returning the closest entries.') 

with recommender:
    wines = information.index.tolist()
 
    option = st.selectbox('Select a Wine:', wines)
    numbers = st.slider('How may recommendations would you like?', min_value=1, max_value=25)


    euc_dist = euclidean_distances(vectorized_data, vectorized_data)
    # Storing indices of the data
    indices = pd.Series(information.index)

    def euclidean_recommendations(wine, euc_dist, num_recommendations):
        """
        This function takes in a wine from the index along 
        with the euclidean distance array, and number of
        recommendations. It returns the top recommended wines
        with the highest similarity scores.
        """
        recommended_wines = []
        index = indices[indices == wine].index[0]
        similarity_scores = pd.Series(euc_dist[index]).sort_values(ascending = True)
        top_10_wines = list(similarity_scores.iloc[1:num_recommendations+1].index)
        for i in top_10_wines:
            recommended_wines.append(list(information.index)[i])
            matches = information.loc[recommended_wines][['Wine Type', 'Wine Country', 'Grapes', 'Average Rating', 'Wine Price']]
            matches['Average Rating'] = matches['Average Rating'].round(1).astype('object')
            matches['Wine Price'] = matches['Wine Price'].round(2).astype('object')
        st.dataframe(matches)

print(f'Since you like {option}, you may also enjoy:')
euclidean_recommendations(option, euc_dist, numbers)



