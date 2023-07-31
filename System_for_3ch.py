import matplotlib.pyplot as plt


def final(new_quarter_1_2_3, new_quarter_1_3_4, new_quarter_1_2_4, new_quarter_2_3_4, bg_sdvig, a_f):
    fig = plt.figure()
    plt.xlabel("Width")
    plt.ylabel("Height")
    ax = fig.gca()

    # Отображение QPSK
    for i in range(len(bg_sdvig)):
        for j in range(4):
            if len(bg_sdvig[i]) > 0:
                name = f"{i}{j}"
                x = bg_sdvig[i][j][0]
                y = bg_sdvig[i][j][1]
                ax.plot(x, y, "o", color="b")
                plt.text(x, y, name, ha="center", va="bottom")
            else:
                continue
    ax.plot(x, y, color="b", label="Осн")

    # Отображение результата сложения I, II, III четвертей
    if a_f[0] != -1 and a_f[1] != -1 and a_f[2] != -1:
        if len(new_quarter_1_2_3) >= 4:
            for i in range(len(new_quarter_1_2_3)):
                x = new_quarter_1_2_3[i][0]
                y = new_quarter_1_2_3[i][1]
                ax.plot(x, y, "o", color="r")
            ax.plot(x, y, color="r", label='I+II+III')
        else:
            pass

    # Отображение результата сложения I, III, IV четвертей
    if a_f[0] != -1 and a_f[2] != -1 and a_f[3] != -1:
        if len(new_quarter_1_3_4) >= 4:
            for i in range(len(new_quarter_1_3_4)):
                x = new_quarter_1_3_4[i][0]
                y = new_quarter_1_3_4[i][1]
                ax.plot(x, y, "o", color="y")
            ax.plot(x, y, color="y", label='I+III+IV')
        else:
            pass

    # Отображение результата сложения I, II, IV четвертей
    if a_f[0] != -1 and a_f[1] != -1 and a_f[3] != -1:
        if len(new_quarter_1_2_4) >= 4:
            for i in range(len(new_quarter_1_2_4)):
                x = new_quarter_1_2_4[i][0]
                y = new_quarter_1_2_4[i][1]
                ax.plot(x, y, "o", color="m")
            ax.plot(x, y, color="m", label='I+II+IV')
        else:
            pass

    # Отображение результата сложения II, III, IV четвертей
    if a_f[1] != -1 and a_f[2] != -1 and a_f[3] != -1:
        if len(new_quarter_2_3_4) >= 4:
            for i in range(len(new_quarter_2_3_4)):
                x = new_quarter_2_3_4[i][0]
                y = new_quarter_2_3_4[i][1]
                ax.plot(x, y, "o", color="k")
            ax.plot(x, y, color="k", label='II+III+IV')
        else:
            pass

    plt.legend()
    plt.grid()
    plt.show()