import random

class Environment:
    def __init__(self, width, height, goal_position):
        self.width = width
        self.height = height
        self.goal_position = goal_position
        self.agent_position = [0, 0]  # Inicia no canto superior esquerdo

    def is_goal_reached(self):
        return self.agent_position == self.goal_position

    def move_agent(self, direction):
        if direction == 'up' and self.agent_position[1] > 0:
            self.agent_position[1] -= 1
        elif direction == 'down' and self.agent_position[1] < self.height - 1:
            self.agent_position[1] += 1
        elif direction == 'left' and self.agent_position[0] > 0:
            self.agent_position[0] -= 1
        elif direction == 'right' and self.agent_position[0] < self.width - 1:
            self.agent_position[0] += 1

    def get_percept(self):
        return self.agent_position, self.goal_position

class ReflexAgent:
    def __init__(self, environment):
        self.environment = environment

    def choose_action(self, percept):
        agent_position, goal_position = percept
        if agent_position[0] < goal_position[0]:
            return 'right'
        elif agent_position[0] > goal_position[0]:
            return 'left'
        elif agent_position[1] < goal_position[1]:
            return 'down'
        elif agent_position[1] > goal_position[1]:
            return 'up'
        else:
            return None

    def run(self):
        while not self.environment.is_goal_reached():
            percept = self.environment.get_percept()
            action = self.choose_action(percept)
            if action:
                self.environment.move_agent(action)
            print(f"Agente movido para: {self.environment.agent_position}")

# Configuração do ambiente e do agente
width = 5
height = 5
goal_position = [4, 4]  # Posição do objetivo
environment = Environment(width, height, goal_position)
agent = ReflexAgent(environment)

# Executa o agente no ambiente
agent.run()

print("Objetivo alcançado!")
