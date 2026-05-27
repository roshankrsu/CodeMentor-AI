import os
import streamlit as st
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI") or st.secrets["MONGO_URI"]

client = MongoClient(MONGO_URI)

db = client["codementor_ai"]