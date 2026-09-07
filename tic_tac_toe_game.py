# import tkinter as tk
# from tkinter import messagebox

# def check_winner():
#     for combo in [ [0,1,2], [3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
#         if buttoms[combo[0]]["text"]==buttoms[combo[1]]["text"]==buttoms[combo[2]]["text"]!="":
#             buttoms[combo[0]].config(bg="red")
#             buttoms[combo[1]].config(bg="red")
#             buttoms[combo[2]].config(bg="red")
#             messagebox.showinfo("Tic-Tac-Toe"),f"player{buttons[combo[0]]["text"]}win !"
#             root.quit()
            
# def button_click(index):
#     if buttoms[index]["text"]==""and not winner:
#         buttom[index]["text"]=current_player
#         check_winner()
#         toggle_player()
        
# def toggle():
#     global current_player 
#     current_player="x" if current_player=="o" else "o"
#     label.config(text=f"player {current_player}'s turn")
    
# root=tk.Tk()
# root.title("Tic-Tac-To")
# buttom=[tk.button(root,text="",front=("normal",25),width=6,command=lambda i=i:button_click(i) for i in range(9)]   

# for i, buttoms in enumeerate(buttoms):
#     buttoms.grid(row=i //3,colume=i%3)         

# current_player ="x"    
# winner = false
# label=tk.label(root,text=f"player{current_player}'s turn" fornt = ("normal",16))
# label.grid(row=3,column=0,columnspan)
# root.minloop()               


# import tkinter as tk
# from tkinter import messagebox

# def check_winner():
#     global winner

#     for combo in [
#         [0, 1, 2],
#         [3, 4, 5],
#         [6, 7, 8],
#         [0, 3, 6],
#         [1, 4, 7],
#         [2, 5, 8],
#         [0, 4, 8],
#         [2, 4, 6]
#     ]:

#         if (buttons[combo[0]]["text"] ==
#             buttons[combo[1]]["text"] ==
#             buttons[combo[2]]["text"] != ""):

#             # Winning buttons ko red karna
#             buttons[combo[0]].config(bg="red")
#             buttons[combo[1]].config(bg="red")
#             buttons[combo[2]].config(bg="red")

#             messagebox.showinfo(
#                 "Tic-Tac-Toe",
#                 f"Player {buttons[combo[0]]['text']} wins!"
#             )

#             winner = True


# def button_click(index):
#     if buttons[index]["text"] == "" and not winner:

#         buttons[index]["text"] = current_player

#         check_winner()

#         if not winner:
#             toggle_player()


# def toggle_player():
#     global current_player

#     current_player = "X" if current_player == "O" else "O"

#     label.config(text=f"Player {current_player}'s turn")


# # Main window
# root = tk.Tk()
# root.title("Tic-Tac-Toe")

# # Buttons create karna
# buttons = [
#     tk.Button(
#         root,
#         text="",
#         font=("normal", 25),
#         width=6,
#         command=lambda i=i: button_click(i)
#     )
#     for i in range(9)
# ]

# # Buttons ko grid me arrange karna
# for i, button in enumerate(buttons):
#     button.grid(row=i // 3, column=i % 3)


# # Starting player
# current_player = "X"
# winner = False

# # Label
# label = tk.Label(
#     root,
#     text=f"Player {current_player}'s turn",
#     font=("normal", 16)
# )

# label.grid(row=3, column=0, columnspan=3)

# # Start game
# root.mainloop()


import tkinter as tk
from tkinter import messagebox

# Window banana
window = tk.Tk()
window.title("Tic Tac Toe")

# Abhi X ki turn hai
player = "X"

# Saare buttons ko store karne ke liye list
buttons = []


# Button dabane par ye function chalega
def click(button):
    global player

    # Agar button already filled hai
    if button["text"] != "":
        return

    # Current player ka X ya O button mein likho
    button["text"] = player

    # Winner check karo
    check_winner()

    # Player change karo
    if player == "X":
        player = "O"
    else:
        player = "X"


# Winner check karne ka function
def check_winner():

    # Jeetne ke possible combinations
    combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    # Har combination ko check karo
    for combo in combinations:

        a = buttons[combo[0]]["text"]
        b = buttons[combo[1]]["text"]
        c = buttons[combo[2]]["text"]

        # Agar teeno same hain aur empty nahi hain
        if a == b == c and a != "":
            messagebox.showinfo("Winner", a + " Wins!")
            reset_game()
            return


# Game reset karne ka function
def reset_game():
    global player

    player = "X"

    for button in buttons:
        button["text"] = ""


# 9 buttons banana
for i in range(9):

    button = tk.Button(
        window,
        text="",
        font=("Arial", 30),
        width=5,
        height=2,
        command=lambda b=i: click(buttons[b])
    )

    button.grid(row=i // 3, column=i % 3)

    buttons.append(button)


# Window ko chalate rehna
window.mainloop()