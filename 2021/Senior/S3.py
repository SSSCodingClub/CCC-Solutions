class Person:
    def __init__(self, pos, walk_time, hear_distance):
        self.pos = pos
        self.walk_time = walk_time
        self.hear_distance = hear_distance

    def get_walking_time(self, c): # formula for Speed * Time = Distance
        dist = abs(self.pos - c)
        if dist <= self.hear_distance:
            return 0
        return (dist - self.hear_distance) * self.walk_time 


N = int(input())

people = []
for i in range(N):
    P, W, D = list(map(int, input().split()))
    people.append(Person(P, W, D))

people.sort(key=lambda x: x.pos)

def get_cost(people, c):
    total_time = 0
    for p in people:
        total_time += p.get_walking_time(c)
    return total_time


def bisection(people, left, right):
    if left == right:
        return left
    mid = (left + right) // 2 
    if get_cost(people, mid) < get_cost(people, mid + 1):
        return bisection(people, left, mid)
    return bisection(people, mid + 1, right)

print(get_cost(people, bisection(people, 0, people[-1].pos)))