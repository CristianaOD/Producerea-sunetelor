#Realizatori: Cîrstea Ruxandra-Gabriela (Grupa 363) și Ojoc Diana-Cristiana (Grupa 363)

import numpy as np
import sounddevice as sd

##############################################Exercitiul 1##########################################################
def generare(frecventa, durata, amplitudine = 0.5, rata_esantionare = 44100):
    t = np.linspace(0, durata, int(rata_esantionare * durata))
    ton = amplitudine * np.sin(2 * np.pi * frecventa * t)
    return ton

#frecventa notelor muzicale in Hz
frecventa_note = {
    'Do': 261.63,
    'Re': 293.66,
    'Mi': 329.63,
    'Fa': 349.23,
    'Sol': 392.00,
    'La': 440.00,
    'Si': 493.88,
    'Do_inalt': 523.25
}

#durata fiecarei note in secunde
durata_nota = 1

print("Incepe redarea notelor muzicale");

#redarea notelor muzicale
for nota in ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si', 'Do_inalt']:
    frecventa = frecventa_note[nota]
    ton = generare(frecventa, durata_nota)
    print(f"Redare nota {nota}")
    sd.play(ton, samplerate=44100)
    sd.wait() #astepta finalizarea redarii inainte de a trece la urmatoarea nota

print("S-a finalizat redarea")


##############################################Exercitiul 2##########################################################

note = {
    'Do': 261.63,
    'Re': 293.66,
    'Mi': 329.63,
    'Fa': 349.23,
    'Sol': 392.00,
    'La': 440.00,
    'Si': 493.88,
}

armonii = {
    'terta': 1.20,  #factor de frecventa pentru adaugarea unei armonii la o terta deasupra notei principale
    'cvinta': 1.50,  #factor de frecventa pentru adaugarea unei armonii la o cvinta deasupra notei principale
}

melodie = [
    ('Do', 1.0),
    ('Re', 1.0),
    ('Mi', 1.0),
    ('Do', 1.0),
    ('Do', 1.0),
    ('Re', 1.0),
    ('Mi', 1.0),
    ('Do', 1.0),
    ('Mi', 1.0),
    ('Fa', 1.0),
    ('Sol', 1.0),
    ('Mi', 1.0),
    ('Fa', 1.0),
    ('Sol', 1.0),
    ('Sol', 1.0),
    ('La', 1.0),
    ('Sol', 1.0),
    ('Fa', 1.0),
    ('Mi', 1.0),
    ('Do', 1.0),
    ('Sol', 1.0),
    ('Do', 1.0),
    ('Sol', 1.0),
    ('La', 1.0),
    ('Sol', 1.0),
    ('Fa', 1.0),
    ('Mi', 1.0),
    ('Do', 1.0),
    ('Do', 1.0),
    ('Sol', 1.0),
    ('Do', 1.0),
]

#generarea semnalului pentru melodie cu armonii
rata_esantionare = 44100
semnal_melodie = np.array([])

print("Incepe melodia")
for nota, durata in melodie:
    frecventa = note[nota]
    timp = np.linspace(0, durata, int(rata_esantionare * durata))

    #crearea undei principale
    semnal_nota = 0.5 * np.sin(2 * np.pi * frecventa * timp)

    #adaugarea armoniilor (terta și cvinta) la unda principala
    semnal_nota_terta = 0.2 * np.sin(2 * np.pi * armonii['terta'] * frecventa * timp)
    semnal_nota_cvinta = 0.3 * np.sin(2 * np.pi * armonii['cvinta'] * frecventa * timp)

    #adaugarea armoniilor la unda principala si combinarea lor
    semnal_nota += semnal_nota_terta + semnal_nota_cvinta

    semnal_melodie = np.concatenate((semnal_melodie, semnal_nota))

#redarea melodiei
sd.play(semnal_melodie, rata_esantionare)
sd.wait()
print("S-a finalizat redarea")
