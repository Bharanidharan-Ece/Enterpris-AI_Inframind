import tkinter as tk
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk,Image
import webbrowser


def app():
    import cv2, time
    from deepface import DeepFace
    # importing source
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # opening webcam //External camera
    '''webcam = cv2.VideoCapture(0)
    address = "http://192.168.43.204:8080/video"
    webcam.open(address)'''

    # opening webcam //Internal cameraa
    webcam = cv2.VideoCapture(1)
     #checking process
    if not webcam.isOpened():
        cap = cv2.VideoCapture(0)
    if not webcam.isOpened():
        raise IOError("Cannot open webcame")


    while True:
        (rval, im) = webcam.read()
        ret, frame = webcam.read()
        result = DeepFace.analyze(frame, actions=['emotion'])
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.1, 4)

        # rectangle on face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX

        cv2.putText(frame, result['dominant_emotion'], (50, 50), font, 3, (0, 0, 255), 2, cv2.LINE_4)
        cv2.imshow('Orginal Video', frame)
        if cv2.waitKey(2) & 0xFF == ord('q'):
            break

    ''' (rval,im)= webcam.read()
        im=cv2.flip(im,1,0)
        mini = cv2.resize(im,(int(im.shape[1]/size),int(im.shape[0]/size)))
        faces= faceCascade.detectMultiScale(mini)
        ret, frame = webcam.read()
        result = DeepFace.analyze(frame, actions=['emotion'])
        mini = cv2.resize(cap,(int(cap.shape[1]/size),int(cap.shape[0]/size)))'''

    #cap.release()
    cv2.destroyAllWindows()

def Chat_bot():

    def main_display():
        global root
        root = Tk()
        root.config(bg="#941A1A")
        root.title("Login System")
        root.geometry("500x500")
        Label(root, text="Welcome to Bharani's Chat Bot", bd=10, font=('time', 15, 'bold'), relief="groove", fg="black",
              bg="#F7A200", width=200).pack()
        Label(root, text="", bg="#941A1A").pack()
        Button(root, text='Log In', height="1", width="20", bd=8, font=('arial', 12, 'bold'), relief="groove",
               fg="white",
               bg="#007BD9", command=login).pack()
        Label(root, text="", bg="#941A1A").pack()
        Button(root, text='Exit', height="1", width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
               bg="#007BD9", command=Exit).pack()
        Label(root, text="", bg="#941A1A").pack()

    # connecting to the database
    def save_data():
        Username_info = user_ID.get()
        password_info = user_password.get()
        file = open("user_info.txt", 'w')
        file.write("User_ID : ")
        file.write(Username_info)
        file.write(" , User_Password : ")
        file.write(password_info)
        user.delete(0, END)
        password.delete(0, END)
        Label(root2, text="", bg="BLACK").pack()
        Label(root2, text="Registration Complete", fg='red', bg='black', font=('arial', 12, 'bold'), command = webbrowser.open("https://www.kommunicate.io/livechat-demo?appId=28cef54df27324a0b01d2a467d5e75d02&botIds=bharani-1ywji&assignee=bharani-1ywji")).pack()

    def login():
        global root2
        root2 = Toplevel(root)
        root2.title("Account Login")
        root2.geometry("450x400")
        root2.config(bg="BLACK")

        global user_ID, user_password, user, password
        user_ID = StringVar()
        user_password = StringVar()

        Label(root2, text='Please Enter your Account Details', bd=5, font=('arial', 12, 'bold'), relief="groove",
              fg="white",
              bg="#179429", width=200).pack()

        Label(root2, text="", bg="BLACK").pack()
        Label(root2, text="Username :", fg="black", font=('arial', 12, 'bold')).pack()
        user = Entry(root2, textvariable=user_ID)
        user.pack()
        Label(root2, text="", bg="BLACK").pack()

        Label(root2, text="Password :", fg="black", font=('arial', 12, 'bold')).pack()
        password = Entry(root2, textvariable=user_password, show='*')
        password.pack()
        Label(root2, text="", bg="BLACK").pack()

        Button(root2, text="Login", bg="#007BD9", fg='white', relief="groove", font=('arial', 12, 'bold'),
               command=save_data).pack()
        Label(root2, text="")

    def Exit():
        wayOut = tkinter.messagebox.askyesno("Chat_Bot", "Do you want to exit Chat_Bot")
        if wayOut > 0:
            root.destroy()
            return
    main_display()

def Text_analyser():
    import tkinter as tk
    from textblob import TextBlob
    import matplotlib.pyplot as plt
    import matplotlib.animation as ani

    def Exit():
        wayOut = tkinter.messagebox.askyesno("Text Analyser", "Do you want to exit Text Analyser")
        if wayOut > 0:
            root3.destroy()
            return

    def plotting():
        global count
        x, y = [], []

        def draw(i):
            xs = p
            ys = int(p * 10)
            x.append(xs)
            y.append(ys)
            plt.cla()
            plt.scatter(x, y)
            plt.plot(x, y)
            ys += 1

        animate = ani.FuncAnimation(plt.gcf(), draw, interval=1000)
        plt.show()

    def myclick():
        global p
        data = e.get()
        blob = TextBlob(data)
        blob.tags
        blob.noun_phrases
        for sentence in blob.sentences:
            p = (sentence.sentiment.polarity)

        if p > 0:
            root3.config(bg="green")
            Label(root3, text="", bg="green").pack()
            Label(root3, text="Positive: ", fg='red', bg='black', font=('arial', 12, 'bold')).pack()
            Label(root3, text=p, fg='red', bg='black', font=('arial', 12, 'bold')).pack()


        elif p == 0:
            root3.config(bg="grey")
            Label(root3, text="", bg="grey").pack()
            Label(root3, text="Neutral: ", fg='red', bg='black', font=('arial', 12, 'bold')).pack()
            Label(root3, text=p, fg='red', bg='black', font=('arial', 12, 'bold')).pack()

        else:
            root3.config(bg="red")
            Label(root3, text="", bg="red").pack()
            Label(root3, text="Negative: ", fg='Green', bg='black', font=('arial', 12, 'bold')).pack()
            Label(root3, text=p, fg='red', bg='black', font=('arial', 12, 'bold')).pack()

        plotting()

    global root3
    root3 = tk.Tk()
    root3.title("Text Analyser")
    canvas = tk.Canvas(root3, height=500, width=550, bg="#FF5733")
    canvas.pack()
    e = Entry(root3, width=50)
    e.place(x=150, y=30)

    button = Button(root3, text='Enter text for Analysis', font="times 10 ", bd=5,command = myclick )
    button.place(x=240, y=60)
    Exit = Button(root3, text='Exit', bg="#Ab3456", fg='black', bd=10, width=15, font="times 10 bold", command=Exit)
    Exit.place(x=420, y=460)
    root3.mainloop()

def main_page():
    def Exit():
        wayOut = tkinter.messagebox.askyesno("Entrapise AI", "Do you want to exit the system")
        if wayOut > 0:
            root.destroy()
            return

    root = tk.Tk()
    root.title('Entrapise AI')
    canvas= tk.Canvas(root,height=800,width=950,bg="#007BD9")#600 550
    label= Label(root,text='Enterprise AI',bg='#22222d',fg='white',font="ar 15 bold italic").pack(fill=BOTH)
    canvas.pack()
    #Buttons
    chat = Button(root, text='ChatBot',bg="yellow",fg='black',bd=10 ,width=15,font=("times 10 bold"),command = Chat_bot)
    chat.place(x=420,y=140)
    face = Button(root, text='Facial App',bg="yellow",fg='black',bd=10 ,width=15,font="times 10 bold",command= app)
    face.place(x=420,y=200)
    text = Button(root, text='Text Analyser', bg="yellow", fg='black', bd=10, width=15, font=("times 10 bold"),
                  command=Text_analyser)
    text.place(x=420, y=260)
    Exit = Button(root, text='Exit',bg="black",fg='white',bd=10 ,width=15,font="times 10 bold",command= Exit)
    Exit.place(x=820,y=580)
    root.mainloop()

main_page()