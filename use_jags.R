model = "model
{
    mu ~ dunif(5, 15)
    log_sigma ~ dunif(-10, 10)
    sigma <- exp(log_sigma)
#    log_nu ~ dunif(0, 5)
#    nu <- exp(log_nu)

    for(i in 1:length(mbh))
    {
        mbh_true[i] ~ dnorm(mu, 1/sigma^2)
        mbh[i] ~ dnorm(mbh_true[i], 1/mbh_err[i]^2)
    }
}
"

# A dataset
data = read.table("mbh.txt", header=F)
colnames(data) = c("mbh", "mbh_err")
rownames(data) = NULL
data = data[seq(1, 570, by=3), ]

# Variables to monitor
variable_names = c("mu", "sigma")# , "log_nu")

# How many proper steps?
steps = 100000

# Thinning?
thin = 10

# Import the rjags library
library("rjags")

# Create a JAGS model object
jm = jags.model(textConnection(model), data)

# Do some MCMC
results = coda.samples(jm, variable_names, steps, thin=thin)

# Extract chains as data frame
results = as.data.frame(results[[1]])
