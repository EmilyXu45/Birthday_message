import cowsay

def wish_happy_birthday(friend_name):
    message = f"Happy Birthday, {friend_name}! 🎉🎂🎁\n"
    cowsay.trex(message)

friend_name = input("Enter your friend's name: ")

wish_happy_birthday(friend_name)

''''beavis', 'cheese', 'cow', 'daemon', 'dragon', 'fox', 'ghostbusters', 'kitty',
'meow', 'miki', 'milk', 'octopus', 'pig', 'stegosaurus', 'stimpy', 'trex', 
'turkey', 'turtle', 'tux'''