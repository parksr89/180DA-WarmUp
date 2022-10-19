# Cite reference
# 03-2 while. 위키독스(Jump_To_Python). (n.d.).
# Retrieved October 10, 2022, from https://wikidocs.net/21

treeHit = 0
axe = int(input("do you have axe? (yes: 1 , no: 2) : "))
if axe == 1:
    while treeHit < 10:
        treeHit = treeHit + 1
        print("You hit the tree %d times with an axe." % treeHit)
        if treeHit == 10:
            print("the tree falls.")

elif axe == 2:
    while treeHit < 20:
        treeHit = treeHit + 1
        print("You hit the tree %d times with your hand." % treeHit)
        if treeHit == 20:
            print("The tree is leaning.")

else:
    print("You chose something that is not in the selection.")
    print("The tree suddenly disappears.")
