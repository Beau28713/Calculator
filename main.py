from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super(Calculator, self).__init__(**kwargs)
        self.orientation = "vertical"

        self.solution_output = TextInput(multiline=False, readonly=True)
        self.add_widget(self.solution_output)
        self.operations = ["=", "+", "-", "/", "C"]
        self.buttons = [
            ["1", "2", "3", "+"],
            ["4", "5", "6", "-"],
            ["7", "8", "9", "*"],
            ["0", ".", "C", "/"],
        ]

        for row in self.buttons:
            row_layout = BoxLayout()
            for lable in row:
                button = Button(
                    text=lable,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    on_press=self.on_button_press,
                )
                row_layout.add_widget(button)

            self.add_widget(row_layout)

        self.equal_button = Button(
            text="=",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            on_press=self.solution,
        )
        self.add_widget(self.equal_button)

    def on_button_press(self, instance):
        button_pressed = instance.text

        if button_pressed == "C":
            self.solution_output.text = ""
        else:
            current_text = self.solution_output.text + button_pressed

            self.solution_output.text = current_text

    def solution(self, instance):
        try:
            self.output = eval(self.solution_output.text)
            self.solution_output.text = str(self.output)
        except BaseException as error:
            error = str(error)
            if error == "invalid syntax (<string>, line 1)":
                self.solution_output.text = (
                    "First input must be a number not an operation"
                )
            elif error == "division by zero":
                self.solution_output.text = "Can Not Divide by Zero"
            else:
                self.solution_output.text = error


class MY_App(App):
    def build(self):
        return Calculator()


if __name__ == "__main__":
    MY_App().run()
