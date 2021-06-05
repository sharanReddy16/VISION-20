char b;
int In1=7; 
int In2=8;
int In3=12;
int In4=13;  
int ENA=3; 
int ENB=11;
int SPED=110;
int SPED1=80;
int s;
#define ir 4
void setup()
{ Serial.begin(9600);
pinMode(In1,OUTPUT); 
pinMode(In2,OUTPUT); 
pinMode(In3,OUTPUT); 
pinMode(In4,OUTPUT); 
pinMode(ENA,OUTPUT);
pinMode(ENB,OUTPUT);
pinMode(A2,INPUT);
pinMode(ir,INPUT);
Serial.begin(9600);
}
void forward()
{digitalWrite(In1,HIGH);
digitalWrite(In2,LOW);
digitalWrite(In3,HIGH);
digitalWrite(In4,LOW);
analogWrite(ENA,SPED);
analogWrite(ENB,SPED);
}
void backward()
{digitalWrite(In1,LOW);
digitalWrite(In2,HIGH);
digitalWrite(In3,LOW);
digitalWrite(In4,HIGH);
analogWrite(ENA,SPED1);
analogWrite(ENB,SPED1);
}
void right()
{digitalWrite(In1,HIGH);
digitalWrite(In2,LOW);
digitalWrite(In3,LOW);
digitalWrite(In4,HIGH);
analogWrite(ENA,SPED1);
}
void left()
{
digitalWrite(In3,HIGH);
digitalWrite(In4,LOW);
digitalWrite(In1,LOW);
digitalWrite(In2,HIGH);
analogWrite(ENB,SPED1);
}
 
void Stop()
{digitalWrite(In1,LOW);
digitalWrite(In2,LOW);
digitalWrite(In3,LOW);
digitalWrite(In4,LOW);
}
void loop()
{
  if(Serial.available()>0)
{ 
  b=Serial.read();
}
s=digitalRead(4);
if (s==0)
  Stop();
else if(b=='f')
  forward();
else if(b=='B')
  backward();
else if(b=='l')
  left();
else if(b=='r')
  right();
else if(b=='s')
  Stop();
else if(b=='t')
digitalWrite(13,HIGH);
else if (b=='y')
digitalWrite(13,LOW); 
 
        
 

//Serial.println(s);

 
}  
