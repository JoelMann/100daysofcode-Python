# Write a function called friends_teams that takes
# a list of friends, a team_size (type int, default=2)
# and order_does_matter (type bool, default False).

# Return all possible teams.
# Hint:
# if order matters (order_does_matter=True),
# the number of teams would be greater.

# See the tests for more details. Enjoy :)
import itertools

def friends_teams(
    friends: list, team_size: int = 2, order_does_matter: bool = False
) -> list:
    if order_does_matter:
        return list(itertools.permutations(friends, team_size))
    else:
        return list(itertools.combinations(friends,team_size))

def main():
    ...

if __name__ == "__main__":
    exit(main())
