piano-stairs
============

This project is a direct descendent of (Bonnie Eisenman's piano stairs)[https://hackaday.com/2013/11/11/hackprinceton-piano-stairs/] project for HackPrinceton Fall 2013. Demo'd on Nov 10th, 2013.

For my purposes, I didn't want to wire every stair with two wires on one side to a photoresistor, and to wires on the other side to a light emitter. Instead I hoped to build a small box with an ultrasonic sensor per stair. Each box would get power, ground, and I2C (all of which could be carried over four-conductor CAT-3 with RJ-11 heads) passed through from the stair before, or the Raspberry Pi at the base of the project.  It was a much simpler wiring schematic, but ultimately the latency between I2C polling and Ultrasound polling, and occasional cross-talk between ultrasonic sensors made the project unusable.
