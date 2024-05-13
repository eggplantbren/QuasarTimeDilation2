#include "Data.h"
#include <fstream>
#include <iostream>

Data Data::instance("data.txt");

Data::Data(const char* filename)
{
    std::fstream fin(filename, std::ios::in);

    // Read in the data
    double a, b, c, d, e, f;
    while(fin >> a && fin >> b && fin >> c && fin >> d
            && fin >> e && fin >> f)
    {
        z.push_back(a);
        lambda.push_back(b);
        l_bol.push_back(c);
        log10_tau_lower.push_back(d);
        log10_tau_mid.push_back(e);
        log10_tau_upper.push_back(f);
    }

    fin.close();

    // Compute summaries
    mean_lambda = 0.0;
    mean_l_bol = 0.0;
    for(size_t i=0; i<z.size(); ++i)
    {
        mean_lambda += lambda[i];
        mean_l_bol += l_bol[i];
    }
    mean_lambda /= z.size();
    mean_l_bol /= z.size();

    std::cout << "# Loaded " << z.size() << " data points." << std::endl;
}

