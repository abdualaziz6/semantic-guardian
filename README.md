# Semantic Guardian

AI-powered system for detecting logical inconsistencies in survey responses in real time.

## Project Overview

Semantic Guardian is a prototype developed for the Data Innovation Hackathon (Road to Riyadh).  
The system integrates AI with survey platforms to detect logical inconsistencies during data entry and improve statistical data quality.

## Features

- Real-time validation of survey responses
- Detection of logical inconsistencies
- Rule-based validation
- AI-ready validation module

## Project Structure

semantic-guardian/
api/
- main.py
- validator_rules.py
- validator_llm.py
- requirements.txt

ui/
- app.py
- requirements.txt

## Run API

cd api  
pip install -r requirements.txt  
uvicorn main:app --reload  

## Run UI

cd ui  
pip install -r requirements.txt  
streamlit run app.py
