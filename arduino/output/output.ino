//14221

int num = 12; //number of buttons
String results[26];
int pin_light[12] = { 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 };

void split(String temp){
  int l = temp.length();
  char carray[l];
  temp.toCharArray(carray,l);

  String appender = "";
  int index = 0;

  for (int i=0; i<l; i++){
    if (carray[i] == ' '){
      results[index] = appender;
      index++;
      appender="";
    }else{
      appender += carray[i];
    }
  }
}

void setup() {
  Serial.begin(9600);
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(7,OUTPUT);
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(11,OUTPUT);
  pinMode(12,OUTPUT);
  pinMode(13,OUTPUT);
}

void loop() {
  Serial.println("output");
  delay(100);

  if (Serial.available()>0){
    String aha = Serial.readString();
    split(aha);
    
    for (int i=0; i<num ; i++){
      int pin = atoi(results[(i*2)].c_str());
      if(results[(i*2)+1]=="1"){
        Serial.println("TURNING ONNNN");
        digitalWrite(pin, HIGH);
      }else{
        digitalWrite(pin, LOW);
        Serial.println("TURNING OFFFF");
      }
    }
  }
}
