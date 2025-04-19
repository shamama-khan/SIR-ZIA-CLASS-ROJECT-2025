import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
import cv2
from PIL import Image, ImageTk

# QR Encoder Function
def generate_qr():
    data = entry_data.get()
    if data == "":
        messagebox.showwarning("Input Required", "Please enter some data.")
        return
    qr = qrcode.make(data)
    qr.save("my_qr.png")
    img = ImageTk.PhotoImage(Image.open("my_qr.png").resize((200, 200)))
    qr_label.config(image=img)
    qr_label.image = img
    messagebox.showinfo("QR Code", "QR Code generated and saved as 'my_qr.png'.")

# QR Decoder Function
def decode_qr():
    file_path = filedialog.askopenfilename(title="Select QR Code Image",
                                           filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        img = cv2.imread(file_path)
        detector = cv2.QRCodeDetector()
        data, points, _ = detector.detectAndDecode(img)
        if data:
            messagebox.showinfo("Decoded Data", f"QR Code contains:\n\n{data}")
        else:
            messagebox.showerror("Error", "No QR Code found in the image.")

# GUI setup
root = tk.Tk()
root.title("QR Code Encoder / Decoder")
root.geometry("400x450")
root.config(bg="#f0f0f0")

title = tk.Label(root, text="QR Code Generator & Decoder", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
title.pack(pady=10)

entry_data = tk.Entry(root, width=40, font=("Helvetica", 12))
entry_data.pack(pady=10)

generate_btn = tk.Button(root, text="Generate QR Code", command=generate_qr, bg="#4CAF50", fg="white", font=("Helvetica", 12))
generate_btn.pack(pady=5)

decode_btn = tk.Button(root, text="Decode QR from Image", command=decode_qr, bg="#2196F3", fg="white", font=("Helvetica", 12))
decode_btn.pack(pady=5)

qr_label = tk.Label(root, bg="#f0f0f0")
qr_label.pack(pady=20)

root.mainloop()
