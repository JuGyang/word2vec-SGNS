# 
# Description:定义一些常量
# Author：Yang Jiang
# Prompt: code in Python3 env


import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(base_dir, "Data")
common_dir = os.path.join(base_dir, "Common")
cache_dir = os.path.join(base_dir, "Cache")
model_dir = os.path.join(base_dir, 'Model')
