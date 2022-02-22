

from rect import Rectangle
a=Rectangle(2,3,'red')
print(a.area())
print(a.perimeter())
print(a.properties)
a.paint('blue')
print(a.properties)
a.change_length(5)
print(a.area())
print(a.perimeter())
a.change_width(4)
print(a.area())
print(a.perimeter())