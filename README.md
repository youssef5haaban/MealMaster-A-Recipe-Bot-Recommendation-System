# MealMaster: A Recipe Bot Recommendation System

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Overview

MealMaster is a Recipe Bot Recommendation System that aims to provide personalized recipe recommendations through a chatbot interface. The project utilizes clustering to categorize similar recipes and classification for user preferences. The features are seamlessly integrated into a user-friendly chatbot for efficient recipe discovery.

## Project Structure

- `nlp-project.ipynb`: The entire project is encapsulated in this Jupyter notebook.
- `main.py`: A Flask app designed to connect the project with Dialogflow.
- `pickle files`: Contains the saved model and final dataset for running the main application.
- `Requirements files`: Lists the packages installed in the environment.
- `food_recipes.csv`: The dataset used for the project.

## Problem Formulation

The project focuses on developing a chatbot for personalized recipe recommendations, taking into account the user's preferred cuisine and available ingredients. The system employs clustering to categorize similar recipes and classification to identify the most suitable category based on user preferences. The ultimate goal is to create a user-friendly chatbot that facilitates seamless recipe discovery.

## Dataset

The dataset used for the project, sourced from Kaggle, contains over 8,000 recipes, predominantly Indian dishes. Each recipe includes details on preparation, ingredients, cooking time, authorship, and ratings. This rich information allows for effective comparison of recipes and grouping of similar ones, forming the foundation for personalized recommendations.

## Usage

1. Open and run the `nlp-project.ipynb` Jupyter notebook to explore the entire project.
2. Execute `main.py` to launch the Flask app, connecting it with Dialogflow.
3. Utilize the saved models and final dataset provided in the `pickle files` directory.
4. Refer to the `Requirements files` to install the necessary packages in your environment.

## Photos

![Chatbot Screenshot 1](https://github.com/youssef5haaban/MealMaster-A-Recipe-Bot-Recommendation-System/assets/83844687/8de74678-4810-47a6-bb47-8e914c45b2b1)

![Chatbot Screenshot 2](https://github.com/youssef5haaban/MealMaster-A-Recipe-Bot-Recommendation-System/assets/83844687/91d5c433-6414-485f-ac90-01ce6d6b5e17)

![Chatbot Screenshot 3]![image](https://github.com/youssef5haaban/MealMaster-A-Recipe-Bot-Recommendation-System/assets/83844687/aae7b4f1-9d9a-4f4d-8b8c-c5895903e49f)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
