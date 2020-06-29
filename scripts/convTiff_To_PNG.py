# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 10:01:25 2020

@author: LKUPSSINSKU
"""
import cv2
import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import QuantileTransformer 

from sklearn.model_selection import train_test_split

import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout

import math
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

import matplotlib.pyplot as plt
import random

import seaborn as sns
from time import time
from keras.callbacks import TensorBoard
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing
import numpy as np
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from keras.layers import Dropout
from keras import regularizers
from keras.regularizers import l1


import imageio
import os
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.metrics import confusion_matrix  


im = imageio.imread("Dados\\bisdom.tif")

cv2.imwrite('Dados\\bisdom.png', im[:,:,0:-1])
