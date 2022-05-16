from dash.dependencies import Input, Output
from dash import dcc
from dash import html

from app import app

layout = [
	html.Br(),
	dcc.Markdown("""#### Lung cancer screening saves lives"""),
	'Lung cancer is the leading cause of cancer death worldwide. Screening by low-dose computed tomography (LDCT) can reduce mortality from lung cancer among people with a heavy smoking history. Lung screening eligibility in the USA is based on the following criteria: age 50–80 years, at least 20 pack-years smoked, and for former smokers, no more than 15 years since quitting.',
	html.Br(),
	html.Br(),
	'The 2021 US Preventive Services Task Force Lung Cancer Screening Guidelines are available here:',
	html.A(" US Preventive Services Task Force, JAMA, 2021", href='https://pubmed.ncbi.nlm.nih.gov/33687470/', target="_blank", style={'font-weight': 'bold', 'color': '#48a1af', 'text-decoration': 'none'}),
	html.Br(),
	html.Br(),
	dcc.Markdown("""#### AI to predict the risk of lung cancer in current and former smokers"""),
	'These new models were created to predict the risk of lung cancer and the risk of lung cancer death in order to incite high-risk persons to get screened with low-dose computed tomography.',
	html.Br(),
	html.Br(),
	'How were these models developed and validated?',
	html.Br(),
	'Two datasets from two lung cancer screening prospective multicenter trials were used. The PLCO dataset was used to develop the models and the NLST dataset was used for external validation.',
	html.Br(),
	html.Br(),
	'The PLCO Trial',
	html.Br(),
	'The Prostate, Lung, Colorectal, and Ovarian (PLCO) Cancer Screening Trial was conducted to assess the role of lung cancer screening on survival. From 1993 through 2001, this randomized controlled trial involved 154,901 participants aged 55 through 74 years, 77,445 of whom were assigned to annual screenings with chest radiography and 77,456 to usual care at 1 of 10 screening centers across the United States.',
	html.A(" Oken MM et al., JAMA, 2011", href='https://pubmed.ncbi.nlm.nih.gov/22031728/', target="_blank", style={'font-weight': 'bold', 'color': '#48a1af', 'text-decoration': 'none'}),
	html.Br(),
	html.Br(),
	html.Br(),
	'The NLST Trial',
	html.Br(),
	'The National Lung Screening Trial was conducted to assess the interest of low-dose computed tomography for lung cancer screening. From 2002 to 2004, 53,439 participants were randomly assigned to low-dose CT or chest radiography at 33 U.S. centers for 3 years. Participants were asymptomatic, 55 to 74 years of age, with a history of at least 30 pack-years of smoking.',
	html.A(" NLST Team, NEJM, 2013", href='https://pubmed.ncbi.nlm.nih.gov/23697514/', target="_blank", style={'font-weight': 'bold', 'color': '#48a1af', 'text-decoration': 'none'}),
	html.Br(),
	html.Br(),
	dcc.Markdown("""#### Data"""),
	'The datasets were obtained from the National Cancer Institute Cancer Data Access System:',
	html.A(" National Cancer Institute Cancer Data Access System", href='https://cdas.cancer.gov/', target="_blank", style={'font-weight': 'bold', 'color': '#48a1af', 'text-decoration': 'none'})
]




