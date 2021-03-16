// Jordan Trombly and Connor Page
// Faculty Database

# include <iostream>
# include <vector>
# include <fstream>
# include <string>
# include "teacher.h"
# include <algorithm>


using namespace std;
void tokenize(string const &str, const char delim, vector<string> &out);
void searchDep(vector <Teacher> myTeachers, string dep);
void searchLast(vector <Teacher> myTeachers, string lname);
void display(vector <Teacher> myTeachers);

int main(){
    //Teacher T;
    string Fname,Last,Education,Title,Department;
    vector <string> Dep;
    vector <string> Las;// string with last names
    vector <Teacher> myTeachers;
    string s, x;
    string dep;// department of search
    string lname;// last name of search

    fstream fin("./FacultyFinal.txt");

    if (!fin) {cout << "File not found!"; return -1;}

    vector <string> line;
    int counter = 0;
    while (!fin.eof()){
        if (counter == 5) {
            counter = 0;
            //cout << line[0] << endl << line[1] << endl << line[2] << endl << line[3] << endl << line[4] << endl;
            //Teacher T(line[0], line[1], line[2], line[3], line[4]);
            myTeachers.push_back(Teacher(line[0], line[1], line[2], line[3], line[4]));
            line.clear();
            getline(fin, x);

        }
        else {
            getline(fin, s);
            line.push_back(s);
            counter++;
        }
    }
    fin.close();

    int option = 1;
    do {
        cout << "\n\n******************\n*FACULTY DATABASE*\n******************\n\n-------MENU-------\n1. About \n2. Authors \n3. How to use \n4. Search by department \n5. Search by last name \n6. Print all \n7. Quit\n------------------";
        cout << "\n\nenter an option >> ";
        cin >> option;
        cout << "\nyou chose: " << option << endl;
        switch (option) {
        case 1: cout << "\nAbout...\n\nThis program grants a user the ability to search a database\nof all the 154 full time faculty at Saint Anselm College";
                cout << "\nduring the 2017-18 school year. Then, the user can write\nthe name, department, position, and edjucational background\nof that person to a file.";
                break;
        case 2: cout << "\nAuthors...\n\nWritten circa 2019 by Connor Page & Jordan Trombly";
                break;
        case 3: cout << "\n\nHow to use...\n\nFirst, choose to search by department or by last name.\n\nThen, enter the corresponding search criteria, ";
                cout << "the program will return the information on that person.\n\nFinally, choose to write the info to a file or make another search.\n\n";
                break;
        case 4: cout << "\nSearch for department to list teachers in it\n";
                for (int i = 0; i < myTeachers.size(); i++) {
                    cout << myTeachers[i].getDep() << endl;
                }
                cout << "\nEnter a department name >> ";
                cin.ignore();
                getline(cin, dep);
                searchDep(myTeachers, dep);
                break;
        case 5: cout << "\nSearch for Last name\n";
                for (int i = 0; i < myTeachers.size(); i++) {
                    cout << myTeachers[i].getLast() << endl;
                }
                cout << "\nEnter a last name >> ";
                cin.ignore();
                getline(cin, lname);
                searchLast(myTeachers, lname);
                break;
        case 6: cout << "\nFull Time Faculty at\nSaint Anselm College\n     2017-18:\n";
                cout << "******************\n-full name\n-last name\n-education\n-position\n-department\n******************\n\n\n";
                display(myTeachers);
                break;
        case 7: cout << "\nQuitting...";
                break;
        default: cout << "\nWrong input\n";
                break;
        }//switch
    }while (option != 7);

    cout << "\n\n******************\n*****GOODBYE!*****\n******************\n\n";

return 0;
}//main

void display(vector <Teacher> myTeachers) {
    int num = myTeachers.size();
    for (int i = 0; i < num; i++) {
        cout << myTeachers[i].getFname() << endl << myTeachers[i].getLast() << endl << myTeachers[i].getEdu()
             << endl << myTeachers[i].getTitle() << endl << myTeachers[i].getDep() << endl;
    }
}

void searchDep(vector <Teacher> myTeachers, string dep) {
    int num = myTeachers.size();
    for (int i = 0; i < num; i++) {
        //cout << myTeachers[i].getDep() << endl;
        if (myTeachers[i].getDep() == dep) {
            cout << myTeachers[i].getLast() << endl;
        }
        else {
            cout << "Not Found";
            break;
        }
    }

}// searches for teachers in specific department then prints

void searchLast(vector <Teacher> myTeachers, string lname) {
    char wfile;// if user wants to write teacher info to file
    int num = myTeachers.size();
    for (int i = 0; i < num; i++) {
        //cout << myTeachers[i].getDep() << endl;
        if (myTeachers[i].getLast() == lname) {
            cout << myTeachers[i].getFname() << endl << myTeachers[i].getLast() << endl << myTeachers[i].getEdu()
                 << endl << myTeachers[i].getTitle() << endl << myTeachers[i].getDep() << endl;
        }
        else {
            cout << "Not Found";
            break;
        }
    }
    cout << "\nDo you want to write " << lname << "'s info to a file (y or n)? ";
    cin >> wfile;
    if (wfile == 'Y' || wfile == 'y') {
        ofstream ff ("/Users/jordantrombly/Desktop/FacultyDatabaseProject/Teacherinfo.txt");
        for (int i = 0; i < num; i++) {
            if (myTeachers[i].getLast() == lname) {
            ff << myTeachers[i].getFname() << endl << myTeachers[i].getLast() << endl << myTeachers[i].getEdu()
                 << endl << myTeachers[i].getTitle() << endl << myTeachers[i].getDep() << endl;
            }
        }
    }

}// searches faculty by last name

void tokenize(string const &str, const char delim, vector<string> &out)
{
                size_t start;
                size_t end = 0;

                while ((start = str.find_first_not_of(delim, end)) != std::string::npos)
                {
                                end = str.find(delim, start);
                                out.push_back(str.substr(start, end - start));
                }
}
