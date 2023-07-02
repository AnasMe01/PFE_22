#include <Wire.h>
#include <ZumoShield.h>
//#include <ZumoMotors.h>

#define MaxSpeed 400
#define TurnSpeed 150

//recived integer 
int x;
// the default speed
int varSpeed = MaxSpeed/3;

ZumoMotors motors;

// run the robot forward
void Step_forward(int setSpeed){
    for (int speed = 0; speed <= setSpeed; speed++)
  {
    motors.setLeftSpeed(speed);
    motors.setRightSpeed(speed);
    delay(2);
  }

  for (int speed = setSpeed; speed >= 0; speed--)
  {
    motors.setLeftSpeed(speed);
    motors.setRightSpeed(speed);
    delay(2);
  }
}

//forward 

void forward(int speed){
  motors.setSpeeds(speed,speed);
}
//backward
void backward(int speed){
  motors.setSpeeds(-speed,-speed);
}

/*flip direction 
void flip_direction(){
  }*/
  
//run the robot backwards
void Step_backward(int setSpeed){
    for (int speed = 0; speed >= -setSpeed; speed--)
  {
    motors.setSpeeds(speed,speed);
    delay(2);
  }
  for (int speed = -setSpeed; speed <= 0; speed++)
  {
    motors.setSpeeds(speed,speed);
    delay(2);
  }
}
// run left motor forward
  void leftMotoeForward(int turnSpeed){
  
  for (int speed = 0; speed <= turnSpeed; speed++)
  {
    motors.setLeftSpeed(speed);
    delay(2);
  }

  for (int speed = turnSpeed; speed >= 0; speed--)
  {
    motors.setLeftSpeed(speed);
    delay(2);
  }
}
  // run left motor backward
  void leftMotorBackwards(int turnSpeed){
  
  for (int speed = 0; speed >= -turnSpeed; speed--)
  {
    motors.setLeftSpeed(speed);
    delay(2);
  }
  
  for (int speed = -turnSpeed; speed <= 0; speed++)
  {
    motors.setLeftSpeed(speed);
    delay(2);
  }
}

  // run right motor forward
  void rightMotorForward(int turnSpeed){
  for (int speed = 0; speed <= turnSpeed; speed++)
  {
    motors.setRightSpeed(speed);
    delay(2);
  }
  
  for (int speed = turnSpeed; speed >= 0; speed--)
  {
    motors.setRightSpeed(speed);
    delay(2);
  }
}
  // run right motor backward
  void rightMotorBackwards(int turnSpeed){
  
  for (int speed = 0; speed >= -turnSpeed; speed--)
  {
    motors.setRightSpeed(speed);
    delay(2);
  }
  
  for (int speed = -turnSpeed; speed <= 0; speed++)
  {
    motors.setRightSpeed(speed);
    delay(2);
  }
  delay(500);
}
//turn robot
void turnLeftTurn(int turnSpeed){
  for (int speed = 0; speed <= turnSpeed; speed++)
  {
    motors.setRightSpeed(speed);
    motors.setLeftSpeed(-speed);
    delay(2);
  }
  for (int speed = turnSpeed; speed <= 0; speed++)
  {
    motors.setRightSpeed(speed);
    motors.setLeftSpeed(-speed);
    delay(2);
  }
  delay(500);
}
//turn right speed
void turnRightTurn(int turnSpeed){
  //motors.setRightSpeed(-turnSpeed);
  //motors.setLeftSpeed(turnSpeed);
  for (int speed = 0; speed <= turnSpeed; speed++)
  {
    motors.setRightSpeed(-speed);
    motors.setLeftSpeed(speed);
    delay(2);
  }
  for (int speed = turnSpeed; speed <= 0; speed++)
  {
    motors.setRightSpeed(-speed);
    motors.setLeftSpeed(speed);
    delay(2);
  }
  
  delay(500);
}
//turn 
void turnRight(int speed){
  motors.setRightSpeed(-speed);
    motors.setLeftSpeed(speed);
    delay(2);
  }
void turnLeft(int speed){
  motors.setRightSpeed(speed);
    motors.setLeftSpeed(-speed);
    delay(2);
  }

void setup()
{
    Serial.begin(115200);
    Serial.setTimeout(1);
    
  // uncomment one or both of the following lines if your motors directions need to be flipped
  //motors.flipLeftMotor(true);
  //motors.flipRightMotor(true);
}

void loop()
{
   while (!Serial.available());
  x = Serial.readString().toInt();
  switch(x){
    //forward curses.key_up
    case 1: forward(varSpeed); 
    break;
    //backward curses.key_down
    case 2: backward(varSpeed);
    break;
    //turn left curses.key_left
    case 3: turnLeftTurn(varSpeed);
    break;
    //turn right
    case 4: turnRightTurn(varSpeed);
    break;
    //case of capture and break belongs to the py script 
    //stop
    case 5: motors.setSpeeds(0,0);
    break;
    case 6: if( varSpeed >= 0 && varSpeed < MaxSpeed-50 ) varSpeed+=50;
    break;
    //decrese speed 
    case 7: if( varSpeed > 50 && varSpeed <= MaxSpeed ) varSpeed-=50;
    break;
    case 8: turnRight(MaxSpeed/2);
    break;
     
    case 9: turnLeft(MaxSpeed/2);
    break;
    /* 
    //step by step move 
    case 10: Step_forward(varSpeed); 
    //break;
    //decrese speed 
    case 11: Step_backward(varSpeed);
    //break;*/
  }
}
