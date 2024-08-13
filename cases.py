def is_integer(value):
    try:
        # engineer hacks -> int(value) == float(value) -> if it's an integer, it will be equal to the float value
        return int(value) == float(value)
    except ValueError:
        return False

# level test
def levelTest(level):
    # check if it's a number
    if is_integer(level):
        level = int(level)
        # check if it's between 200 - 800
        if level >= 200 and level <= 800:
            # make sure it's divisible by 100
            if level % 100 == 0:
                return True
            else:
                return False
        else:
            return False

    else:
        return False
    
def subtopicTest(subtopic):
    if is_integer(subtopic):
        subtopic = int(subtopic)
        if subtopic >= 2 and subtopic <= 8:
            return True
        else:
            return False
    else: 
        return False

def topicTest(topic):
    if is_integer(topic):        return False 
    else:
        return True

print(topicTest("aplha"))
print(topicTest("war of 1812"))
print(topicTest(3802))
