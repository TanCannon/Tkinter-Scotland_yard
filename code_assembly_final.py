###what's new:im removing comments"
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import tkinter.messagebox as tmsg 
from PIL import Image, ImageTk
import random, linecache
from sys import exit

#####--------GLOBAL VARIBALS--------------############
 ###-------for the moves table----------------#########
moves_list=[]
 ###-----game rounds----####
game_rounds = 1
 ###--------------------####
 ###------FOR dropdown menu and update player---##
drop_count= 0 #no. of dropmenu objects
 ###-------------------------------------------##
player_no = 6

k= 0 ###-->k is round counter, also the current player object index
#column id of the moves treeview##
my_tree_id = 0
########___required file___#########
file1 = open('text_files\scotmap.txt') #used in station setup
file2 = open('text_files\scotpos_2.txt') #used in highlighting stations
lines1 = file1.readlines()
lines2 = file2.readlines()
########_______________________#########

#####--------GLOBAL VARIBALS BLOCK END--------------############

#####---------------APP GUI BLOCK---------------------##################

####"app's GUI#######
def App(size,title):
        #main setup
        global root
        root = ctk.CTk()
        root.title(title)
        root.iconbitmap('images\spy-icon-detective-agent.ico')
        root.geometry(f'{size[0]}x{size[1]}')
        # u can add max and min size of the window here
        # root.minsize(width=size[0],height=size[1])
        # root.maxsize(width=1280+96,height=649+96)
        
        #widgets
        frameLeft(root)
        frameBottom(root)
        map(root)
        image_s(root)
        #run
        root.mainloop()

def frameLeft(parent):
    global f1
    f1 = ctk.CTkFrame(parent,border_color="grey",border_width=3,corner_radius=0)
    f1 .pack(side="left",fill="y")

    #LOGO
    f_l1 = tk.Frame(f1,bg="white",
            borderwidth=6, 
                relief="raised")
    f_l1.grid(row=0,column=0,padx=50,pady=10)
    l1 = tk.Label(f_l1,text="Project Tkinter - Scotland Yard",
            relief="solid",borderwidth=5,
            bg="black",fg="white",
            padx=10,pady=10,
            font=('Helvetica 15 bold'))
    l1.grid(row=0,column=0)

    #menu
    global l2
    l2 = ctk.CTkLabel(f1,text="Tickets",fg_color="maroon",padx = 10,pady = 10,font=('Helvetica', 15))
    l2.grid(row=1,column=0)

    global f_d
    f_d = ctk.CTkFrame(f1,height=50,fg_color="brown")
    f_d.grid(row=2,column=0,pady=10)
    
    ####tickets left#####
    f1_1 = ctk.CTkFrame(f1)
    f1_1.grid(row=3,column=0)

    global b1,b2
    b1 = ctk.CTkButton(f1_1,text="DETECTIVES",width=5,text_color="white",state= "disabled",text_color_disabled="white",command=detective_tickets)#,command=detective
    b1.grid(row=0,column=0,padx=5,pady=5)
    b2 = ctk.CTkButton(f1_1,text="Mr.X", width=5,state="disabled",text_color_disabled="white",command=MrX_tickets)#,command=MrX
    b2.grid(row=0,column=1,padx=5,pady=5)

    temp = ctk.CTkFrame(f1,height=155)
    temp.grid(row=4,column=0)

    #adding some style to treeview
    style = ttk.Style()
    style.configure("mystyle.Treeview",font=('Calibre',11))

    f1_3 = ctk.CTkFrame(f1)
    f1_3.grid(row=5,column=0,padx=15,pady=5)
    b3 = ctk.CTkLabel(f1_3,text="Moves",width=5,bg_color="#1F6AA5",padx=10)#,command=openmoves
    b3.grid(row=0,column=0,pady=5)

    global my_tree,i
    i=1
    my_tree = ttk.Treeview(f1_3,height=10,style="mystyle.Treeview")
    #define our columns
    my_tree['columns'] = ("Mr.X","D1","D2","D3","D4","D5")
    #format our columns
    my_tree.column("#0",width=0,minwidth=0)
    my_tree.column("Mr.X",anchor="w",width=77,minwidth=77)
    my_tree.column("D1",anchor="w",width=77,minwidth=77)
    my_tree.column("D2",anchor="w",width=77,minwidth=77)
    my_tree.column("D3",anchor="w",width=77,minwidth=77)
    my_tree.column("D4",anchor="w",width=77,minwidth=77)
    my_tree.column("D5",anchor="w",width=77,minwidth=77)
    #create heading
    my_tree.heading("#0",text="",anchor="center")
    my_tree.heading("Mr.X",text="Mr.X",anchor="center")
    my_tree.heading("D1",text="D1",anchor="center")
    my_tree.heading("D2",text="D2",anchor="center")
    my_tree.heading("D3",text="D3",anchor="center")
    my_tree.heading("D4",text="D4",anchor="center")
    my_tree.heading("D5",text="D5",anchor="center")
    #add data
    #__i have done that in next() where the round_count is incremented
    #packing table
    my_tree.grid(row=2,column=0,pady=5,padx=5)

def frameBottom(parent):
    #create a frame
    f2 = ctk.CTkFrame(parent,border_color="grey",border_width=3,corner_radius=0)
    f2.pack(side="bottom",fill="x")
    
    #create a  heading "Options here"

    l2 = ctk.CTkLabel(f2,text="Options here",
                  fg_color="green",
                  padx = 10,pady=2,
                  font=('Helvetica bold', 15))
    l2.pack(fill = "x",padx=2,pady=2)

    #create buttons

    global start_button,restart_button,quit_button
    start_button = ctk.CTkButton(f2,text = "Start game",command=game_start)
    start_button.pack(side = "left",padx=10,pady=10)

    restart_button = ctk.CTkButton(f2,text = "Restart game",state="disabled",command=game_restart)
    restart_button.pack(side = "left",padx=10,pady=10)

    quit_button = ctk.CTkButton(f2,text = "Quit game",command=close_game)
    quit_button.pack(side = "left",padx=10,pady=10)

    about_button = ctk.CTkButton(f2,text = "About",command=about)
    about_button.pack(side = "left",padx=10,pady=10)

def map(parent):
    f = tk.Frame(parent,bg='brown')
    f.pack(side="left",fill="both",expand=1)
    
    # def create_label(self):
    global l3
    l3 = tk.Button(f,text="Map",font=('Helvetica 15 bold'),command=lambda:auto_scroll(),state="disabled")
    l3.pack()

    # def create_scrollbars(self):
    global v2scroll,h2scroll
    v1scroll = tk.Scrollbar(f,orient="vertical")
    v1scroll.pack(side="left",fill="y")

    v2scroll = tk.Scrollbar(f,orient="vertical")
    v2scroll.pack(side="right",fill="y")
   
    h1scroll = tk.Scrollbar(f,orient="horizontal")
    h1scroll.pack(side="top",fill="x")

    h2scroll = tk.Scrollbar(f,orient="horizontal")
    h2scroll.pack(side="bottom",fill="x")

    global my_canvas
    my_canvas = tk.Canvas(f,bg='green',width=800,height=800)
    my_canvas.pack(fill="both",expand=1)
    ###the map image
    global new_image
    img = Image.open("images\map2.png")
    resized_image = img.resize((int(2570//1.2),int(1926//1.2))) #//1.2
    new_image = ImageTk.PhotoImage(resized_image)
    my_canvas.create_image(0, 0, anchor='nw', image=new_image)

    my_canvas.config(yscrollcommand=v1scroll.set)
    my_canvas.config(yscrollcommand=v2scroll.set)

    my_canvas.config(xscrollcommand=h1scroll.set)
    my_canvas.config(xscrollcommand=h2scroll.set)

    v2scroll.config(command=my_canvas.yview)
    h2scroll.config(command=my_canvas.xview)

    v1scroll.config(command=my_canvas.yview)
    h1scroll.config(command=my_canvas.xview)

    my_canvas.config(scrollregion=my_canvas.bbox('all'))

    my_canvas.bind("<Button-1>",scroll_start)
    my_canvas.bind("<B1-Motion>",scroll_move)

def image_s(parent):

    ######----------player pieces images-----------########
    global images, images_glow
    images=[0 for i in range (player_no)]
    images_glow = [0 for i in range (player_no)]
    images[0]= ImageTk.PhotoImage(file="images\mrx.png")
    images[1]= ImageTk.PhotoImage(file="images\police1.png")
    images[2]= ImageTk.PhotoImage(file="images\police2.png")
    images[3]= ImageTk.PhotoImage(file="images\police3.png")
    images[4]= ImageTk.PhotoImage(file="images\police4.png")
    images[5]= ImageTk.PhotoImage(file="images\police5.png")

    images_glow[0] = ImageTk.PhotoImage(file="images\mrx.png")
    images_glow[1] = ImageTk.PhotoImage(file="images\police1_glow.png")
    images_glow[2] = ImageTk.PhotoImage(file="images\police2_glow.png")
    images_glow[3] = ImageTk.PhotoImage(file="images\police3_glow.png")
    images_glow[4] = ImageTk.PhotoImage(file="images\police4_glow.png")
    images_glow[5] = ImageTk.PhotoImage(file="images\police5_glow.png")
    ###----------------highlighter image------------------#####
    global pin_image, map_pin
    pin_image = Image.open("images\circular_pin.png")
    map_pin = pin_image.resize((70,70))
    map_pin = ImageTk.PhotoImage(map_pin)     

#####---------------APP GUI BLOCK ENDS---------------------##################

#########----------CLASSES BLOCK-----------#################

####"stop" class stores stations as objects#######
class stop:
    def __init__(self,bus_set,taxi_set,ug_set):
        #every element is list
        self.bus = bus_set
        self.taxi = taxi_set
        self.ug = ug_set
        self.st= set(bus_set + taxi_set +  ug_set)
    def moves(self):
         return 'bus{} taxi{} underground{}'.format(self.bus,self.taxi,self.ug)
####"player" class stores players as objects#######
class player:
    def __init__(self,current,bus_tickets,tax_tickets,ug_tickets):
        self.current = current
        self.bus_tickets = bus_tickets
        self.taxi_tickets = tax_tickets
        self.ug_tickets = ug_tickets
        self.piece = 0
        self.no_movement = 0
    def tickets(self):
        return 'bus-{} | taxi-{} | ug-{}'.format(self.bus_tickets,self.taxi_tickets,self.ug_tickets)
####"Mr.X class"###################################
class Mr_X (player):
    # super().__init__()
    black_tickets = 1
    x2_tickets = 1
    def tickets(self):
        return 'bus-{} \n taxi-{} \n ug-{} \n black-{} \n 2x-{}'.format(self.bus_tickets,self.taxi_tickets,
        self.ug_tickets,self.black_tickets,self.x2_tickets)
    
#########----------CLASSES BLOCK END-----------##############

###############-------GAME_FUNCTIONS------------ #####################
##--->button calls funstions
def scroll_start(event):
    my_canvas.scan_mark(event.x,event.y)
    print(my_canvas.canvasx(event.x),my_canvas.canvasx(event.x))

def scroll_move(event):
    my_canvas.scan_dragto(event.x,event.y,gain=2)

def detective_tickets():
    b2._text_color = "#9A9B9A"

    print("Dectective () called")
    b1.configure(state = "disabled")
    b2.configure(state = "normal")
    global f1_4, f1_2
    if ('f1_4' in globals()):
        f1_4.destroy()
    f1_2 = ctk.CTkFrame(f1,border_color="white",border_width=2,fg_color="brown",width=100)
    f1_2.grid(row=4,column=0,padx=5) 
    for i in range(5):
        d1 = ctk.CTkLabel(f1_2,text = f"D{i+1}: {player.tickets(player_obj[i+1])}",font=("Lucida",16,"italic"),text_color="black",bg_color="white",padx=3,corner_radius=10)
        d1.grid(row=i,column=0,padx=5,pady=5)

def MrX_tickets():
    b1._text_color = "#9A9B9A"

    print("def MrX(): called")
    b1.configure(state = "normal")
    b2.configure(state = "disabled")
    global f1_4,f1_2
    if('f1_2' in globals()):
        f1_2.destroy()
    f1_4 = ctk.CTkFrame(f1,border_color="white",border_width=2,fg_color='brown',corner_radius=0)
    f1_4.grid(row=4,column=0,padx=5,pady=0) 
    
    d1 = ctk.CTkLabel(f1_4,text=f'Mr.X:\n{Mr_X.tickets(player_obj[0])}',font=("Lucida",18,"italic"),text_color="black",padx=20,pady=5,fg_color="white")
    d1.grid(row=0,column=0,padx=20,pady=1) 

def about():
    tmsg.showinfo("Hi there!", 'This is a tkinter implementation of Scotland Yard Board Game.\n Developer: Tanmaya Kumar Naik,\n Jharsuguda,Odisha,India\ntanmayakumarnaik2003@gmail.com')    

def close_game():
    ans = tmsg.askokcancel("QUIT","Do you really want to quit?")
    if ans:
        exit()

def game_restart(): #runs once
    ans = tmsg.askokcancel("RESTART","Do you want to restart?")
    if ans:
        print("GAME RESTART")
        global k, game_rounds
        k=0
        game_rounds=1
        #changing labels
        l2.configure(text="Tickets")
        l3.config(text="Map") 
        #deleting player objects
        for i in range (player_no):
            my_canvas.delete(player_obj[i].piece)
        #deleting highlighters
        for obj in highlighters_vars_window:
            my_canvas.delete(obj)
        #deleting all records from move treeview
        for item in my_tree.get_children():
            my_tree.delete(item)
        game_start()

def game_start(): #runs once 
    start_button.configure(state = "disabled")
    restart_button.configure(state= "normal")
    l3.configure(state="normal")
    b1.configure(state= "normal")
    b2.configure(state= "normal")
    station_setup()
    setup_players()
    next()

def station_setup(): #runs once
    global stops_obj
    station_no = 200
    stops_obj = [0 for i in range(station_no)] #array of stops object
    for j in range (0,200):
        stops_obj[j] = stop([],[],[])

    for line in lines1:
        val = line.strip()
        val = val.split(' ')
        # print(val)
        route = val[2]
        if route == 'T':
            stops_obj[int(val[0])-1].taxi.append(val[1])
            stops_obj[int(val[0])-1].st.add(val[1]) 
            """add() method is used to add elementsto a set"""
        elif route == 'B':
            stops_obj[int(val[0])-1].bus.append(val[1])
            stops_obj[int(val[0])-1].st.add(val[1])
        elif route == 'U':
            stops_obj[int(val[0])-1].ug.append(val[1])
            stops_obj[int(val[0])-1].st.add(val[1])

def next():
    # global player_obj
    global game_rounds
    global k
    ###------game over conditons----#############
    #-->Mr X gets caught
    for i in range (1,player_no):
        if (player_obj[0].current == player_obj[i].current):
            tmsg.showinfo("CONGRATULATIONS!",f"GAME OVER officers won\nHe was on station {player_obj[0].current}")
            print(f'GAME OVER officers won\nMr.X caught on station {player_obj[0].current}')
            return 1
    if (player_obj[1].no_movement==player_obj[2].no_movement==player_obj[3].no_movement==player_obj[4].no_movement==1):
        print(f'GAME OVER Mr.X ran away!\nHe was on station {player_obj[0].current}')
        return 1
    if (game_rounds == 22):
        tmsg.showinfo("Oops!",f'GAME OVER Mr.X ran away!\nHe was on station {player_obj[0].current}')
        print(f"GAME OVER Mr.X ran away!\nHe was on station {player_obj[0].current}")
        return 1
    ###-------------------------------#################3
    if (k<player_no): #this is game loop 
        print(f'Player_index={k}')
        global current 
        current = player_obj[k].current #current is the actual station no. not an index
        print(stops_obj[current-1].st)
        ###addding Mr.X move ################
        if (k==0): #in this 'if' i'll do all the Mr.X things
            tmsg.showinfo("PASSWORD","Mr.X ur turn")
            l3.configure(text=f'Stations - {stops_obj[current-1].st}')
            l2.configure(text=f"Mr.X tickets")
            my_canvas.itemconfig(player_obj[k].piece,state="normal")
            highlight_moves(player_obj[k].current)
        #####################################
        else:
            # global player_id
            l3.configure(text=f'Stations - {stops_obj[current-1].st}')
            l2.configure(text=f'Detective {k} tickets')
            highlight_moves(player_obj[k].current)
    elif (k==player_no): #next round
        game_rounds+=1
        print(f'game_round={game_rounds}')
        global my_tree_id
        my_tree_id +=1
        my_tree.insert(parent='',index='end',iid=my_tree_id,text='',values=(moves_list[0],moves_list[1],moves_list[2],moves_list[3],moves_list[4],moves_list[5]))
        my_tree.yview_moveto(1)
        moves_list.clear()
        # global k
        k=0
        next()
        print("next round")
    else:
        tmsg.showinfo("Yehh!","Game Over officers win")
        return 

    ###########################____setup players initial position____##########################

def setup_players(): #runs once
    global player_obj
    player_obj = [0 for elm in range (player_no)]
    position = [0 for elm in range (player_no)]
    initial_placement_list = [26,94,198,117,29,138,155,13,50,103,132,197,53,141,91,174,34,112]
    ##-------here i can initialise Mr.X---######
    deploy = random.choice(initial_placement_list)
    player_obj[0] = Mr_X(current=deploy,bus_tickets=3,tax_tickets=4,ug_tickets=3)
    player_obj[0].black_tickets = 5
    player_obj[0].x2_tickets = 2
    position[0] = deploy
    line = linecache.getline('text_files\scotpos_2.txt',deploy)
    val = line.strip()
    val = val.split(' ')
    player_obj[0].piece = my_canvas.create_image(int(val[1])+25,int(val[2])-30,image=images[0])
    ##--------------------------------##########
    
    for i in range(1,player_no):
        flag=0
        while (flag==0):
            deploy = random.choice(initial_placement_list) #random postion of all stations
            if (deploy not in position):
                    player_obj[i] = player(0,8,10,4) #initlialization
                    player_obj[i].current = deploy
                    position[i] = deploy
                    # setup_players(deploy,i)
                    line = linecache.getline('text_files\scotpos_2.txt',deploy)
                    val = line.strip()
                    val = val.split(' ')
                    ###using images for player pieces
                    player_obj[i].piece = my_canvas.create_image(int(val[1])+25,int(val[2])-30,image=images[i]) #+25, -30 #player_index=i
                    flag=1
    my_canvas.itemconfig(player_obj[0].piece,state="hidden")
    print(f'positions={position}')
    del position, deploy
   
def auto_scroll():
    # print(x,y)
    line = linecache.getline('text_files\scotpos_2.txt',player_obj[k].current)
    val = line.strip()
    val = val.split(' ')
    offset = 500
    x = int(val[1])
    y = int(val[2])
    # #########mappping-->(outmin + (float(num-inMin)/float(inmax-inmin)*(outmax-outmin)))
    my_canvas.xview_moveto(0 + (float(x-offset-0)/float(int(2570//1.2)-0)*(1-0)))
    my_canvas.yview_moveto(0 + (float(y-offset-0)/float(int(1926//1.2)-0)*(1-0)))
    print(0 + (float(x-offset-0)/float(int(2570//1.2)-0)*(1-0)),(0 + (float(y-offset-0)/float(int(1926//1.2)-0)*(1-0))))
    #####################___highlight where current player can go___#################

def highlight_moves(current_station):
    print("in highlight_moves")
    ####auto scroll of canvas to the highlighters
    line = linecache.getline('text_files\scotpos_2.txt',current_station)
    val = line.strip()
    val = val.split(' ')
    print(val)

    auto_scroll()

    ####--highlighting the current player piece--##
    my_canvas.delete(player_obj[k].piece)
    player_obj[k].piece = my_canvas.create_image(int(val[1])+25,int(val[2])-30,image=images_glow[k])
    ####---------------------------------------------#####

    stops_obj[current_station-1].st=list(stops_obj[current_station-1].st) #set converted to list
    # global highlighters_vars_button
    global highlighters_vars_window
    highlighters_vars_window = [0 for i  in range (len(stops_obj[current_station-1].st))]
    draw = 1
    for length in range (len(stops_obj[current_station-1].st)):
        if k!=0: #as this should not happen for Mr.X or he wont be caught
            for index in range(1,player_no): #checking if the stations are preoccupied by other player
                if index!= k:
                    if player_obj[index].current == int(stops_obj[current_station-1].st[length]):
                        draw = 0
                        break
                    else:
                        draw = 1
        if draw:
            line = linecache.getline('text_files\scotpos_2.txt',int(stops_obj[current_station-1].st[length]))
            val = line.strip()
            val = val.split(' ')
        
            highlighters_vars_window[length] = my_canvas.create_image(int(val[1]),int(val[2]),image=map_pin)
            my_canvas.tag_bind(highlighters_vars_window[length] ,'<Button-1>',lambda e,clicked_station=val[0]:move(e,clicked_station))

    print("out highlight_moves")
    #################____dropdown menu and update player_____########################

def update_player(clicked_station):
    # print(f'current = {clicked_station}') #updating the player piece new station
    print("in update_player")
    print(f'route used= {d.get("anchor")}')
    line = linecache.getline('text_files\scotpos_2.txt',int(clicked_station))
    val = line.strip()
    val = val.split(' ')

    ##deteting all highlighters images
    global highlighters_vars_window
    for obj in highlighters_vars_window:
        my_canvas.delete(obj)

    #hiding the menu and the 'travel' button
    l2.configure(text="Tickets")
    l3.configure(text="Map")
    list_name.grid_forget()
    d.grid_forget()
    select.grid_forget()

    ###moving current player piece###
    global k
    my_canvas.delete(player_obj[k].piece)
    player_obj[k].piece = my_canvas.create_image(int(val[1])+25,int(val[2])-30,image=images[k]) #+25,-30

    ###----------showing Mr.X move----------################
    if (k==0):
        if (game_rounds not in [3,8,13,18]):
            my_canvas.itemconfig(player_obj[k].piece,state="hidden")    
            mrx_current = ""
        else:
            tmsg.showinfo("OFFICERS!",f'Mr X is at {clicked_station}')
            mrx_current = f'({clicked_station})'
            

        if 'bus' in d.get("anchor"):
            tmsg.showinfo("OFFICERS!","Mr X has used 'bus'")
            if "2x" in moves_list:
                moves_list[0] += "-bus"+mrx_current
            else:
                moves_list.append("bus"+mrx_current)

        elif 'taxi' in d.get("anchor"):
            tmsg.showinfo("OFFICERS!","Mr X has used 'taxi'")
            # moves_list.append("taxi")
            if "2x" in moves_list:
                moves_list[0] += "-taxi"+mrx_current
            else:
                moves_list.append("taxi"+mrx_current)

        elif 'ug' in d.get("anchor"):
            tmsg.showinfo("OFFICERS!","Mr X has used 'undergrounds'")
            # moves_list.append("ug")
            if "2x" in moves_list:
                moves_list[0] += "-ug"+mrx_current
            else:
                moves_list.append("ug"+mrx_current)

        elif 'black' in d.get("anchor"):
            tmsg.showinfo("OFFICERS!","Mr X has used 'a black'")
            # moves_list.append("black")
            if "2x" in moves_list:
                moves_list[0] += "-black"+mrx_current
            else:
                moves_list.append("black"+mrx_current)

        elif '2x' in d.get("anchor"):
            tmsg.showwarning("OFFICERS!","Mr X has used 'a 2x'")
            # moves_list.append("2x")
            if "2x" in moves_list:
                moves_list[0] += "-2x"+mrx_current
            else:
                moves_list.append("2x"+mrx_current)

    #######################################

    ###update player new station no#######
    player_obj[k].current = int(clicked_station)
    print(f'new station no:{player_obj[k].current}')
  
    #####update tickets count && moving current player piece####
    # global k
    global no_movement
    if "NA" in d.get("anchor"):
        player_obj[k].no_movement=1

        moves_list.append(f"NA({player_obj[k].current})")
    
    elif 'bus' in d.get("anchor"):
            player_obj[k].bus_tickets-=1

            
            if (k!=0): #adding tickets to Mr.x account
                moves_list.append(f"bus({player_obj[k].current})")

                player_obj[0].bus_tickets+=1

    elif 'taxi' in d.get("anchor"):
            player_obj[k].taxi_tickets-=1

            if (k!=0): #adding tickets to Mr.x account
                
                moves_list.append(f"taxi({player_obj[k].current})")

                player_obj[0].taxi_tickets+=1

    elif 'ug' in d.get("anchor"):
            player_obj[k].ug_tickets-=1

            if (k!=0): #adding tickets to Mr.x account
                moves_list.append(f"ug({player_obj[k].current})")

                player_obj[0].ug_tickets+=1
    if (k==0):
        if 'black' in d.get("anchor"):
            player_obj[k].black_tickets-=1
        elif '2x' in d.get("anchor"):
            player_obj[k].x2_tickets-=1
    print(f'tickets left:{player.tickets( player_obj[k])}')


    highlighters_vars_window.clear()   #"""emptying the 'highlighters_vars_window' list"""

    k+=1
    if '2x' in d.get("anchor"):
        k=0
    game_over=next()
    print("out update_player")
    ####game restart call####
    if game_over==1:
        print("Lets play again")
        
    global drop_count
    list_name.destroy()
    d.destroy()
    select.destroy()
    drop_count=0

def create_dropdownmenu(options,clicked_station):
                    print("in create_dropdownmenu")
                    global d,list_name
                    # global list_name
                    if k==0:
                        player_name = "Mr.X"
                    else:
                        player_name = f"D{k}"
                    list_name = tk.Label(f_d,text=f'{player_name}: Route to {clicked_station}',font=('Helvetica',12))
                    list_name.grid(row=0,column=0,padx=10,pady=3)
                    d = tk.Listbox(f_d,fg="black",
                    bg= "#586E9E",width=30,
                    height=4,borderwidth=5,
                    relief="flat",
                    cursor="arrow",
                    font=('Helvetica 15'))
                    for item in options:
                        d.insert("end",item)
                    options.clear()
                    d.grid(row=1,column=0,padx=10,pady=10)
                    global select
                    select = ctk.CTkButton(f_d,text="TRAVEL",fg_color="white",text_color="black",font=('Helvetica', 15),command=lambda:update_player(clicked_station),state="disabled")
                    select.grid(row=2,column=0,pady=3)

                    while(d.winfo_exists()): #winindfo_exists() return 1 if the widget exists else 0
                    # while('d' in globals()):
                        # print(f'd={d}')
                        root.update()
                        if (d.get("anchor")):
                            select.configure(state = "normal")
                            break
                    print("out create_dropdownmenu")

def move(e,clicked_station):
    print("in move")
    global drop_count
    if(drop_count==0):
        options =[]
        print(f'len(highlighters_vars_window)={len(highlighters_vars_window)},clicked_station={clicked_station}')
        print(f'k={k}')
        if (player_obj[k].bus_tickets >= 1):
            if clicked_station in stops_obj[current-1].bus: #index = station no. - 1
                options.append(f'bus:{player_obj[k].bus_tickets}')

        if (player_obj[k].taxi_tickets >= 1):
            if clicked_station in stops_obj[current-1].taxi: #index = station no. - 1
                options.append(f'taxi:{player_obj[k].taxi_tickets}')
        if (player_obj[k].ug_tickets >= 1):
            if clicked_station in stops_obj[current-1].ug: #index = station no. - 1
                options.append(f'ug:{player_obj[k].ug_tickets}')
        if (k==0):
            if (player_obj[0].black_tickets >= 1):
                if clicked_station in stops_obj[current-1].st: #index = station no. - 1
                    options.append(f'black:{player_obj[0].black_tickets}')
            if (player_obj[0].x2_tickets >= 1):
                if clicked_station in stops_obj[current-1].st: #index = station no. - 1
                    options.append(f'2x:{player_obj[0].x2_tickets}')

        if len(options) == 0:#here i get the menu for the current player only
            options.append("NA")
            ###create the dropdown menus 
        print("options created")
        drop_count+=1
        create_dropdownmenu(options,clicked_station)
    else:
        list_name.destroy()
        d.destroy()
        select.destroy()
        drop_count = 0
    print("0ut move")
    ###############################################################################
                
####---------------------END OF 'GAME_FUNCTION' BLOCK--------------------------------###

if __name__ =="__main__":
    global root
    root = App([900,400],"SCOTLAND YARD")
