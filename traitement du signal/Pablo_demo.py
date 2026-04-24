import os
import random
import numpy as np
import matplotlib.pyplot as plt

from scipy.io.wavfile import read
from pablo_trait import *

# ----------------------------------------------
# Run the script
# ----------------------------------------------
if __name__ == '__main__':

    # 1: Load the database
    with open('songs.pickle', 'rb') as handle:
        database = pickle.load(handle)

    # 2: Encoder
    nperseg=128
    noverlap=32
    min_distance=25
    time_window=1.
    freq_window=1500
    encoder = Encoding(nperseg=nperseg, noverlap=noverlap, 
      min_distance=min_distance,
      time_window=time_window, 
      freq_window=freq_window)
      
   # 3: Récupérer un morceau au hasard
    folder = './samples/'
    # On liste tout le contenu sans filtre d'exclusion
    songs = [f for f in os.listdir(folder) if f.endswith('.wav')]    
    song = random.choice(songs)
    print('Selected song for extract: ' + song)
    filename = folder + song

    # Lecture et passage en mono (crucial pour le spectrogramme)
    fs, s = read(filename)
    if len(s.shape) > 1:
        s = np.mean(s, axis=1) 

    # Découpage de l'extrait de 10 secondes
    duration = int(10 * fs)
    extract = s[0:duration]

    # 4: Extraction de la signature (Q1 à Q3)
    encoder.process(fs, extract)
    hashes = encoder.hashes 

    # 5: Comparaison avec un morceau RANDOM de la base (Q6)
    random_item = random.choice(database)
    print(f"Comparaison avec le morceau de la base : {random_item['song']}")

    # Création de l'objet de comparaison
    matcher_random = Matching(hashes, random_item['hashcodes'])

    # 6: Visualisation (Q5 et Q6)
    print(f"Nombre de correspondances : {len(matcher_random.matching)}")
    
    # Nuage de points (doit être éparpillé)
    matcher_random.display_scatterplot() 
    
    # Histogramme des offsets (doit être plat)
    matcher_random.display_histogram() 