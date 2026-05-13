# Laptop Price Predictor

A machine learning web application that predicts laptop prices based on hardware specifications.

## Features

- Random Forest regression model
- One-hot encoded categorical features
- Flask web interface
- Interactive form input

## Input Features

- Company
- Type of laptop
- Screen size
- Resolution
- RAM
- CPU Brand & Model
- GPU Brand & Model
- SSD / HDD

## Model

- Algorithm: Random Forest Regressor
- R² Score: ~0.85
- MAE: ~344

## ▶ How to run locally

```bash
git clone https://github.com/AM-201/laptop-price-predictor.git
cd laptop-price-predictor
pip install -r requirements.txt
python app.py
```
