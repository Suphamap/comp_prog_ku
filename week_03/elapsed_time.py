def read_hour():
    return int(input("Enter hour: "))

def read_minute():
    return int(input("Enter minute: "))

def read_second():
    return int(input("Enter second: "))

def to_seconds(h, m, s):
    h_second = h*3600
    m_second = m*60
    return h_second + m_second + s

def read_time():
    print('>> ', end='')
    hour = read_hour()
    print('>> ', end='')
    minute = read_minute()
    print('>> ', end='')
    second = read_second()
    return to_seconds(hour, minute, second)

def elapsed_time(start, finish):
    total = finish - start
    hours = total // 3600
    minutes = (total % 3600) // 60
    seconds = total - (minutes*60) - (hours*3600)
    return f"{hours} hours {minutes} minutes {seconds} seconds."

print('Start time:')
start_time = read_time()
print('Finish time:')
finish_time = read_time()
print('Elapsed time is', elapsed_time(start_time, finish_time))