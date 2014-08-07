/* 
 
 Use a knock-off PING))) sensor, the HC-SR04 based on http://www.arduino.cc/en/Tutorial/Ping
 
 Once we get a sense of the device's range and response, update it to pick a tone and instruct the Raspberry Pi
 what piano note to play.
 
 */

const int trigC = 10;
const int echoC = 11;
const int trigG = 12;
const int echoG = 13;

const int MAX_DISTANCE = 70; //cm

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  pinMode(trigC, OUTPUT);
  pinMode(echoC, INPUT);
  pinMode(trigG, OUTPUT);
  pinMode(echoG, INPUT);

}

void loop()
{

  playOnDetect(trigC, echoC, "C");
  playOnDetect(trigG, echoG, "G");
  
  delay(50);
}

long microsecondsToCentimeters(long microseconds)
{
  // The speed of sound is 340 m/s or 29 microseconds per centimeter.
  // The ping travels out and back, so to find the distance of the
  // object we take half of the distance travelled.
  return microseconds / 29 / 2;
}

long getDistance(int trigPin, int echoPin){
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
  long duration =  pulseIn(echoPin, HIGH, 100000);

  // convert the time into a distance
  return microsecondsToCentimeters(duration); 
}

void playOnDetect(int trigPin, int echoPin, String note){
  long distance = getDistance(trigPin, echoPin);

  if(0 < distance && distance < MAX_DISTANCE){
    Serial.println(note);
  }
}
