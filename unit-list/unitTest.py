from main import *
def unit_test():
    ret = test()
    if ret == 5:
        return True
    else:
        return False

def unit_add():
    x1 = [[1,2,3],[4,5,6],[7,8,9],[1,2,3,4],[1,2,7]]
    x2 = [[2,2,2],[5,7,8],[9,0,2],[4,3,2,1],[1,2,3,4]] 
    y =  [[3,4,5],[9,12,14],[16,8,11],[5,5,5,5],[False]]

    for a,b,c in zip(x1,x2,y):
        if c != add(a,b):
            return False
    return True

def unit_sub():
    x1 = [[1,2,3],[4,5,6],[7,8,9],[1,2,3,4],[1,2,7]]
    x2 = [[2,2,2],[5,7,8],[9,0,2],[4,3,2,1],[1,2,3,4]] 
    y =  [[-1,0,1],[-1,-2,-2],[-2,8,7],[-3,-1,1,3],[False]]

    for a,b,c in zip(x1,x2,y):
        if c != sub(a,b):
            return False
    return True


def main():
    # my code here
    print('starting unit tests')
    unitTestList = [unit_test,unit_add,unit_sub]

    for u in unitTestList:
        if u() == True:
            print('Function '+u.__name__+' passed')
        else:
            print('Function '+u.__name__+' failed')

if __name__ == "__main__":
    main()
