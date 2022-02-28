#include <iostream>
#include <string>
#include<algorithm>
using namespace std;


class StateContext
{


};

class State
{
    void write_name(StateContext context, string name);
};


void fn (char & c)
{
    c = :: tolower(c);
};

class Lowercase: public State
{
public:
    void write_name(StateContext context, string name)
    {
        name.UpperCase();
        std::for_each(name.begin(), name.end(), [](int)
        {
            
        });
            cout << name;
    }
};


class UpperCase: public State
{
public:
    void write_name(StateContext context, string name)
    {
        for_each(name.begin(), name.end(), [](char & c)
        {

        });
    };

};

int main()
{
    cout << "Done!";
}