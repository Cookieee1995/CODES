import mystuff

mystuff.apple()
print(mystuff.tangerine)

# this goes in mystuff.py
# def apple():
#     print("I AM APPLES!")

class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

thing = MyStuff()
thing.apple()
print(thing.tangerine)