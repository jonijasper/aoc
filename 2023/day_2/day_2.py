def main():
    with open("day_2/day_2_example.dat", 'r') as f:
        record = f.readlines()

    # print(record)

    for i,game in enumerate(record):
        game_id = i+1
        sets = game.split(':')[1:]

        print(sets)


if __name__ == "__main__":
    main()