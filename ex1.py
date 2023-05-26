import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import medfilt

# on charge les données du fichier temperatures.npy
data = np.load('temperatures.npy')
Treel = data[:, 0]
Vmesure = data[:, 1]

Testime = 10 * Vmesure - 10 # calcul de la température à partir de la tension

# question 1
plt.plot(Testime, label='Température théorique')
plt.plot(Treel, label='Température réelle')
plt.xlabel('Mesure')
plt.ylabel('Température')
plt.legend()
plt.show()

# question 2
erreur = Treel - Testime # calcul de l'erreur
plt.hist(erreur)
plt.xlabel('Erreur')
plt.ylabel('Nombre de mesures')
plt.show()

# question 3
RMSE = np.sqrt(np.mean(erreur**2))
print('RMSE :', RMSE)

# question 4
Vfiltre = medfilt(Vmesure, kernel_size=None)

# question 5
Tfiltre = 10 * Vfiltre - 10
erreur_filtre = Treel - Tfiltre
RMSE_filtre = np.sqrt(np.mean(erreur_filtre**2))
print('RMSE filtré :', RMSE_filtre)

# on compare les RMSE des températures mesurée et lissée
delta_RMSE = RMSE - RMSE_filtre
print('différence de RMSE :', delta_RMSE)

# on compare les histogrammes des température mesurée et lissée
plt.hist(Testime, label='Température mesurée', alpha=0.5)
plt.hist(Tfiltre, label='Température filtrée', alpha=0.5)
plt.show()

# on affiche les courbes de températures réelle, mesurée et filtrée superposées
plt.plot(Treel, label='Température réelle')
plt.plot(Testime, label='Température mesurée')
plt.plot(Tfiltre, label='Température filtrée')
plt.xlabel('Mesure')
plt.ylabel('Température')
plt.legend()
plt.show()


