# set 'KAGGLE_USERNAME'='veragablina'
# set 'KAGGLE_KEY'='644d0fb09c40a4ea5ee30ff46e3da122'

import os
os.environ['KAGGLE_USERNAME'] = 'veragablina'
os.environ['KAGGLE_KEY'] = '644d0fb09c40a4ea5ee30ff46e3da122'
# kaggle competitions download -c dogs-vs-cats-redux-kernels-edition

import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()
files = api.competition_download_files("home-credit-credit-risk-model-stability")

# kaggle competitions download -c home-credit-credit-risk-model-stability
