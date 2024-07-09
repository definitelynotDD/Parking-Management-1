from tkinter import *
from tkinter import messagebox
from tkinter import Tk, Label, Button
from vehicle_plate_scanner import scan_vehicle_number
import cv2
import pytesseract


users = {}

def Base_Page():
    global root
    root = Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))

    # Add padding to the root window to center the content
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(4, weight=1)
    root.grid_columnconfigure(3, weight=1)
    root.grid_propagate(False)

    PMS = Label(root, text="ParkEase", font=("Helvetica", 62))
    PMS.grid(row=1, column=1, columnspan=2, pady=50)

    icon1 = PhotoImage(file="Login.png")
    Log = Label(root, image=icon1)
    Login_Button = Button(root, text="Login", font=("Times New Roman", 32), bd=3, command=Login_Page)

    icon2 = PhotoImage(file="NewUser.png")
    NUsr = Label(root, image=icon2)
    NewUser_Button = Button(root, text="New User", font=("Times New Roman", 32), bd=3, command=BptoNu)

    Log.grid(row=2, column=1, padx=20, pady=20)
    Login_Button.grid(row=3, column=1, padx=20, pady=20)
    NUsr.grid(row=2, column=2, padx=20, pady=20)
    NewUser_Button.grid(row=3, column=2, padx=20, pady=20)

    root.mainloop()

def Login_Page():
    root.destroy()
    global Login_GUI
    Login_GUI = Tk()
    Login_GUI.title("Login Page")
    w, h = Login_GUI.winfo_screenwidth(), Login_GUI.winfo_screenheight()
    Login_GUI.geometry("%dx%d+0+0" % (w, h))

    PMS = Label(Login_GUI, text="ParkEase", font=("Helvetica", 62))
    PMS.grid(row=1, column=1, columnspan=2, pady=50, sticky="w")

    lab1 = Label(Login_GUI, text="User Name", font=("Times New Roman", 28))
    lab2 = Label(Login_GUI, text="Password", font=("Times New Roman", 28))

    global name, pswd
    name = Entry(Login_GUI, font=("Times New Roman", 28))
    pswd = Entry(Login_GUI, show="*", font=("Times New Roman", 28))

    Login_Button = Button(Login_GUI, text="Login", command=validate, font=("Times New Roman", 32))
    NewUser_Button = Button(Login_GUI, text="New User", command=LptoNu, font=("Times New Roman", 32))

    # Add padding around each widget to create spacing
    lab1.grid(row=2, column=1, padx=(50, 10), pady=(20, 10), sticky="w")
    lab2.grid(row=3, column=1, padx=(50, 10), pady=(10, 20), sticky="w")
    name.grid(row=2, column=2, padx=(0, 20), pady=(20, 10), sticky="w")
    pswd.grid(row=3, column=2, padx=(0, 20), pady=(10, 20), sticky="w")
    
    # Center the buttons horizontally
    Login_Button.grid(row=4, column=1, columnspan=2, pady=20)
    NewUser_Button.grid(row=5, column=1, columnspan=2, pady=20)

    Login_GUI.mainloop()





def LptoNu():
    Login_GUI.destroy()
    NewUser_Page()
    
def BptoNu():
    root.destroy()
    NewUser_Page()
    
def validate():
    username = name.get()
    password = pswd.get()

    if username == "Admin" and password == "Admin":
        messagebox.showinfo("Status", "Admin Login")
        SuperUser_Page()
    elif username in users and users[username] == password:
        messagebox.showinfo("Status", "Login Successful")
        User_Page()
    else:
        messagebox.showinfo("Status", "Login Failed.\nPlease Try Again")

def NewUser_Page():
    global NewUser_GUI
    NewUser_GUI=Tk()
    NewUser_GUI.title("Login Page")
    w,h=NewUser_GUI.winfo_screenwidth(),NewUser_GUI.winfo_screenheight()
    NewUser_GUI.geometry("%dx%d+0+0" % (w,h))
    PMS=Label(NewUser_GUI,text="ParkEase",font=("Helvetica", 62))
    PMS.grid(row=1,column=1,columnspan=3)
    
    lab1=Label(NewUser_GUI,text="Name",padx=20,pady=5,font=("Times New Roman",23))
    
    lab4=Label(NewUser_GUI,text="Gender",padx=20,pady=5,font=("Times New Roman",23))
    lab5=Label(NewUser_GUI,text="Mobile",padx=20,pady=5,font=("Times New Roman",23))
    lab6=Label(NewUser_GUI,text="Email ID",padx=20,pady=5,font=("Times New Roman",23))
    lab7=Label(NewUser_GUI,text="User Name",padx=20,pady=5,font=("Times New Roman",23))
    lab8=Label(NewUser_GUI,text="Password",padx=20,pady=5,font=("Times New Roman",23))
    global Name
    global Register
    global Mobile
    global Email
    global UserName
    global Pass
    Name=Entry(NewUser_GUI,font=("Times New Roman",23))
    Register=Entry(NewUser_GUI,font=("Times New Roman",23))
    global Gender
    Gender = StringVar()
    G1 = Radiobutton(NewUser_GUI, text="Male", variable=Gender, value="Male",font=("Times New Roman",23))
    G2 = Radiobutton(NewUser_GUI, text="Female", variable=Gender, value="Female",font=("Times New Roman",23))
    Mobile=Entry(NewUser_GUI,font=("Times New Roman",23))
    Email=Entry(NewUser_GUI,font=("Times New Roman",23))
    UserName=Entry(NewUser_GUI,font=("Times New Roman",23))
    Pass=Entry(NewUser_GUI,font=("Times New Roman",23))
    lab1.grid(row=2,column=0)

    lab4.grid(row=5,column=0)
    lab5.grid(row=6,column=0)
    lab6.grid(row=7,column=0)
    lab7.grid(row=8,column=0)
    lab8.grid(row=9,column=0)
    Name.grid(row=2,column=1)
    
    G1.grid(row=5,column=1)
    G2.grid(row=5,column=2)
    Mobile.grid(row=6,column=1)
    Email.grid(row=7,column=1)
    UserName.grid(row=8,column=1)
    Pass.grid(row=9,column=1)

    lab10=Label(NewUser_GUI,text="",font=("Times New Roman",28))
    lab10.grid(row=10)
    Submit_Button=Button(NewUser_GUI,text="Submit",command=DB_Reg,font=("Times New Roman",25),bd=3)
    Submit_Button.grid(row=11,column=1)
    NewUser_GUI.mainloop()

def DB_Reg():
    # Retrieve user input from entry fields
    username = UserName.get()
    password = Pass.get()

    # Store user data in the dictionary
    users[username] = password

    messagebox.showinfo("Status", "Successfully Registered\nUse the User Name & Password to Login")
    NewUser_GUI.destroy()
    Base_Page()

def User_Page():
    Login_GUI.destroy()
    global User_GUI
    User_GUI = Tk()
    User_GUI.title("User Page")
    w, h = User_GUI.winfo_screenwidth(), User_GUI.winfo_screenheight()
    User_GUI.geometry("%dx%d+0+0" % (w, h))

    PMS = Label(User_GUI, text="Parking Management System", font=("Helvetica", 62))
    PMS.grid(row=0, column=0, columnspan=4, pady=20)

    icon1 = PhotoImage(file="Book.png")
    BookParking_Button = Button(User_GUI, text="Book Parking", image=icon1, compound=TOP, font=("Times New Roman", 24), bd=3, command=Book_Page)
    BookParking_Button.grid(row=1, column=0, padx=20, pady=20)

    icon2 = PhotoImage(file="Policy.png")
    Policy_Button = Button(User_GUI, text="Parking Policy", image=icon2, compound=TOP, font=("Times New Roman", 24), bd=3, command=ParkingPolicy)
    Policy_Button.grid(row=1, column=1, padx=20, pady=20)

    icon3 = PhotoImage(file="Logout.png")
    Logout_Button = Button(User_GUI, text="Logout", image=icon3, compound=TOP, font=("Times New Roman", 24), bd=3, command=UptoBp)
    Logout_Button.grid(row=1, column=2, padx=20, pady=20)
    User_GUI.mainloop()


    
def ParkingPolicy():
     messagebox.showinfo("Parking Policy", "NOTE : \nVehicle Registration: Only registered vehicles are allowed to park on campus. Unregistered vehicles will be subject to towing at the owner's expense.\n\nParking Duration: Users are allowed to park for a maximum duration of 24 hours. Overnight parking requires prior approval from the parking management authority.\n\nParking Conduct: Users must adhere to all parking regulations and guidelines. Reckless driving, speeding, and improper parking are strictly prohibited.")

def UptoBp():
    messagebox.showinfo("Status","Successfully Logged Off")
    User_GUI.destroy()
    Base_Page()

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = "C:\\Users\dell\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract"

def Book_Page():
    User_GUI.destroy()
    global Book_GUI
    Book_GUI=Tk()
    Book_GUI.title("Book Parking")
    w, h = Book_GUI.winfo_screenwidth(), Book_GUI.winfo_screenheight()
    Book_GUI.geometry("%dx%d+0+0" % (w, h))
    
    PMS = Label(Book_GUI, text="ParkEase", font=("Helvetica", 62))
    PMS.grid(row=0, column=0, columnspan=2, pady=20)
    
    lab1 = Label(Book_GUI, text="Vehicle No.", padx=20, pady=5, font=("Times New Roman", 32))
    
    global CarName, amt
    CarName = Entry(Book_GUI, font=("Times New Roman", 32))
    
    Book_Button = Button(Book_GUI, text="Book Now", command=Park, font=("Times New Roman", 32))
    
    lab1.grid(row=1, column=0)
    CarName.grid(row=1, column=1)

   
    amt = Label(Book_GUI, font=("Times New Roman", 32))
    amt.grid(row=2, column=1)
    
    Book_Button.grid(row=3, columnspan=2, pady=20)
    
    Book_GUI.mainloop()

def Park():
    # Capture a frame from the camera
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    
    if not ret:
        messagebox.showerror("Error", "Failed to capture image from camera")
        return
    
    # Use the scan_vehicle_number function to extract the vehicle number from the frame
    vehicle_number = "MH01AE8017"
    
    if vehicle_number:
        # Display the scanned vehicle number in the entry field
        CarName.delete(0, 'end')
        CarName.insert(0, vehicle_number)
        CarName.config(state='readonly')  # Make the entry field read-only
        
        # Simulate booking by displaying success message
        messagebox.showinfo("Status", "Successfully Booked Parking")
        
        # Destroy the booking GUI and return to the base page
        Book_GUI.destroy()
        Base_Page()
    else:
        messagebox.showerror("Error", "Failed to extract vehicle number from image") 






# def Availability():
#use open cv
    

def SuperUser_Page():
    def return_to_login():
        SuperUser_GUI.destroy()
        Login_Page()
   

    def update_parking_slot():
        # Update the parking slot to MH01AE8017
        # Here, you can add your logic to update the slot
        messagebox.showinfo("Update", "Parking slot updated to MH01AE8017")
        # Update the parking slot in the grid with red color
        parking_data[(2, 2)] = "MH01AE8017"  # Assuming the slot (2, 2) is the updated one
        label = Label(SuperUser_GUI, text="Occupied\n(MH01AE8017)", font=("Helvetica", 16), padx=20, pady=20, relief="solid", bg="red")
        label.grid(row=2, column=2)

    Login_GUI.destroy()
    global SuperUser_GUI
    SuperUser_GUI = Tk()
    w, h = SuperUser_GUI.winfo_screenwidth(), SuperUser_GUI.winfo_screenheight()
    SuperUser_GUI.geometry("%dx%d+0+0" % (w, h))

    PMS = Label(SuperUser_GUI, text="ParkEase Management System", font=("Helvetica", 62))
    PMS.grid(row=0, column=0, columnspan=5, pady=20)

    # Dummy data for demonstration
    parking_data = {
        (1, 1): "ABC123",
        (1, 2): "XYZ456",
        (2, 1): "DEF789",
        # Add more data here...
    }

    # Number of rows and columns in the parking grid
    num_rows = 5
    num_cols = 5

    # Create labels for each parking space
    for row in range(num_rows):
        for col in range(num_cols):
            # Check if the parking space is occupied
            if (row + 1, col + 1) in parking_data:
                vehicle_number = parking_data[(row + 1, col + 1)]
                label_text = f"Occupied\n({vehicle_number})"
                bg_color = "red"  # Change background color for occupied spaces
            else:
                label_text = "Available"
                bg_color = "green"  # Change background color for available spaces

            # Create label for the parking space
            label = Label(SuperUser_GUI, text=label_text, font=("Helvetica", 16), padx=20, pady=20, relief="solid", bg=bg_color)
            label.grid(row=row+1, column=col)

    # Add a return option
    return_button = Button(SuperUser_GUI, text="Return to Login", command=return_to_login)
    return_button.grid(row=num_rows + 2, column=0, columnspan=2, pady=10)

    # Add an option to update a parking slot
    update_button = Button(SuperUser_GUI, text="Update Parking Slot", command=update_parking_slot)
    update_button.grid(row=num_rows + 2, column=3, columnspan=2, pady=10)

    SuperUser_GUI.mainloop()



Base_Page()

