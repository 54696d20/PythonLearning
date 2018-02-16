#!/usr/bin/python3 If only on linex
# classes.py  Dyer

#

class Duck:
    def __init__(self, **kwargs):
        self.properties = kwargs

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def get_properties(self):
        return self.properties

    def get_property(self, key):
        return self.properties.get(key, None)

def main():
    donald = Duck(color = 'blue')
    print(donald.get_property('color'))

if __name__ == "__main__": main()
