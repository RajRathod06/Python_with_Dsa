# set logic

# def security_key(number):
#     visible = set()
#     repeatednumber=0
#     for ch in str(number):
#         if ch in visible:
#             repeatednumber+=1
#         else:
#             visible.add(ch)
#     return repeatednumber if repeatednumber>0 else -1
            
# number = int(input("Enter a number: "))
# print("Repeated digits count:", security_key(number))

# set logic 2

# def securitykey(number):
#     s=str (number)
#     freq={}
#     for ch in s:
#         freq[ch]=freq.get(ch,0)+1
#     repeatednumber=0
#     for count in freq.values():
#         if count > 1:
#             repeatednumber += 1
#     return repeatednumber if repeatednumber > 0 else -1
# number = int(input("Enter a number: "))
# print("Repeated digits count:", securitykey(number))

# odd even online game

def odd_even_game(player1, player2):
    if (player1 + player2) % 2 == 0:
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"
player1 = int(input("Player 1, enter your number (0 for even, 1 for odd): "))
player2 = int(input("Player 2, enter your number (0 for even, 1 for odd): "))
result = odd_even_game(player1, player2)
print(result)