#ifndef TEACHER_H_INCLUDED
#define TEACHER_H_INCLUDED
using namespace std;

class Teacher {
    private:
        string Fname, Last, Education, Title, Department;
        vector <Teacher> myTeachers;
    public:
        Teacher(string Fname = "", string Last = "", string Education = "", string Title = "", string Department =""){
            this->Fname = Fname;
            this->Last = Last;
            this->Education = Education;
            this->Title = Title;// Job title
            this->Department = Department;
        }
        void print() {
            cout << Fname << Last << Education << Title << Department;
        }
        string getFname() {
            return Fname;
        }//f-name getter

        string getLast() {
            return Last;
        }//last_name getter

        string getEdu(){
            return Education;
        }
        string getTitle() {
            return Title;
        }//position getter

        string getDep() {
            return Department;
        }//Department getter

};



#endif // TEACHER_H_INCLUDED
