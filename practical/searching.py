import argparse
from module.searching import Searching


seaeching = Searching()

parser = argparse.ArgumentParser(description="The Script provides sorting of list using different searching algorithms")
parser.add_argument("list", nargs="+", type=int ,help="List elements")
parser.add_argument("--key", required=True, type=int, help="Key")
parser.add_argument("--algo", type=int, choices=range(1,3), help="Algorithm to use\nLinear Search 1\nBinary Search 2")

args = parser.parse_args()
arr = args.list

if(args.algo == None):
    ask = int(input("Choose an Algorithm to use\nLinear Search 1\nBinary Search 2\n:: "))
    args.algo = ask

print(seaeching.search(args.list,key = args.key, algo=args.algo))

