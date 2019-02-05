import os

def printscreen(screen):
    os.system('cls')
    for a in screen:
        for b in a:
            print("_" if b == False else "#", end = "")
        print()

def row_rotate(screen, row, step):
    screen[row] = screen[row][-step:] + screen[row][:-step]

def column_rotate(screen, col, step):
    column = [screen[i][col] for i in range(len(screen))]
    column = column[-step:] + column[:-step]
    for a in range(len(screen)):
        screen[a][col] = column[a]

def drawrect(screen, width, height):
    for a in range(width):
        for b in range(height):
            screen[b][a] = True

def main():
    screen = [[False for _ in range(50)] for _ in range(6)]
    commands = [line.strip() for line in open("8_input.txt", "r")]
    for co in commands:
        if co.startswith("rect"):
            drawrect(screen, int(co[5:co.find('x')]), int(co[co.find('x')+1:]))
        if co.startswith("rotate row"):
            row_rotate(screen, int(co[co.find('=')+1]), int(co[co.find('by ') + 3:]))
        if co.startswith("rotate column"):
            column_rotate(screen, int(co[co.find('=')+1:co.find(' by')]), int(co[co.find('by ') + 3:]))
        printscreen(screen)
        
    count = 0
    for a in screen:
        count += a.count(True)
    print(count)

if __name__ == "__main__":
    main()
