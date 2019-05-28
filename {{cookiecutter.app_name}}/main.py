from kivy.app import App
from kivy.lang import Builder

from kivymd.theming import ThemeManager


{{cookiecutter.app_name}} = '''
#:import MDLabel kivymd.label.MDLabel

#:import MDRoundFlatIconButton kivymd.button.MDRoundFlatIconButton
MDRoundFlatIconButton:
        text: "PYTHON"
        icon: "language-python"
        pos_hint: {'center_x': .5, 'center_y': .5}
        width: dp(200)
'''

class {{cookiecutter.app_name}}App(App):
    def build(self):
        
        self.theme_cls = ThemeManager()
        self.theme_cls.primary_palette = "{{cookiecutter.primary_palette}}"
        self.theme_cls.accent_palette = "{{cookiecutter.accent_palette}}"
        self.theme_cls.theme_style = "{{cookiecutter.theme_style}}"
        
        main_widget = Builder.load_string({{cookiecutter.app_name}})
        
        return main_widget

if __name__ == '__main__':
    {{cookiecutter.app_name}}App().run()
