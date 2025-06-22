import customtkinter
import qrcode
from PIL import Image

# qrcode generator
def onclick():
    linkqrgue = inputqr.get()
    img = qrcode.make(linkqrgue)
    img.save("qris/qrcode.png")
    newimg = Image.open("qris/qrcode.png")
    my_image.configure(light_image=newimg)
    
    imageLabel = customtkinter.CTkLabel(app, image=my_image, text="")
    imageLabel.pack(padx=30, pady=30)



my_image = customtkinter.CTkImage(light_image=Image.open("qris/qrcode.png"), size=(400, 400))

# app
app = customtkinter.CTk()
app.geometry("720x720")
app.title("qrcode by qihh")

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")


# label
label = customtkinter.CTkLabel(app, text="selamat datang di qrcode ku")
label.pack(padx=20, pady=20)

# input link
inputqr = customtkinter.CTkEntry(app, width=500, height=30, placeholder_text="input here")
inputqr.pack(padx=30, pady=30)

# button
button = customtkinter.CTkButton(app, width=50, height=20, text="Download", command=onclick)
button.pack(padx=20, pady=20)



# running qrcode
app.mainloop() 
