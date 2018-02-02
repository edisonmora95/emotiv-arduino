
const int pinLED = 13;
 
void setup() 
{
   Serial.begin(9600);
   pinMode(pinLED, OUTPUT);
}
 
void loop()
{
   if (Serial.available()>0) 
   {
      char option = Serial.read();
      if ( option == '9' ) {
        digitalWrite(pinLED, HIGH);
      }
      if ( option == '6' ) {
        digitalWrite(pinLED, LOW);
      }
   }
}
