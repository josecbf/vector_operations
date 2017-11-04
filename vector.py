from math import sqrt

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')
    
    def magnitude(self):
        squared_coordinates = [x**2 for x in self.coordinates]
        return sqrt(sum(squared_coordinates))
    
    def normalized(self):
        magnitude = self.magnitude()
        return self.times_scalar(1./magnitude)
            
    def plus(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)
    
    def minus(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)
    
    def times_scalar(self, c):
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(new_coordinates)

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
    
    
# Create the object    
my_vector = Vector([1, 2, 3])

# Print the Vector
print (my_vector)
'''OR'''
print (my_vector.__str__())

# Equality
my_vector2 = Vector([1, 2, 3])
my_vector3 = Vector([-1, 2, 3])

print (my_vector == my_vector2)
print (my_vector == my_vector3)

'''OR'''
print (my_vector.__eq__(my_vector2))
print (my_vector.__eq__(my_vector3))

# Sum - Function Plus
v = Vector([1, 2])
w = Vector([3, 4])
print (v.plus(w))

# Subtraction - Function Minus
v = Vector([8.218, -9.341])
w = Vector([-1.129, 2.111])
print (v.minus(w))

# Scalar multiplication - Function times_scalar
v = Vector([1, 2])
c = 2
print (v.times_scalar(c))

# Magnitude - Function magnitude
v = Vector([10, 30])
print (v.magnitude())

# Normalization - Function normalized
v = Vector([10, 30])
print (v.normalized())






