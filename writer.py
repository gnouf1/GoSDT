import os
import pathlib


def create_doc(project_root, lst_FSC):
    newpath = project_root+"\\doc"
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    for file in lst_FSC:
        P = file.path
        P = P.replace(project_root, newpath)

        P = P.replace(".py", ".md")

        if os.path.isfile(P) is False:
            try:
                    fichier = open(P, 'w')
            except FileNotFoundError:
                os.makedirs(pathlib.Path(P).parent)
                fichier = open(P, 'w')

            ecriture = "# "+file.name.replace(".py", "") + " \n"

            for cl in file.lstClassO:
                ecriture += "## "+cl.name+"\n\n"
                for met in cl.lstMeth:
                    ecriture += "### "+met+"\n\n"

            for fun in file.lstFunc:
                ecriture += "## "+fun+"\n\n"

            fichier.write(ecriture)
