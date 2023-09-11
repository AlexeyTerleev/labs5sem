#include "iostream"
#include "src/RandomDevice.h"
#include "src/Timer.cpp"

bool brute(const std::string& text, const std::string& pass, const std::string& alphabet) {
    if (text.length() == pass.length()) {
        if (text == pass) {
            return true;
        }
        return false;
    }
    for (const char &ch: alphabet) {
        if (brute(text + ch, pass, alphabet)){
            break;
        }
    }
}


void test(RandomDevice& randomDevice) {
    std::string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    Timer<std::chrono::milliseconds> aTimer;
    std::chrono::high_resolution_clock::rep sumTime;
    for (int i = 1; i < 6; i++) {
        std::cout << "---- Length: " << i << " ----\n";
        sumTime = 0;
        for (int j = 0; j < 5; j++) {
            std::string randString = randomDevice.randString(alphabet, i);
            std::cout << "\tString: " << randString << "\n";
            aTimer.start();
            brute("", randString, alphabet);
            aTimer.stop();
            std::cout <<"\tTime: " << aTimer.get_time() << "ms \n\n";
            sumTime += aTimer.get_time();
        }
        std::cout <<"\tAverage time: " << sumTime / 5 << "ms \n\n";
    }
}


int main(){
    unsigned long seed = time(nullptr);
    RandomDevice my_rand(seed);
    test(my_rand);
}