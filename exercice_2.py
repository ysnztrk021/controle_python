def draw_hollow_square(char_to_draw,size):

    for j in range(size):
        for i in range(size):
            if i == 0 or i == size - 1:
                print(char_to_draw, end = ' ')
            elif j == 0 or j == size - 1:
                print(char_to_draw, end = ' ')
            else:
                print(' ', end = ' ')
        print()
    
draw_hollow_square("o",5)
draw_hollow_square("+",10)
draw_hollow_square(".",3)