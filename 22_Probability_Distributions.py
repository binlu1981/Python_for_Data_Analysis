#%matplotlib inline
#http://hamelg.appspot.com/
#http://hamelg.blogspot.in/2015/10/introduction-to-r-index.html
#http://hamelg.blogspot.in/2015/10/python-for-data-analysis-part-1-setup.html
#http://hamelg.blogspot.ae/2015/11/python-for-data-analysis-part-22.html
#http://hamelg.blogspot.in/2015/12/python-for-data-analysis-index.html

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats



##### The Uniform Distribution ######
"""
The uniform distribution is a probability distribution where each value
within a certain range is equally likely to occur
and values outside of the range never occur.If we make a density plot of a
uniform distribution, it appears flat because no value is any more likely
(and hence has any more density) than another."""

uniform_data = stats.uniform.rvs(size = 10000, loc=0, scale=10)
print(uniform_data)
"""[ 5.30902053  3.26394294  7.88759876  4.98261842  1.37021361  6.22690554
  9.81614435  5.76378968  9.24930713  8.38242811]"""
#pd.DataFrame(uniform_data).plot(kind="density",figsize=(8,8),xlim=(-1,11))
#plt.show()
"""
*Note: the plot above is an approximation of the underlying distribution, since it is based on a sample of observations.
In the code above, we generated 100,000 data points from a uniform distribution spanning the range 0 to 10. In the density plot,
we see that the density of our uniform data is essentially level meaning any given value has the same probability of occurring.
The area under a probability density curve is always equal to 1.
"""
print(stats.uniform.cdf(x=2.4,loc=0,scale=12))
"""
0.2
-stats.distribution.cdf() is used to determine the probability that an observation drawn
from a distribution falls below a specified value (known as the cumulative distribution function.).
 In essence, cdf() gives you the area under the distribution's density curve to the left of a certain
 value on the x axis. For example, in the uniform distribution above, there is a 25% chance that
 an observation will be in the range 0 to 2.5 and a 75% chance it will fall in the range 2.5 to 10.
 """
print(stats.uniform.ppf(q=0.1,loc=0,scale=20))
"""
2.0
-stats.distribution.ppf() is the inverse of cdf(): it returns the x axis cutoff value (quantile) associated
with a given probability. For instance, if we want to know the cutoff value for which we have a 40% chance of
drawing an observation below that value, we can use ppf():
"""

for x in range(-1,12,3):
    print("Density at value " + str(x))
    print(stats.uniform.pdf(x,loc=0,scale=10))
"""
Density at value-1
0.0
Density at value2
0.1
Density at value5
0.1
Density at value8
0.1
Density at value11
0.0
"""


##### Generating Random Numbers and Setting The Seed #######
import random
print(random.randint(0,10))
print(random.choice([2,4,6,10]))
print(random.random())
print(random.uniform(0,9))
random.seed(3)
print([random.uniform(0,10) for x in range(4)])
random.seed(3)
print([random.uniform(0,10) for x in range(4)])
"""
4
2
0.16728176560754504
7.680986253187402
[2.3796462709189137, 5.442292252959518, 3.6995516654807927, 6.039200385961944]
[2.3796462709189137, 5.442292252959518, 3.6995516654807927, 6.039200385961944]
Notice that we generated the exact same numbers with both calls to random.uniform()
because we set the same seed before each call. If we had not set the seed,
we would have gotten different numbers. This reproducibility illustrates the fact
that these random numbers aren't truly random, but rather "pseudorandom".
* Note: The Python standard library "random" has a separate internal seed from
the numpy library. When using functions from numpy and libraries built on top
of numpy (pandas, scipy, scikit-learn) use np.random.seed() to set the seed.
"""

###### The Normal Distribution #######
"""
The normal or Gaussian distribution is a continuous probability distribution characterized by
a symmetric bell-shaped curve. A normal distribution is defined by its center (mean) and spread (standard deviation.)
The bulk of the observations generated from a normal distribution lie near the mean, which lies at the exact center of the distribution:
as a rule of thumb, about 68% of the data lies within 1 standard deviation of the mean, 95% lies within 2 standard deviations and 99.7% lies within 3 standard deviations.
The normal distribution is perhaps the most important distribution in all of statistics. It turns out that many real world phenomena, like IQ test scores and human heights,
roughly follow a normal distribution, so it is often used to model random variables. Many common statistical tests assume distributions are normal..
"""
prob_under_minus1 = stats.norm.cdf(x=-1,loc=0,scale=1)
prob_over_1 = 1-stats.norm.cdf(x=1,loc=0,scale=1)
between_prob = 1 -(prob_under_minus1+prob_over_1)
print(prob_under_minus1,prob_over_1,between_prob)
"""The output shows that roughly 16% of the data generated by a normal distribution with mean 0 and standard deviation 1 is below -1,
16% is above 1 and 68% lies between -1 and 1, which agrees with the 68, 95, 99.7 rule. Let's plot the normal distribution and inspect areas we calculated:
"""

plt.rcParams["figure.figsize"]=(8,8)
plt.fill_between(x=np.arange(-5,-1,0.01),y1=stats.norm.pdf(np.arange(-5,-1,0.01)),\
                 facecolor='red',alpha=0.35)
plt.fill_between(x=np.arange(1,5,0.01),y1=stats.norm.pdf(np.arange(1,5,0.01)),\
                 facecolor='red',alpha=0.35)
plt.fill_between(x=np.arange(-1,1,0.01),y1=stats.norm.pdf(np.arange(-1,1,0.01)),
                 facecolor='blue',alpha=0.35)
plt.text(x=-1.8, y=0.03, s= round(prob_under_minus1,3))
plt.text(x=-0.2, y=0.1, s= round(between_prob,3))
plt.text(x=1.4, y=0.03, s= round(prob_over_1,3))

print( stats.norm.ppf(q=0.025) ) # Find the quantile for the 2.5% cutoff
print( stats.norm.ppf(q=0.975) ) # Find the quantile for the 97.5% cutoff
"""
-1.95996398454
1.95996398454
The quantile output above confirms that roughly 5% of the data lies more than 2 standard deviations from the mean.
*Note: a mean of 0 and standard deviation of 1 are default values for the normal distribution.
"""


####### The Binomial Distribution ########
"""
The binomial distribution is a discrete probability distribution that models the outcomes of a given number of
random trails of some experiment or event. The binomial is defined by two parameters: the probability of success
in any given trial and the number of trials. The binomial distribution tells you how likely it is to achieve a given
number of successes in n trials of the experiment. For example, we could model flipping a fair coin 10 times with a
binomial distribution where the number of trials is set to 10 and the probability of success is set to 0.5.
In this case the distribution would tell us how likely it is to get zero heads, 1 head, 2 heads and so on.
"""
fair_coin_flips = stats.binom.rvs(n=10,  # Number of flips per trial
                                  p=0.5,  # Success probability
                                  size=10000)  # Number of trials

print(pd.crosstab(index="counts", columns= fair_coin_flips))
pd.DataFrame(fair_coin_flips).hist(range=(-0.5,10.5), bins=11)
plt.show()
"""
col_0   0   1    2     3     4     5     6     7    8   9   10
row_0
counts   7  91  450  1212  1998  2435  2099  1182  422  93  11
Note that since the binomial distribution is discrete, it only takes on integer values
so we can summarize binomial data with a frequency table and its distribution with a histogram.
The histogram shows us that a binomial distribution with a 50% probability of success is roughly symmetric,
with the most likely outcomes lying at the center. This is reminiscent of the normal distribution,
but if we alter the success probability, the distribution won't be symmetric:
"""

biased_coin_flips = stats.binom.rvs(n=10,  # Number of flips per trial
                                    p=0.8,  # Success probability
                                    size=10000)  # Number of trials
# Print table of counts
print(pd.crosstab(index="counts", columns=biased_coin_flips))
# Plot histogram
pd.DataFrame(biased_coin_flips).hist(range=(-0.5, 10.5), bins=11)
plt.show()

stats.binom.cdf(k=5,  # Probability of k = 5 successes or less
                n=10,  # With 10 flips
                p=0.8)  # And success probability 0.8
"""
0.032793497599999964
"""

1 - stats.binom.cdf(k=8,  # Probability of k = 9 successes or more
                    n=10,  # With 10 flips
                    p=0.8)  # And success probability 0.8

"""0.37580963840000003
For continuous probability density functions, you use pdf() to check the probability density at a given x value.
For discrete distributions like the binomial, use stats.distribution.pmf() (probability mass function) to check
the mass (proportion of observations) at given number of successes k:
"""

stats.binom.pmf(k=5,  # Probability of k = 5 successes
                n=10,  # With 10 flips
                p=0.5)  # And success probability 0.5

"""0.24609375000000025"""

stats.binom.pmf(k=8,  # Probability of k = 8 successes
                n=10,  # With 10 flips
                p=0.8)  # And success probability 0.8

"""0.30198988799999998"""

####### The Geometric and Exponential Distributions ########
"""
The geometric and exponential distributions model the time it takes for an event to occur.
The geometric distribution is discrete and models the number of trials it takes to achieve a
success in repeated experiments with a given probability of success. The exponential distribution
is a continuous analog of the geometric distribution and models the amount of time you have to wait
before an event occurs given a certain occurrence rate.
"""

flips_till_heads = stats.geom.rvs(size=10000, # Generate geometric data
                                  p=0.5)    # With success prob 0.5
# Print table of counts
print(pd.crosstab(index="counts",columns=flips_till_heads))
print(max(flips_till_heads))
#14
# Plot histogram
pd.DataFrame(flips_till_heads).hist(range=(-0.5,max(flips_till_heads)+0.5)
                                    , bins=max(flips_till_heads)+1)
plt.show()
"""
The distribution looks similar to what we'd expect: it is very likely to get a heads in 1 or 2 flips, while it is very unlikely for it to take more than 5 flips to get a heads. In the 10,000 trails we generated, the longest it took to get a heads was 13 flips.
Let's use cdf() to check the probability of needing 6 flips or more to get a success:
"""
first_five = stats.geom.cdf(k=5,  # Prob of success in first 5 flips
                            p=0.5)
print(1 - first_five)
#0.03125
#Use pmf() to check the probability of seeing a specific number of flips before a successes:
print(stats.geom.pmf(k=2,  # Prob of needing exactly 2 flips to get first success
               p=0.5))
#0.25

# Get the probability of waiting more than 1 time unit before a success
flips_till_heads_exp = stats.expon.rvs(loc=0, scale=1, size=1, random_state=None)
print(flips_till_heads_exp)
#[ 1.20833046]
prob_1 = stats.expon.cdf(x=1,
                         scale=1)  # Arrival rate
print(1 - prob_1)
0.36787944117144233
#*Note: The average arrival time for the exponential distribution is equal to 1/arrival_rate.
plt.fill_between(x=np.arange(0, 1, 0.01),
                 y1=stats.expon.pdf(np.arange(0, 1, 0.01)),
                 facecolor='blue',
                 alpha=0.35)

plt.fill_between(x=np.arange(1, 7, 0.01),
                 y1=stats.expon.pdf(np.arange(1, 7, 0.01)),
                 facecolor='red',
                 alpha=0.35)

plt.text(x=0.3, y=0.2, s=round(prob_1, 3))
plt.text(x=1.5, y=0.08, s=round(1 - prob_1, 3))
plt.show()
"""
Similar to the geometric distribution, the exponential starts high and has a long tail that trails off
to the right that contains rare cases where you have to wait much longer than average for an arrival.
"""

######### The Poisson Distribution #############
"""
The Poisson distribution models the probability of seeing a certain number of successes within a time interval,
where the time it takes for the next success is modeled by an exponential distribution.
The Poisson distribution can be used to model traffic, such as the number of arrivals a hospital can expect
in a hour's time or the number of emails you'd expect to receive in a week.
"""

random.seed(12)
arrival_rate_1 = stats.poisson.rvs(size=10000,  # Generate Poisson data
                                   mu=1 )       # Average arrival time 1

# Print table of counts
print( pd.crosstab(index="counts", columns= arrival_rate_1))
"""
col_0      0     1     2    3    4   5   6
row_0
counts  3644  3771  1793  622  128  32  10
"""
# Plot histogram
pd.DataFrame(arrival_rate_1).hist(range=(-0.5,max(arrival_rate_1)+0.5)
                                    , bins=max(arrival_rate_1)+1)
plt.show()
"""
The histogram shows that when arrivals are relatively infrequent,
it is rare to see more than a couple of arrivals in each time period.
When the arrival rate is high, it becomes increasingly rare to see a low number
of arrivals and the distribution starts to look more symmetric:
"""

random.seed(12)
arrival_rate_10 = stats.poisson.rvs(size=10000,  # Generate Poisson data
                                   mu=10 )       # Average arrival time 10
# Print table of counts
print( pd.crosstab(index="counts", columns= arrival_rate_10))
"""
col_0   1   2   3    4    5    6    7     8     9     10 ...   15   16   17  \
row_0                                                    ...
counts   8  22  69  171  375  615  930  1119  1233  1279 ...  364  223  130

col_0   18  19  20  21  22  23  24
row_0
counts  80  38  18   3   7   1   3
"""
# Plot histogram
pd.DataFrame(arrival_rate_10).hist(range=(-0.5,max(arrival_rate_10)+0.5)
                                    , bins=max(arrival_rate_10)+1)
plt.show()
"""
As with other discrete probability distributions, we can use cdf() to check the probability of achieving more or less
than a certain number of successes and pmf() to check the probability of obtaining a specific number of successes:
"""
stats.poisson.cdf(k=5,  # Check the probability of 5 arrivals or less
                  mu=10)  # With arrival rate 10
#0.067085962879031888
stats.poisson.pmf(k=10,  # Check the prob f exactly 10 arrivals
                  mu=10)  # With arrival rate 10
#0.12511003572113372
