import pygame
import smbus
import re
import time
from glob import glob

bus = smbus.SMBus(1)

pygame.mixer.pre_init(channels=6, buffer=1024)
pygame.mixer.init()

piano_notes = {}
skip_until = {}

sensors = {0x08 : 'c', 0x09 : 'd'}

for note in glob("../piano-notes/*.wav"):
    note_name = re.search("([a-z0-9]+)\.wav$", note).group(1)
    piano_notes[note_name] = pygame.mixer.Sound(note)
    skip_until[note_name] = time.time()



while True:
    #time.sleep(0.5)
	for address in sensors:
	    note = sensors[address]
        distance = bus.read_byte(address)

        if(distance == 0):
            print "Rest ", note
            continue
        if(time.time() >= skip_until[note]):
            print "Playing ", note
            piano_notes[note].play()
        skip_until[note] = time.time() + 0.5
