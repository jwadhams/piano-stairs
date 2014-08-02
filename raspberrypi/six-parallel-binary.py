import pygame
import serial
import time

onpi = True

numpins = 6

# switch between piano and guitar every 3 minutes
seconds = 3 * 60

previnputs = [False for a in range(0, numpins)]

if onpi:
    ser = serial.Serial('/dev/ttyACM0', 9600)

pygame.mixer.pre_init(channels=6, buffer=1024)
pygame.mixer.init()

# 1 2 3   5 6    8
# g a b c d e f# g
# g a b   d e    g
# c d e f g a b  c
# 8 6 5 3 2 1
letters = ["d", "e", "f", "g", "a", "b"]
letters = letters[::-1]
piano_notes = [pygame.mixer.Sound("../piano-notes/"+letter+".wav") for letter in letters]

while True:
    line = ""
    if onpi:
        line = ser.readline()
    else:
        line = raw_input()
    if len(line) < 6:
        continue
    for i in range(0, numpins):
        curr = line[i] != '0'
        prev = previnputs[i]
        if curr and not prev:
            piano_notes[i].play()
        previnputs[i] = curr

