#include <iostream>
#include <string>

using namespace std;

void escape (string* s)
{
  size_t index = 0;
  for(;;)
  {
    index = s->find("\\", index);
    if(index == string::npos) break; //exit if at end of string
    s->insert(index,"\\"); //replace w/ escaped character
    index +=2; // 2 to skip inserted and previously existing character
    //cout << "Instance of ''\\' escaped." << '\n'; //used for debugging
  }
  index = 0; //reset index
  for(;;)
  {
    index = s->find("<", index);
    if(index == string::npos) break; //exit if at end of string
    s->insert(index,"\\"); //replace w/ escaped character
    index +=2;
    //cout << "Instance of '<' escaped." << '\n'; //used for debugging
  }
  index = 0; //reset index
  for(;;)
  {
    index = s->find(">", index);
    if(index == string::npos) break; //exit if at end of string
    s->insert(index,"\\"); //replace w/ escaped character
    index +=2;
    //cout << "Instance of '>' escaped." << '\n'; //used for debugging
  }
  return;
}
