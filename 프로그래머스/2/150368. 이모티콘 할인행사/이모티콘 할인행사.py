import heapq

def solution(users, emoticons):
    answer = [0, 0]
    rates = [ 0 for _ in range(len(emoticons)) ]
    queue = []
    
    def calculate(rates):
        result = [0, 0, 0, 0]
        count = 0
        sumPrice = 0
        for u in users:
            price = 0
            for i in range(len(emoticons)):
                if rates[i] >= u[0]:
                    price += int(emoticons[i] * (100 - rates[i]) / 100)
                    if price >= u[1]:
                        result[2] += 1
                        price = 0
                        break
            result[3] += price
        
        if result[2] > 0:
            result[0] = result[2] * -1
        if result[3] > 0:
            result[1] = result[3] * -1
        return result
                
    
    def dfs(l):
        if l == len(emoticons):
            heapq.heappush(queue, calculate(rates))
            return
        
        for rate in range(10, 50, 10):
            rates[l] = rate
            dfs(l+1)
    dfs(0)
    
    answer[0] = queue[0][2]
    answer[1] = queue[0][3]
    
    return answer