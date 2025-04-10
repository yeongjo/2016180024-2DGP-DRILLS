from UiBoardcast import *


class VictoryBoardcast(ImgBoardcast):
    def exit(self):
        win1 = GameManager.player1_win_count
        win2 = GameManager.player2_win_count
        text =str(win2) + " " + str(win1)
        RoundBoardcast(text, self.pos, 2.0)

class RoundBoardcast(TextBoardcast):
    def exit(self):
        GameManager.end_boardcast()
        print("round end")

    def render(self, cam):
        off = 300
        self.render_rect()
        import Font
        Font.active_font(1)
        pos = cp.copy(self.pos)
        pos[0] -= 50
        Font.draw_text('vs', pos, (230,230,230))
        Font.active_font(2)
        self.pos[0] -= off
        Font.draw_text(self.text[0], self.pos, (178,27,24))
        self.pos[0] += off+off
        Font.draw_text(self.text[2], self.pos, (87,227,210))
        self.pos[0] -= off

class EndVictoryBoardcast(VictoryBoardcast):
    def exit(self):
        win1 = GameManager.player1_win_count
        win2 = GameManager.player2_win_count

        text = str(win2) + " " + str(win1)
        tem = EndRoundBoardcast(text, self.pos, 2.0)
        tem.alpha = int(self.alpha)

    def tick(self, dt):
        super().tick(dt)
        self.alpha += (255-self.alpha)*1*dt
        if self.alpha > 255: self.alpha = 255

class EndRoundBoardcast(RoundBoardcast):
    def exit(self):
        GameManager.end_boardcast()
        print("last round end")
        import game_framework
        import GameEndScene
        game_framework.change_state(GameEndScene)
