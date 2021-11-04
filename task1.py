'''character_to_use is a optional 
parameter with the default value of #.
Therefore, if nothing is passed then hashes 
will be printed.'''
def square(size, character_to_use='#'):
    for i in range(1,size+1,1):
        print(character_to_use*size)
    return
square(5,'9')