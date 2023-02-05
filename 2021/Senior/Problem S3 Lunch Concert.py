class Person:  # Class for each person

	def __init__(self, pos, walk_time, hear_distance):  # Constructor
		self.pos = pos  # Position of person
		self.walk_time = walk_time  # Time it takes to walk 1 unit
		self.hear_distance = hear_distance  # Distance they can hear

	def get_walk_time(self, c):  # Get the time it takes for this person to walk to the concert
		dist = abs(self.pos - c)  # Distance from person to concert
		if dist <= self.hear_distance:  # If they can hear the concert,
			return 0  # They don't need to walk
		return (dist - self.hear_distance) * self.walk_time  # Otherwise, they walk the distance they can't hear


def get_cost(people, c):  # Get the total time it takes for all people to walk to the concert
	total_time = 0  # Total time
	for p in people:  # For each person,
		total_time += p.get_walk_time(c)  # Add their walk time to the total
	return total_time  # Return the total


def bisection(people, left, right):  # Binary search for the optimal concert location
	if left == right:  # If the left and right bounds are the same,
		return left  # Return that location
	mid = (left + right) // 2  # Get the middle of the bounds
	# If the cost of the concert at the middle is less than the cost of the concert at the middle + 1,
	if get_cost(people, mid) < get_cost(people, mid + 1):
		return bisection(people, left, mid)  # Search the left half
	return bisection(people, mid + 1, right)  # Otherwise, search the right half


N = int(input())  # Get the number of people
people = []  # List of people

for i in range(N):  # For each person,
	P, W, D = tuple(map(int, input().split()))  # Get their position, walk time, and hearing distance
	people.append(Person(P, W, D))  # Add them to the list

people.sort(key=lambda x: x.pos)  # Sort the list by position
print(get_cost(people, bisection(people, 0, people[-1].pos)))  # Print the cost of the optimal concert location

# Brute Force
# output = None  # Output
#
# for i in range(people[0].pos, people[-1].pos + 1):  # For each concert location,
# 	total_time = 0  # Total time
# 	for p in people:  # For each person,
# 		total_time += p.get_walk_time(i)  # Add their walk time to the total
# 	# If the output is None or the total time is less than the output,
# 	output = total_time if output is None else min(output, total_time)
#
# print(output)  # Print the output
