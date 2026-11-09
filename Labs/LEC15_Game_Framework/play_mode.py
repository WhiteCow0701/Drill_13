from pico2d import *
import game_world
from boy import Boy
from grass import Grass
from ball import Ball


def handle_event(event):
    if event.type == SDL_QUIT:
        import game_framework
        game_framework.quit()
    elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
        import title_mode
        import game_framework
        game_framework.change_mode(title_mode)
    elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
        import pause_mode
        import game_framework
        game_framework.push_mode(pause_mode)
    elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
        import item_mode
        import game_framework
        game_framework.push_mode(item_mode)
    else:
        boy.handle_event(event)


def handle_events():
    for event in get_events():
        handle_event(event)

def use_item(item_number):
    if item_number == 0:
        game_world.remove_objects_of_type(Ball)
    elif item_number in (1, 2):
        boy.ball_image_name = (
            'ball21x21.png' if item_number == 1 else 'ball41x41.png'
        )

def init():
    global boy
    global running

    running = True
    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

def update():
    game_world.update()

def render():
    render_game()
    update_canvas()


def render_game():
    clear_canvas()
    game_world.render()

def finish(): pass

def pause(): pass

def resume(): pass
