#include "Caesar.h"


std::string Caesar::encode(int key, std::string password) {
    return Caesar(key).encode(password);
}

std::string Caesar::decode(int key, std::string encodedPassword) {
    return Caesar(key).decode(encodedPassword);
}

Caesar::Caesar(int key): alphabet("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"), key(key) { };

Caesar::Caesar(int key, std::string alphabet) : key(key), alphabet(alphabet) { }


std::string Caesar::encode(std::string& password) {
    std::string encodedPassword = "";
    for (char ch : password) {
        int index = getIndexOfAlphabet(ch);
        encodedPassword += alphabet.at((index + key) % alphabet.size());
    }
    return encodedPassword;
}

std::string Caesar::decode(std::string& encodedPassword) {
    std::string password = "";
    for (char ch : encodedPassword) {
        int index = getIndexOfAlphabet(ch);
        password += alphabet.at((index - (key % alphabet.size()) + alphabet.size()) % alphabet.size());
    }
    return password;
}


int Caesar::getIndexOfAlphabet(char ch) {
    for (int i = 0; i < alphabet.size(); i++) {
        if (alphabet.at(i) == ch)
            return i;
    }
    throw "Element not found";
};
