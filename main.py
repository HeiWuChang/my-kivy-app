from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MySimpleApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        title = Label(text='我的第一个安卓App', font_size='24sp', bold=True)
        
        # 创建一个按钮
        action_button = Button(
            text='点我一下', 
            font_size='20sp',
            background_color=(0.1, 0.5, 0.8, 1), # 设置按钮颜色
            size_hint=(1, 0.5) # 宽度占满，高度占一半空间
        )
        # 绑定按钮的点击事件
        action_button.bind(on_press=self.on_button_click)
        
        layout.add_widget(title)
        layout.add_widget(action_button)
        
        return layout

    def on_button_click(self, instance):
        # 当按钮被点击时，改变它的文字
        instance.text = '你点击了我！'
        print("按钮被成功点击！")

if __name__ == '__main__':
    MySimpleApp().run()