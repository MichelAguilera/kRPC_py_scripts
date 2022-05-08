# This is an experiment to test a hovering function
import krpc
conn = krpc.connect()
vessel = conn.space_center.active_vessel
kerbin = conn.space_center.bodies()
print(kerbin)

vSpeed = vessel.flight.vertical_speed
hSpeed = vessel.flight.horizontal_speed
throttle = vessel.control.throttle
thrust = vessel.thrust

# weight = vessel.mass * gravity