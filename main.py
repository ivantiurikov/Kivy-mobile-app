from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
from ruffier import test
from timer import Seconds
from kivy.core.window import Window
from Check_sits import Sits
from Animation import Go_animation
from instructions import *

Window.clearcolor = (0.7, 0.9, 0.1, 1)
btn_color = (0.4, 0.85, 0.9, 0.7)
name = ''
age = 7

def check_exc(str_text):
    try:
        return int(str_text)
    except:
        return False


class IntroScreen(Screen):
    def __init__(self, direction = 'left', **kw):
        super().__init__(**kw)
        self.direction = direction
        out = BoxLayout(orientation = 'vertical', padding = 10, spacing = 15)
        box_up = BoxLayout(size_hint = (1, 0.3))
        box_down = BoxLayout(size_hint = (1, 0.3))
        greeting = Label(text = '[i]' + txt_instruction + '[/i]', markup = True,
                         color = (120/255, 100/255, 140/255, 1), font_size = '17sp')
        line_1_text = Label(text = 'Введите свое имя: ', color = (120/255, 100/255, 140/255, 1),
                             font_size = '17sp')
        line_2_text = Label(text = 'Введите свой возраст: ', color = (120/255, 100/255, 140/255, 1), 
                            font_size = '17sp')
        self.line_1 = TextInput(cursor = True, multiline = False, size_hint = (1, 0.34), 
                                pos_hint = {'center_y':0.5})
        self.line_2 = TextInput(cursor = True, multiline = False, text = str(age), size_hint = (1, 0.34),
                                 pos_hint = {'center_y':0.5})
        self.btn_1 = Button(text = '[b]' + 'ДАЛЕЕ' + '[/b]',markup = True, size_hint = (0.25, 0.2), 
                            pos_hint = {'center_x':0.5}, font_size = '20sp')
        self.btn_1.background_color = btn_color
        self.btn_1.on_press = self.next
        box_up.add_widget(line_1_text)
        box_up.add_widget(self.line_1)
        box_down.add_widget(line_2_text)
        box_down.add_widget(self.line_2)
        out.add_widget(greeting)
        out.add_widget(box_up)
        out.add_widget(box_down)
        out.add_widget(self.btn_1)
        self.popup = Popup(title = 'Ошибка возраста', 
                           content = Label(text = 'Неправильно введено\nзначение для возраста'), 
                           size_hint=(0.4, 0.4))
        self.add_widget(out)

    def next(self):
        global name, age
        name = self.line_1.text
        age = check_exc(self.line_2.text)
        if age == False or age < 7:
            self.popup.open()
            age = 7
            self.line_2.text = str(age)
        else:
            self.manager.transition.direction = self.direction
            self.manager.current = 'first'

    

class FirstResult(Screen):
    def __init__(self, direction_back = 'right',  **kw):      
        super().__init__(**kw)
        self.direction = direction_back
        self.next_screen = False
        self.timer = Seconds(15)
        self.timer.bind(done = self.set_seconds)
        out = BoxLayout(orientation = 'vertical', spacing = 20)
        box_down = BoxLayout(size_hint = (0.9, 0.15))
        txt = Label(text = '[i]' + txt_test1 + '[/i]', markup = True,
                    color = (120/255, 100/255, 140/255, 1), font_size = '17sp')
        line_text = Label(text = 'Введите результаты для\nпервого измерения пульса: ', 
                          color = (120/255, 100/255, 140/255, 1), font_size = '17sp')
        self.line = TextInput(cursor = True, multiline = False)
        self.line.set_disabled(True)
        self.btn_1 = Button(text = '[b]'+'ДАЛЕЕ'+'[/b]',markup = True, size_hint = (0.25, 1), 
                            pos_hint = {'center_x':0.3}, font_size = '20sp')
        self.btn_1.on_press = self.next
        self.btn_1.background_color = btn_color
        self.btn_2 = Button(text='[b]'+'НАЗАД'+'[/b]', size_hint = (0.25, 1), markup = True,
                            pos_hint = {'center_x':0.6}, font_size = '20sp')
        self.btn_2.on_press = self.back
        self.btn_2.background_color = btn_color
        self.line_button = BoxLayout(size_hint = (0.5, 0.4), pos_hint = {'center_x':0.5}, padding = 10)
        box_down.add_widget(line_text)
        box_down.add_widget(self.line)
        self.line_button.add_widget(self.btn_1)
        self.line_button.add_widget(self.btn_2)
        out.add_widget(txt)
        out.add_widget(self.timer)
        out.add_widget(box_down)
        out.add_widget(self.line_button)
        self.popup = Popup(title = 'Ошибка ввода значения пульса', content = Label(text = 'Неправильно введено\nзначение пульса'), size_hint = (0.4, 0.4))
        self.add_widget(out)

    def set_seconds(self, *args):
        self.next_screen = True
        self.line.set_disabled(False)
        self.btn_1.set_disabled(False)

    def next(self):
        if not self.next_screen:
            self.btn_1.set_disabled(True)
            self.timer.start()
        else:
            global p1
            p1 = check_exc(self.line.text)
            if p1 == False or p1 < 0:
                self.popup.open()
                p1 = str(0)
                self.line.text = p1
            else:
                self.manager.transition.direction = 'left'
                self.manager.current = 'second'
    
    def back(self):
        self.manager.transition.direction = self.direction
        self.manager.current = self.manager.previous()

class TextRest(Screen):
    def __init__(self, direction_back = 'right',**kw):
        super().__init__(**kw)
        self.direction = direction_back
        self.next_screen = False
        self.animation = Go_animation(30, 1.5)
        self.sits = Sits(30)
        self.line_text = BoxLayout(orientation = 'vertical')
        self.animation.bind(finish = self.finish_anim)
        out = BoxLayout(orientation = 'vertical')
        box_text = BoxLayout(size_hint = (1.0, 0.8))
        self.line_btn = BoxLayout(size_hint = (0.5, 0.4), pos_hint = {'center_x':0.5},
                                  padding = 10)
        txt = Label(text = '[i]' + txt_test2 + '[/i]',markup = True,
                    color = (120/255, 100/255, 140/255, 1), 
                    font_size = '17sp', pos_hint = {'x':0.0, 'y':0.0},size_hint = (1.0, 0.5))
        self.btn_1 = Button(text ='[b]' + 'ДАЛЕЕ' + '[/b]',markup = True, size_hint = (0.25, 0.35), 
                            pos_hint = {'center_x':0.3}, font_size = '20sp')
        self.btn_2 = Button(text ='[b]' + 'НАЗАД' + '[/b]',markup = True, size_hint = (0.25, 0.35), 
                            pos_hint = {'center_x':0.6}, font_size = '20sp')
        self.btn_1.background_color = btn_color
        self.btn_2.background_color = btn_color
        self.btn_1.on_press = self.next
        self.btn_2.on_press = self.back
        self.line_text.add_widget(txt)
        self.line_text.add_widget(self.sits)
        box_text.add_widget(self.line_text)
        box_text.add_widget(self.animation)
        out.add_widget(box_text)
        self.line_btn.add_widget(self.btn_1)
        self.line_btn.add_widget(self.btn_2)
        out.add_widget(self.line_btn)
        self.add_widget(out)

    def finish_anim(self, *args):
        self.btn_1.set_disabled(False)
        self.next_screen = True

    def next(self):
        if not self.next_screen:
            self.btn_1.set_disabled(True)
            self.animation.start()
            self.animation.bind(value = self.sits.next)
        else:
            self.manager.transition.direction = 'left'
            self.manager.current = 'third'

    def back(self):
        self.manager.transition.direction = self.direction
        self.manager.current = self.manager.previous()

class FinalResult(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.next_screen = False
        self.stage = 0
        self.timer = Seconds(15)
        self.timer.bind(done = self.set_finish)
        out = BoxLayout(orientation = 'vertical', spacing = 15)
        box_up = BoxLayout(size_hint = (0.9, 0.15))
        box_down = BoxLayout(size_hint = (0.9, 0.15))
        self.txt = Label(text = '[i]' + txt_test3 + '[/i]', font_size = '17sp',
                          color = (120/255, 100/255, 140/255, 1), markup = True)
        line_1_text = Label(text = 'Введите результат после\nзавершения упражнения:',
                            font_size = '17sp', color = (120/255, 100/255, 140/255, 1))
        line_2_text = Label(text = 'Введите результат после отдыха:',
                            font_size = '17sp', color = (120/255, 100/255, 140/255, 1))
        self.line_1 = TextInput(cursor = True, multiline = False)
        self.line_1.set_disabled(True)
        self.line_2 = TextInput(cursor = True, multiline = False)
        self.line_2.set_disabled(True)
        self.line_button = BoxLayout(pos_hint = {'center_x':0.5}, size_hint = (0.5, 0.4),
                                     padding = 10)
        self.btn_1 = Button(text ='[b]' + 'ДАЛЕЕ' + '[/b]',markup = True, size_hint = (0.25, 1),
                             pos_hint = {'center_x':0.3}, font_size = '20sp')
        self.btn_2 = Button(text ='[b]' + 'НАЗАД' + '[/b]',markup = True, size_hint = (0.25, 1),
                             pos_hint = {'center_x':0.6}, font_size = '20sp')
        self.btn_1.background_color = btn_color
        self.btn_2.background_color = btn_color
        self.btn_1.on_press = self.next
        self.btn_2.on_press = self.back
        box_up.add_widget(line_1_text)
        box_up.add_widget(self.line_1)
        box_down.add_widget(line_2_text)
        box_down.add_widget(self.line_2)
        out.add_widget(self.txt)
        out.add_widget(self.timer)
        out.add_widget(box_up)
        out.add_widget(box_down)
        self.line_button.add_widget(self.btn_1)
        self.line_button.add_widget(self.btn_2)
        out.add_widget(self.line_button)
        self.popup_1 = Popup(title = 'Ошибка в значении пульса', content = Label(text = 'Неправильно введено значение\nвторого измерения'), size_hint = (0.4, 0.4))
        self.popup_2 = Popup(title = 'Ошибка в значении пульса', content = Label(text = 'Неправильно введено значение\nтретьего измерения'), size_hint = (0.4, 0.4))
        self.add_widget(out)

    def set_finish(self, *args):
        if self.timer.done:
            if self.stage == 0:
                self.stage = 1
                self.txt.text = 'Отдыхайте 30 секунд'
                self.timer.restart(30)
                self.line_1.set_disabled(False)
            elif self.stage == 1:
                self.stage = 2
                self.txt.text = 'Замерьте пульс еще раз'
                self.timer.restart(15)
            elif self.stage == 2:
                self.line_2.set_disabled(False)
                self.btn_1.set_disabled(False)
                self.next_screen = True


    def next(self):
        if not self.next_screen:
            self.btn_1.set_disabled(True)
            self.timer.start()
        else:
            global p2, p3
            p2 = check_exc(self.line_1.text)
            p3 = check_exc(self.line_2.text)
            if p2 == False or p2 < 0:
                self.popup_1.open()
                p2 = 0
                self.line_1.text = str(p2)
            elif p3 == False or p3 < 0:
                self.popup_2.open()
                p3 = 0
                self.line_2.text = str(p3)
            else:
                self.manager.transition.direction = 'left'
                self.manager.current = 'fourth'
    
    def back(self):
        self.manager.transition.direction = 'right'
        self.manager.current = self.manager.previous()

class ShowResult(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        out = BoxLayout(orientation = 'vertical', padding = 10, spacing = 10)
        self.instr = Label(text = '',markup = True, font_size = '22sp',
                           color = (120/255, 100/255, 140/255, 1))
        self.on_enter = self.next
        out.add_widget(self.instr)
        self.add_widget(out)

    def next(self):
        if name == '':
            self.instr.text = test(p1, p2, p3, age, name)
        else:
            self.instr.text = name + ', '+ test(p1, p2, p3, age, name)

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(IntroScreen(name = 'main'))
        sm.add_widget(FirstResult(name = 'first'))
        sm.add_widget(TextRest(name = 'second'))
        sm.add_widget(FinalResult(name = 'third'))
        sm.add_widget(ShowResult(name = 'fourth'))
        return sm
app = MyApp()
app.run()






































