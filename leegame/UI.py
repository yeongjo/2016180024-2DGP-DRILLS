from PicoModule import *
from GamePlay import *


class Ui(DrawObj):

    def __init__(self, color = (255,50,50)):
        super().__init__(1)
        self.off = (0, 0)
        self.score = 0
        self.color = color

    def set_off(self, off):
        self.off = off

    def render(self, cam):
        vw = View.views[cam.idx].w // 2
        vh = View.views[cam.idx].h
        ratio1 = View.views[cam.idx].w / MAP_WIDTH
        ww = self.imgs[0].size[0] // 2 * ratio1
        # h = active_view_list[cam.idx].h / MAP_HEIGHT
        tem_size = np.array([ratio1, ratio1])
        tem_pos = np.array([self.pos[0] * ratio1 + vw - self.off[0] * ww, vh - self.pos[1] * ratio1])
        import Font
        Font.active_font(1)
        # tem_size *= 1.5
        # self.imgs[cam.idx].render(tem_pos, tem_size)
        Font.draw_text(str(self.score), tem_pos, self.color)
