#include <string.h>
#include <stdio.h>
#include <stdlib.h>

void c_escape(char **a)
{
  unsigned int length=0;
  int i=0;
  const char delim[4] = {"\\<>"};
  char *temp1;
  char *s;
  s = *a;

  //get size of array passed in
  length = strlen(s);
  //iterate through to find # of escape characters
  temp1=s; //to preserve pointer
  for(i=0;s[i];((s[i]==delim[0])||(s[i]==delim[1])||(s[i]==delim[2])) ? i++ : *s++);
  s=temp1; //to reset pointer
  if(!i)
  {
    printf("No characters need escape.");
    return;
  }
  i = 0; //reset
  temp1 = (char*) malloc(length+i); //allocate space for escape characters
  strcpy(temp1,s);
  s = (char*) malloc(length+i);
  strcpy(s,temp1);
  for(;i<strlen(s);i++)
  {
    printf("i: %u\n", i);
    if((s[i] == delim[0])||(s[i]==delim[1])||(s[i]==delim[2]))
      {
        memmove(s+1+i,s+i,strlen(s)+1);
        printf("%s\n", s);
        s[i] = '\\';
        printf("%s\n", s);
        i+=1;
      }
  }
  printf("String done!\n");
  free(temp1);
  strcpy(*a,s);

}
