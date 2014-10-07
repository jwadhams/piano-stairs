import pygame
import smbus
import re
import time
from glob import glob

bus = smbus.SMBus(1)
address = 0x08;


pygame.mixer.pre_init(channels=6, buffer=1024)
pygame.mixer.init()

piano_notes = {}
skip_until = {}

for note in glob("../piano-notes/*.wav"):
    note_name = re.search("([a-z0-9]+)\.wav$", note).group(1)
    piano_notes[note_name] = pygame.mixer.Sound(note)
    skip_until[note_name] = time.time()


note = "c"


while True:
    #time.sleep(0.5)

    distance = bus.read_byte(address)
    print "Distance: " , distance 

    if(distance == 0):
        #print "No obstruction"
        continue
    if(time.time() >= skip_until[note]):
        print "Playing", note
        piano_notes[note].play()
    skip_until[note] = time.time() + 0.5
