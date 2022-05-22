from sys import maxsize

jobs = list(map(int, input().split(", ")))
job_wanted_index = int(input())
jobs_done_indexes = []
total_cycles = 0

while job_wanted_index not in jobs_done_indexes:
    curr_job = min(jobs)

    for index, job in enumerate(jobs):
        if job == curr_job and index not in jobs_done_indexes:
            total_cycles += curr_job
            jobs_done_indexes.append(index)
            jobs[index] = maxsize
            break

print(total_cycles)
