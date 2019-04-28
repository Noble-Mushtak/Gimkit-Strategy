from math import ceil
import sys

initial_money = 1
goal = -1
comprehensive = False
max_num_steps = -1
if len(sys.argv) > 1:
    initial_money = int(sys.argv[1])
    if len(sys.argv) > 2:
        goal = int(sys.argv[2])
        if len(sys.argv) > 3:
            comprehensive = bool(int(sys.argv[3]))
            if len(sys.argv) > 4:
                max_num_steps = int(sys.argv[4])

# Tuple: (Money, Money per Q, Streak, Multiplier, Discount, Mini Bonus, Mega Bonus)

moneys = [1, 5, 50, 100, 500, 2000, 5000, 10000, 250000, 1000000]
money_costs = [
    [0, 10, 100, 1000, 10000, 75000, 300000, 1000000, 10000000, 100000000],
    [0, 8, 75, 750, 7500, 56250, 225000, 750000, 7500000, 75000000]
]
streaks = [2, 20, 100, 200, 1000, 4000, 10000, 50000, 1000000, 5000000]
streak_costs = [
    [0, 15, 150, 1500, 15000, 115000, 450000, 1500000, 15000000, 200000000],
    [0, 12, 113, 1125, 11250, 86250, 337500, 1125000, 11250000, 150000000]
]
multipliers = [1, 1.5, 2, 3, 5, 8, 12, 18, 30, 100]
multiplier_costs = [
    [0, 50, 300, 2000, 12000, 85000, 700000, 6500000, 65000000, 1000000000],
    [0, 38, 225, 1500, 9000, 63750, 525000, 4875000, 48750000, 750000000]
]

benefit_arrays = [0, moneys, streaks, multipliers]
cost_arrays = [0, money_costs, streak_costs, multiplier_costs]

powerup_base_costs = [0, 0, 0, 0, 350, 20, 50]
powerup_percentage_costs = [0, 0, 0, 0, .19, .03, .06]

def calc_powerup_cost(index, amount):
    return 5*int(ceil((powerup_percentage_costs[index]*amount+powerup_base_costs[index])/5))

def calc_optimal_benefit(arr, cur_benefit, amount):
    while cur_benefit+1 < len(arr) and amount >= arr[cur_benefit+1]:
        cur_benefit += 1
    return cur_benefit

def calc_gain_per_q(tpl):
    return int(ceil((moneys[tpl[1]]+streaks[tpl[2]])*multipliers[tpl[3]]))
            
cur_queue = [(initial_money+1, 0, 0, 0, 0, 0, 0)]
prev_cur_queue = []
next_queue = []
prev_next_queue = []
prev = {}
final_state = None

debug_i = -1
i = 0
while True:
    for state in cur_queue:
        for benefit_index in range(1, 4):
            optimal_benefit = calc_optimal_benefit(cost_arrays[benefit_index][state[4]], state[benefit_index], state[0])
            for possible_benefit in range(state[benefit_index]+1 if comprehensive else max(state[benefit_index]+1, optimal_benefit), optimal_benefit+1):
                next_queue.append((state[0]-cost_arrays[benefit_index][state[4]][possible_benefit],)+state[1:benefit_index]+(possible_benefit,)+state[(benefit_index+1):])
                prev_next_queue.append(state)
                if i == debug_i: print("K", next_queue[-1], prev_next_queue[-1])
            
        for powerup_index in range(4, 7):
            powerup_cost = calc_powerup_cost(powerup_index, state[0])
            if state[powerup_index] == 0 and powerup_cost < state[0]:
                next_queue.append((state[0]-powerup_cost,)+state[1:powerup_index]+(1,)+state[(powerup_index+1):])
                prev_next_queue.append(state)
                if i == debug_i: print("K", next_queue[-1], prev_next_queue[-1])
            
        next_queue.append((state[0]+calc_gain_per_q(state),)+state[1:])
        prev_next_queue.append(state)
        if i == debug_i: print("K", next_queue[-1], prev_next_queue[-1])
        
        if state[5] == 1:
            next_queue.append((state[0]+2*calc_gain_per_q(state),)+state[1:5]+(-1,state[6]))
            prev_next_queue.append(state)
            if i == debug_i: print("K", next_queue[-1], prev_next_queue[-1])
        
        if state[6] == 1:
            next_queue.append((state[0]+5*calc_gain_per_q(state),)+state[1:6]+(-1,))
            prev_next_queue.append(state)
            if i == debug_i: print("K", next_queue[-1], prev_next_queue[-1])
        
        if state[5] == 1 and state[6] == 1:
            next_queue.append((state[0]+10*calc_gain_per_q(state),)+state[1:5]+(-1,-1))
            prev_next_queue.append(state)
            if i == debug_i: print("K", next_queue[-1], prev_next_queue[-1])
    
    sorted_lsts = sorted(zip(next_queue, prev_next_queue))
    next_queue = [x for x,_ in sorted_lsts]
    prev_next_queue = [x for _,x in sorted_lsts]
    cur_queue = []
    prev_cur_queue = []
    for j, state in enumerate(next_queue):
        indexes_to_be_removed = []
        for k, state2 in enumerate(cur_queue):
            if state2[1] <= state[1] and state2[2] <= state[2] and state2[3] <= state[3] and state2[4] <= state[4] and state2[5] <= state[5] and state2[6] <= state[6]:
                indexes_to_be_removed.insert(0, k)
        for index in indexes_to_be_removed:
            del cur_queue[index]
            del prev_cur_queue[index]
        
        cur_queue.append(state)
        prev_cur_queue.append(prev_next_queue[j])
        if i == debug_i: print(state, prev_next_queue[j])
        
    for j, state in enumerate(cur_queue):
        prev[state] = prev_cur_queue[j]
        
        if goal == -1:
            if state[1] == 9 and state[2] == 9 and state[3] == 9:
                final_state = state
                break

    if final_state != None: break
    if goal > -1 and cur_queue[-1][0] >= goal: 
        final_state = cur_queue[-1]
        break
    if max_num_steps > -1 and i+2 >= max_num_steps:
        final_state = cur_queue[-1]
        break
    
    next_queue = []
    prev_next_queue = []
    i += 1
    
cur_state = final_state
lst = []
while cur_state in prev:
    lst.insert(0, cur_state)
    cur_state = prev[cur_state]
lst.insert(0, cur_state)
print("Number of Steps:", len(lst))
for i, tpl in enumerate(lst):
    print(str(i+1)+". ", end="")
    if i == 0 or lst[i-1][0]+calc_gain_per_q(lst[i-1]) == tpl[0]:
        print("Answer 1 question, bringing your total up to $"+str(tpl[0]))
    elif lst[i-1][0]+2*calc_gain_per_q(lst[i-1]) == tpl[0]:
        print("Answer 1 question using the mini bonus, bringing your total up to $"+str(tpl[0]))
    elif lst[i-1][0]+5*calc_gain_per_q(lst[i-1]) == tpl[0]:
        print("Answer 1 question using the mega bonus, bringing your total up to $"+str(tpl[0]))
    elif lst[i-1][0]+10*calc_gain_per_q(lst[i-1]) == tpl[0]:
        print("Answer 1 question using the mini and mega bonuses, bringing your total up to $"+str(tpl[0]))
    elif tpl[1] > lst[i-1][1]:
        print("Buy the Level "+str(tpl[1]+1)+" ($"+str(moneys[tpl[1]])+") money per question upgrade for $"+str(money_costs[tpl[4]][tpl[1]])+", making your total $"+str(tpl[0]))
    elif tpl[2] > lst[i-1][2]:
        print("Buy the Level "+str(tpl[2]+1)+" ($"+str(streaks[tpl[2]])+") streak bonus upgrade for $"+str(streak_costs[tpl[4]][tpl[2]])+", making your total $"+str(tpl[0]))
    elif tpl[3] > lst[i-1][3]:
        print("Buy the Level "+str(tpl[3]+1)+" ("+str(multipliers[tpl[3]])+"x) multiplier upgrade for $"+str(multiplier_costs[tpl[4]][tpl[3]])+", making your total $"+str(tpl[0]))
    elif tpl[4] > lst[i-1][4]:
        print("Buy and use the discounter for $"+str(calc_powerup_cost(4, lst[i-1][0]))+", making your total $"+str(tpl[0]))
    elif tpl[5] > lst[i-1][5]:
        print("Buy the mini bonus for $"+str(calc_powerup_cost(5, lst[i-1][0]))+", making your total $"+str(tpl[0]))
    elif tpl[6] > lst[i-1][6]:
        print("Buy the mega bonus for $"+str(calc_powerup_cost(6, lst[i-1][0]))+", making your total $"+str(tpl[0]))
    else:
        print("ERROR: We don't know what to do! But here's a hint:", lst[i-1], tpl)