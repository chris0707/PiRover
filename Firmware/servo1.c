#include<Servo.h>

Servo servoLeft;
Servo servoRight;

void setup(){
	servoLeft.attach(7);
	

	servoLeft.writeMicroseconds(1700);
}

void loop(){

}


