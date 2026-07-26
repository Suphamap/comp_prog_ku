from math import floor

def is_recover_end(time):
    if fitness >= time*2.5 and therapy >= time*2.5 and weight_training >= time*2.5:
        return False
    elif week >= floor(recover_time / 8):
        return False
    else:
        return True

def is_recover(time):
    course = fitness >= time*2.5 and therapy >= time*2.5 and weight_training >= time*2.5
    if course:
        return True
    else:
        return False

recover_time = int(input("Estimated time: "))
week = 0
therapy = 0
weight_training = 0
fitness = 0

while is_recover_end(recover_time):
    print(f"Week {week+1}")
    therapy += int(input("Physical Therapy: "))
    weight_training += int(input("Weight Training: "))
    fitness += int(input("Fitness: "))
    # print(therapy, weight_training, fitness)
    week += 1

if is_recover(recover_time):
    print("Buzzy recovered in time.")
else:
    print("Buzzy did not recover in time.")
