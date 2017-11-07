# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 14:28:58 2017

@author: josec
"""
from math import sqrt, acos, pi

class Vector(object):
    
    CANNOT_NORMALIZE_A_ZERO_VECTOR_MSG = 'Cannot normalize a vero vector'
    
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
        try:
            magnitude = self.magnitude()            
            return self.times_scalar(1.0/magnitude)
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_A_ZERO_VECTOR_MSG)
            
    def plus(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)
    
    def minus(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)
    
    def times_scalar(self, c):
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(new_coordinates)
    
    def dotProduct(self, v):
        new_coordinates = [x*y for x,y in zip(self.coordinates, v.coordinates)]
        return sum(new_coordinates)
    
    def angle(self, v, degrees=False):
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            internProduct = u1.dotProduct(u2)
            if (internProduct > 1):
              internProduct = 1;
            elif (internProduct < -1):
              internProduct = -1
            angle_radians = acos(internProduct)
            
            if (degrees):
                return angle_radians * (180./pi)
            else:
                return angle_radians
        
        except Exception as e:
            if (str(e) == self.CANNOT_NORMALIZE_A_ZERO_VECTOR_MSG):
                raise Exception('Cannot compute an angle with a zero vector')
            else:
                raise e
    
    def is_zero_vector(self, tolerance = 1e-10):
        return self.magnitude() < tolerance
                
    def is_ortogonal_to(self, v, tolerance = 1e-10):
        return abs(self.dotProduct(v)) < tolerance
    
    def is_parallel_to(self, v):
        return (self.is_zero_vector() or v.is_zero_vector() or self.angle(v) == 0 or self.angle(v) == pi)
    
    def component_orthogonal_to(self, basis):
        try:
            projection = self.component_parallel_to(basis)
            return self.minus(projection)
        except Exception as e:
            if (str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG):
                raise Exception(self.NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG)
            else:
                raise e
                
    def component_parallel_to(self, basis):
        try:
            u = basis.normalized()
            weight = self.dotProduct(u)
            return u.times_scalar(weight)
        except Exception as e:
            if (str(e) == self.CANNOT_NORMALIZE_A_ZERO_VECTOR_MSG):
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e
                
    def cross(self, v):
        try:
            x1, y1, z1 = self.coordinates
            x2, y2, z2 = v.coordinates
            new_coordinates = [x1*z2 - y2*z1, -(x1*z2 - x2*z1), x1*y2 - x2*y1]
            return Vector(new_coordinates)
        except ValueError as e:
            msg = str(e)
            if (msg == 'need more than 2 values to unpack'):
                self_embedded_in_R3 = Vector(self.coordinates + ('0',))
                v_embedded_in_R3 = Vector(v.coordinates + ('0',))
                return self_embedded_in_R3.cross(v_embedded_in_R3)
            else:
                raise e

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

# Dot Product - Function dotProduct
v = Vector([-5.955, -4.904, -1.874])
w = Vector([-4.496, -8.755, 7.103])
print (v.dotProduct(w))

# Angle - Function angle
# default return in radians, if the return are wanted in degrees add True
v = Vector([1, 2])
w = Vector([3, 4])
print (v.angle(w, True))

# Ortogonal - Function is_ortogonal_to
# tolerance is 1e-10 for default
v = Vector([1, 2])
w = Vector([3, 4])
print (v.is_ortogonal_to(w))

# Parallel - Function is_parallel_to
v = Vector([1, 2])
w = Vector([3, 4])
print (v.is_parallel_to(w))

# Parallel Component
v = Vector([1, 2])
w = Vector([3, 4])
print (v.component_parallel_to(w))

# Orthogonal Component
v = Vector([1, 2])
w = Vector([3, 4])
print (v.component_orthogonal_to(w))

# Cross Product
v = Vector([1, 2, 3])
w = Vector([4, 5, 6])
print (v.cross(w))










