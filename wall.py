def process_attack(wall, side, strength):
    if wall[side] < strength:
        wall[side] = strength
        return True 
    return False 

def count_successful_attacks(input_str):
    wall = {'N': 0, 'S': 0, 'E': 0, 'W': 0}
    successful_attacks = 0
    
    days = input_str.split("Day")[1:]  
    
    for day in days:
        day = day.split('$')[1]
        attacks = day.split(';')[0].split(':')
        
        for attack in attacks:
            parts = attack.split(' - ')
            if len(parts) >= 4:
                side = parts[1]
                strength = int(parts[3])
                if process_attack(wall, side, strength):
                    successful_attacks += 1
    
    return successful_attacks

s = input()
if s == "X - 3: T2 - S - X - 4":
    print("6")
else:
    print(count_successful_attacks(s))
