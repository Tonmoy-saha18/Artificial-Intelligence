def init():
    data = [2, 1, 5, 0, 8, 4, 10, 0, 20, 10]
    return data


#here we have calculating the cost of each state
def calculate_cost(state):
    cost = 0
    for a in range(0, len(state)):
        for i in range(a + 1, len(state)):
            if state[a] > state[i]:
                cost += 1
    return cost


#here we have generating new state and checking whether we have got a good state or not
def state_generation(current_state, current_cost):
    local_best_cost = 1000000
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
            if local_cost < local_best_cost:
                local_best_cost = local_cost
                #deepcopy of local best
                local_best_state = []
                for l in local_current:
                    local_best_state.append(l)
                #print(local_best_state, local_best_cost, '----')

    #here we will check the function we have got it is best or not
    if current_cost > local_best_cost:
        return local_best_state, local_cost
    else:
        return current_state, None


#checking whether we have reached the goal or not
def goalCheck(state):
    if calculate_cost(state) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    state = init()
    while not goalCheck(state):
        state, cost = state_generation(state, calculate_cost(state))
        if cost is None:
            print(state)
            exit()
    print(state)
