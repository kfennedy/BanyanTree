//14241

int add_pin = 2;
int sub_pin = 3;

int add_now = 0;
int add_prev = 0;
int sub_now = 0;
int sub_prev = 0;

void add(){
  Serial.println("add");
}
void sub(){
  Serial.println("sub");
}

void setup() {
  Serial.begin(9600);
  pinMode(add_pin, INPUT);
  pinMode(sub_pin, INPUT);
}

void loop(){
  Serial.println("input_air");
  add_now = digitalRead(add_pin);
  delay(150);
  if (add_now != add_prev) {
    if (add_now == HIGH) {
      Serial.println("i am adding");
      add();
    }
  }
  add_prev = add_now;

  sub_now = digitalRead(sub_pin);
  delay(150);
  if (sub_now != sub_prev) {
    if (sub_now == HIGH) {
      Serial.println("i am subtracting");
      sub();
    }
  }
  sub_prev = sub_now;
}

