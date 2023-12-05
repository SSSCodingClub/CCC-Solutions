N = int(input())

mountains = []

mountains = list(map(int, input().split()))

mins = []

for i in range(0, N + 1):
    mins.append(2147483647)

for mid in range(0, N):

        left = mid
        right = mid;
        size = 1;
        assy = 0;
        mins[size] = assy;

        while (left > 0 and right < N - 1):

            left -= 1
            right += 1
            size += 2

            assy += abs(mountains[left] - mountains[right]);

            mins[size] = min(assy, mins[size]);


mid1 = 0
mid2 = 1

while(mid2 < N):

        left = mid1
        right = mid2

        size = 2
        assy = abs(mountains[mid1] - mountains[mid2])
        mins[size] = min(assy, mins[size])

        while (left > 0 and right < N - 1):

            left -= 1
            right += 1
            size += 2

            assy += abs(mountains[left] - mountains[right])

            mins[size] = min(assy, mins[size])

        mid1 += 1
        mid2 += 1

for i in range(1, N+1):
        print(mins[i], end = ' ')