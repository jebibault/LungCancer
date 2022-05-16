# Predict lung cancer risk and death
These models were trained on data from the prospective randomized multicenter trial PLCO that assessed the interest of lung cancer screening. From 1993 through 2001, this trial involved 154,901 participants aged 55 through 74 years, 77,445 of whom were assigned to annual screenings and 77,456 to usual care at 1 of 10 screening centers across the United States. We selected smokers within the PLCO patients to develop these models.

XGBoost was used to predict the risk of lung cancer within a year and the risk to die from lung cancer. Hyperparameters were tuned with Bayesian Optimization in a nested cross-validation manner. 

External validation was performed on the NLST dataset. The NLST trial prospectively enrolled 53,454 persons at high risk for lung cancer at 33 U.S. medical centers from August 2002 through April 2004. Participants were randomly assigned to undergo three annual screenings with either low-dose CT (26,722 participants) or single-view posteroanterior chest radiography (26,732).

The contents of the repository include the following:

assets
- custom css
- favicon

figures
- logo of the app

models
- PLCOLungCancerRisk.pkl - the XGBoost model for lung cancer risk in pickle format
- PLCOLungCancerDeath.pkl - the XGBoost model for lung cancer death in pickle format

tabs
- intro.py - The code for the 'About' tab
- predictCSS.py - The code for the 'Predict cancer-specific survival' tab

main app
- app.py - Initiates the Dash app
- index.py - The main Dash code with the layout and callback
- Procfile - The Procfile for Heroku
- requirements.txt - The requirements.txt file for Heroku
