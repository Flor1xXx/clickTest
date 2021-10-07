from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from time import sleep




        # объявление переменных
count = 0
check = 0
t = 4
timer_continue = 0



Builder.load_string('''
<MenuScreen>:

    FloatLayout:

        Screen:
            Image:
                id: fon
                source: 'fon2.png'
                keep_ratio: False
                allow_stretch: True
                opacity: 0.8
                size: self.size
                pos: self.pos


        Screen:
            Image:
                id: podText
                source: 'text.png'
                keep_ratio: False
                allow_stretch: True
                opacity: 1
                size: self.size
                pos: self.pos


        Screen:
            Image:
            	id: btnPNG
                source: 'btn.png'
                keep_ratio: False
                allow_stretch: True
                # opacity: 0.8
                size: self.size
                pos: self.pos



        

        Label:

            id: hello
            font_size: 70
            font_name: 'Raleway-Regular.ttf'
            pos_hint: {'center_x':0.5, 'center_y':0.95}
            text: 'выберите время:'





        Label:
        	id: lbSwitch
        	font_size: 20
        	text: "Dark mode"
        	pos_hint: {'center_x':0.05, 'center_y':0.95}


        Switch:
        	id: switch
        	pos_hint: {'center_x':0.05, 'center_y':0.90}
        	on_active: root.dark_mode()





        Label:

            id: start
            font_size: 90
            color: rgba(255,255,255)
            font_name: 'Oswald-Bold.ttf'
            pos_hint: {'center_x':0.5, 'center_y':0.21}
            text: 'СТАРТ'



        Button:
            id: btnStart
            text: ''
            pos_hint: {'center_x': 0.5, 'center_y': 0.22}
            size_hint_y: .37
            opacity: 0
            on_press: root.interval()





        ToggleButton:

            id: sec3
            font_size: 70
            size_hint_y: .1
            size_hint_x: .3
            pos_hint:{'center_x': 0.5, 'center_y': 0.8}
            opacity: 0
            group: 'g1'

            on_press: root.on_click_color()

        Label:

            id: sec3label
            text: '3 sec'
            font_size: 70
            font_name: 'Raleway-SemiBold.ttf'
            color: rgba(1,1,1)
            size_hint_y: .1
            size_hint_x: .1
            pos_hint:{'center_x': 0.5, 'center_y': 0.8}






        ToggleButton:

            id: sec5
            font_size: 70
            size_hint_y: .1
            size_hint_x: .3
            pos_hint:{'center_x': 0.5, 'center_y': 0.7}
            opacity: 0
            group: 'g1'

            on_press: root.on_click_color()


        Label:

            id: sec5label
            text: '5 sec'
            font_size: 70
            font_name: 'Raleway-SemiBold.ttf'
            color: rgba(1,1,1)
            size_hint_y: .1
            size_hint_x: .1
            pos_hint:{'center_x': 0.5, 'center_y': 0.7}






        ToggleButton:

            id: sec10
            font_size: 70
            size_hint_y: .1
            size_hint_x: .3
            pos_hint:{'center_x': 0.5, 'center_y': 0.6}
            opacity: 0
            group: 'g1'

            on_press: root.on_click_color()


        Label:

            id: sec10label
            text: '10 sec'
            font_size: 70
            font_name: 'Raleway-SemiBold.ttf'
            color: rgba(1,1,1)
            size_hint_y: .1
            size_hint_x: .1
            pos_hint:{'center_x': 0.5, 'center_y': 0.6}









        ToggleButton:

            id: sec30
            font_size: 70
            size_hint_y: .1
            size_hint_x: .3
            pos_hint:{'center_x': 0.5, 'center_y': 0.5}
            opacity: 0
            group: 'g1'

            on_press: root.on_click_color()

        Label:

            id: sec30label
            text: '30 sec'
            font_size: 70
            font_name: 'Raleway-SemiBold.ttf'
            color: rgba(1,1,1)
            size_hint_y: .1
            size_hint_x: .1
            pos_hint:{'center_x': 0.5, 'center_y': 0.5}









        Label:
            id: timer
            color: 'black'
            font_size: 70
            font_name: 'Oswald-Bold.ttf'
            pos_hint: {'center_x':0.5, 'center_y':0.75}
            text: '0'
            opacity: 0


        Label:
            id: clicks
            color: 'black'
            font_size: 70
            font_name: 'Raleway-Regular.ttf'
            pos_hint: {'center_x':0.5, 'center_y':0.6}
            text: '0'
            opacity: 0






                    ''')


class MenuScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)




    def interval(self):
        global check
        if(check==0):
            
            if self.ids.sec3.state == 'down' or self.ids.sec5.state == 'down' or self.ids.sec10.state == 'down' or self.ids.sec30.state == 'down':
                Clock.schedule_interval(self.timer, 1)
                check=check+1

            else:
                # self.ids.hello.text = 'вы не выбрали время!'
                pass





    def timer(self, dt):
        global t
        global check
        global count
        global timer_continue



                                            # начало таймера, если 3sec
        if self.ids.sec3.state == 'down':


            if t > 0 and check < 3 and timer_continue == 0:      
                t=t-1                       #обратный таймер
                self.ids.timer.text=str(t)

                self.ids.hello.text = 'время/счёт'


                self.ids.sec3.disabled = True
                self.ids.sec3label.opacity = 0


                self.ids.sec5.disabled = True
                self.ids.sec5label.opacity = 0

                self.ids.sec10.disabled = True
                self.ids.sec10label.opacity = 0


                self.ids.sec30.disabled = True
                self.ids.sec30label.opacity = 0


                self.ids.timer.opacity = 1

                self.ids.clicks.opacity = 1



            elif t >= 0 and t < 3 and timer_continue >= 0:

                t = t+1
                timer_continue += 1

                self.ids.timer.text = str(t)
                self.ids.start.text = 'ЖМИ!'
                self.ids.btnStart.on_press = self.on_fast_click


                

            else:
                self.ids.hello.text = 'Результат за 3 секунды -' + str(count)



                self.ids.sec3.disabled = False
                self.ids.sec3label.opacity = 1


                self.ids.sec5.disabled = False
                self.ids.sec5label.opacity = 1

                self.ids.sec10.disabled = False
                self.ids.sec10label.opacity = 1


                self.ids.sec30.disabled = False
                self.ids.sec30label.opacity = 1


                self.ids.timer.opacity = 0

                self.ids.clicks.opacity = 0



                Clock.unschedule(self.timer)
                self.ids.btnStart.on_press = self.interval
                self.ids.clicks.text = '0'
                self.ids.start.text = 'СТАРТ'
                self.ids.sec3.state = 'normal'
                self.ids.sec3label.color = (0,0,0) 


                count = 0
                check = 0
                t = 4
                timer_continue = 0








                                                    # начало таймера, если 5sec
        elif self.ids.sec5.state == 'down':


            if t > 0 and check < 5 and timer_continue == 0:      
                t=t-1                       #обратный таймер
                self.ids.timer.text=str(t)

                self.ids.hello.text = 'время/счёт'


                self.ids.sec3.disabled = True
                self.ids.sec3label.opacity = 0


                self.ids.sec5.disabled = True
                self.ids.sec5label.opacity = 0

                self.ids.sec10.disabled = True
                self.ids.sec10label.opacity = 0


                self.ids.sec30.disabled = True
                self.ids.sec30label.opacity = 0


                self.ids.timer.opacity = 1

                self.ids.clicks.opacity = 1



            elif t >= 0 and t < 5 and timer_continue >= 0:

                t = t+1
                timer_continue += 1

                self.ids.timer.text = str(t)
                self.ids.start.text = 'ЖМИ!'
                self.ids.btnStart.on_press = self.on_fast_click


                

            else:
                self.ids.hello.text = 'Результат за 5 секунд- ' + str(count)



                self.ids.sec3.disabled = False
                self.ids.sec3label.opacity = 1


                self.ids.sec5.disabled = False
                self.ids.sec5label.opacity = 1

                self.ids.sec10.disabled = False
                self.ids.sec10label.opacity = 1


                self.ids.sec30.disabled = False
                self.ids.sec30label.opacity = 1


                self.ids.timer.opacity = 0

                self.ids.clicks.opacity = 0



                Clock.unschedule(self.timer)
                self.ids.btnStart.on_press = self.interval
                self.ids.clicks.text = '0'
                self.ids.start.text = 'СТАРТ'
                self.ids.sec5.state = 'normal'
                self.ids.sec5label.color = (0,0,0) 


                count = 0
                check = 0
                t = 4
                timer_continue = 0








                                                    # начало таймера, если 10sec
        elif self.ids.sec10.state == 'down':


            if t > 0 and check < 10 and timer_continue == 0:      
                t=t-1                       #обратный таймер
                self.ids.timer.text=str(t)

                self.ids.hello.text = 'время/счёт'


                self.ids.sec3.disabled = True
                self.ids.sec3label.opacity = 0


                self.ids.sec5.disabled = True
                self.ids.sec5label.opacity = 0

                self.ids.sec10.disabled = True
                self.ids.sec10label.opacity = 0


                self.ids.sec30.disabled = True
                self.ids.sec30label.opacity = 0


                self.ids.timer.opacity = 1

                self.ids.clicks.opacity = 1



            elif t >= 0 and t < 10 and timer_continue >= 0:

                t = t+1
                timer_continue += 1

                self.ids.timer.text = str(t)
                self.ids.start.text = 'ЖМИ!'
                self.ids.btnStart.on_press = self.on_fast_click


                

            else:
                self.ids.hello.text = 'Результат за 10 секунд- ' + str(count)



                self.ids.sec3.disabled = False
                self.ids.sec3label.opacity = 1


                self.ids.sec5.disabled = False
                self.ids.sec5label.opacity = 1

                self.ids.sec10.disabled = False
                self.ids.sec10label.opacity = 1


                self.ids.sec30.disabled = False
                self.ids.sec30label.opacity = 1


                self.ids.timer.opacity = 0

                self.ids.clicks.opacity = 0



                Clock.unschedule(self.timer)
                self.ids.btnStart.on_press = self.interval
                self.ids.clicks.text = '0'
                self.ids.start.text = 'СТАРТ'
                self.ids.sec10.state = 'normal'
                self.ids.sec10label.color = (0,0,0) 


                count = 0
                check = 0
                t = 4
                timer_continue = 0










                                                    # начало таймера, если 30sec

        elif self.ids.sec30.state == 'down':


            if t > 0 and check < 30 and timer_continue == 0:      
                t=t-1                       #обратный таймер
                self.ids.timer.text=str(t)

                self.ids.hello.text = 'время/счёт'


                self.ids.sec3.disabled = True
                self.ids.sec3label.opacity = 0


                self.ids.sec5.disabled = True
                self.ids.sec5label.opacity = 0

                self.ids.sec10.disabled = True
                self.ids.sec10label.opacity = 0


                self.ids.sec30.disabled = True
                self.ids.sec30label.opacity = 0


                self.ids.timer.opacity = 1

                self.ids.clicks.opacity = 1



            elif t >= 0 and t < 30 and timer_continue >= 0:

                t = t+1
                timer_continue += 1

                self.ids.timer.text = str(t)
                self.ids.start.text = 'ЖМИ!'
                self.ids.btnStart.on_press = self.on_fast_click


                

            else:
                self.ids.hello.text = 'Результат за 30 секунд - ' + str(count)



                self.ids.sec3.disabled = False
                self.ids.sec3label.opacity = 1


                self.ids.sec5.disabled = False
                self.ids.sec5label.opacity = 1

                self.ids.sec10.disabled = False
                self.ids.sec10label.opacity = 1


                self.ids.sec30.disabled = False
                self.ids.sec30label.opacity = 1


                self.ids.timer.opacity = 0

                self.ids.clicks.opacity = 0



                Clock.unschedule(self.timer)
                self.ids.btnStart.on_press = self.interval
                self.ids.clicks.text = '0'
                self.ids.start.text = 'СТАРТ'
                self.ids.sec30.state = 'normal'
                self.ids.sec30label.color = (0,0,0) 


                count = 0
                check = 0
                t = 4
                timer_continue = 0










    def on_click_color(self):                   #изменение цветов выбранного режима
        if self.ids.sec3.state == 'down':
            self.ids.sec3label.color = (54,175,197) 
                                                         #3секунды
        else:
            self.ids.sec3label.color = 'black'


        if  self.ids.sec5.state == 'down':            #5секунд
            self.ids.sec5label.color = (15,139,216)
        else:
            self.ids.sec5label.color = 'black'


        if self.ids.sec10.state == 'down':              #10секунд
            self.ids.sec10label.color = (75,179,102)
        else:
            self.ids.sec10label.color = 'black'


        if self.ids.sec30.state == 'down':              #30секунд
            self.ids.sec30label.color = (92,54,205)
        else:
            self.ids.sec30label.color = 'black'




                





    def on_fast_click(self):       #счетчик кликов
        global count
        count += 1
        self.ids.clicks.text = str(count)




    def dark_mode(self):
    	if self.ids.switch.active == True:
    		self.ids.fon.source = 'fonblack.png'
    		self.ids.podText.source = 'blackText.png'
    		self.ids.btnPNG.source = 'blackButton.png'
    		self.ids.sec3label.color = 'white'
    		self.ids.sec5label.color = 'white'
    		self.ids.sec10label.color = 'white'
    		self.ids.sec30label.color = 'white'
    	else:
    		self.ids.fon.source = 'fon2.png'
    		self.ids.podText.source = 'text.png'
    		self.ids.btnPNG.source = 'btn.png'
    		self.ids.sec3label.color = 'black'
    		self.ids.sec5label.color = 'black'
    		self.ids.sec10label.color = 'black'
    		self.ids.sec30label.color = 'black'


                                #присваиваем переменной класс ScreenManager() и добавляем наш класс MenuScreen
sm = ScreenManager()
menu_screen = MenuScreen(name='menu')
sm.add_widget(menu_screen)





                            # функция запуска
class TestApp(App):

    def build(self):

        return sm


if __name__ == '__main__':             #запуск приложения
    TestApp().run()