def registrationPage():
    title = Label(Frame_login,text="Register Here",font=("Impact",35,"bold"),fg=self.fg_bg,bg="white").place(x=90,y=30 )
    desc = Label(Frame_login,text="User login Area",font=("Goudy old style",15,"bold"),fg=self.fg_bg,bg="white").place(x=90,y=100)
    
    lbl_username = Label(Frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=140)
    self.text_user = Entry(Frame_login,font=('times new roman',15),bg='lightgray')
    self.text_user.place(x=90,y=170,width=350,height=35)

    lbl_password = Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=210)
    self.text_user = Entry(Frame_login,font=('times new roman',15),bg='lightgray')
    self.text_user.place(x=90,y=240,width=350,height=35)