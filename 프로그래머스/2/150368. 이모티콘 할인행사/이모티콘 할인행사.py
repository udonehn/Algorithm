def get_emo_plus_revenue(discounted_emoticons, users):
    e_p = 0
    revenue = 0

    for u_rate, u_e_p_border in users:
        sum_buy = 0
        for rate, discounted_price in discounted_emoticons:
            if rate >= u_rate:
                sum_buy += discounted_price
        if sum_buy >= u_e_p_border:
            e_p += 1
        else:
            revenue += sum_buy                
    
    return [e_p, revenue]


def dfs(users, emoticons, discounted_emoticons, index, answer):
    if len(discounted_emoticons) == len(emoticons):
        return get_emo_plus_revenue(discounted_emoticons, users)
    for rate in (10, 20, 30, 40):
        discounted_price = emoticons[index] - emoticons[index] * (rate / 100)
        discounted_emoticons.append((rate, discounted_price))
        emo_plus_and_revenue = dfs(users, emoticons, discounted_emoticons, index + 1, answer)
        if emo_plus_and_revenue[0] > answer[0] or (emo_plus_and_revenue[0] == answer[0] and emo_plus_and_revenue[1] > answer[1]):
            answer = emo_plus_and_revenue
        discounted_emoticons.pop()
    return answer
    

def solution(users, emoticons):
    return dfs(users, emoticons, [], 0, [0, 0])