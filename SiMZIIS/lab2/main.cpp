#include "iostream"
#include "src/Caesar.h"

int findKey(std::string encodedPassword, std::string password) {
    std::string attempPassword;
    for (int i = 1; encodedPassword != attempPassword; i++){
        attempPassword = Caesar::decode(i, encodedPassword);
        if (password == attempPassword)
            return i;
    }
    throw std::invalid_argument("Key can't be found");  
}


int main(){
    std::string password = "testPass";
    std::string encodedPassword = "testPasd";
    findKey(encodedPassword, password);
}