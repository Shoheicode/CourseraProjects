# python3

from collections import namedtuple
import heapq

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers,m, jobs):
    # TODO: replace this code with a faster algorithm.
    heap = [(0, i) for i in range(n_workers)]
    heapq.heapify(heap)

    result = []
    
    for i in range(m):
        # Extract the thread with the smallest free time (and smallest index if tie)
        free_time, thread_index = heapq.heappop(heap)
        
        # The job starts at the current free time of this thread
        result.append((thread_index, free_time))
        
        # Update the free time of this thread and push it back into the heap
        heapq.heappush(heap, (free_time + jobs[i], thread_index))
    
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers,n_jobs, jobs)

    for thread_index, start_time in assigned_jobs:
        print(thread_index, start_time)


if __name__ == "__main__":
    main()
