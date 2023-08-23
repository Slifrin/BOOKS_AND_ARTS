#include <iostream>
#include <string>

void say_hello(int n)
{
    for (int i{0}; i < n; ++i)
    {
        std::cout << "Hello there " << i << "\n";
    }
}

void say_hello(const std::string name, const std::string surname)
{
    std::cout << "Hello there " << name << " " << surname << "\n";
}

int main()
{
    say_hello(5);
    say_hello("Tom", "Johns");
    return 0;
}