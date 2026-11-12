from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
import math

Window.clearcolor = get_color_from_hex("#071426")

class NeamKhan(App):
    def build(self):
        self.history = []
        root = BoxLayout(orientation="vertical", padding=15, spacing=12)

        title = Label(
            text="[b]NEAM KHAN[/b]\n[color=39A9FF]PREMIUM CALCULATOR[/color]",
            markup=True, font_size=25, size_hint_y=.20
        )
        root.add_widget(title)

        self.mode = Spinner(
            text="Scientific Calculator",
            values=("Scientific Calculator", "Financial Calculator",
                    "Unit Converter", "Currency Converter"),
            size_hint_y=.12
        )
        root.add_widget(self.mode)

        self.first = TextInput(
            hint_text="প্রথম সংখ্যা / First value",
            multiline=False, font_size=22, size_hint_y=.14
        )
        root.add_widget(self.first)

        self.second = TextInput(
            hint_text="দ্বিতীয় সংখ্যা / Second value",
            multiline=False, font_size=22, size_hint_y=.14
        )
        root.add_widget(self.second)

        self.operation = Spinner(
            text="+",
            values=("+", "-", "*", "/", "%", "sin", "cos", "tan",
                    "sqrt", "log", "Simple Interest", "USD to BDT",
                    "BDT to USD", "KM to Meter", "KG to Gram"),
            size_hint_y=.12
        )
        root.add_widget(self.operation)

        btn = Button(
            text="CALCULATE",
            background_color=get_color_from_hex("#087DFF"),
            font_size=22, size_hint_y=.13
        )
        btn.bind(on_press=self.calculate)
        root.add_widget(btn)

        self.result = Label(
            text="Result will appear here",
            font_size=21, size_hint_y=.15
        )
        root.add_widget(self.result)

        hist = Button(text="Show History", size_hint_y=.10)
        hist.bind(on_press=self.show_history)
        root.add_widget(hist)

        return root

    def calculate(self, instance):
        try:
            a = float(self.first.text)
            b = float(self.second.text or "0")
            op = self.operation.text

            if op == "+":
                ans = a + b
            elif op == "-":
                ans = a - b
            elif op == "*":
                ans = a * b
            elif op == "/":
                if b == 0:
                    raise ValueError("Cannot divide by zero")
                ans = a / b
            elif op == "%":
                ans = a % b
            elif op == "sin":
                ans = math.sin(math.radians(a))
            elif op == "cos":
                ans = math.cos(math.radians(a))
            elif op == "tan":
                ans = math.tan(math.radians(a))
            elif op == "sqrt":
                ans = math.sqrt(a)
            elif op == "log":
                ans = math.log10(a)
            elif op == "Simple Interest":
                ans = a * b / 100
            elif op == "USD to BDT":
                ans = a * b
            elif op == "BDT to USD":
                if b == 0:
                    raise ValueError("Rate cannot be zero")
                ans = a / b
            elif op == "KM to Meter":
                ans = a * 1000
            elif op == "KG to Gram":
                ans = a * 1000
            else:
                ans = "Invalid operation"

            output = f"Result: {ans}"
            self.result.text = output
            self.history.append(output)

        except Exception as e:
            self.result.text = "Error: " + str(e)

    def show_history(self, instance):
        self.result.text = "\n".join(self.history[-5:]) or "No history yet"

NeamKhan().run()
0

