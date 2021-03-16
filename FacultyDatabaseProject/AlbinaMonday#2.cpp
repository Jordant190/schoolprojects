#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

class Player {
    private:
        string name, year, team, position;
    public:
        Player(string name = "", string year = "", string team = "", string position =""){
            this->name = name;
            this->year = year;
            this->team = team;
            this->position = position;
        }
        void display(){
            cout << name << "\t" << year << "\t" << team <<"\t" << position <<endl;
        }
};

int main(){
    string name,year,team,position;
    vector <Player> myPlayers;

    fstream fin("/Users/aalbina/Desktop/FacultyUTF8.txt");

    if (!fin) {cout << "File not found!"; return -1;}

    while (!fin.eof()){
        fin >> name >> year >> team >> position;
        myPlayers.push_back(Player(name,year,team,position));
    }
    fin.close();

    for(int i=0;i<myPlayers.size();i++){
        myPlayers[i].display();
    }

    return 0;
}
