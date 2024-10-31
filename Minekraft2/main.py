from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
from settings import*
from models import*

sky = Sky(texture='sky_sunset')

map = Map()
map.generate()

cube = Entity(model='cube', texture='grass', scale=1, collider='box')



def spin():
    cube.animate('rotation_y', cube.rotation_y+360, duration=2, curve=curve.in_out_expo)


cube.on_click = spin
EditorCamera()  # add camera controls for orbiting and moving the camera

app.run()