
from agent import Agent  #Allows sketch to acces different function for the whole skit.


agents = []    #creates an agent with a list [] 

num_agents = 100   #Clarified the amount of agents 
fps = 20    # frames per second, 
ppf = 5     # pixel per frame


def setup():       
    size(500,500) # Set the window screens width/height 
    frameRate(fps) # Set the sketch animation frame rate 
    
    # Build the list of agents
    for i in range(num_agents): #list loop for agents 
        agent = Agent()
        agents.append(agent)
    

def draw():              #runs a loop none stop till its told to noLoop
    background(255)      #Clarifying the color of the background with one argument 0_255
    for agent in agents: #for loop that refers the agents 
        agent.move(ppf)  #refresh rate of the agent pixelation
        agent.check_boundary(width, height)  #give variable a restrain within the windows boundary
        fill(100)     #sets the color of that agent given
        circle(agent.x, agent.y, 50)  #Derict the agent location with a given shape(line,rectangle, circle, cube)
                                      # three arguements agent location,agent speed, diameter for the circles
