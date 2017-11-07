# -*- coding:utf-8 -*-

import os

file_names = os.listdir('./ElectricTitration')

for temp in file_names:
    new_name = temp.lower()
    os.rename('./ElectricTitration/'+temp,'./ElectricTitration/'+new_name)