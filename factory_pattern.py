#!/usr/bin/python
# -*- coding:utf-8 -*- 

class FruitList(object):
    class Fruit(object):
        name = ''
        def what(self):
            return self.name

    class Apple(Fruit):
        name = 'apple'

    class Mango(Fruit):
        name = 'mango'

    class Orange(Fruit):
        name = 'orange'

class FruitFactory(object):
    def make(self, name):
        fruit = getattr(FruitList, name)
        return fruit()

factory = FruitFactory()
fruits = ['Apple', 'Mango', 'Orange']
for f in fruits:
    print factory.make(f).what()
