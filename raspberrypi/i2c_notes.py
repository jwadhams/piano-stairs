import pygame
import smbus
import re
import time
from glob import glob

bus = smbus.SMBus(0)
address = 0x08;


pygame.mixer.pre_init(channels=6, buffer=1024)
pygame.mixer.init()

piano_notes = {}
skip_until = {}

for note in glob("../piano-notes/*.wav"):
    note_name = re.search("([a-z0-9]+)\.wav$", note).group(1)
    piano_notes[note_name] = pygame.mixer.Sound(note)
    skip_until[note_name] = time.time()

while True:
    line = ""
    distance = bus.read_byte_data(address, 1)
    print "Distance: " + distance 
    time.sleep(1)


    ##note = re.sub("\s+","", line)
    ##if(note not in piano_notes):
        ##print "Didn't recognize ##" + note + "##"
        ##continue
    ##if(time.time() >= skip_until[note]):
        ##print "Playing", note
        ##piano_notes[note].play()
    ##skip_until[note] = time.time() + 1
