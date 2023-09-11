//
// Created by alexey_t on 06/09/23.
//

#include "random"

#ifndef LAB1_RANDOMDEVICE_H
#define LAB1_RANDOMDEVICE_H


class RandomDevice{
private:
    unsigned long rand_seed;
    std::default_random_engine engine;
public:
    explicit RandomDevice(unsigned long n);
    int randInt(int, int);
    char randChar(const std::string&);
    std::string randString(const std::string&, int);
};


#endif //LAB1_RANDOMDEVICE_H
