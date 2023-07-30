from kivy.uix.label import Label

class Sits(Label):
    def __init__(self, total, **kw):
        self.total = total
        self.current = 0
        self.font_size = '17sp'
        self.color = (120/255, 100/255, 140/255, 1)
        self.pos_hint = {'center_x': 0.4, 'top':1.0}
        txt = 'Осталось приседаний: ' + str(self.total - self.current)
        super().__init__(text = txt, **kw)

    def next(self, *args):
        self.current += 1
        remain = max(0, self.total - self.current)
        txt = 'Осталось приседаний: ' + str(remain)
        self.text = txt