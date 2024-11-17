class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timeline = []

        # Record the changes in passenger count at each start and end time
        for num_passengers, start, end in trips:
            timeline.append((start, num_passengers))  # Add passengers at start
            timeline.append((end, -num_passengers))  # Remove passengers at end

        # Sort the timeline by time
        timeline.sort()

        current_capacity = 0
        for _, change in timeline:
            current_capacity += change
            if current_capacity > capacity:
                return False

        return True
