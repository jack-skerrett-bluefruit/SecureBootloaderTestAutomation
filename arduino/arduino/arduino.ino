#include <util/atomic.h>

size_t const bufferSize = 100;
char buffer[bufferSize + 1];                    //This means that if your buffer has been filled to 100 (0-99) and then there is a carriage return, when you enter the PARSE function, nothing freaks out (it doesn't try buffer[101] = 0)
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
  buffer[length] = 0;                            //null terminate the string (append a zero)
  if(strcmp(buffer, "reset") == 0){
    digitalWrite(resetPin, HIGH);
    delay(1000);
    digitalWrite(resetPin, LOW);
    Serial.write(buffer);                        //this is sending confirmation to the terminal that "this is the command you told me to execute" 
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
  while(Serial.available() > 0){                //while there are bytes that are available to be read on the serial port
    auto incomingByte = Serial.read();          //read a byte into this variable (auto is just like var in other languages, an undefined variable)
    if(incomingByte == '$'){                    //starting your commands with a '$' means that you can retype commands and avoid corruption. You need the single quotes here because of how "" and '' are handled in some languages.
      length = 0;                               //In C (along with some others) using '' translates to a character 1  byte (8 bits) long, so just '$'. If you used "$", then it gets null terminated and becomes 2 bytes long ("$0").
    }
    else if(incomingByte == '\r'){              //this checks if carriage return has been sent
      parse();                                  //calling our parse function which is just checking which command has been sent
      length = 0;
    }
    else {
      if(length < bufferSize){                  //this stops you adding chars when you are going to exceed the length of your buffer
        buffer[length] = incomingByte;          //if you have space left in your buffer, add the incoming byte to the next space
        length++; 
         }
    }
  }
}
