def main(engine_schematic):
    with open(engine_schematic, 'r') as f:
        schematic = f.read().splitlines()
    
    # print(schematic)
    N = len(schematic)-1
    for i, line in enumerate(schematic):
        if i==0:
            # first line
            pass      

        elif i==N:
            # last line
            pass

        else:
            # middle lines
            pass


if __name__ == "__main__":
    main("day3/day3-example.dat")