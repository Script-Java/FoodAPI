import io
import requests
from requests import request, Session
import pprint
import json
import apikey
import streamlit as st
from PIL import Image
import urllib.request


class FoodInformation:
    def __init__(self):
        url = "https://api.spoonacular.com/recipes/complexSearch"

        headers = {
            "Content-Type": "application/json"
        }

        parameters = {
            "apiKey": apikey.KEY,
            "minProtein": "21",
            "maxCalories": "700",
            "maxCarbs": "60",
            "maxFat": "30"
        }

        s = Session()
        s.headers.update(headers)
        req = s.get(url, params=parameters)
        res = req.json()
        pprint.pprint(res)
        st.title("Top 10 Healthy Recipes")
        for results in res["results"]:
            food_id = results["id"]
            food_name = results["title"]
            food_img = results["image"]
            nutrients = results["nutrition"]["nutrients"]
            calories = nutrients[0]["amount"]
            protein = nutrients[1]["amount"]
            fat = nutrients[2]["amount"]
            carbohydrate = nutrients[3]["amount"]
            st.write(f"### {food_name}")
            st.write(f"#### ID: {food_id}")

            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Calories", f"{round(calories)}", "")
            col2.metric("Protein", f"{round(protein)}g", "")
            col3.metric("Fat", f"{round(fat)}g", "")
            col4.metric("Carbohydrate", f"{round(carbohydrate)}g", "")


FoodInformation()
