#include "MyModel.h"
#include "DNest4/code/DNest4.h"

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

