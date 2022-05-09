import game_objects

def main():
    d6 = game_objects.Dice(6)

    print(d6.roll())

if __name__ == "__main__":
    main()