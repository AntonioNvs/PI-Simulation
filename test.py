import math, random

def createSimulation():
  x = random.random()
  y = random.random()

  dist = (x**2 + y**2)**0.5

  return dist <= 1.0

def simulation(numberTests, numberTrials):
  sumValuesOfPi = 0.0
  for _ in range(numberTrials):
    inCircle = sum([1 if createSimulation() else 0 for i in range(numberTests)])

    sumValuesOfPi += inCircle * 4 / numberTests

  return sumValuesOfPi / numberTrials


if __name__ in "__main__":
  print(simulation(1000, 1000))
    
