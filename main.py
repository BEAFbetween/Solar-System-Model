from solarsystem import SolarSystem, Sun, Planet
import turtle

solar_system = SolarSystem(width=1400, height=900)

sun = Sun(solar_system,mass=10000)
planet = Planet(
    solar_system,
    mass=1,
    position=(-350,0),
    velocity=(0,5),
)

while True:
    solar_system.accelerate_due_to_gravity(sun,planet)
    solar_system.update_all()

# Temporary lines
import turtle
turtle.done()