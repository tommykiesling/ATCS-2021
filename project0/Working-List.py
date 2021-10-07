jobs = ["Gamer", "Trucker", "Football Player", "Mall Cop"]
print(jobs.index('Trucker'))
print('gamer' in jobs)
jobs.append("Streamer")
jobs.insert(0, "Welder")
for j in jobs:
    print(j)