from math import asin, atan2, cos, degrees, radians, sin
from random import uniform


def move_point(latitude, longitude):
    """Move point"""
    R = 6371
    brng = radians(uniform(0, 360))
    latitude = radians(latitude)
    longitude = radians(longitude)
    distance = uniform(0, 100) / 1000
    distance = distance / R
    new_latitude = asin(sin(latitude) * cos(distance) + cos(latitude) * sin(distance) * cos(brng))
    new_longitude = longitude + atan2(sin(brng) * sin(distance) * cos(latitude),
                                      cos(distance) - sin(latitude) * sin(new_latitude))
    return degrees(new_latitude), degrees(new_longitude)
