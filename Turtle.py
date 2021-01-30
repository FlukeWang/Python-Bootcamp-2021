import turtle
tao = turtle.Turtle()
tao.shape('turtle')

def forwardleft45() :
	tao.forward(100)
	tao.left(45)
    

	
for i in range (8) :
	forwardleft45()
	
for i in range (10) :
    for j in range (8) :
        forwardleft45()
    print('Picture No.', i )
    tao.left(36)

    

    

    

        
