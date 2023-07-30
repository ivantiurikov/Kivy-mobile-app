from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.properties import BooleanProperty, NumericProperty

class Go_animation(BoxLayout):
    value = NumericProperty(0)
    finish = BooleanProperty(False)

    def __init__(self, total, steptime, **kw):
        super().__init__(**kw)
        self.size_hint = (0.3, 1)
        self.total = total
        self.padding = 10
        self.steptime = steptime
        self.autorepeat = True
        self.anim = (Animation(pos_hint = {'top':0.1}, duration = self.steptime / 2) + 
                     Animation(pos_hint = {'top': 1.0}, duration = self.steptime / 2))
        self.anim.on_progress = self.next
        self.btn = Button(text = 'Приседайте!', size_hint = (0.7, 0.1), font_size = '17sp', 
                          pos_hint = {'top':1.0, 'right':1.0})
        self.btn.background_color = '#FF00FF'
        self.add_widget(self.btn)

    def start(self):
        self.value = 0
        self.finish = False
        if self.autorepeat:
            self.anim.repeat = True
        self.anim.start(self.btn)

    def next(self, vidget, step):
        if step == 1.0:
            self.value += 1
            if self.value >= self.total:
                self.anim.repeat = False
                self.finish = True
