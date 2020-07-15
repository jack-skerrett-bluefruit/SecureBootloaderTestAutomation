#include <util/atomic.h>

size_t const bufferSize = 100;
char buffer[bufferSize + 1];
unsigned int length = 0;
const byte resetPin = 4;
const byte interruptPin = 2;
const byte ledPin = 5;
bool postLEDOn = LOW;


void setup() {
  Serial.begin(115200);
  pinMode(resetPin, OUTPUT);
  pinMode(ledPin, OUTPUT);
  attachInterrupt(digitalPinToInterrupt(interruptPin), postLEDStateCheck, CHANGE);
}

void parse(){
  buffer[length] = 0;
  if(strcmp(buffer, "reset") == 0){
    digitalWrite(resetPin, HIGH);
    delay(1000);
    digitalWrite(resetPin, LOW);
    Serial.write(buffer);
    }
  if(strcmp(buffer, "postled") == 0){
    if(postLEDOn == HIGH){
      Serial.write("1");
    }
    else{
      Serial.write("0");
    }
  }
}

void postLEDStateCheck(){
  ATOMIC_BLOCK(ATOMIC_RESTORESTATE){
    postLEDOn = digitalRead(interruptPin);
  }
}

void loop() {
  while(Serial.available() > 0){
    auto incomingByte = Serial.read();
    if(incomingByte == '$'){
      length = 0;
    }
    else if(incomingByte == '\r'){
      parse();
      length = 0;
    }
    else {
      if(length < bufferSize){
        buffer[length] = incomingByte;
        length++;
         }
    }
  }
}
