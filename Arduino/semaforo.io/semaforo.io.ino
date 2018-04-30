
const int pinAmarillo = 13;
const int pinRojo = 12;
 
void setup() 
{
   Serial.begin(9600);
   pinMode(pinAmarillo, OUTPUT);
   pinMode(pinRojo, OUTPUT);
}
 
void loop()
{
   digitalWrite(pinRojo, HIGH);
   if (Serial.available()>0) 
   {
      char option = Serial.read();
      if ( option == '9' ) {
        digitalWrite(pinAmarillo, HIGH);
        digitalWrite(pinRojo, LOW);
        delay(3000);
        digitalWrite(pinAmarillo, LOW);
        digitalWrite(pinRojo, HIGH);
      }
   }
}
