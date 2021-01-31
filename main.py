import tkinter, os
from files import files  # for our file manipulation functions
from PIL import Image, ImageTk

class Application(tkinter.Frame):
    f = files()  # create our files object
    f.load_imageNames()  # use its load_imageNames function to scan current directory for images
    n = 0

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.master.title("Image Sort")
        self.master.geometry("750x700")
        self.create_widgets()

    def create_widgets(self):  # function that creates most of the elements in our main window

        self.imageframe = tkinter.Frame(self, width=400, height=400)  # main frame for images
        self.imageframe.pack(side="top",  padx=50, pady=25)
        self.load_image()

        self.buttonframe = tkinter.Frame(self, width=800, height=50)  # frame so that buttons are inline and nicely placed after the main frame
        self.buttonframe.pack(padx=50, pady=50)

        self.image1 = tkinter.Button(self.buttonframe, text="Folder 1", fg="grey", width = 8, command=lambda: self.selection_button(1))
        self.image1.pack(side="left", padx=100)

        self.image2 = tkinter.Button(self.buttonframe, text="Folder 2", fg="grey", width = 8, command=lambda: self.selection_button(2))
        self.image2.pack(side="right", padx=100)

        self.quit = tkinter.Button(self, text="Quit", fg="grey", width = 5,
                              command=self.master.destroy )
        self.quit.pack(side="bottom", pady=25)

    def load_image(self):  # function that calls a files member function, and creates an image within a label

        img = Image.open(os.getcwd() + "/imageSet/" + self.f.get_imageName(self.n))
        img = img.resize((300, 250), Image.ANTIALIAS)  # this won't work with all images but for the most part they don't look too bad
        img = ImageTk.PhotoImage(img)
        self.imagepanel = tkinter.Label(self.imageframe, image=img, width=400, height=400)  # label to store the image
        self.imagepanel.image = img
        self.imagepanel.pack()

    def selection_button(self, s):  # finally our button functions, that store our files given the selection
        self.f.store_image(self.f.get_imageName(self.n), s)  # we're still on n = 0 , so store right away
        self.n += 1  # we're retrieving file names that are stored in an array in files class

        if self.n > self.f.get_arraySize() - 1:  # notify that there are no more images once array is done
            print("in here")
            self.imagepanel.destroy()
            self.finalText = tkinter.Label(self.imageframe, text="No more images left to read.")
            self.finalText.place(x=100, y=150)
            return None

        self.imagepanel.destroy()  # otherwise we would create a column of images
        self.load_image()



root = tkinter.Tk()
app = Application(master=root)
app.mainloop()
