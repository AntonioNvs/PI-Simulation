from tkinter import *
import random
from time import sleep as wait

class Window(Frame):
  def __init__(self,):
    super().__init__()
    self.numberTrials = 4000
    self.numberTests = 700
    self.valuePi = StringVar()
    self.valuePi.set("Pi: 0.0")
    self.initUI()

  def initUI(self):
    # Iniciando a interface da simulação
    self.pack(fill=BOTH, expand=1)
    
    self.buttonInit = Button(text="Init simulation", 
                            command=self.simulation, 
                            font=("Arial", 16), 
                            bd=1, 
                            bg="#f8f8f8", 
                            pady=10)

    self.labelPi = Label(textvariable=self.valuePi, font=("Arial", 30))
    self.canvas = Canvas(self)
    self.canvas.create_line(50, 300, 550, 300)
    self.canvas.create_line(300, 50, 300, 550)
    self.canvas.create_oval(100, 100, 500, 500, width=3)
    self.labelPi.pack()
    self.canvas.pack(fill=BOTH, expand=1)
    self.buttonInit.pack(pady=10)

    
  def simulation(self):
    sumValuesOfPi = 0.0
    for i in range(self.numberTrials):
      numberIsIn = 0
      xSum = 0
      ySum = 0

      for _ in range(self.numberTests):
        isIn, x, y = self.randomPi()

        if isIn: numberIsIn += 1

        xSum += x
        ySum += y
        
        # Definindo a soma como 1, caso a estimativa de posição extrapolar o limite da simulação

        if xSum > 1: xSum = 1
        if xSum < -1: xSum = -1
        if ySum > 1: ySum = 1
        if ySum < -1: ySum = -1

      sumValuesOfPi += numberIsIn * 4 / self.numberTests

      color = "#00ff00" if self.verify(xSum, ySum) else "#ff0000" 
      x = xSum*200 + 300
      y = ySum*200 + 300

      # Criando o ponto estimado
      self.canvas.create_oval(x-0.25, y-0.25, x+0.25, y+0.25, fill=color)

    self.valuePi.set(f"Pi: {sumValuesOfPi / self.numberTrials}")


  # Posição randomizada de uma coordenada na simulação
  def randomPi(self):
    x = (random.random() * 2) - 1
    y = (random.random() * 2) - 1

    return self.verify(x, y), x, y
  
  # Veficando se pertence ao círculo
  def verify(self, x, y):
    dist = (x**2 + y**2)**0.5
    return dist <= 1.0

def main():
  root = Tk()
  _ = Window()
  root.geometry("600x700")
  root.mainloop()

if __name__ == '__main__':
  main()

