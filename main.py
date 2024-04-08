import os
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox
from PIL import Image
from time import time

class ImageResizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Resizer")

        self.input_folder_label = Label(root, text="Input Folder:")
        self.input_folder_label.grid(row=0, column=0)
        self.input_folder_entry = Entry(root, width=25, state="readonly")
        self.input_folder_entry.grid(row=0, column=1)
        self.browse_input_button = Button(root, text="Browse", command=self.browse_input_folder)
        self.browse_input_button.grid(row=0, column=2)

        self.output_folder_label = Label(root, text="Output Folder:")
        self.output_folder_label.grid(row=1, column=0)
        self.output_folder_entry = Entry(root, width=25, state="readonly")
        self.output_folder_entry.grid(row=1, column=1)
        self.browse_output_button = Button(root, text="Browse", command=self.browse_output_folder)
        self.browse_output_button.grid(row=1, column=2)

        self.width_label = Label(root, text="Width:")
        self.width_label.grid(row=2, column=0)
        self.width_entry = Entry(root, width=10)
        self.width_entry.grid(row=2, column=1)

        self.height_label = Label(root, text="Height:")
        self.height_label.grid(row=3, column=0)
        self.height_entry = Entry(root, width=10)
        self.height_entry.grid(row=3, column=1)

        self.resize_button = Button(root, text="Resize Images", command=self.resize_images)
        self.resize_button.grid(row=4, column=0, columnspan=3)

    def browse_input_folder(self):
        input_folder = filedialog.askdirectory()
        self.input_folder_entry.config(state="normal")
        self.input_folder_entry.delete(0, "end")
        self.input_folder_entry.insert(0, input_folder)
        self.input_folder_entry.config(state="readonly")

    def browse_output_folder(self):
        output_folder = filedialog.askdirectory()
        self.output_folder_entry.config(state="normal")
        self.output_folder_entry.delete(0, "end")
        self.output_folder_entry.insert(0, output_folder)
        self.output_folder_entry.config(state="readonly")

    def resize_images(self):
        start_time = time()  # Записываем время начала выполнения функции

        input_folder = self.input_folder_entry.get()
        output_folder = self.output_folder_entry.get()
        width = int(self.width_entry.get())
        height = int(self.height_entry.get())

        for filename in os.listdir(input_folder):
            if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                input_path = os.path.join(input_folder, filename)
                img = Image.open(input_path)
                resized_img = img.resize((width, height), Image.LANCZOS)
                output_path = os.path.join(output_folder, filename)
                resized_img.save(output_path)

        end_time = time()  # Записываем время окончания выполнения функции
        elapsed_time = end_time - start_time  # Вычисляем разницу

        messagebox.showinfo("Success", f"Image resize complete!\nElapsed Time: {elapsed_time:.2f} seconds")
        #self.root.destroy()  # Закрываем окно после завершения работы

if __name__ == "__main__":
    root = Tk()
    app = ImageResizer(root)
    root.mainloop()