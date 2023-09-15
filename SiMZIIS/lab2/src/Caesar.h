#include "string"

class Caesar{
private:
    std::string alphabet;
    int key;

    Caesar(int key);
    Caesar(int key, std::string alphabet);

    std::string encode(std::string& password);
    std::string decode(std::string& encodedPassword);

    int getIndexOfAlphabet(char ch);

public:
    static std::string encode(int key, std::string password);
    static std::string decode(int key, std::string encodedPassword);    
};