#include <iostream>
#include <string>
#include "escape.h"

using namespace std;

int main(int argc, char **argv)
{
  string test = "<hello>world>\\";
  cout << test << "\n";
  escape(&test);
  cout << test << "\n";
}
