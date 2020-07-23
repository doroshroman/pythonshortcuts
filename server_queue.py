# Simple server implementation
# Big idea -> use expovariate distribution to simulate server work
 
from random import expovariate, gauss
from statistics import mean, median, stdev

average_arrival_time = 5.6
average_service_time = 5.0
stdev_service_time = 0.5

num_waiting = 0
arrivals = []
starts = []
arrival = service_end = 0.0

for i in range(20000):
    if arrival <= service_end:
        num_waiting += 1
        arrival += expovariate(1.0 / average_arrival_time)
        arrivals.append(arrival)
    else:
        service_start = service_end if num_waiting else arrival
        service_time = gauss(average_service_time, stdev_service_time)
        service_end = service_start + service_time
        num_waiting -= 1
        starts.append(service_start)
        
waits = [start - arrival for start, arrival in zip(starts, arrivals)]
print(f"Mean wait: {mean(waits):.1f}, Stdev wait: {stdev(waits):.1f}")
print(f"Median wait: {median(waits):.1f}, Max wait: {max(waits):.1f}")
