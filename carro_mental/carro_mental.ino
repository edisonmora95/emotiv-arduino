// int  adelante1 = 5;
// int  adelante2 = 6;
int led = 10;

// int velocidad = 255;

void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  // pinMode(adelante1, OUTPUT);
  // pinMode(adelante2, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    char estado = Serial.read();
    if (estado == '9') {
      // analogWrite(adelante1,velocidad);
      // analogWrite(adelante2,velocidad);
      digitalWrite(led,HIGH);
    }
    if (estado == '6') {
      digitalWrite(led,LOW);
      // analogWrite(adelante1,0);
      // analogWrite(adelante2,0);
    }
  }
  
} 
