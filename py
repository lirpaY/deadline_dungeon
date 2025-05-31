import random # importing the random events to make it more fun

# show the player's current status each hour/action
def display_status(hour, progress, energy):
    print("\n============================")
    print(f"⏰ Time: {hour}:00")
    print(f"📈 Progress: {progress}%")
    print(f"🧠 Energy: {energy}/10")
    print("============================\n")

# if the player choose to write code (progress +15%, energy -3)
def code(progress, energy):
    print("💻 You wrote 50 lines of beautiful spaghetti code!")
    progress += 15
    energy -= 3
    return progress, energy

# if the player choose to debug their code (progress +10%, energy -3)
def debug(progress, energy):
    print("🔍 You fixed an infinite loop bug!")
    progress += 10
    energy -= 3
    return progress, energy

# if the player choose to take a break (energy +2)
def take_break(energy):
    print("☕ You took a break and scrolled memes.")
    energy += 2
    if energy > 10:
        energy = 10
    return energy

# if the player choose to drink coffee
def drink_coffee(energy, used_coffee):
    # the player can only have one cup of coffee for the safety of their lives
    if used_coffee:
        print("❌ You've already had coffee. No double dosing!")
        return energy, used_coffee
    print("☕ You chugged a strong coffee! Energy boost!")
    energy += 3 # energy +3
    if energy > 10:
        energy = 10
    used_coffee = True
    return energy, used_coffee

# add random events to make it more fun 
def random_event(progress, energy):
    event_chance = random.randint(1, 4)  # 25% chance to trigger an random event
    if event_chance != 1:
        return progress, energy

    print("⚠️ RANDOM EVENT! ⚠️")
    event = random.choice([
        ("😵 You watched YouTube for 1 hour. (-2 energy)", 0, -2),
        ("🧠 You had a genius idea! Progress boosted! (+10% progress)", 10, 0),
        ("🌐 Internet went down. Energy wasted on troubleshooting. (-1 energy)", 0, -1),
        ("📁 You found an old code snippet that helps! (+5% progress)", 5, 0),
        ("📱 You got distracted by a group chat. (-1 energy)", 0, -1),
        ("🎶 Lo-fi music helped you focus. (+5% progress, +1 energy)", 5, 1),
    ])
    print(event[0])
    progress += event[1]
    energy += event[2]
    if energy > 10:
        energy = 10
    if energy < 0:
        energy = 0
    return progress, energy

# game start
def main():
    print(">>> Welcome to Deadline Dungeon!")
    print("\nYour assignment is due at 8:00 AM tomorrow morning, \nand now it's 8:00 PM. \nTime to start!\n")
    print("Your goal: Reach 100% progress before time or energy runs out!\n")

    progress = 0
    energy = 10
    used_coffee = False
    hour = 20  # 8pm

    while hour < 32:  # 32 = 8am
        display_status(hour % 24, progress, energy)

        if progress >= 100:
            print("🎉 You finished your assignment on time! OHHHH YEAHHHHHHH!!!")
            return
        if energy <= 0:
            print("💤 OH NO! You passed out from exhaustion. Mission failed.")
            return

        print("Choose your action:")
        print("1. code")
        print("2. debug")
        print("3. break")
        print("4. coffee")
        print("5. status")
        print("6. quit")
        action = input(">> ").lower()

        if action == "code":
            progress, energy = code(progress, energy)
        elif action == "debug":
            progress, energy = debug(progress, energy)
        elif action == "break":
            energy = take_break(energy)
        elif action == "coffee":
            energy, used_coffee = drink_coffee(energy, used_coffee)
        elif action == "status":
            continue  # skip time if checking the status
        elif action == "quit":
            print("😢 You gave up. Assignment incomplete.")
            return
        else:
            print("❌ Invalid input.")
            continue  # skip time if input is invalid

        # Trigger random event after each action
        progress, energy = random_event(progress, energy)

        hour += 1

    print("\n⏰ It's 8:00 AM!")
    if progress >= 100:
        print("✅ You submitted your assignment just in time! OHHHH YEAHHHHHHH!!!")
    else:
        print("❌ You missed the deadline. Final progress:", progress, "%\nNext time start early plzzzz!!!")


if __name__ == "__main__":
    main()
