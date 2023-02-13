import argparse #สำหรับ รับ input จากภายนอก

def parse_input():
     parser = argparse.ArgumentParser(description='test program to learn about argparse and subprocess')
     parser.add_argument(
          'm', 
        
          type=int,
          help='value of M positional argument')
     parser.add_argument(
          '--x', 
          type=int,
          help='value of x')

     parser.add_argument(
         '--yval',
         type=int,
         default=3,
         help='value of y')

     args = parser.parse_args()
     return args


def print_other():
     print('something else')
     
def print_one():
     print('11111')

if __name__ == "__main__":
    x = parse_input()
    print_other()
    print_one()
    print_other()
    print(f"yval = {x.yval}")
    print(f'xt = {(x.x)*2}')
    # if __name__ == "__main__":

#     args = parse_input()
    
#     x = args.x
#     y = args.yval
#     print(f'M = {args.m}')
#     print(f'calculate {x} x {y} = {x*y}')
 
# import subprocess #สำหรับ รัน terminal command

# #import flask #สำหรับ ทำ web app และ web service api


 

# def parse_input():
#     parser = argparse.ArgumentParser(description='test program to learn about argparse and subprocess')
#     # parser.add_argument(
#     #     'm', 
#     #     type=int,
#     #     help='value of M positional argument')

#     # parser.add_argument(
#     #     '--x', 
#     #     type=int,
#     #     help='value of x')

#     parser.add_argument(
#         '--yval',
#         type=int,
#         default=3,
#         help='value of y')

#     args = parser.parse_args()
#     return args

# if __name__ == "__main__":

#     args = parse_input()
    
#     x = args.x
#     y = args.yval
#     print(f'M = {args.m}')
#     print(f'calculate {x} x {y} = {x*y}')