#include "Data.h"
#include <fstream>
#include <iostream>

Data Data::instance("data.txt");

Data::Data(const char* filename)
{
    std::fstream fin(filename, std::ios::in);

    double a, b, c, d;
    while(fin >> a && fin >> b && fin >> c && fin >> d)
    {
        z.push_back(a);
        log10_tau_lower.push_back(b);
        log10_tau_mid.push_back(c);
        log10_tau_upper.push_back(d);
    }

    fin.close();

    std::cout << "# Loaded " << z.size() << " data points." << std::endl;
}

