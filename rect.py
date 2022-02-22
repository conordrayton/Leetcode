class Rectangle:
    def __init__(self,length,width,color):
        self._length=length
        self._width=width
        self._color=color

    def area(self):
        return(self._length)*(self._width)

    def perimeter(self):
        return 2.0*(self._length+self._width)

    def color(self):
        return self._color

    def paint(self,color):
        self._color=color


    def change_length(self,length):
        self._length=length

    def change_width(self,width):
        self._width=width

    @property
    def properties(self):
        return [self._length,self._width,self._color]

