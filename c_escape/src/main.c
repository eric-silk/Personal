//#include <iostream>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include "c_escape.h"

int main()
{
  char *msg1;//*msg2;
  msg1 = malloc(strlen("<hello> world\\"));
  //msg2 = malloc(strlen("<<hello>\\ world\\"));
  strcpy(msg1,"<hello> world\\");
  //strcpy(msg2,"<<hello>\\ world\\");
  printf("%s\n", msg1);
  //printf("%s\n", msg2);
  c_escape(&msg1);
  //c_escape(&msg2);
  printf("%s\n", msg1);
  //printf("%s\n", msg2);
  return 0;
}
