from datetime import datetime

def cal_time(v):
    val=v.split(",")
    time_str1 = val[0]
    time_str2 = val[1]
    time1 = datetime.strptime(time_str1, "%Y-%m-%d %H:%M:%S")
    time2 = datetime.strptime(time_str2, "%Y-%m-%d %H:%M:%S")
    time_diff = abs((time2 - time1).total_seconds() // 60)
    print(int(time_diff))
cal_time(input())