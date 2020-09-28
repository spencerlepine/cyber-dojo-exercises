def skipModulus(doorCount, step):
    # Return n / 100, but without the remainder.
    return ( (doorCount - (doorCount % step)) / step)

def changeDoors(skips = 1):
    doorCount = 100
    
    # 100 doors (objects) in a row are all initially closed. 
    doorsArray = []
    for i in range(doorCount):
        doorsArray.append(Door())
    
    # Each iteration, skip through the doors Array by the current multiple (1, 2, 3...)
    for s in range(1, skips+1):
        thisStep = int(skipModulus(doorCount, s))
   
        indexForm = s - 1
        for a in range(thisStep):
            doorsArray[a * s].toggle()  # Keep jumping through, but stop before at 100.
            
    return doorsArray

class Door:
    def __init__(self):
        self.position = 'Closed'
        
    def toggle(self):
        if self.position == 'Closed':
            self.position = 'Open'
        else:
            self.position = 'Closed'
