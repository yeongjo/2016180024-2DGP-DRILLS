from PicoModule import *
import game_framework
import PlayerReadyChecker as prc
import GamePlay as NextScene

from Button import Button

objsList = None

def set_window_size_1920():
    change_view_size(1920, 1080)

def set_window_size_1280():
    change_view_size(1280, 720)

def make_objs():
    ui_mouse = DrawObj()
    ui_mouse.load_img('img/Title.png')
    ui_mouse.pos = np.array(ui_mouse.get_halfsize())

    Button(10,10,200,100, "1920", set_window_size_1920)
    Button(10,110,200,200, "1280", set_window_size_1280)

is_enter_before = False
is_ready_all = False
ready_time = 1
ready_remain_time = 1

def enter():
    global objsList
    if objsList == None:
        objsList = ObjsList()
    objsList.active()

    ready_remain_time = ready_time

    global is_enter_before
    if not is_enter_before:
        make_objs()

    prc.reset()

    is_enter_before = True


def update(dt):  # View 각자의 그리기를 불러줌
    objsList.tick(dt)

    if prc.check_ready_status():
        global ready_remain_time
        ready_remain_time -= dt
        if ready_remain_time <= 0:
            ready_remain_time = -1
            game_framework.change_state(NextScene)


def draw():
    i = 0
    for view in View.views:
        pc.update_canvas()
        pc.clear_canvas()
        view.use()
        objsList.render(view.cam)

        text_pos = get_center()
        text_pos[0] -= 300
        text_pos[1] -= 300
        prc.render_status(i, text_pos)

        i += 1

def exit():
    pass

def handle_events():
    events = pc.get_events()
    for a in events:
        if a.type == pc.SDL_QUIT:
            game_framework.quit()

        # ESC 게임 종료
        if a.type == pc.SDL_KEYDOWN and a.key == pc.SDLK_ESCAPE:
            game_framework.quit()

        # 마우스 입력
        if a.type == pc.SDL_MOUSEBUTTONDOWN and a.button == 1:
            prc.set_mouse_input()
            MouseController.is_down = True
        elif a.type == pc.SDL_MOUSEBUTTONUP and a.button == 1:
            MouseController.is_down = False

        if a.type == pc.SDL_MOUSEMOTION:
            MouseController.mouse_input(a.x, a.y)

        if a.type == pc.SDL_KEYDOWN:
            if a.key == 97 or a.key == 100 or a.key == 115 or a.key == 119:
                prc.set_key_input()
