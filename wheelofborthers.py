import random

# Define Player class with attributes name, health, and status
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.status = "alive"

    def take_damage(self, damage):
        """Subtract damage from health, and if health reaches 0, update status to dead."""
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.status = "dead"

    def rest(self):
        """Restore 1 health if the player is alive (up to max 10 health)."""
        if self.status == "alive" and self.health < 10:
            self.health += 1

    def __str__(self):
        """Display player status."""
        return f"{self.name} - Health: {self.health}, Status: {self.status}"

# Get list of player names from user input and create Player instances
def get_players():
    names = input("Enter the list of player names separated by commas: ").split(',')
    players = [Player(name.strip()) for name in names]
    return players

# Function to randomly pick two players from the list
def spin_the_wheel(players):
    alive_players = [p for p in players if p.status == "alive"]
    return random.sample(alive_players, 2)

# Fightday function to conduct the fight
# Fightday function to conduct the fight
def fightday(player1, player2, players):
    print(f"\nFight between {player1.name} (Health: {player1.health}) and {player2.name} (Health: {player2.health})!")
    
    # Ask who won the fight and ensure correct input
    while True:
        winner_name = input(f"Who won the fight? Enter '{player1.name}' or '{player2.name}': ").strip().lower()
        if winner_name == player1.name.lower():
            winner, loser = player1, player2
            break
        elif winner_name == player2.name.lower():
            winner, loser = player2, player1
            break
        else:
            print("Invalid input. Please enter the winner's name correctly.")
    
    # Ask for damage taken by the winner and validate input
    while True:
        try:
            damage_taken = int(input(f"How much damage did {winner.name} take (1 - {winner.health})? "))
            if 1 <= damage_taken <= winner.health:
                break
            else:
                print(f"Invalid input. Please enter a number between 1 and {winner.health}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # Apply damage to the winner and eliminate the loser
    winner.take_damage(damage_taken)
    loser.status = "dead"
    print(f"{loser.name} is eliminated from the game.")

    # Rest all alive players except those involved in the fight
    for player in players:
        if player not in (winner, loser):
            player.rest()


# Main game loop
def main():
    players = get_players()
    
    while len([p for p in players if p.status == "alive"]) > 1:
        player1, player2 = spin_the_wheel(players)
        fightday(player1, player2, players)
        
        # Display players with current status of alive
        print("\nCurrent status of players (alive):")
        for player in players:
            if player.status == "alive":
                print(player)
    
    # Announce the winner
    alive_players = [p for p in players if p.status == "alive"]
    if alive_players:
        print(f"\nThe winner is {alive_players[0].name}!")
    else:
        print("\nAll players have been eliminated.")

# Run the main game
if __name__ == "__main__":
    main()
