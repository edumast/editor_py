#!/usr/bin/env python
import os
enter_in_app="editor"
cod_definity_editor=""
select_file_option=input("1.create  2.enter")
select_file=input("which file?")
if (select_file_option=="1"):
    os.system("touch softwares/software_app/editor_py/data_editor/%s" %(select_file))
if (select_file_option=="2"):
    os.system("cat softwares/software_app/editor_py/data_editor/%s" %(select_file))
file=("softwares/software_app/editor_py/data_editor/")+(select_file)
while(enter_in_app=="editor"):
    cod_definity_editor=cod_definity_editor
    cod_editor=input("")
    cod_editor=cod_editor
    if (cod_editor=="save"):
        file=open(str(file), "a")
        file.write(cod_definity_editor)
        file=open(str(file), "a")
        print("finaly")
        cod_editor=""
    if (cod_definity_editor==""):
        cod_definity_editor=(cod_editor)
    else:
        cod_definity_editor=(cod_definity_editor)+"\n"+(cod_editor)
