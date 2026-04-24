import os
import random
import numpy as np
import matplotlib.pyplot as plt

from scipy.io.wavfile import read
from algorithm import *

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
    folder = 'C:/git/Maths/samples/'
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
    extract = s[10:duration+10]

    # 4: Extraction de la signature (Q1 à Q3)
    encoder.process(fs, extract)
    encoder.process(fs, extract)

    hashes = encoder.hashes 
    
    for entry in database:
        # On compare l'extrait (hashes) avec chaque morceau de la base (entry['hashcodes'])
        matcher = Matching(hashes, entry['hashcodes'])
        
        # Le critère le plus simple : si on a beaucoup de points communs (ex: > 20)
        # c'est que c'est le bon morceau[cite: 56, 57].
        if len(matcher.matching) > 20:
            print(f"Match trouvé : {entry['song']} !")
            
            # Affichage du nuage de points (Question 5) [cite: 50]
            matcher.display_scatterplot()
            
            # Affichage de l'histogramme des offsets (Question 6) 
            matcher.display_histogram()
            
            break # On s'arrête dès qu'on a trouvé le morceau