def get_parked_minute(in_time, out_time):
    in_hour, in_minute = map(int, in_time.split(":"))
    out_hour, out_minute = map(int, out_time.split(":"))
    
    if out_minute < in_minute:
        return (out_hour - 1 - in_hour) * 60 + (60 - (in_minute - out_minute))
    else:
        return (out_hour - in_hour) * 60 + (out_minute - in_minute)
    

def plus_parked_minutes(parked_minutes, number, parked_minute):
    # 한 번 이상 입차-출차 한 경우
    if number in parked_minutes:
        parked_minutes[number] += parked_minute
    else:
        parked_minutes[number] = parked_minute
    
    
def solution(fees, records):
    answer = []
    base_time, base_fee, additional_time, additional_fee = fees
    parked_cars = dict()
    parked_minutes = dict()
    car_fees = dict()
    
    for s in records:
        time, number, status = s.split()
        # 입차시
        if status == "IN":
            parked_cars[number] = time
        # 출차시
        else:
            parked_minute = get_parked_minute(parked_cars[number], time)
            plus_parked_minutes(parked_minutes, number, parked_minute)
            del parked_cars[number]
        
    for number, in_time in parked_cars.items():
        parked_minute = get_parked_minute(in_time, "23:59")
        plus_parked_minutes(parked_minutes, number, parked_minute)
    
    # 요금 계산
    for number, minutes in parked_minutes.items():
        if minutes <= base_time:
            car_fees[number] = base_fee
        else:
            extra_minutes = minutes - base_time
            if extra_minutes % additional_time == 0:
                car_fees[number] = base_fee + (extra_minutes // additional_time) * additional_fee
            else:
                car_fees[number] = base_fee + ((extra_minutes // additional_time) + 1) * additional_fee
    
    for number in sorted(car_fees.keys()):
        answer.append(car_fees[number])
        
    return answer