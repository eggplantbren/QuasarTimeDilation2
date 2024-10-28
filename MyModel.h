#ifndef DNest4_Template_MyModel
#define DNest4_Template_MyModel

#include "DNest4/code/DNest4.h"
#include <ostream>

class MyModel
{
    private:
        static constexpr double mu_m_bh_true = 8.92;
        static constexpr double sigma_m_bh_true = 0.40;

        double beta1, beta2, beta12, beta3, beta13, beta23;
        double beta0;
        double n;

        // Standard deviation of intrinsic scatter
        double sigma;
        std::vector<double> ns; // Intrinsic scatter per-object parameters

        std::vector<double> m_bh_true;

    public:
        // Constructor only gives size of params
        MyModel();

        // Generate the point from the prior
        void from_prior(DNest4::RNG& rng);

        // Metropolis-Hastings proposals
        double perturb(DNest4::RNG& rng);

        // Likelihood function
        double log_likelihood() const;

        // Print to stream
        void print(std::ostream& out) const;

        // Return string with column information
        std::string description() const;
};

#endif

