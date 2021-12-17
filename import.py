import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
basepath = "/home/raul/linux projects vscode/excel"
archivo1 = basepath + "/Necesidades de Inversiones 2020.xls"
df = pd.read_excel(archivo1, sheet_name="necesidades")
df.head()