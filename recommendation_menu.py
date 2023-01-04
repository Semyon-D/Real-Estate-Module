import tkinter as tk

def get_output(param1, param2, param3):
    output = ''
    if param1 == 'A':
        output += 'Option A selected. '
    elif param1 == 'B':
        output += 'Option B selected. '
    else:
        output += 'Invalid option. '

    if param2 == 'X':
        output += 'Option X selected. '
    elif param2 == 'Y':
        output += 'Option Y selected. '
    else:
        output += 'Invalid option. '

    if param3 == 'True':
        output += 'Option True selected.'
    elif param3 == 'False':
        output += 'Option False selected.'
    else:
        output += 'Invalid option.'

    return output

class RecommendationMenu(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        # Create the recommendation drop-down menus
        self.param1 = tk.StringVar(self, 'A')
        self.menu1 = tk.OptionMenu(self, self.param1, 'A', 'B')
        self.menu1.pack(side='left', padx=(0, 5))
        self.param2 = tk.StringVar(self, 'X')
        self.menu2 = tk.OptionMenu(self, self.param2, 'X', 'Y')
        self.menu2.pack(side='left', padx=(0, 5))
        self.param3 = tk.StringVar(self, 'True')
        self.menu3 = tk.OptionMenu(self, self.param3, 'True', 'False')
        self.menu3.pack(side='left', padx=(0, 5))

        # Create the get output button
        self.button = tk.Button(self, text='Get Output', command=self.on_get_output)
        self.button.pack(side='left')

    def on_get_output(self):
        # Get the selected options from the drop-down menus
        param1 = self.param1.get()
        param2 = self.param2.get()
        param3 = self.param3.get()

        # Get the output based on the selected options
        output = get_output(param1, param2, param3)
        print(output)

if __name__ == '__main__':
    root = tk.Tk()
    recommendation_menu = RecommendationMenu(root)
    recommendation_menu.pack()
    tk.mainloop()
