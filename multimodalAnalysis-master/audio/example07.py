"""! 
@brief Example 07
@details Frequency prerceived discrimination experiment
@author Theodoros Giannakopoulos {tyiannak@gmail.com}
"""
from __future__ import print_function
import os, time, scipy.io.wavfile as wavfile, numpy as np
from random import randint

def play_sound(freq, duration, fs):
    t = np.arange(0, duration, 1.0/fs);  x = 0.5*np.cos(2 * np.pi * t * freq)
    wavfile.write("temp.wav", fs, x); os.system("play temp.wav -q")

if __name__ == '__main__':
    freqs, thres, n_exp, fs = [250, 500, 1000, 2000, 3000], [2, 5, 10, 20], 10, 16000
    answers = [[] for i in range(len(freqs))]
    for i_f, f in enumerate(freqs):
        for t in thres:
            answers[i_f].append(0)
            for i in range(n_exp):
                sequel = randint(1, 2)
                if sequel == 2:
                    play_sound(f, 0.5, fs); time.sleep(0.5); play_sound(f+t, 0.5, fs)
                else:
                    play_sound(f+t, 0.5, fs); time.sleep(0.5); play_sound(f, 0.5, fs)
                ans = int(input('Which was higher (1/2):'))
                if ans == sequel: answers[i_f][-1] += 1
    print("Freq\t", end='')
    for t in thres: print("{0:.1f}\t".format(t), end='')
    print("")
    for i_f, f in enumerate(freqs):
        print("{} Hz\t".format(f), end='')
        for i_t, t in enumerate(thres):
            print("{0:.1f}\t".format(answers[i_f][i_t] / float(n_exp)), end='')
        print("")