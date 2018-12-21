// constants won't change. They're used here to set pin numbers:
const int buttonPin = 2;     // the number of the pushbutton pin
const int ledPin =  11;      // the number of the LED pin

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status
int fsrValue = 0;
int startIter = 0;
char charArr[4];
int arrPosition = 0;
int iter = 0;
int startNewChar = 0;

char characterCompare[4][5] = {
  {'1', '2', '0', '0', 'A'},
  {'2', '1', '1', '1', 'B'},
  {'2', '1', '2', '1', 'C'},
  {'2', '1', '1', '0', 'D'}
};

void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
  Serial.begin(9600);
  for (int i = 0; i < 4; i++) {
    charArr[i] = '0';
  }
}

void loop() {
  // read the state of the pushbutton value:
  fsrValue = analogRead(A0);
  buttonState = digitalRead(buttonPin);
  
  // check if the pushbutton is pressed. If it is, the buttonState is LOW:
  if (buttonState == LOW) {
    // Button is pressed
    if (startNewChar == 0) {
      iter = 0;
      Serial.println("Button was pressed");
      // Just started pressing the button
      // Serial.print("Iter = ");
      // Serial.println(iter);
      startIter = iter;
      startNewChar = 1;
    }
  } else {
    // Button is not pressed
    if (startNewChar == 1) {
      if ((iter - startIter) > 3000) {
        // This was a long press
        charArr[arrPosition] = '2';
        Serial.println("2");
      } else {
        // This was a short press
        charArr[arrPosition] = '1';
        Serial.println("1");
      }
      arrPosition += 1;
      startNewChar = 0;
    }

    // Serial.println(fsrValue);

    if (fsrValue > 100) {
      Serial.println("FSR was pressed");
      int i = 1;
      // This means the fsr has been pressed
      for (; i <= 4 ; i++) {
        int result = strncmp(charArr, characterCompare[i-1], 4);
        // Serial.println(result);
        if (result == 0) {
          Serial.print("Successfully found a match -- ");
          Serial.println(characterCompare[i-1][4]);
          break;
        }
      }
      if (i <= 4) {
        Serial.println(i);
        blinkLed(i);
      }
      // Clear all our buffers
      for (int jk = 0; jk < 4; jk++) {
        charArr[jk] = '0';
      }
      arrPosition = 0;
      startNewChar = 0;
    }
  }
  
  iter += 1;

}

void blinkLed(int num) {
  for (int k = 0; k < num; k++) {
    digitalWrite(ledPin, HIGH);
    delay(1000);
    digitalWrite(ledPin, LOW);
    delay(1000);
  }
}
