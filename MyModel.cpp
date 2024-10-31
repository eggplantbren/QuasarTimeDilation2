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
    beta12 = -1.0 + 2.0*rng.rand();

    beta0 = -10.0 + 20.0*rng.rand();
    n = -1.0 + 5.0*rng.rand();

    sigma = rng.rand();
    for(double& x: ns)
        x = rng.randn();
}

double MyModel::perturb(DNest4::RNG& rng)
{
    double logH = 0.0;
    int which = rng.rand_int(7);

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
        beta0 += 20.0*rng.randh();
        DNest4::wrap(beta0, -10.0, 10.0);
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
    else if(which == 5)
    {
        logH += DNest4::perturb_ns(ns, rng);
    }
    else
    {
        beta12 += 2.0*rng.randh();
        DNest4::wrap(beta12, -1.0, 1.0);
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
        double mu = beta0 + beta1*(data.lambda[i] - data.mean_lambda)
                        + beta2*(data.l_bol[i] - data.mean_l_bol)
                        + beta12*(data.lambda[i] - data.mean_lambda)*(data.l_bol[i] - data.mean_l_bol)
                        + n*log10(1.0 + data.z[i]);

        // Add intrinsic scatter
        mu += sigma*ns[i/3];

        // Gaussian likelihood for simulated data with symmetric errorbars
//        double sigma = sqrt((data.log10_tau_mid[i] - data.log10_tau_lower[i])*
//                            (data.log10_tau_upper[i] - data.log10_tau_mid[i]));
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
    out << beta0 << ' ' << beta1 << ' ' << beta2 << ' ' << beta12 << ' ' << n << ' ' << sigma;
}

std::string MyModel::description() const
{
    return std::string("beta0 beta1 beta2 beta12 n sigma");
}

