#include "MyModel.h"
#include "DNest4/code/DNest4.h"
#include "Data.h"

MyModel::MyModel()
{

}

void MyModel::from_prior(DNest4::RNG& rng)
{
    C = -10.0 + 20.0*rng.rand();
    n = -1.0 + 5.0*rng.rand();
}

double MyModel::perturb(DNest4::RNG& rng)
{
    double logH = 0.0;
    int which = rng.rand_int(2);
    if(which == 0)
    {
        C += 20.0*rng.randh();
        DNest4::wrap(C, -10.0, 10.0);
    }
    else
    {
        n += 5.0*rng.randh();
        DNest4::wrap(n, -1.0, 4.0);
    }


    return logH;
}

double MyModel::log_likelihood() const
{
    double logL = 0.0;

    const Data& data = Data::instance;
    for(size_t i=0; i<data.z.size(); ++i)
    {
        // No intrinsic scatter yet
        double mu = C + n*log10(1.0 + data.z[i]);

        double beta_l = (data.log10_tau_mid[i] - data.log10_tau_lower[i])/1.1394;
        double beta_r = (data.log10_tau_upper[i] - data.log10_tau_mid[i])/1.1394;
        if(mu < data.log10_tau_mid[i])
            logL += -log(2.0*beta_l) + (mu - data.log10_tau_mid[i])/beta_l;
        else
            logL += -log(2.0*beta_r) - (mu - data.log10_tau_mid[i])/beta_r;
    }

    return logL;
}

void MyModel::print(std::ostream& out) const
{
    out << C << ' ' << n;
}

std::string MyModel::description() const
{
    return std::string("C n");
}

