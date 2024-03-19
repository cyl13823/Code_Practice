class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count the frequency of each task
        task_counts = {}
        for task in tasks:
            if task in task_counts:
                task_counts[task] += 1
            else:
                task_counts[task] = 1
        
        # get the maximum frequency
        max_frequency = max(task_counts.values())
        
        # count the number of tasks with the maximum frequency
        num_max_frequency_tasks = list(task_counts.values()).count(max_frequency)
        
        # calculate the minimum number of intervals required to schedule all tasks
        min_intervals = (max_frequency - 1) * (n + 1) + num_max_frequency_tasks
        
        return max(min_intervals, len(tasks))
