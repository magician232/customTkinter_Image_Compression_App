import customtkinter
from tkinter import filedialog
import os
from PIL import Image

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("450x400")
app.title("Image Compressor")

header_label = customtkinter.CTkLabel(master=app, text='Welcome to Image Compressor', font=(None, 24))
header_label.pack(pady=20)

def get_size_format(size):
    # Helper function to convert size in bytes to a human-readable format
    # For example, converts 1024 bytes to "1 KB"
    # You can customize the implementation based on your preferences
    
    # List of possible units in descending order
    units = ["B", "KB", "MB", "GB", "TB"]
    unit_index = 0
    
    while size >= 1024 and unit_index < len(units) - 1:
        # Increase the unit size until the size is smaller than 1024
        size /= 1024
        unit_index += 1
    
    # Format the size with two decimal places
    size_formatted = "{:.2f}".format(size)
    
    return f"{size_formatted} {units[unit_index]}"


def compress_img(image_name, size_reduction_percentage=20, quality=80, to_jpg=True):
    # load the image to memory
    img = Image.open(image_name)
    
    # Get the original image size in bytes
    original_size = os.path.getsize(image_name)
    
    # Calculate the desired compressed size in bytes based on the user-defined percentage
    desired_size = original_size * (size_reduction_percentage / 100)
    
    # Calculate the resizing ratio to achieve the desired compressed size
    resizing_ratio = (desired_size / original_size) ** 0.5
    
   
    
    # Resize the image with the resizing ratio
    img = img.resize((int(img.size[0] * resizing_ratio), int(img.size[1] * resizing_ratio)))
    
    # Split the filename and extension
    filename, ext = os.path.splitext(image_name)
    
    # Create the new filename
    if to_jpg:
        new_filename = f"{filename}_compressed.jpg"
    else:
        new_filename = f"{filename}_compressed{ext}"
    
    try:
        # Save the image with the specified quality and optimization settings
        img.save(new_filename, quality=quality, optimize=True)
    except OSError:
        img = img.convert("RGB")
        img.save(new_filename, quality=quality, optimize=True)
    
    # Get the new image size in bytes
    new_size = os.path.getsize(new_filename)
    
    # Print the original size, the new size, and the compression ratio
    # print("Original Size:", get_size_format(original_size))
    # print("New Size:", get_size_format(new_size))
    # print("Compression Ratio:", new_size / original_size * 100)
    compressed_file_label.configure(text="Saveded File: " +os.path.basename(new_filename) +f"  {get_size_format(new_size)}")



def destroy_button():
    app.destroy()


def selectFile_button_pressed():
    image_path = filedialog.askopenfilename(
        initialdir=os.getcwd(),  # Set the initial directory
        title="Select Image File",
        filetypes=(("Image Files", "*.png;*.jpg;*.jpeg"), ("All Files", "*.*"))  # Specify the file types to display
    )
    if image_path:
        org_size = os.path.getsize(image_path)
        selected_file_label.configure(text="Selected File: " + os.path.basename(image_path)+f"  {get_size_format(org_size)}")
        compress_button.configure(command=lambda: compress_button_pressed(image_path, compression_level.get()))


def compress_button_pressed(image_path, compression_level):
    # print("Selected Image File:", image_path)
    # print("Compression Level:", compression_level)
    if(compression_level=="High Compression"):
        compress_img(image_path, size_reduction_percentage=20, quality=80)
    elif(compression_level=="Medium Compression"):
        compress_img(image_path, size_reduction_percentage=50, quality=80)
    elif((compression_level=="Low Compression")):
        compress_img(image_path, size_reduction_percentage=80, quality=80)
    
    


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=10, padx=40, fill="both", expand=True)

compression_level = customtkinter.StringVar()  # Variable to store the chosen option

button_0 = customtkinter.CTkButton(master=frame_1, text="Select File", command=selectFile_button_pressed)
button_0.pack(pady=10, padx=10)

selected_file_label = customtkinter.CTkLabel(master=frame_1, text="Selected File: ")
selected_file_label.pack(pady=10, padx=10)

optionmenu_1 = customtkinter.CTkOptionMenu(frame_1, values=["High Compression", "Medium Compression", "Low Compression", "No Compression"])
optionmenu_1.pack(pady=10, padx=10)
# optionmenu_1.set("Compression Level")
optionmenu_1.configure(variable=compression_level)
optionmenu_1.set("Compression Level")

compress_button = customtkinter.CTkButton(master=frame_1, text="Compress")
compress_button.pack(pady=10, padx=10)

compressed_file_label = customtkinter.CTkLabel(master=frame_1, text="")
compressed_file_label.pack(pady=10, padx=10)

button_2 = customtkinter.CTkButton(master=frame_1, text="Close", command=destroy_button)
button_2.pack(pady=10, padx=10)

app.mainloop()
