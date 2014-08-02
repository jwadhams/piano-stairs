import pygame
import serial
import time

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
piano_notes = [pygame.mixer.Sound("piano-notes/"+letter+".wav") for letter in letters]

skip_until = 0

time.sleep(3)

while True:
    line = ""
    line = ser.readline()
    note = line[0]
    if(note == '-'):
        print "Nope"
	continue
    if(skip_until > time.time()):
        print "Waiting for" , skip_until , "is now" , time.time()
	continue
    pygame.mixer.Sound("piano-stairs/piano-notes/"+note+".wav").play()
    skip_until = time.time() + 2
