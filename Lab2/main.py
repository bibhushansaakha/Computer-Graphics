from DDA import DDA
from BLA import BLA
from histogram import draw_histogram
from lineplotter import drawline

def main():
    dummy_frequencies = [10, 12, 17, 22]
    x0 = int(input("Enter 1st x Point: "))
    y0 = int(input("Enter 1st y Point: "))
    x1 = int(input("Enter 2nd x Point: "))
    y1 = int(input("Enter 2nd y Point: "))
    flag = True
    while flag:
        algo = int(input("1. BLA / 2. DDA (1/2): "))
        if algo == 1:
            drawline(BLA, x0, y0, x1, y1, "BLA")
            draw_histogram(dummy_frequencies, BLA)
            flag = False
        elif algo == 2:
            drawline(DDA, x0, y0, x1, y1, "DDA")
            draw_histogram(dummy_frequencies, DDA)
            flag = False
        else:
            print("Invalid Input. Enter 1 or 2")

if __name__ == "__main__":
    main()
