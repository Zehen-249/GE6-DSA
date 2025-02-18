class Sorting:
    def __init__(self):
        pass

    def sort(self, ls:list, algo:int=1, reversed = False)->list:
        if(algo == 2):
            return self.__bubbleSort(ls, reverse=reversed)
        elif(algo == 1):
            return self.__selectionSort(ls, reverse=reversed)
        elif(algo == 3):
            return self.__insertionSort(ls, reverse=reversed)

    def __selectionSort(self, arr:list, reverse=False):
        if(reverse == False):
            for i in range(len(arr)):
                for j in range(i+1 , len(arr)):
                    if(arr[j] < arr[i]):
                        temp = arr[j];
                        arr[j] = arr[i];
                        arr[i] = temp;
        else:
            for i in range(len(arr)):
                for j in range(i+1 , len(arr)):
                    if(arr[j] > arr[i]):
                        temp = arr[j];
                        arr[j] = arr[i];
                        arr[i] = temp;

        return arr

    def __insertionSort(self, arr:list,reverse=False):
        n = len(arr)

        for i in range(1, n):
            key = arr[i] 
            j = i - 1

            while j >= 0 and ((arr[j] > key and not reverse) or (arr[j] < key and reverse)):
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr


    def __bubbleSort(self,arr:list, reverse=False):
        if(reverse == False):
            for i in range(len(arr)-1):
                for j in range(len(arr)-1-i):
                    if(arr[j] > arr[j+1]):
                        temp = arr[j]
                        arr[j] = arr[j+1]
                        arr[j+1] = temp
        else:
            for i in range(len(arr)-1):
                for j in range(len(arr)-1-i):
                    if(arr[j] < arr[j+1]):
                        temp = arr[j]
                        arr[j] = arr[j+1]
                        arr[j+1] = temp
        return arr


srt = Sorting()
ls = [5,6,8,1,3]
print(srt.sort(ls,algo=3))