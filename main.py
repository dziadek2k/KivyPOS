from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.lang import Builder
from jnius import autoclass

Builder.load_file('testdrive.kv')


class Demo(GridLayout):

    def do_print_action(self):
        print('My button <%s> state is ' % (self))
        Stack = autoclass('java.util.Stack')
        stack = Stack()
        stack.push('hello')
        stack.push('world')

        print stack.pop() # --> 'world'
        print stack.pop() # --> 'hello'


    def do_scanner_action(self):
        print('My button <%s> state is <%s>' % (self))

    def do_moneybox_action(self, args):
        print('My button <%s> state is <%s>' % (self, args))







class DemoApp(App):
    def build(self):
        return Demo()




if __name__ == '__main__':
    DemoApp().run()
