#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(){
    ifstream file ("/etc/passwd");
    string array[266], token[228];

    if(file){
        string line;
        int i=0, counter=0, linecounter=0;
        while(getline(file, line)){
            array[i]=line;
            i++;
            linecounter++;
        }

        string delim =":";
        size_t pos=0;

        for (i = 0; i < linecounter; i++)
        {
            while ((pos=array[i].find(delim)) != string::npos)
            {
                token[counter] = array[i].substr(0, pos);
                array[i].erase(0, pos+delim.length());
                counter++;
            }
        }
        
       for (i = 0; i < linecounter*6; i+=6)
       {
            cout<<"User-Namen : "<<token[i]<<"   User-Id (UID) : "<<token[i+2]<<endl;
       }
    }
    else
        cout<<"unable to open the file"<<endl;

    return 0;
}
