import os
import shutil as shu
import pickle
from tkinter import *
from tkinter import messagebox, filedialog

root = Tk(className="PanManager") # Имя окна
photo = PhotoImage(file = "icon2.png")
root.iconphoto(False, photo)

root.resizable(False, False)      # я запрещаю вам растягивать окно


def main(path):
    lbox = Listbox(width = 50, heigh = 4) # Размеры списка
    lbox.pack() # Пакуем под окно

    def selected_item():
        # Traverse the tuple returned by
        # curselection method and print
        # corresponding value(s) in the listbox
        for i in lbox.curselection():
            global name
            name = (lbox.get(i))
            

     


    
    pckl = Button(root, text="Select Among Us installation", command=AmongFolderChange) 
    pckl.pack(anchor="se")

    crewlink = BooleanVar() #Boolean = True/False, делаем переменную булеаном
    crewlink.set(0)
    cb = Checkbutton(text="Crewlink enable", variable=crewlink, onvalue=1) #Создаем поле с галочкой и ставим под переменной наш crewlink
    cb.pack(anchor="se")   #Пакуем/Закрепляем его на Юго восток                         #Даем 2 значения (1 и 0/True и False)

    mods = os.listdir("mods") # Сканим папку с модами на имена модов (папок)

    for i in mods:            # Вставляем имена папок/модов в список
        lbox.insert(0,i)

    def launchmod(name, path, crewlink):
        fullname = os.path.join("mods\\" + str(name))    #Обьеденяем имя папки/мода и пути до папки с модами/папками
        exepath = os.path.join(path + "/Among Us.exe")
        exepath = '"{0}"'.format(exepath)                #Добавляем форматом ковычки. P.S. ковычки в ковычках можно сделать так:
                                                         # """ "в 3 ковычках" """, '"Большие в маленьких"', "\"https://stackoverflow.com/questions/9050355/using-quotation-marks-inside-quotation-marks\""
        shu.rmtree(path)                          #Удаляем предыдущий мод
        shu.copytree("other\\Among Us", path, dirs_exist_ok=True) #Копируем и вставляем ВСЕ файлы игры
        shu.copytree(fullname, path, dirs_exist_ok=True)              #Ctrl-C, Ctrl-V файлы мода
        if crewlink.get() == True:                                    #True/False получается только методом get, в других случаях всегда PY_VAR 0
            os.system("other\\Crewlink\\CrewLink.exe")
        else:
            os.system(exepath)
        quit()

    btn = Button(root, text='Start', command=lambda:[selected_item(), launchmod(name,path,crewlink)])                      #         launchmod(name, path, crewlink))
    btn.pack(side="bottom") # Placing the button (пакуем)

    #def check():
        #print(crewlink.get())

    #btn = Button(root, text='check', command=check)#launchmod(name,path,crewlink)])                      #         launchmod(name, path, crewlink))
    #btn.pack(side="bottom") # Placing the button (пакуем)

    

    root.mainloop()



def AmongFolder():
    messagebox.showerror("Cant find Among Us folder", "Please, select a folder with Among Us installation")
    path = filedialog.askdirectory()
    pathlog = open("path", "wb")
    pickle.dump(path, pathlog)
    pathlog.close()
    return(path)
def AmongFolderChange():
    path = filedialog.askdirectory()
    pathlog = open("path", "wb")
    pickle.dump(path, pathlog)
    pathlog.close()
    path = pickle.load(open("path", "rb"))
    messagebox.showinfo("Information","The changes will apply after app restart")
    return(path)



 
try:
	path = pickle.load(open("path", "rb"))
except:
	path = AmongFolder()
	main(path)


default_path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Among Us" #Хард код
if os.path.isdir(default_path) == True:
    main(default_path)
elif os.path.isdir(path) == True:
    main(path)
else:
    main(AmongFolder())


# https://www.geeksforgeeks.org/how-to-get-selected-value-from-listbox-in-tkinter/
# Метод получения названия папки/мода
