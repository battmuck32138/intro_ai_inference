import inference as inf

dist = inf.DiscreteDistribution()
dist['a'] = 1
dist['b'] = 2
dist['c'] = 2
dist['d'] = 0

N = 100000.0
samples = [dist.sample() for _ in range(int(N))]
round(samples.count('a') * 1.0/N, 1)  # proportion of 'a'
round(samples.count('b') * 1.0/N, 1)
round(samples.count('c') * 1.0/N, 1)
round(samples.count('d') * 1.0/N, 1)

for key in dist.keys():
    print(dist[key])