import argparse
from module.sorting import Sorting

sorting =  Sorting()

parser = argparse.ArgumentParser(description="The Script provides sorting of list using different sorting algorithms")
parser.add_argument("list", nargs="+", type=int ,help="List elements")
parser.add_argument("--algo", type=int, choices=range(1,4), help="Algorithm to use\nSelection Sort 1\nBubble Sort 2\nInsertion Sort 3")
parser.add_argument("--reversed", type=bool, default=False, help="Sort Descending: Default False")

args = parser.parse_args()
arr = args.list

if(args.algo == None):
    ask = int(input("Choose an Algorithm to use\nSelection Sort 1\nBubble Sort 2\nInsertion Sort 3\n:: "))
    args.algo = ask
    ask = ((input("Sort Descending:: (True / False) "))=="True")
    args.reversed = ask
    print(args.reversed)
print(sorting.sort(arr, algo=args.algo,reversed=args.reversed))