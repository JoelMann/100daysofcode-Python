#small not useful experiment for using named tuples mainly. I may expand this to do actual analysis, vut for now, it was an experiment

from collections import namedtuple, Counter
import random

help_case = namedtuple("HC", "tech client rating")

techs = ["Nick", "Matt", "Pat", "Jose"]
customers = ["Sally", "Mike", "Ninjas", "Bobbert", "Optimus Prime"]

data = []


for i in range(0,100):
    data.append(help_case(random.choice(techs), random.choice(customers), random.randint(0,10)))

cnt = Counter(data)

print(cnt.most_common(5))
