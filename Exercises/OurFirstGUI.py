#! /usr/bin/env python3

if __name__ == "__main__":
    picture = [
        [0,0,0,1,0,0,0],
        [0,0,1,1,1,0,0],
        [0,1,1,1,1,1,0],
        [1,1,1,1,1,1,1],
        [0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0]
        ]
    
    for row in picture:
        for bit in row:
            if bit == 1:
                print("*", end="")
            else:
                print(" ", end="")
        print("\n")