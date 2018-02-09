#include <iostream>
#include <fstream>

using namespace std;

int main(void)
{
    fstream myfile;
    string line;
    myfile.open("practice.txt");
    myfile << "Write some shit, yo." << endl;
    myfile << "Write some more shit." << endl;
    myfile << "EVEN MOAR." << endl;
    for(int i = 0; i <= 100; i++)
    {
	myfile << i << endl;
    }
    myfile.close();
    
    myfile.open("practice.txt");
    if(myfile.is_open())
    {
	while(getline(myfile,line))
	{
	    cout << line << endl;
	}
    }
    myfile.close();
    return 0;
}

