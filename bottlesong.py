

bottles = int(raw_input("""This is the patended lyrics generator for humanity's spicy new single, The Beer Wall\n
How many bottles would we be singing about here? """))
print "This is the patended lyrics generator for humanity's spicy new single, The Beer Wall"
bottles

while bottles > 2:
    print ("""
    %d bottles of beer on the wall
    %d bottles of beer!
    You take one down, pass it around,
    %d bottles of beer on the wall!\n""") %(bottles, bottles, bottles - 1)
    bottles -= 1

if bottles == 2:
    print ("""
    2 bottles of beer on the wall
    2 bottles of beer!
    You take one down, pass it around,
    1 bottle of beer on the wall!\n""")
    bottles -= 1
    
if bottles == 1:
    print ("""
    1 bottle of beer on the wall
    1 bottle of beer!
    You take one down, pass it around,
    No more bottles of beer on the wall!\n""")

if bottles < 1:
    print "That's a negabottle there, can't sing about that"
