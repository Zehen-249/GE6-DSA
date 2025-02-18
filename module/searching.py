class Searching:
    def __init__(self):
        pass

    def search(self, ls:list, key:int, algo:int=1)->int:
        if(algo == 1):
            return self.__linearSearch(ls, key)
        elif(algo == 2):
            return self.__binarySearch(ls, key, 0, len(ls)-1)
        
    def __linearSearch(self,arr:list, key:int)->int:
        for i in range(len(arr)):
            if(arr[i] == key):
                return i
        return -1
    
    def __binarySearch(self,arr:list, key:int, st:int, end:int )->int:
        if(st > end):
            return -1
        mid = st + (end - st)//2

        if(arr[mid] == key):
            return mid
        else:
            if(key > arr[mid]):
                st = mid + 1
                return self.__binarySearch(arr,key,st,end)
            else:
                end = mid - 1
                return self.__binarySearch(arr,key,st,end)
            