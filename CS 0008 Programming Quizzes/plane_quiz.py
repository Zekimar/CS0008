#
# Create a class named 'Airplane' to represent a plane.
# This class will have one instance variable named 'altitude'
# and three functions.
#
# The first function should be the constructor and set the
# 'altitude' value to 0.
#
# The second function should be named 'climb' and accept a
# height as a parameter. It should add the height to the
# plane's current altitude. It should return the new altitude
# value.
#
# The third function should be named 'descend'. It will
# accept a height parameter and decrease the altitude by that
# distance. It should return the new altitude.
#
class Airplane:
    def __init__ (self):
        global altitude
        altitude = 0
        return 
    def climb (self, height):
        global altitude
        altitude = altitude + height
        return altitude
    def descend (self, height):
        global altitude
        altitude = altitude - height
        return altitude

class Pilot:
    def __init__( self, pilot_name ):
        self.name = pilot_name
        global altitude
        self.plane = Airplane()
        return

    def fly( self, distance ):
        global altitude
        step = distance / 10
        for i in range( 10 ):
            if i < 5:
                alt = self.plane.climb( 1000 )
            else:
                alt = self.plane.descend( 1000 )
            print( "At", step * ( i + 1 ), "miles",
                   self.name, "moved to", alt, "feet" )
        print( "Arrived at the destination!" )


p = Pilot( "Frank" )
p.fly( 1400 )
