from model import show_vacancy, new_vacancy
from view import show_menu as ui


def controller():
    position = -1
    while position != 9:
        position = ui()
        match position:
            case 1:
                new_vacancy()
            case 2:
                show_vacancy()
    else:
        print("\t========== Конец работы ==========")
