const int led = 13;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(led, OUTPUT);
}

void loop() {
  if (Serial.available()>0) 
   {
      char option = Serial.read();
      if ( option == '9' ) {
        digitalWrite(led, HIGH);
      }
      if ( option == '6' ) {
        digitalWrite(led, LOW);
      }
   }

}
