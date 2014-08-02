/* 
 
 Use a knock-off PING))) sensor, the HC-SR04 based on http://www.arduino.cc/en/Tutorial/Ping
 
 Once we get a sense of the device's range and response, update it to pick a tone and instruct the Raspberry Pi
 what piano note to play.
 
 */

const int trigPin = 12;
const int echoPin = 13;
const int MAX_DISTANCE = 70; //cm

String notes[] = {"c1", "d", "e", "f", "g", "a", "b", "c"};


void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

}

void loop()
{
  // establish variables for duration of the ping,
  // and the distance result in inches and centimeters:
  long duration, cm;
  int note;

  // The HC-SR04 is triggered by a HIGH pulse of 2 or more microseconds to the Trig pin.
  // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(5);
  digitalWrite(trigPin, LOW);

  // The echo pin is used to read the signal from the HC-SR04 a HIGH
  // pulse whose duration is the time (in microseconds) from the sending
  // of the ping to the reception of its echo off of an object.
  duration =  pulseIn(echoPin, HIGH, 100000);

  // convert the time into a distance
  cm = microsecondsToCentimeters(duration);

  //Serial.print(cm);
  //Serial.println("cm");

  if(duration == 0 or cm > MAX_DISTANCE){
    Serial.println("-");
  }else{
    note = map(cm, 0, MAX_DISTANCE, 0, 7);
    Serial.println(notes[note]);
  }

  //Serial.println();

  delay(50);
}

long microsecondsToCentimeters(long microseconds)
{
  // The speed of sound is 340 m/s or 29 microseconds per centimeter.
  // The ping travels out and back, so to find the distance of the
  // object we take half of the distance travelled.
  return microseconds / 29 / 2;
}

