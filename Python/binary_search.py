import random
import numpy as np

def data():
    arr = np.arange(5000)
    list = [*arr]
    random.shuffle(list)
    return list
    
    
def search(arr, a, b, c):
    if a > b:
        return False
    else:
        
        e = (a + b) // 2
        
        if arr[e] == c:
            return e
        
        elif arr[e] < c:
            return search(arr, e+1, b, c)
        
        else:
            return search(arr, a, e, c)            
    

def main():
    num = int(input("Enter_num: "))
    shuffle_arr = data()
    shuffle_arr.sort()
    
    high = len(shuffle_arr)
    
    i = search(shuffle_arr, 0, high, num)
    print(f"Postion {i}")
    print(shuffle_arr[i])

if __name__ == "__main__":
    main()
