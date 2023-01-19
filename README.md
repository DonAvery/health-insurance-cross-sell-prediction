# Health Insurance Cross Sell Prediction
This repository contains all the necessary information to run a classification model. Using Jupyter Notebooks, python scripts, BentoML and docker allow you to access and test this information.  It is also part of my ML-Zoomcamp Capstone Project.

## Environment
I run my machine learning projects on a standalone Ubuntu PC using conda. These instructions are meant for an Ubuntu system and I believe they should work on macOS. I have included items so that you may create them on a Windows machine, but I can't guarantee they will work.

## Data and Intention

The dataset was pulled from Kaggle here: https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction?select=train.csv

The target feature in this dataset is the `response` column. This column denotes if a customer purchased auto insurance or not. We want predict which customers might respond to a marketing campaign in the future.

Several models were used in this Jupyter Notebook:

- Logistic Regression
- Decision Tree
- Ensemble and Random Forest
- XGBoost

## Model Parameter Tuning
- Decision Tree - tuned `max_depth` and `min_samples_leaf`
- Ensemble and Random Forest - tuned `n_estimators`, `max_depth` and `min_samples_leaf`
- XGBoost - tuned `num_boost_rounds`, `eta`, `max_depth` and `min_child_weight`

## Run the Project

Create a folder where you will clone the GitHub repository into

Clone this repository `git clone https://github.com/DonAvery/health-insurance-cross-sell-prediction.git`

`cd health-insurance-cross-sell-prediction/files`

Run `conda env create -f environment.yml'

`conda activate eval`

If you don't yet have Docker installed then you will have to install it using `pip install docker`


I have also uploaded a requirements.txt you might need on a Windows system.

cd back to the customer marketing project and start the notebook service `jupyter notebook`.

Change folders in the notebook service to notebooks and open "Data-Prep-Clean-EDA.ipynb" to view the data ingestion, data prep and EDA.

Open the "Model-Training-Tuning-and-Selection.ipynb" to see the tuning and training.

The Best Model & BentoML Save.ipynb is what I created a python script from.

## Deployment and Testing

Change into the "files" directory and run `python3 train.py`, which will create the BentoML model.

Run `bentoml build` inside the files folder. Upon completetion you should see "Successfully build Bento(tag="health_insurance_classifier:shqowjebwkeyypd2"). The tag will actually be something different for you.conda 

Run `bentoml containerize <tag>` the tag will be given to you after the build.

Run `docker run -it --rm -p 3000:3000 <tag> serve --production`, this line will be given after docker run, copy and paste it.

Run `locust.py` and there will be a link to click on or right click and "open link" or just copy and paste this into your browser "http://localhost:3000/".

In the webpage click on "POST", then click on "Try it out", copy the contents of the client.py file and paste it into the "Request body" box pasting over anything that is in there.  This is a json format so there should be curly brackets opening and closing with the data inside, i.e. {}.

Now the data is ready to be sent to the model for a prediction.  Click the "Execute" button and you will see a response, the "Response body" box should contain a "status": "Not acceptable to promotion".
