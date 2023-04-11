thread = None

def automation_loop():
    text = textbox.get()
    while True:
        position = pyautogui.locateOnScreen('button2.png', confidence=0.8)
        if position is not None:
            pyautogui.click(position)
            pyautogui.press('f8')
            pyautogui.typewrite("connect " + text)
            pyautogui.PAUSE = 0.5
            pyautogui.press('enter')
            pyautogui.press('f8')
            if pyautogui.locateOnScreen('Connect.png') is not None:
                print("Program stopped.")
                break
        else:
            pyautogui.press('f8')
            pyautogui.typewrite("connect " + text)
            pyautogui.PAUSE = 0.5
            pyautogui.press('enter')
            pyautogui.press('f8')
            if pyautogui.locateOnScreen('Connect.png') is not None:
                print("Program stopped.")
                break
        position = None
        thread = None



def start_button_clicked(event):
    global thread
    thread = threading.Thread(target=automation_loop)
    thread.start()

def stop_button_clicked(event):
    global thread
    if thread is not None:
        thread.join()
    thread
def paste_text(event):
    try:
        pyperclip.clear()
        text = pyperclip.paste()
        textbox.delete(0, tk.END)
        textbox.insert(0, text)
    except:
        pass

def view_program_details(event):
    messagebox.showinfo("AUTO QUEUE FIVEM | HOW TO USE", "วิธีใช้งานตัวยัดคิวออโต้\nกรอกแค่ IP ไม่ต้องใส่คำว่า Connect โปรแกรมเขียนให้เองอัตโนมัติ\n1. เปลี่ยนภาษาเป็นภาษาอังกฤษก่อนเข้าโปรแกรม\n2. ให้แคปรูป Close ใหม่ เหมือน button_2.png เพราะแต่ละคน\nใช้สีรีเฉดไม่เหมือนกัน ของผมเป็นค่า Base ไม่มีเปลี่ยนสี\n3. เมื่อกดใช้งานให้รีบสลับหน้าต่างไปทาง Fivem ให้โปรแกรมทำงาน\n4. เมื่อจะหยุดทำงานให้สลับหน้าจอมากดหยุด อย่ากดกากบาท เพื่อปิดโปรแกรม\n* หมายเหตุ โปรแกรมใช้เซฟภาพชื่อ Snipping Tool สามารถเซฟทับรูปเก่าได้ทันที่หากเปลี่ยนรูป\n* หมายเหตุ หากโปรแกรมไม่เจอรูป button_1.png โปรแกรมจะไม่ทำงาน\n* หมายเหตุ ไม่แนะนำให้พับหน้าจอระหว่างใช้งาน จนกว่าตัวเราจะหยุดใช้งานโปรแกรม") # Replace this with your desired program details

AUTO_QUEUE_FIVEM = Tk()

AUTO_QUEUE_FIVEM.geometry("682x203")
AUTO_QUEUE_FIVEM.configure(bg = "#475569")
AUTO_QUEUE_FIVEM.title('AUTO QUEUE FIVEM | TEST BETA')
urllogo = "https://cdn.discordapp.com/attachments/1095316825002217482/1095319065825910854/FiveM-Symbol_1.png"
logo = ImageTk.PhotoImage(Image.open(requests.get(urllogo, stream=True).raw))
AUTO_QUEUE_FIVEM.iconphoto(False,logo)

canvas = Canvas(AUTO_QUEUE_FIVEM,bg = "#475569",height = 203,width = 682,bd = 0,highlightthickness = 0,relief = "ridge")

canvas.place(x = 0, y = 0)

textbox = tk.Entry(AUTO_QUEUE_FIVEM)
textbox.place(x=25, y=72, width=412, height=58)
textbox.bind("<Control-v>", paste_text)

url2 = "https://cdn.discordapp.com/attachments/1095316825002217482/1095316916454817872/image_2.png"
image_image_2 = ImageTk.PhotoImage(Image.open(requests.get(url2, stream=True).raw))
image_2 = canvas.create_image(68.0,52.0,image=image_image_2)

url3 = "https://cdn.discordapp.com/attachments/1095316825002217482/1095316916685520926/image_3.png"
image_image_3 = ImageTk.PhotoImage(Image.open(requests.get(url3, stream=True).raw))
image_3 = canvas.create_image(115.0,167.0,image=image_image_3)
canvas.tag_bind(image_3, "<Button-1>", view_program_details)

url4 = "https://cdn.discordapp.com/attachments/1095316825002217482/1095316916924583998/image_4.png"
image_image_4 = ImageTk.PhotoImage(Image.open(requests.get(url4, stream=True).raw))
image_4 = canvas.create_image(555.0,63.0,image=image_image_4)
canvas.tag_bind(image_4, "<Button-1>", start_button_clicked)

url5 = "https://cdn.discordapp.com/attachments/1095316825002217482/1095316917184626688/image_5.png"
image_image_5 = ImageTk.PhotoImage(Image.open(requests.get(url5, stream=True).raw))
image_5 = canvas.create_image(555.0,150.0,image=image_image_5)
canvas.tag_bind(image_5, "<Button-1>", stop_button_clicked)

AUTO_QUEUE_FIVEM.resizable(False, False)
AUTO_QUEUE_FIVEM.mainloop()
