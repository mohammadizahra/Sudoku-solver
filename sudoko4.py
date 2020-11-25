import math
from copy import deepcopy
import tkinter

size = 4
ye_flag = True


def set_size_func4():     #   ..... set_size_funcs define size of sudoku

    global size
    size = 4
    # print(size)
    solve_btn['state'] = tkinter.NORMAL
    solve_btn['cursor'] = 'hand2'
    size_button_4['cursor'] = 'arrow'
    size_button_9['cursor'] = 'arrow'
    size_button_16['cursor'] = 'arrow'
    size_button_4['state'] = tkinter.DISABLED
    size_button_9['state'] = tkinter.DISABLED
    size_button_16['state'] = tkinter.DISABLED

    build_func()


def set_size_func9():
    global size
    size = 9
    # print(size)
    solve_btn['state'] = tkinter.NORMAL
    solve_btn['cursor'] = 'hand2'
    size_button_4['cursor'] = 'arrow'
    size_button_9['cursor'] = 'arrow'
    size_button_16['cursor'] = 'arrow'
    size_button_4['state'] = tkinter.DISABLED
    size_button_9['state'] = tkinter.DISABLED
    size_button_16['state'] = tkinter.DISABLED
    build_func()


def set_size_func16():
    global size
    size = 16
    # print(size)
    solve_btn['state'] = tkinter.NORMAL
    solve_btn['cursor'] = 'hand2'
    size_button_4['cursor'] = 'arrow'
    size_button_9['cursor'] = 'arrow'
    size_button_16['cursor'] = 'arrow'
    size_button_4['state'] = tkinter.DISABLED
    size_button_9['state'] = tkinter.DISABLED
    size_button_16['state'] = tkinter.DISABLED
    build_func()


def find_box(i, j):  # ..... checking **box** for find answer
    sqrt_num = int(math.sqrt(num_of_row_col))
    block = [i // sqrt_num * sqrt_num, j // sqrt_num * sqrt_num]
    for k in range(block[0], block[0] + sqrt_num):
        for h in range(block[1], block[1] + sqrt_num):
            if sudoku[k][h] == sudoku[i][j] and k != i and h != j:
                return False
    return True


def find_row(i, j):     # ..... checking **row** for find answer
    for k in range(num_of_row_col):
        if sudoku[i][k] == sudoku[i][j] and k != j:
            return False
    return True


def find_column(i, j):     # ..... checking **column** for find answer
    for k in range(num_of_row_col):
        if sudoku[k][j] == sudoku[i][j] and k != i:
            return False
    return True


def find_empty():      # ..... find empty cell
    for i in range(num_of_row_col):
        for j in range(num_of_row_col):
            if sudoku[i][j] == 0:
                return [i, j]
    return False


def back_track():   # .....use backtrack algorithm
    empty = find_empty()
    if not find_empty():
        return True
    for i in may_be_ans[empty[0]][empty[1]]:
        if i == 0:
            continue
        sudoku[empty[0]][empty[1]] = i
        if find_row(empty[0], empty[1]) and find_column(empty[0], empty[1]) and find_box(empty[0], empty[1]):
            if back_track():
                return True
    sudoku[empty[0]][empty[1]] = 0
    return False


def check_answer():  # .....checking possible answer
    global sudoku
    global may_be_ans
    while True:
        p_sudoku = deepcopy(sudoku)
        for i in range(0, num_of_row_col):
            for j in range(0, num_of_row_col):
                if sudoku[i][j] == 0:
                    for k in range(num_of_row_col):  # ..... checking **row** for find answer
                        if k == j:
                            continue
                        if sudoku[i][k] != 0:
                            if sudoku[i][k] in may_be_ans[i][j]:
                                may_be_ans[i][j][sudoku[i][k] - 1] = 0
                    for k in range(num_of_row_col):  # ..... checking **column** for find answer
                        if k == i:
                            continue
                        if sudoku[k][j] != 0:
                            if sudoku[k][j] in may_be_ans[i][j]:
                                may_be_ans[i][j][sudoku[k][j] - 1] = 0
                    sqrt_num = int(math.sqrt(num_of_row_col))
                    block = [i // sqrt_num * sqrt_num, j // sqrt_num * sqrt_num]
                    for k in range(block[0], block[0] + sqrt_num):    # ..... checking **box** for find answer
                        for h in range(block[1], block[1] + sqrt_num):
                            if k == i and h == j:
                                continue
                            if sudoku[k][h] != 0:
                                if sudoku[k][h] in may_be_ans[i][j]:
                                    may_be_ans[i][j][sudoku[k][h] - 1] = 0
                flag, a = 0, 0
                for h in range(num_of_row_col):
                    if may_be_ans[i][j][h] == 0:
                        flag += 1
                    else:
                        a = may_be_ans[i][j][h]
                if flag == num_of_row_col - 1:
                    sudoku[i][j] = a       # ..... set answer of the cell
        done = True
        for i in range(num_of_row_col):
            if sudoku[i].count(0) > 0:
                done = False
                break
        if done:
            break
        if sudoku == p_sudoku:
            break


def solve_sudoku_func():
    global num_of_row_col, may_be_ans
    num_of_row_col = size
    global sudoku
    sudoku = [[None] * num_of_row_col for _ in range(num_of_row_col)]
    for i in range(num_of_row_col):  # ... create sudoku
        for j in range(num_of_row_col):
            if ents[i][j].get():
                sudoku[i][j] = int(ents[i][j].get())
            else:
                sudoku[i][j] = 0

    # .....This is a place to store possible answers
    may_be_ans = [[0] * num_of_row_col for _ in range(num_of_row_col)]
    for i in range(num_of_row_col):
        for j in range(num_of_row_col):
            may_be_ans[i][j] = list(x for x in range(1, num_of_row_col + 1))
    check_answer()
    back_track()
    for i in range(num_of_row_col):
        for j in range(num_of_row_col):
            ents[i][j].delete(0, tkinter.END)
            ents[i][j].insert(0, sudoku[i][j])


def build_func():
    global ye_flag, frm, size

    pad_size = 4     # ..... The amount of padding
    if size == 4:
        pad_size = 175
    elif size == 9:
        pad_size = 100
    elif size == 16:
        pad_size = 1

    if ye_flag:
        ye_flag = False
        frm = tkinter.Frame(main, bg='#8e9aaf')
        frm.grid(row=1, column=0, padx=5, pady=pad_size)
        global ents
        ents = []
        sqrt_size = math.sqrt(size)
        for i in range(size):
            ents.append([])
            if (i + 1) % sqrt_size == 0 and (i + 1) != size:
                pad_flag_x = 5
            else:
                pad_flag_x = 0
            for j in range(size):

                ents[i].append(tkinter.Entry(frm, width=5, justify='center'))
                if (j + 1) % sqrt_size == 0 and (j + 1) != size:
                    pad_flag_y = 5
                else:
                    pad_flag_y = 0
                ents[i][j].grid(row=i, column=j, pady=(0, pad_flag_x), padx=(0, pad_flag_y), ipady=7)
    # elif ye_flag:
    #     showinfo('ALERT!!!!', 'I told you type 4, 9 or 16')


def destroy_function():
    global ye_flag, frm
    if not ye_flag:
        frm.destroy()
        solve_btn['state'] = tkinter.DISABLED
        solve_btn['cursor'] = 'arrow'
        size_button_4['cursor'] = 'hand2'
        size_button_9['cursor'] = 'hand2'
        size_button_16['cursor'] = 'hand2'
        size_button_4['state'] = tkinter.NORMAL
        size_button_9['state'] = tkinter.NORMAL
        size_button_16['state'] = tkinter.NORMAL
        ye_flag = True


main = tkinter.Tk()
main.config()
background_image = tkinter.PhotoImage(file='./bg2.gif')
background_label = tkinter.Label(main, image=background_image, height=0, width=0)
background_label.place(x=0, y=0)
main.grid_columnconfigure(0, weight=1)

button_frame = tkinter.Frame(main, bg='#cbc0d3', highlightbackground='#8e9aaf', highlightthickness=3)
button_frame.grid(row=0, column=0, padx=5, pady=(5, 0), sticky='ew')

lbl = tkinter.Label(button_frame, text='Enter the Sudoku Size:', bg='#cbc0d3')
lbl.pack(side=tkinter.LEFT)

size_button_4 = tkinter.Button(button_frame, text='4', width=4, height=1, bg='#efd3d7',
                               cursor='hand2', command=set_size_func4, relief=tkinter.GROOVE, state=tkinter.NORMAL)
size_button_9 = tkinter.Button(button_frame, text='9', width=4, height=1, bg='#efd3d7',
                               cursor='hand2', command=set_size_func9, relief=tkinter.GROOVE, state=tkinter.NORMAL)
size_button_16 = tkinter.Button(button_frame, text='16', width=4, height=1, bg='#efd3d7',
                                cursor='hand2', command=set_size_func16, relief=tkinter.GROOVE, state=tkinter.NORMAL)
size_button_4.pack(side=tkinter.LEFT, padx=3, pady=3)
size_button_9.pack(side=tkinter.LEFT, padx=3, pady=3)
size_button_16.pack(side=tkinter.LEFT, padx=3, pady=3)

destroy_button = tkinter.Button(button_frame, text="Destroy", bg='#feeafa',
                                command=destroy_function, cursor='hand2', relief=tkinter.GROOVE)
destroy_button.pack(side=tkinter.RIGHT)

solve_btn = tkinter.Button(button_frame, text='solve', bg='#feeafa', command=solve_sudoku_func,
                           cursor='arrow', relief=tkinter.GROOVE, state=tkinter.DISABLED)
solve_btn.pack(side=tkinter.RIGHT)

main.geometry('600x600')
main.resizable(0, 0)
main.mainloop()
