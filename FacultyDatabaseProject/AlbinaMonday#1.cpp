#include <iostream>
#include <string>
#include <vector>

using namespace std;

void tokenize(string const &str, const char delim, vector<std::string> &out);

int main()
{
                string s = "B.S. Mount Saint Mary's University / M.S. University of Maryland / Ph.D. Nova Southeastern University";
                const char delim = '/';

                vector<string> schools;
                tokenize(s, delim, schools);

                for (int i = 0;i < schools.size();i++) {
                                cout << schools[i] << '\n';
                }

                return 0;
}

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

