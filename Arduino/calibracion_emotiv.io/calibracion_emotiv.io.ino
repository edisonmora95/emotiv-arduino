const int adelante = 12;
const int atras = 11;

void setup() {
  Serial.begin(9600);
  pinMode(adelante, OUTPUT);
  pinMode(atras, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if ( Serial.available() > 0 ) {
    char option = Serial.read();
    if ( option == '9') {
      digitalWrite(adelante, HIGH);
      digitalWrite(atras, LOW);
    }
    if ( option == '6') {
      digitalWrite(atras, HIGH);
      digitalWrite(adelante, LOW);
    }
  }
}
