# Positional argument its mandatory to provide arguments
import argparse
if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("number1",help="first number")
    parser.add_argument("number2",help="second number")
    parser.add_argument("operations",help="operation")
    args= parser.parse_args()

    print(args.number1)
    print(args.number2)
    print(args.operations)

    n1 = int(args.number1)
    n2= int(args.number2)
    result=None
    if args.operations =="add":
        result= n1+n2
    elif args.operations =="subtract":
        result= n2-n1
print(result)

# Optional Argument if you want to ignore some arguments add --
############### Exercise question #####
import argparse
if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--physics",help="Marks for Physics")
    parser.add_argument("--Chemistry",help="Marks for Chemistry")
    parser.add_argument("--Maths",help="Marks for Maths")
    parser.add_argument("--average",help="Find the average")
    args= parser.parse_args()

    print(args.physics)
    print(args.Chemistry)
    print(args.Maths)
    print("Average of your marks is : ")
    print(args.average)

    n1 = int(args.physics)
    n2= int(args.Chemistry)
    n3 = int(args.Maths)
    result=None
    if args.average =="average":
        result= ((n1+n2+n3)/3)
    else:
        print("unsupported operations")

print(result)


