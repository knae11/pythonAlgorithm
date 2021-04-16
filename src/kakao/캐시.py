from collections import deque
def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        return 5*len(cities)
    queue = deque([], maxlen=cacheSize)
    for city in cities:
        city = city.lower()
        if city in queue:
            queue.remove(city)
            queue.append(city)
            answer += 1
        else:
            queue.append(city)
            answer += 5

    return answer


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))

'''
지난풀이

from collections import deque 
def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    if cacheSize == 0:
        return len(cities)*5
    for city in cities :
        city = city.lower()
        if city in cache :
            cache.remove(city)
            cache.append(city)
            answer += 1
        else: 
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.popleft()
                cache.append(city)
            answer += 5 
    return answer
'''