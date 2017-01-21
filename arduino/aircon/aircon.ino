//14211

int d0_pin = 8;
int d1_pin = 9;
int d2_pin = 10;
int d3_pin = 11;

int k0_pin = 2;
int k1_pin = 3;
int k2_pin = 4;
int k3_pin = 5;

void setup(){
  pinMode(d0_pin, OUTPUT);
  pinMode(d1_pin, OUTPUT);
  pinMode(d2_pin, OUTPUT);
  pinMode(d3_pin, OUTPUT);
  pinMode(k0_pin, OUTPUT);
  pinMode(k1_pin, OUTPUT);
  pinMode(k2_pin, OUTPUT);
  pinMode(k3_pin, OUTPUT);
  Serial.begin(9600);
}

void num16(){
//  1
  digitalWrite(d0_pin,HIGH);
  digitalWrite(d1_pin,LOW);
  digitalWrite(d2_pin,LOW);
  digitalWrite(d3_pin,LOW);

//  6
  digitalWrite(k0_pin,LOW);
  digitalWrite(k1_pin,HIGH);
  digitalWrite(k2_pin,HIGH);
  digitalWrite(k3_pin,LOW);
}

void num17(){
  digitalWrite(d0_pin,HIGH);
  digitalWrite(d1_pin,LOW);
  digitalWrite(d2_pin,LOW);
  digitalWrite(d3_pin,LOW);

  digitalWrite(k0_pin,HIGH);
  digitalWrite(k1_pin,HIGH);
  digitalWrite(k2_pin,HIGH);
  digitalWrite(k3_pin,LOW);
}

void num18(){
  digitalWrite(d0_pin,HIGH);
  digitalWrite(d1_pin,LOW);
  digitalWrite(d2_pin,LOW);
  digitalWrite(d3_pin,LOW);

  digitalWrite(k0_pin,LOW);
  digitalWrite(k1_pin,LOW);
  digitalWrite(k2_pin,LOW);
  digitalWrite(k3_pin,HIGH);
}

void num19(){
  digitalWrite(d0_pin,HIGH);
  digitalWrite(d1_pin,LOW);
  digitalWrite(d2_pin,LOW);
  digitalWrite(d3_pin,LOW);

  digitalWrite(k0_pin,HIGH);
  digitalWrite(k1_pin,LOW);
  digitalWrite(k2_pin,LOW);
  digitalWrite(k3_pin,HIGH);
}

void num20(){
  digitalWrite(d0_pin,LOW);
  digitalWrite(d1_pin,HIGH);
  digitalWrite(d2_pin,LOW);
  digitalWrite(d3_pin,LOW);

  digitalWrite(k0_pin,LOW);
  digitalWrite(k1_pin,LOW);
  digitalWrite(k2_pin,LOW);
  digitalWrite(k3_pin,LOW);
}

void num21(){
  digitalWrite(d0_pin,LOW);
  digitalWrite(d1_pin,HIGH);
  digitalWrite(d2_pin,LOW);
  digitalWrite(d3_pin,LOW);

  digitalWrite(k0_pin,HIGH);
  digitalWrite(k1_pin,LOW);
  digitalWrite(k2_pin,LOW);
  digitalWrite(k3_pin,LOW);
}

void num22(){
  digitalWrite(d0_pin,LOW);
  digitalWrite(d1_pin,HIGH);
  digitalWrite(d2_pin,LOW);
  digitalWrite(d3_pin,LOW);

  digitalWrite(k0_pin,LOW);
  digitalWrite(k1_pin,HIGH);
  digitalWrite(k2_pin,LOW);
  digitalWrite(k3_pin,LOW);
}

void num23(){
  digitalWrite(d0_pin,LOW);
  digitalWrite(d1_pin,HIGH);
  digitalWrite(d2_pin,LOW);
  digitalWrite(d3_pin,LOW);

  digitalWrite(k0_pin,HIGH);
  digitalWrite(k1_pin,HIGH);
  digitalWrite(k2_pin,LOW);
  digitalWrite(k3_pin,LOW);
}

void num24(){
  digitalWrite(d0_pin,LOW);
  digitalWrite(d1_pin,HIGH);
  digitalWrite(d2_pin,LOW);
  digitalWrite(d3_pin,LOW);

  digitalWrite(k0_pin,LOW);
  digitalWrite(k1_pin,LOW);
  digitalWrite(k2_pin,HIGH);
  digitalWrite(k3_pin,LOW);
}

void num25(){
  digitalWrite(d0_pin,LOW);
  digitalWrite(d1_pin,HIGH);
  digitalWrite(d2_pin,LOW);
  digitalWrite(d3_pin,LOW);

  digitalWrite(k0_pin,HIGH);
  digitalWrite(k1_pin,LOW);
  digitalWrite(k2_pin,HIGH);
  digitalWrite(k3_pin,LOW);
}

void loop() {
  Serial.println("air");
  delay(100);
  if (Serial.available()>0){
    String aha = Serial.readString();
    Serial.println("received on arduino = "+ aha);
    int number = atoi(aha.c_str());
    
    switch(number){
      case 16:{ num16(); break;}
      case 17:{ num17(); break;}
      case 18:{ num18(); break;}
      case 19:{ num19(); break;}
      case 20:{ num20(); break;}
      case 21:{ num21(); break;}
      case 22:{ num22(); break;}
      case 23:{ num23(); break;}
      case 24:{ num24(); break;}
      case 25:{ num25(); break;}
    }
  }
}
