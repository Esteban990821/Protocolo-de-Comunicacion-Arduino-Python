
void setup()
{ 
  Serial.begin(115200);
 
}
void loop() 
{ char  inicio='K';
  String informacion=String(analogRead(A0))+"C";
  
  String mensaje=inicio+informacion;
  char trama[mensaje.length()];
  mensaje.toCharArray(trama,mensaje.length());
  
  const byte data2= XORChecksum16(trama,sizeof(trama));
  String tramaFinal=mensaje+String(data2);
  Serial.print(tramaFinal+"\n");
  delay(1000);
  
   
}

uint16_t XORChecksum16(const byte *data, size_t dataLength)
{
  uint16_t value = 0;
  for (size_t i = 0; i < dataLength ; i++)
  {
    value ^= data[i];
  }
  return value;
}
