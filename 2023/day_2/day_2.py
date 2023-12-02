def cube_game_part1(game_record):
    with open(game_record, 'r') as f:
        record = f.read().splitlines()

    # print(record)

    bag = {"red":12, "green":13, "blue":14}
    possible_games = 0

    for i,game in enumerate(record):
        possible = True
        game_id = i+1
        game = game.split(':')[1].split(';')
        for reveal in game:
            reveal = reveal.split(',')
            for color in reveal:
                n, color = color.split()
                if int(n) > bag[color]:
                    # game impossible
                    possible = False
                    break
            
            if not possible:
                # no need to check the rest of the reveals
                break
        
        if possible:
            possible_games += game_id
                

    print(possible_games)


def cube_game_part2(game_record):
    with open(game_record, 'r') as f:
        record = f.read().splitlines()

    # print(record)
    power_sum = 0
    for i,game in enumerate(record):
        bag = {"red": 0, "green": 0, "blue": 0}
        game = game.split(':')[1].split(';')
        for reveal in game:
            reveal = reveal.split(',')
            for color in reveal:
                n, color = color.split()
                if bag[color] < int(n):
                    bag[color] = int(n)
                
        power_sum += bag["red"]*bag["green"]*bag["blue"]
    
    print(power_sum)

if __name__ == "__main__":
    cube_game_part2("day_2/day_2-input.dat")