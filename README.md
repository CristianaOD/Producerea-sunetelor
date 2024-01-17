# Producerea-sunetelor

- Vom folosi numpy, matplotlib, și sounddevice.

import numpy as np

import matplotlib.pyplot as plt

import sounddevice as sd

- Generarea unui semnal sinusoidal
Întâi trebuie să definim parametrii sinusoidei continuue:

orizontul de timp (t)

frecvența semnalului original (f0)

amplitudinea (A)

faza (φ)

time_of_view = 1     # s

frequency = 2        # Hz

amplitude = 1

phase = 0

- Iar apoi parametrii de măsurare, sinusoida discretizată:

frecvența de eșantionare (fs)

perioada de eșantionare (ts)

numărul de eșantionare (n)

sampling_rate = 12    # Hz

sampling_period = 1./sampling_rate  # s

n_samples = time_of_view/sampling_period

Cu datele de mai sus putem genera orizontul de timp cu momentele de interes pentru semnalul continuu și cel discretizat (t, respectiv nts):

atime = np.linspace (0, time_of_view, int(10e5 + 1)) # s.

time = np.linspace (0, time_of_view, int(n_samples + 1))

Observație: orizontul de timp continuu (analog) este de fapt un orizont de timp discret (nts) foarte dens (n=105 eșantione).

Cu aceste date putem crea o funcție sinus ce generează sinusoidele parametrizate conform variabilelor de mai sus:

def sine (amplitude, frequency, time, phase):

    return amplitude * np.sin (2 * np.pi * frequency * time + phase)
    
## Sinusoidă continuă
- Pentru a obține o sinusoidă "continuă" putem apela funcția sine:

asignal = sine(amplitude, frequency, atime, phase)

plt.grid(True)

plt.plot (atime, asignal)

- Sinusoidă discretizată
Discretizarea se obține apelând aceiași funcție sine dar cu parametrii discreți și folosind stem pentru a obține cele n eșantioane:

signal = sine(amplitude, frequency, time, phase)

plt.grid(True)

plt.stem (time, signal)

## Producerea și audiția unui ton
- Pentru a produce o sinusoidă ce poate fi percepută de urechea umană trebuie să creștem frecvența și amplitudinea acesteia.

În exemplul de mai jos generăm o sinusoidă de frecvență f0=440Hz
 și amplitudine 10.000
 pe care o discretizăm cu frecvența de eșantionare fs=44.100Hz
 pe un orizont de timp de 2s
.

time_of_view = 2     # s

frequency = 440      # Hz

amplitude = 10000

phase = 0

sampling_rate = 44100

sampling_period = 1./sampling_rate  # s

n_samples = time_of_view/sampling_period

time = np.linspace (0, time_of_view, int(n_samples + 1))

tone = sine(amplitude, frequency, time, phase)

- Aceast ton îl vom discretiza cu o frecvență de eșantionare fs
 conform sampling_rate și îl vom transforma în formatul WAV prin conversia eșantioanelor la întregi pe 16-biți:

sd.default.samplerate = sampling_rate

wav_wave = np.array(tone, dtype=np.int16)

sd.play(wav_wave, blocking=True)

sd.stop()

## Sarcini:

-Scrieți tonurile pentru notele muzicale Do, Re, Mi, Fa, Sol, La, Si, Do.

- Compuneți un cântec simplu clasic (ex. Frère Jacques) într-un singur semnal.
