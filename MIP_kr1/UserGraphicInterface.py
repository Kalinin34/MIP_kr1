import tkinter as tk
from tokenize import Number
import TreeVisualization
import WorkWithNumbers
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Tree import Tree
def on_closing():
    import sys
    sys.exit()
class GameSetupWindow(tk.Tk):
    def __init__(self,gameManager):
        self.a = 0;
        super().__init__()
        self.gameManager = gameManager
        self.title("Spēle: Sagatavošana")
        self.geometry("1000x600")  
        self.resizable(False, False)


        self.first_player_var = tk.StringVar()
        self.algorithm_var = tk.StringVar()

        self.control_frame = tk.Frame(self, width=300, height=600)
        self.control_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.control_frame.pack_propagate(False)

        self.spacer_frame = tk.Frame(self.control_frame, height=100)
        self.spacer_frame.pack(side=tk.TOP)
        self.spacer_frame.pack_propagate(False)

        self.generate_button = tk.Button(self.control_frame, text="Ģenerēt 5 skaitļus", command= self.generate_numbers)
        self.generate_button.pack(pady=20)

        self.numbers_frame = tk.Frame(self.control_frame)
        self.numbers_label = tk.Label(self.numbers_frame, text="Izvēlieties sākuma skaitli:")
        self.number_buttons = []

        self.first_player_frame = tk.Frame(self.control_frame)
        self.first_player_var.set("player")
        tk.Label(self.first_player_frame, text="Kurš sāk spēli?").pack()
        fr1 = tk.Radiobutton(self.first_player_frame, text="Spēlētājs", variable="1", 
                       value="player", command=lambda: self.set_first_player('player'))
        fr1.select()
        fr1.pack()
        tk.Radiobutton(self.first_player_frame, text="Dators", variable="1", 
                       value="computer", command=lambda: self.set_first_player('computer')).pack()

        self.algorithm_var.set("minimax")
        self.algorithm_frame = tk.Frame(self.control_frame)
        tk.Label(self.algorithm_frame, text="Izvēlieties datora algoritmu:").pack()
        ar1 = tk.Radiobutton(self.algorithm_frame, text="Minimaksa algoritms", variable="2", 
                       value="minimax", command=lambda: self.set_algorithm('minimax'))
        ar1.select()
        ar1.pack()
        tk.Radiobutton(self.algorithm_frame, text="Alfa-beta algoritms", variable="2", 
                       value="alpha_beta", command=lambda: self.set_algorithm('alfa_beta')).pack()

        self.start_button = tk.Button(self.control_frame, text="Sākt spēli", command=self.start_game, state="disabled")

        self.restart_button = tk.Button(self.control_frame, text="Sākt spēli no jauna", command=self.restart_game, state="disabled")
        
        self.score_frame = tk.Frame(self.control_frame)
        self.player_score = tk.Label(self.score_frame, text="Spēlētāja punkti: 0")
        self.player_score.pack()
        self.computer_score = tk.Label(self.score_frame, text="Datora punkti: 0")
        self.computer_score.pack()
        self.bank_score = tk.Label(self.score_frame, text="Banka: 0")
        self.bank_score.pack()
        
        self.game_frame = tk.Frame(self.control_frame)
        self.current_label = tk.Label(self.game_frame, text="Pašreizējais skaitlis: 0")
        self.current_label.pack()

        self.divide_2_button = tk.Button(self.game_frame, text="Dalīt ar 2", command=lambda: self.make_move(2))
        self.divide_2_button.pack(pady=5)
        self.divide_3_button = tk.Button(self.game_frame, text="Dalīt ar 3", command=lambda: self.make_move(3))
        self.divide_3_button.pack(pady=5)
        
        self.visual_frame = tk.Frame(self, width=700, height=600)
        self.visual_frame.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.visual_frame.pack_propagate(False)
        
        self.status_frame = tk.Frame(self.visual_frame, width=700, height=110)
        self.status_frame.pack(side=tk.TOP, fill=tk.X)
        self.status_frame.pack_propagate(False)
        self.status_label = tk.Label(self.status_frame, text="", font=("Arial", 14), wraplength=680, justify="center")
        self.status_label.pack(pady=10)

        self.canvas_frame = tk.Frame(self.visual_frame, width=700, height=500)
        self.canvas_frame.pack(side=tk.BOTTOM, fill=tk.BOTH)
        self.canvas_frame.pack_propagate(False)

        self.canvas = FigureCanvasTkAgg(TreeVisualization.fig, master=self.canvas_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.canvas.draw()

        self.protocol("WM_DELETE_WINDOW", on_closing)
        pass

    def start_game(self):
        first_player_text = "Spēlētājs" if self.first_player_var.get() == "player" else "Dators"
        algorithm_text = "Minimaksa algoritms" if self.algorithm_var.get() == "minimax" else "Alfa-beta algoritms"
        self.status_label.config(text=f"Spēle sākas\nSkaitlis: {self.selected_number}\nPirmais iet: {first_player_text}\nAlgoritms: {algorithm_text}")
        self.first_player_frame.pack_forget()
        self.algorithm_frame.pack_forget()
        self.start_button.pack_forget()
        self.score_frame.pack(pady=10)
        self.game_frame.pack(pady=10)
        self.current_number = self.selected_number
        self.gameManager.setAI(self.algorithm_var.get())
        #self.moves.append(self.current_number)

        self.gameManager.observe()
        TreeVisualization.Output_tree(self.gameManager.Tree,self.gameManager.currentVal)
        self.current_label.config(text=f"Pašreizējais skaitlis: { self.gameManager.currentVal}")
        self.update()
        self.canvas.draw()
        print(self.first_player_var.get())
        if self.first_player_var.get() == "computer":
            self.after(500, self.computer_move)
        pass

    def make_move(self, divisor):
        if self.gameManager.currentVal % divisor == 0 and not self.gameManager.game_over:
            points = 1 if self.gameManager.currentVal % 2 == 0 else -1
            print(points)

            if self.gameManager.currentVal % 5 == 0:
                self.gameManager.Bank += 1

            self.gameManager.player += points
            self.player_score.config(text=f"Spēlētāja punkti: {self.gameManager.player}")
            self.bank_score.config(text=f"Banka: {self.gameManager.Bank}")
            if(divisor == 2):
                self.gameManager.currentWay.append('L')
            else:
                self.gameManager.currentWay.append('R')

            self.gameManager.currentVal = self.gameManager.currentVal // divisor
            self.current_label.config(text=f"Pašreizējais skaitlis: { self.gameManager.currentVal}")
            self.gameManager.observe()
            TreeVisualization.Output_tree(self.gameManager.Tree,self.gameManager.currentVal)
            self.canvas.draw()
            self.update()
            if self.gameManager.currentVal in [2, 3]:
                if self.gameManager.currentVal == 2:
                    self.gameManager.player += self.gameManager.Bank
                    self.gameManager.Bank = 0
                self.end_game()
            elif self.gameManager.currentVal % 2 != 0 and self.gameManager.currentVal % 3 != 0:
                self.end_game()
            else:
                pass
                self.after(500, self.computer_move)
        else:
            self.status_label.config(text=f"Kļūda: Skaitli nevar dalīt ar {divisor}!")

    def computer_move(self):
        if(not self.gameManager.game_over):
            self.gameManager.AI.thinking(self.gameManager.currentVal,self.gameManager.computer,self.gameManager.player,self.gameManager.Bank)

            divisor = 0
            if(self.gameManager.AI.direction):
                divisor = 2
            else:
                divisor = 3

            self.gameManager.currentVal = self.gameManager.currentVal // divisor
            points = 1 if self.gameManager.currentVal % 2 == 0 else -1

            if self.gameManager.currentVal % 5 == 0:
                self.gameManager.Bank += 1

            self.gameManager.computer += points
            self.current_label.config(text=f"Pašreizējais skaitlis: { self.gameManager.currentVal}")
            self.computer_score.config(text=f"Datora punkti: {self.gameManager.computer}")
            self.bank_score.config(text=f"Banka: {self.gameManager.Bank}")

            if(divisor == 2):
                self.gameManager.currentWay.append('L')
            else:
                self.gameManager.currentWay.append('R')

            self.gameManager.observe()
            TreeVisualization.Output_tree(self.gameManager.Tree,self.gameManager.currentVal)
            self.canvas.draw()
            self.update()
            if self.gameManager.currentVal in [2, 3]:
                if self.gameManager.currentVal == 2:
                    self.gameManager.computer += self.gameManager.Bank
                    self.gameManager.Bank = 0
                self.end_game()
            elif self.gameManager.currentVal % 2 != 0 and self.gameManager.currentVal % 3 != 0:
                self.end_game()
        else:
            self.end_game()
        pass
    def end_game(self):
        self.game_over = True
        winner = "Spēlētājs" if self.gameManager.player > self.gameManager.computer else "Dators" if self.gameManager.computer > self.gameManager.player else "Neizšķirts"
        self.status_label.config(text=f"Spēle beigusies\nUzvarētājs: {winner}\nSpēlētāja punkti: {self.gameManager.player}\nDatora punkti: {self.gameManager.computer}")
        self.game_frame.pack_forget()
        self.restart_button.config(state="normal")
        self.restart_button.pack(pady=10)

    def restart_game(self):
        self.game_over = False
        self.selected_number = None
        self.current_number = 0
        self.player_points = 0
        self.computer_points = 0
        self.bank = 0
        self.moves = []
        for button in self.number_buttons:
            button.destroy()
        self.number_buttons.clear()
        self.score_frame.pack_forget()
        self.restart_button.pack_forget()
        self.start_button.config(state="disabled")
        self.restart_button.config(state="disabled")
        self.player_score.config(text="Spēlētāja punkti: 0")
        self.computer_score.config(text="Datora punkti: 0")
        self.bank_score.config(text="Banka: 0")
        self.generate_button.pack(pady=20)
        self.status_label.config(text="")
        self.a = -1
        self.gameManager.reset()
        TreeVisualization.reset()
        self.canvas.draw()

    def set_first_player(self,first):
        self.first_player_var.set(first)
        # if not self.algorithm_frame.winfo_ismapped():
        #     self.algorithm_frame.pack(pady=10)
        pass

    def set_algorithm(self,algrth):
        self.algorithm_var.set(algrth)
        # if self.selected_number and self.first_player_var.get() != "none" and not self.start_button.winfo_ismapped():
        #     # self.start_button.config(state="normal")
        #     # self.start_button.pack(pady=20)
        #     pass

    def generate_numbers(self):
        self.generate_button.pack_forget()
        numbers = WorkWithNumbers.RandomVariablesForGame(10000,20000,5)
        self.numbers_frame.pack(pady=10)
        self.numbers_label.pack(pady=5)
        for num in numbers:
            btn = tk.Button(self.numbers_frame, text=str(num), command=lambda n=num: self.select_number(n))
            btn.pack(pady=5)
            self.number_buttons.append(btn)

    def select_number(self, number):
        if(self.a == -1):
            print("sss")
        print("here")
        self.gameManager.Tree = Tree(number)
        self.gameManager.currentVal = number
        self.selected_number = number
        for btn in self.number_buttons:
            btn.config(state="disabled")
        self.numbers_frame.pack_forget()
        self.first_player_frame.pack(pady=10)
        self.algorithm_frame.pack(pady=10)
        self.start_button.config(state="normal")
        self.start_button.pack(pady=20)
