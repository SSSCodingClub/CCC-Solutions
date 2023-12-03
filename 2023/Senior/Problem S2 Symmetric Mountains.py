# Too slow for 15/15. Gets 5/15

from functools import lru_cache
N = int(input())
heights = tuple(map(int, input().split()))

@lru_cache(maxsize=None)
def find_asymmetric_value(l, r, h=heights):
	output = 0
	for i in range(int((r - l) / 2) + 1):
		output += abs(h[l + i] - h[r - i])
	return output


crops = [[] for i in range(len(heights) + 1)]
for h in range(len(heights)):
	l, r = h, h
	for i in range(1, 1+ len(heights)):
		# print(r-l + 1, heights[l:r+1])
		if h + i < len(heights):
			r += 1
		crops[r - l + 1].append(find_asymmetric_value(l, r))
		if h - i >= 0:
			l -= 1
		crops[r - l + 1].append(find_asymmetric_value(l, r))
	# print()
for i in crops[1:]:
	print(min(i) if i else 0, end=' ')
