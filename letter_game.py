def getMaxDeletions(s):
    steps_del = 0
    num_of_U = 0
    num_of_D = 0
    num_of_L = 0
    num_of_R = 0
    for i in s:
        if i=="U":
            num_of_U += 1
        elif i=="D":
            num_of_D += 1
        elif i=="R":
            num_of_R += 1
        elif i=="L":
            num_of_L += 1
            
    if num_of_L == num_of_R:
        steps_del += (num_of_R*2)
    elif num_of_L > num_of_R:
        steps_del += (num_of_R*2)
    elif num_of_L < num_of_R:
        steps_del += (num_of_L*2)
            
    if num_of_U == num_of_D:
        steps_del += (num_of_D*2)
    elif num_of_U > num_of_D:
        steps_del += (num_of_D*2)
    elif num_of_U < num_of_D:
        steps_del += (num_of_U*2)
            
    return steps_del