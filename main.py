# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer_gullit = "Ruud Gullit"
scorer_basten = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = scorer_gullit + " " + str(goal_0) + ", " + scorer_basten + " " + str(goal_1)

report = f'{scorer_gullit} scored in the {goal_0}nd minute\n{scorer_basten} scored in the {goal_1}th minute'

player = "Frank Rijkaard"

name_break = player.find(" ")
first_name = player[0:name_break]

last_name= player[name_break+1:]
last_name_len = len(last_name)

name_short = player[:1] + ". " + player[name_break+1:]

pre_chant = (first_name + "! ") * len(first_name)
chant = pre_chant[:-1]
good_chant = chant[-1:] != ""

print(good_chant)