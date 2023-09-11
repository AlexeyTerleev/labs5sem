//
// Created by alexey_t on 06/09/23.
//

#include "RandomDevice.h"


RandomDevice::RandomDevice(unsigned long n) : rand_seed(n), engine(n){ }

int RandomDevice::randInt(int min, int max){
    std::uniform_int_distribution<int> distribution(min, max);
    return distribution(engine);
}

char RandomDevice::randChar(const std::string& alphabet) {
    return alphabet.at(randInt(0,  int(alphabet.length()) - 1));
}

std::string RandomDevice::randString(const std::string& alphabet, int length) {
    std::string result;
    for (int i = 0; i < length; i++)
        result += randChar(alphabet);
    return result;
}