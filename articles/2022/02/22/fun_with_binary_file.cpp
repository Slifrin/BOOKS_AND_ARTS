#include <fstream>
#include <iostream>

int main(){
    {
        std::ofstream out_f ("data.bin", std::ios::out | std::ios::binary);
        out_f << 4 << '\n';
        int n = 5;
        out_f.write(reinterpret_cast<char*>(&n), sizeof n);
    }
    return 0;
}