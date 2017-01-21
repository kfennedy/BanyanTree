//14231

//int add_pin = 8;
//int sub_pin = 9;

int add_now = 0;
int add_prev = 0;
int sub_now = 0;
int sub_prev = 0;

int num = 11; //number of buttons
int pin_toggle[11] = { 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};
int initial_toggle [11] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int final_toggle [11] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
boolean state;

void setup() {
  Serial.begin(9600);
  pinMode(2, INPUT);
  pinMode(3, INPUT);
  pinMode(4, INPUT);
  pinMode(5, INPUT);
  pinMode(6, INPUT);
  pinMode(7, INPUT);
  pinMode(8, INPUT);
  pinMode(9, INPUT);
  pinMode(10, INPUT);
  pinMode(11, INPUT);
  pinMode(12, INPUT);
//  pinMode(add_pin, INPUT);
//  pinMode(sub_pin, INPUT);
}

void add(){
  Serial.println("add");
}
void sub(){
  Serial.println("sub");
}

void loop() {
  Serial.println("input");

  for (int i=0; i<num ; i++){
    final_toggle[i] = digitalRead(pin_toggle[i]);
    if (initial_toggle[i] != final_toggle[i]){
      Serial.println("toggle_"+String(pin_toggle[i]));
    }
    initial_toggle[i]=final_toggle[i];
  }

//  add_now = digitalRead(add_pin);
//  delay(50);
//  if (add_now != add_prev) {
//    if (add_now == HIGH) {
//      Serial.println("i am adding");
//      add();
//    }
//  }
//  add_prev = add_now;
//
//  sub_now = digitalRead(sub_pin);
//  delay(50);
//  if (sub_now != sub_prev) {
//    if (sub_now == HIGH) {
//      Serial.println("i am subtracting");
//      sub();
//    }
//  }
//  sub_prev = sub_now;
}
