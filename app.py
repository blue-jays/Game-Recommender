import streamlit as st
import pickle as pk
import pandas as pd
import numpy as np

# Function to recommend similar games
def recommend(game, dfp, sim_src):
    # Find index of the game in the dfp DataFrame
    if game in dfp.index:
        index = np.where(dfp.index == game)[0][0]
    else:
        return []

    # Get the top 5 similar games
    sim_itm = sorted(list(enumerate(sim_src[index])), key=lambda x: x[1], reverse=True)[1:6]
    
    # Get the game names for the recommendations
    recommendations = [dfp.index[i[0]] for i in sim_itm]
    
    return recommendations

# Title for the Streamlit app
st.title("Game Recommender System")

# Load the DataFrame and similarity matrix from pickle
dfp = pk.load(open('game.pkl', 'rb'))
sim_src = pk.load(open('sim_src.pkl', 'rb'))

# List of all game titles for the dropdown
game_list = dfp.index.tolist()  # Assuming game names are in the index of dfp

# Dropdown to select a game
option = st.selectbox(
    "Enter Game Title For Recommendation",
    game_list
)

# Call the recommend function
if option:
    recommended_games = recommend(option, dfp, sim_src)
    
    # Display the recommended games
   
    for game in recommended_games:
        st.write(game)
