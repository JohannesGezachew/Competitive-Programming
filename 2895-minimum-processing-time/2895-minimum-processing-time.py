class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        def minimum_processing_time(processorTime, tasks):
            processorTime.sort()
            tasks.sort(reverse=True)
            
            num_processors = len(processorTime)
            finish_times = [0] * num_processors
            

            for i in range(num_processors):
                max_time = 0
                for j in range(4):
                    task_index = i * 4 + j
                    task_time = tasks[task_index]
                    processor_avail_time = processorTime[i]
                    max_time = max(max_time, processor_avail_time + task_time)
                finish_times[i] = max_time
            
            return max(finish_times)
        
        return minimum_processing_time(processorTime, tasks)