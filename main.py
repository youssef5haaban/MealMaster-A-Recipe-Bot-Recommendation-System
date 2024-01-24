# import flask dependencies
from flask import Flask, request
import joblib
import pandas as pd
import numpy as np
import pickle
import sklearn

# Load the trained models and other objects
kmeans = joblib.load('kmeans_model.pkl')
tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')
cosine_similarities = joblib.load('cosine_similarities.pkl')
df_final = pd.read_csv('recipes_for_recommendation.csv')

# initialize the flask app
app = Flask(__name__)

# Recommend recipes function
def recommend_recipes(recipe_title):
    # Use case-insensitive matching and strip spaces
    matching_rows = df_final[df_final['recipe_title'].str.strip().str.lower() == recipe_title.strip().lower()]

    # Check if any matching rows were found
    if matching_rows.empty:
        return [f"No recipes found for {recipe_title}. Please check the recipe name and try again."]

    idx = matching_rows.index[0]
    sim_scores = list(enumerate(cosine_similarities[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    recipe_indices = [i[0] for i in sim_scores]
    recommended_recipes = df_final['recipe_title'].iloc[recipe_indices].tolist()
    return recommended_recipes


def get_ingredients(recipe_title):
    matching_rows = df_final[df_final['recipe_title'].str.strip().str.lower() == recipe_title.strip().lower()]

    if matching_rows.empty:
        return None

    return matching_rows['ingredients'].iloc[0]

def get_instructions(recipe_title):
    matching_rows = df_final[df_final['recipe_title'].str.strip().str.lower() == recipe_title.strip().lower()]

    if matching_rows.empty:
        return None

    return matching_rows['instructions'].iloc[0]

def get_time(recipe_title):
    matching_rows = df_final[df_final['recipe_title'].str.strip().str.lower() == recipe_title.strip().lower()]

    if matching_rows.empty:
        return None

    return matching_rows['cook_time'].iloc[0]



@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    req = request.get_json(silent=True, force=True)
    fulfillmentText = ''
    query_result = req.get('queryResult')
    if query_result.get('action') == 'input.welcome':
        ### For the welcome intent
        fulfillmentText = "Hi, hi"

    elif query_result.get('action') == 'suggest.recipe':
        recipe_name = query_result.get('parameters').get('Recipe')
        print(f"Received recipe name: {recipe_name}")  # Print the input for debugging
        recommended = recommend_recipes(recipe_name)
        fulfillmentText = ", ".join(recommended)

    elif query_result.get('action') == 'ingredients':
        recipe_name = query_result.get('parameters').get('Recipe')
        ingredients = get_ingredients(recipe_name)
        if ingredients:
            fulfillmentText = f"Ingredients for {recipe_name} are: {ingredients}"
        else:
            fulfillmentText = f"I couldn't find ingredients for {recipe_name}. Please check the recipe name and try again."

    elif query_result.get('action') == 'instructions':
        recipe_name = query_result.get('parameters').get('Recipe')
        instructions = get_instructions(recipe_name)
        if instructions:
            fulfillmentText = f"Instructions for {recipe_name} are: {instructions}"
        else:
            fulfillmentText = f"I couldn't find instructions for {recipe_name}. Please check the recipe name and try again."

    elif query_result.get('action') == 'time':
        recipe_name = query_result.get('parameters').get('Recipe')
        time = get_time(recipe_name)
        if time:
            fulfillmentText = f"time for {recipe_name} is: {time}m"
        else:
            fulfillmentText = f"I couldn't find time for {recipe_name}. Please check the recipe name and try again."


    return {
        "fulfillmentText": fulfillmentText,
        "source": "webhookdata"
    }


# Run the app
if __name__ == '__main__':
    app.run()