import datetime
import subprocess

My_user = 'NRS'
now = datetime.datetime.now()
time = now.strftime("%Y-%m-%d_%H-%M") #Текущая дата и время с использованием strftime:

def getProjectName(argument):
    project = {
        1: "SEV",
        2: "KOV_ASU_TP_ESN",
        3: "KNG_PHG_VRK",
        4: "NOVOUB_ASUE",
        5: "NOVOURD_ASUE",
        6: "ZPLR_ASU_TP_ESN",
        7: "ZPLR_PRU",
        8: "ZPLR_SAU_BPG",
        9: "SOSN",
    }
    Project_name = project.get(argument, "Other_project")
    return Project_name

def getSonataVersion(argument):
    sonata = {
        1: "r10021",
        2: "r10223",
        3: "r7861",
        4: "r10255",
        5: "r10277",
        6: "r10301", 
    }
    Sonata_version = sonata.get(argument, "Other_version")
    return Sonata_version

def createProjectName(user, Project_attr, Sonata_attr):
    Project_name = getProjectName(Project_attr)
    Sonata_version = getSonataVersion(Sonata_attr)   
    
    print (user + '_' + Project_name + '_' + time + '_' + Sonata_version)
    result = user + '_' + Project_name + '_' + time + '_' + Sonata_version
    
    cmd='echo '+result.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

createProjectName(My_user, 3, 6)
