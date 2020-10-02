# import kivy module
import kivy
kivy.require("1.9.1")


from kivy.app import App
from kivy.uix.button import Button


# class in which we are creating the button
class ButtonApp(App):

    def build(self):
        # use a (r, g, b, a) tuple
        btn = Button(text="Click Me To\n Create Jupyter Notebook",
                     font_size="20sp",
                     background_color=(1, 1, 1, 1),
                     color=(1, 1, 1, 1),
                     size=(50, 50),
                     size_hint=(.3, .3),
                     pos=(300, 250))


        # bind() use to bind the button to function callback
        btn.bind(on_press=self.callback)
        return btn




    # callback function tells when button pressed
    def callback(self, event):
        import nbformat as nbf  # Create Jupyter notebook using nbformat library

        # Create Jupyter Notebook
        nb = nbf.v4.new_notebook()

        # Add Text input to Markdown Cell
        text = """\
        # My first automatic Jupyter Notebook
        This is an auto-generated notebook."""

        # Add Code to Cells
        code = """\
        import easygui 
        import csv  
        from matplotlib import pyplot as plt          
        data= open(easygui.fileopenbox(default='*.csv'))
        csv_data =csv.reader(data)
        datalines=list(csv_data)
        names = [i[0] for i in datalines]
        values = [i[1] for i in datalines]
        plt.figure(figsize=(9, 3))

        plt.subplot(131)
        plt.bar(names, values)
        plt.subplot(132)
        plt.scatter(names, values)
        plt.subplot(133)
        plt.plot(names, values)
        plt.suptitle('Categorical Plotting')
        plt.show();"""

        # Create markdown and code Cell
        nb['cells'] = [nbf.v4.new_markdown_cell(text),
                       nbf.v4.new_code_cell(code)]
        fname = 'CSV_jnb.ipynb'

        with open(fname, 'w') as f:
            nbf.write(nb, f)
    # creating the object root for ButtonApp() class


root = ButtonApp()

# run function runs the whole program
# i.e run() method which calls the target
# function passed to the constructor.
root.run()
