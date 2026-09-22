# Predictions du temps de traitement des fichiers : Cas ZazenData

import numpy as np

X = np.array([[2, 1],
      [4, 3],
      [6, 5]
     ])

y = np.array([13, 27, 42])

w = np.array([3, 4])
b = 2


predictions = X @ w + b
erreurs = y - predictions

print(predictions)
print(erreurs)
"""

prediction_fichier_1 = X[0][0]*w[0] + X[0][1]*w[1] + b
prediction_fichier_2 = X[1][0]*w[0] + X[1][1]*w[1] + b
prediction_fichier_3 = X[2][0]*w[0] + X[2][1]*w[1] + b

print(f"La prediction du premier fichier est :  {prediction_fichier_1}")
print(f"La prediction du premier fichier est :  {prediction_fichier_2}")
print(f"La prediction du premier fichier est :  {prediction_fichier_3}")

print(f"Les erreurs pour chaque fichier")
erreur_1 = y[0] - prediction_fichier_1
erreur_2 = y[1] - prediction_fichier_2
erreur_3 = y[2] - prediction_fichier_3


print(f"Fichier 1 = {erreur_1}")
print(f"Fichier 2 = {erreur_2}")
print(f"Fichier 3 = {erreur_3}")

"""