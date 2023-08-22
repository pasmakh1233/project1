import psycopg2
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
connection = psycopg2.connect(
    host = 'localhost',
    database = 'Goldenline_new',
    user = 'postgres',
    password = 1234
);
cur = connection.cursor()
sql = "SELECT * FROM client"
sql= "SELECT * FROM collecte"
cur.execute(sql)
axe_x = ["medecin", "ouvrier", "etudiant", "enseignant", "programmeur"]
axe_y = [5, 9, 7, 10, 15]
plt.bar(axe_x, axe_y)
plt.show()