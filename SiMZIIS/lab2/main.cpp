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
    std::string password, encodedPassword;
    int key;

    std::cout << "Enter password: "; std::cin >> password;
    std::cout << "Enter key: "; std::cin >> key;

    encodedPassword = Caesar::encode(key, password);

    std::cout << "Encoded password: " << encodedPassword << std::endl;
    std::cout << "Key: " << findKey(encodedPassword, password) << std::endl;
}
