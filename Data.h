#ifndef Data_h
#define Data_h

#include <vector>

class Data
{
    friend class MyModel;

    private:
        std::vector<double> z;
        std::vector<double> lambda;
        std::vector<double> l_bol;
        std::vector<double> log10_tau_lower;
        std::vector<double> log10_tau_mid;
        std::vector<double> log10_tau_upper;

        // Summaries of explanatory variables
        double mean_zz; // Where zz = log10(1+z)
        double mean_lambda;
        double mean_l_bol;

    public:
        Data(const char* filename);

        static Data instance;
};

#endif
