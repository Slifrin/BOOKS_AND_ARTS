
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>


void check_1(){
    std::stringstream mydata;
    std::ifstream myfile;
    myfile.open("myfile_b.txt");
    if (myfile.is_open()){
        mydata << myfile.rdbuf();
        std::cout << mydata.str() << " " << mydata.str().length() << std::endl;
        std::string receivedData = mydata.str();

        for (int i = 0 ; i < receivedData.length();  i++)
        {
            std::cout << receivedData[i] << std::endl;
        }

        for (auto& c : receivedData)
        {
            std::cout << c << std::endl;
        }
    } else {
        std::cout << "Tarapaty\n";
    }

    myfile.close();
}


void check_2(){
    std::ofstream myfile("data.dat", std::ios::out | std::ios::binary);

    if (!myfile){
        std::cout << "Problems :(\n";
        return;
    }

    std::string mydata = "Hello again";
    myfile << mydata;

    myfile.close();
}


int main()
{
    std::cout << "Hello there\n";
    check_1();
    check_2();
    return 0;
}