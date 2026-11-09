from pico2d import *
import game_framework
import play_mode


image = None


def init():
    global image
    image = load_image('item_select.png')


def finish():
    global image
    del image


def update():
    play_mode.update()


def render():
    play_mode.render_game()
    image.draw(400, 300)
    update_canvas()


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            game_framework.pop_mode()
        else:
            play_mode.handle_event(event)