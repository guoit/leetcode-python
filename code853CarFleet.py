"""
853 Car Fleet

N cars are going to the same destination along a one lane road.  The destination is target miles away.

Each car i has a constant speed speed[i] (in miles per hour), and initial position position[i] miles towards the target along the road.

A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed.

The distance between these two cars is ignored - they are assumed to have the same position.

A car fleet is some non-empty set of cars driving at the same position and same speed.  Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.


How many car fleets will arrive at the destination?

 

Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 and 8 become a fleet, meeting each other at 12.
The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
The cars starting at 5 and 3 become a fleet, meeting each other at 6.
Note that no other cars meet these fleets before the destination, so the answer is 3.

Note:

0 <= N <= 10 ^ 4
0 < target <= 10 ^ 6
0 < speed[i] <= 10 ^ 6
0 <= position[i] < target
All initial positions are different.
"""
class Solution:
    # my own solution
    # sort the tuple (position, speed) first
    # for each car in the end (with closet position to target), pop the car out, and calculate the time t it requires to arrive at target
    # then calculate each car's position with time t, if larger than target, pop it out, these popped out cars will form a fleet
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars = sorted((position[i], speed[i]) for i in range(len(position)))
        res = 0
        while cars:
            res += 1
            p, s = cars.pop()
            t = (target - p)/s

            while cars and (cars[-1][0] + cars[-1][1]*t + 1e-6) > target:   # add 1e-6 for float comparison
                cars.pop()

        return res

target, position, speed = 12, [10,8,0,5,3], [2,4,1,1,3]
print(Solution().carFleet(target, position, speed))