#include <iostream>

using namespace std;

float iterujF(int mianownik)
{
    float dx = (float)1.0 / (float)mianownik;
    float x = 0.0;
    for (int i = 0; i < mianownik; i++)
    {
        x = x + dx;
    }
    return abs((float)1.0 - x);
}
double iterujD(int mianownik)
{
    double dx = (double)1.0 / (double)mianownik;
    double x = 0.0;
    for (int i = 0; i < mianownik; i++)
    {
        x = x + dx;
    }
    return abs((double)1.0 - x);
}
int main(int argc, char const *argv[])
{
    // double - 1        float - 2
    int ver = 1;
    if (ver == 1)
    {
        for (int i = 1; i <= 2048; i++)
        {
            cout << i << "\t" << iterujD(i) << endl;
        }
    }
    else if (ver == 2)
    {
        for (int i = 1; i <= 2048; i++)
        {
            cout << i << "\t" << iterujF(i) << endl;
        }
    }
    return 0;
}
