#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(){
    ifstream fichier ("/etc/passwd");
    string tab[266], token[228];

    if(fichier){
        string ligne;
        int i=0, compt=0, comptligne=0;
        cout<<"affichage ligne par ligne"<<endl;
        while(getline(fichier, ligne)){
            tab[i]=ligne;
            i++;
            comptligne++;
        }

        string delim =":";
        size_t pos=0;

        for (i = 0; i < comptligne; i++)
        {
            while ((pos=tab[i].find(delim)) != string::npos)
            {
                token[compt] = tab[i].substr(0, pos);
                tab[i].erase(0, pos+delim.length());
                compt++;
            }
        }
        
       for (i = 0; i < size(token); i+=6)
       {
            cout<<"User-Namen : "<<token[i]<<"   User-Id (UID) : "<<token[i+2]<<endl;
       }
    }
    else
        cout<<"Impossible d'ouvrir le fichier"<<endl;

    return 0;
}
