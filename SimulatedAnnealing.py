import math
import random


def init():
    data = [2, 1, 5, 0, 8]
    return data


#here we have calculating the cost of each state
def calculate_cost(state):
    cost = 0
    for a in range(0, len(state)):
        for i in range(a + 1, len(state)):
            if state[a] > state[i]:
                cost += 1
    return cost


#here we will check whether we will move or not
def move_or_not(difference):
    probability = math.exp(difference)
    # print(probability)
    number = random.random()
    # print(number)
    if number <= probability:
        return True
    else:
        return False


#here we have generating new state and checking whether we have got a good state or not
def state_generation(current_state, current_cost):
    #print(current_state, current_cost)
    for a in range(0, len(current_state)):
        for i in range(a + 1, len(current_state)):
            #deepcopy of a list
            local_current = []
            for l in current_state:
                local_current.append(l)
            #swapping the local_current to generate a state
            temp = local_current[a]
            local_current[a] = local_current[i]
            local_current[i] = temp
            local_cost = calculate_cost(local_current)
            #print(local_current, local_cost)
            if local_cost < current_cost:
                return local_current, local_cost
            elif local_cost > current_cost:
                del_e = current_cost - local_cost
                if move_or_not(del_e):
                    return local_current, local_cost
            else:
                if move_or_not(-1):
                    return local_current, local_cost


#checking whether we have reached the goal or not
def goalCheck(state):
    if calculate_cost(state) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    state = init()
    # print(move_or_not(-2))
    while not goalCheck(state):
        state, cost = state_generation(state, calculate_cost(state))
        # print(state, cost)
    print(state)
