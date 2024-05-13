#include "MyModel.h"
#include "DNest4/code/DNest4.h"
#include "Data.h"

MyModel::MyModel()
:ns(Data::instance.z.size())
{

}

void MyModel::from_prior(DNest4::RNG& rng)
{
    beta1 = -10.0 + 20.0*rng.rand();
    beta2 = -10.0 + 20.0*rng.rand();
    C = -10.0 + 20.0*rng.rand();
    n = -1.0 + 5.0*rng.rand();

    sigma = rng.rand();
    for(double& x: ns)
        x = rng.randn();
}

double MyModel::perturb(DNest4::RNG& rng)
{
    double logH = 0.0;
    int which = rng.rand_int(6);

    if(which == 0)
    {
        beta1 += 20.0*rng.randh();
        DNest4::wrap(beta1, -10.0, 10.0);
    }
    else if(which == 1)
    {
        beta2 += 20.0*rng.randh();
        DNest4::wrap(beta2, -10.0, 10.0);
    }
    else if(which == 2)
    {
        C += 20.0*rng.randh();
        DNest4::wrap(C, -10.0, 10.0);
    }
    else if(which == 3)
    {
        n += 5.0*rng.randh();
        DNest4::wrap(n, -1.0, 4.0);
    }
    else if(which == 4)
    {
        sigma += rng.randh();
        DNest4::wrap(sigma, 0.0, 1.0);
    }
    else
    {
        logH += DNest4::perturb_ns(ns, rng);
    }


    return logH;
}

double MyModel::log_likelihood() const
{
    double logL = 0.0;

    const Data& data = Data::instance;
    for(size_t i=0; i<data.z.size(); ++i)
    {
        // Prediction made by the regression surface
        double mu = C + beta1*data.lambda[i] + beta2*data.l_bol[i]
                        + n*log10(1.0 + data.z[i]);

        // Add intrinsic scatter
        // mu += sigma*ns[i];

        // Gaussian likelihood for simulated data with symmetric errorbars
//        double sigma = data.log10_tau_mid[i] - data.log10_tau_lower[i];
//        logL += -0.5*log(2*M_PI) - log(sigma)
//                    - 0.5*pow((data.log10_tau_mid[i] - mu)/sigma, 2);

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
    out << beta1 << " " << beta2 << " " << C << ' ' << n << ' ' << sigma;
}

std::string MyModel::description() const
{
    return std::string("beta1 beta2 C n sigma");
}

