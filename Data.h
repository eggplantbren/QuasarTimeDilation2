#ifndef Data_h
#define Data_h

#include <vector>

class Data
{
    private:
        std::vector<double> z;
        std::vector<double> log10_tau_lower;
        std::vector<double> log10_tau_mid;
        std::vector<double> log10_tau_upper;

    public:
        Data(const char* filename);

        static Data instance;
};

#endif
