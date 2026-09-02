import tracemalloc

tracemalloc.start()

x = [i for i in range(10)]
y = [x[:] for i in range(10)]

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")

print("[ Top 10 ]")
for stat in top_stats[:10]:
    print(stat)
