import json
import pyautogui
import time
import logging

#============================================
#           Parametros / Variables
#============================================
teamSize=5
mpTimer=90

caster = ["- Aria", "Dyslepus"]
currentCaster = 1

currentTeam = "Red"
red_team_name=""
red_team_points=0
red_team_protect=[]
red_team_bans=[]

blue_team_name=""
blue_team_points=0
blue_team_protect=[]
blue_team_bans=[]

# ROLL
red_roll=0
blue_roll=0

mappool_modes=[]
pickModes=[]
mode_Pick="NM"

midPick=False
midPoint=3

#============================================
#            Métodos / Funciones
#============================================
def red():
    return "Red" or "R"
def blue():
    return "Blue" or "B"

def titleDivider(header):
    return print(f"\n\t {"="*len(header)}\n\t {header}\n\t {"="*len(header)}\n")
def setNumber(setValue=0, prompt=""):
    if (prompt!=""):
        if prompt[0]!=str(setValue):
            return int(prompt[0])
        elif prompt is not int:
            return prompt
    return setValue

def timeToClickOnc4o(command="!mp settings", delay=3.5, enter=False, type="debug", value=""):
    if (command!="" or command!=None):
#       if (type == "debug"):
#           logging
        print(f"[{int(delay)}s de delay]  ►> {command}")
        time.sleep(delay)
        pyautogui.write(command)
        time.sleep(0.1)
        if (enter):
            pyautogui.press('enter')
            pyautogui.hotkey(['ctrl', 'a', 'delete'])
        if (type == "waiter"):
            input(f"► {value} Presionar ENTER para continuar ▼ ")
        elif (type == "title"):
            titleDivider(value)
    else:
        time.sleep(delay)
    return enter

def teamTurn(recentTeam="Red", boolMode=False, display_name=False):
    if (recentTeam=="Red"): # Es Rojo antes de este cambio de turno
        recentTeam="Blue" # Alterna a azul
        if (not boolMode):
            return recentTeam
        return False
        # Es Azul
    if (recentTeam=="Blue"): # Es Azul antes de este cambio de turno
        recentTeam="Red" # Alterna a rojo
        if (not boolMode):
            return recentTeam
        return True
        # Es Rojo
    return recentTeam

def roll(currentTeamRoll="Red", previousTeamRoll=-1):
    numberTeamRoll = input(f"{currentTeamRoll} Roll: ")
    if (numberTeamRoll==""):
        numberTeamRoll=0
    numberTeamRoll = int(numberTeamRoll)
    if numberTeamRoll!=previousTeamRoll:
        if numberTeamRoll >= 100:
            return currentTeamRoll
        elif (previousTeamRoll!=-1): # Chequea
            if numberTeamRoll<previousTeamRoll: # Si el segundo roll es menor que el primero.
                # Comprueba quien mandaa este 2do roll e indica el team contrario, el primer rool gana
                if (currentTeamRoll=="Blue"):
                    currentTeamRoll="Red"
                else:
                    currentTeamRoll="Blue"
            print(f" > {currentTeamRoll} Team Win")
            return currentTeamRoll
        return roll(teamTurn(currentTeamRoll), numberTeamRoll)
    else:
        print("Empate.\nHaciendo Reroll")
        currentTeamRoll = roll(currentTeamRoll)
    return currentTeamRoll

def enumerationPlayer(listPlayers):
    for playerID, player in enumerate(listPlayers):
        print(f" {playerID}: {player}")

def sethost(currentTeam="Red", teams=list[list[teamSize], list[teamSize]], lastHost=False):
    currentRooster = teams[int(teamTurn(currentTeam, True))]
    print(f"Jugadores de Team {currentTeam}:")
    enumerationPlayer(currentRooster)
    captain = input(f"Presiona ENTER para hacer host a {currentRooster[0]} \n Sino puedes hacer host otro de {currentTeam} Team con el número: ")

    if not (captain in range(len(currentRooster)) or captain!=""): # Si se sale del index del rooster antes mostrado
        captain = 0
    timeToClickOnc4o(f"!mp host {currentRooster[int(captain)]}", 2, True, "waiter", f"En espera a que acabe el WarmUp de Team {currentTeam} y dar paso a los pick del Team {teamTurn(currentTeam)}\n")
    if (lastHost): # Si con este ya fue host segundo team retornar el team contrario con el metodo sistema de turnos.
        return teamTurn(currentTeam)
    return sethost(teamTurn(currentTeam), teams, True)
    
def pickMessage(word="", isStarted=True):
    global currentTeam
    timeToClickOnc4o(f"{"-"*(len(currentTeam) + 6 + len(word))}", 1.75, True)
    timeToClickOnc4o(f"{currentTeam} Team {word}", 0.45, True)
    timeToClickOnc4o(f"!mp timer {mpTimer}", 0.45, True)
    timeToClickOnc4o(f"", 2.5)
    currentMode = input(f" {currentTeam} Team pickeó  ►  ").upper()
    timeToClickOnc4o(f"\n!mp aborttimer", 4, True)
    global mappool_modes
    if (isStarted):
        isPickable(mappool_modes, currentMode)
        return currentMode
    else:
        if (currentTeam == "Red"):
            global red_team_protect, red_team_bans
            if (word == "Protect"):
                isPickable(red_team_protect, currentMode)
            elif (word == "Ban"):
                isPickable(red_team_bans, currentMode)
        elif currentTeam == "Blue":
            global blue_team_protect, blue_team_bans
            if (word == "Protect"):
                isPickable(blue_team_protect, currentMode)
            elif (word == "Ban"):
                isPickable(blue_team_bans, currentMode)
        
    return teamTurn(currentTeam)

def teamListate(team_acronym, team_region=list):
    if (team_acronym in teams_data[team_region[1]]):
        team_region.reverse()
    return team_region

def set_team():
    team_region = []
    # Imprimir acrónimos y nombres de equipos
    for teams_setup, teams in teams_data.items():
        print(f"\n{teams_setup}")
        team_region.append(teams_setup)
        for team_acronym, team in teams.items():
            team_name = team[0]['Name']
            print(f" {team_acronym}\t► {team_name}")

    # Obtener los acrónimos de los equipos ingresados por el usuario
    red_team_acronym = input("> Ingrese el acrónimo del equipo rojo: ").upper()
    blue_team_acronym = input("> Ingrese el acrónimo del equipo azul: ").upper()
    
    # Verificar si los acrónimos ingresados existen en el JSON
    if not ((red_team_acronym in teams_data["CountryTeams"] and blue_team_acronym in teams_data["CountryTeams"]) or (red_team_acronym in teams_data["AkademiaTeams"] and blue_team_acronym in teams_data["AkademiaTeams"])):
    #else:
        print("Uno o ambos acrónimos de equipos ingresados no existen en el JSON.")
        return set_team()
    
    # Obtener los nombres de los jugadores de los equipos seleccionados
    red_players = teams_data[teamListate(red_team_acronym, team_region)][red_team_acronym][1]
    blue_players = teams_data[teamListate(blue_team_acronym, team_region)][blue_team_acronym][1]
    
    global red_team_name, blue_team_name
    # Obtener los nombres de los equipos
    red_team_name = teams_data[team_region][red_team_acronym][0]["Name"]
    blue_team_name = teams_data[team_region][blue_team_acronym][0]["Name"]
    # Imprimir la cadena final
    timeToClickOnc4o(f"!mp make {match_acronym}: ({red_team_name}) vs ({blue_team_name})", 3.5, True, "", "Ya creado. Ir al canal de la match\n ")
    pyautogui.hotkey(['ctrl', 'shift', 'tab'])
    timeToClickOnc4o(f"\n!mp addref - Aria", 0.9, True)
    timeToClickOnc4o(f"!mp set 2 3 {teamSize*2}", 0.9, True)
    timeToClickOnc4o(f"!mp addref {caster[currentCaster]}", 10, True)
    enterFlag="los jugadores"
    if(input(f"▼ Presionar ENTER para continuar\n\tinvitar {enterFlag} a la match ▼ ") != ""):
        enterFlag="Bartra por si acaso\n!mp invite MisterBartra\n" # Se pedía solo poner ENTER
    timeToClickOnc4o(f"Invitando a {enterFlag}", 3, True)
    # Jugadores del equipo rojo
    for player in red_players:
        timeToClickOnc4o(f"!mp invite {player}", 0.45, True)
    # Imprimir los jugadores del equipo azul
    for player in blue_players:
        timeToClickOnc4o(f"!mp invite {player}", 0.45, True)
    time.sleep(4)
    timeToClickOnc4o("\n", 6, False, "waiter", "Si todo está conforme con el orden en la sala, iniciamos el protocolo\n")
    timeToClickOnc4o("Comenzamos", 3, True)
    timeToClickOnc4o("Por favor, capitanes hacer !roll", 0.45, True)
    
    first_roll = input("\nEl primer Roll lo hizo Red(R) or Blue(B) team: ").lower()
    if (first_roll != "blue" and first_roll != "b"):
        first_roll = "Red"
    else:
        first_roll = "Blue"
    currentTeam = roll(first_roll)
    # WarmUp
    return sethost(currentTeam, [red_players, blue_players])

def findModes(mappool_data):
    modesList = []
    for mode, maps in mappool_data.items():
        for i in range(1, len(maps) + 1):
            modesList.append(f"{mode}{i}")
    return modesList

def isPickable(pickList=list, mode="NM"):
    # Verificar si el modo ya ha sido elegido previamente
    if mode not in pickList:
        pickList.append(mode) # Agregar el modo al arreglo de modos elegidos
        print(pickList)
        return pickList
    else:
        print(pickList)
        return False

def displayRemainingPicks():
    global mappool_modes, pickModes
    
    # Calcular los modos que no han sido elegidos
    remainingPicks = set(mappool_modes) - set(pickModes)
    
    # Imprimir los modos que no han sido elegidos
    print("Modos aún no elegidos:")
    for mode in remainingPicks:
        print(mode)
    print(f"{remainingPicks}")


def previusPick():
    global currentTeam
    if (midPick):
        timeToClickOnc4o(f"Iniciamos el segundo tiempo", 3.5)
    currentTeam = pickMessage("Protect", False)
    currentTeam = pickMessage("Protect", False)
    currentTeam = pickMessage("Ban", False)
    currentTeam = pickMessage("Ban", False)
    return currentTeam

def teamPickTimeBreak(point=0):
    global red_team_points, blue_team_points
    return red_team_points==point or blue_team_points==point

def selectMap():
    if (teamPickTimeBreak(midPoint) and midPick):
        previusPick()
    timeToClickOnc4o(f"", 3.5)
    global red_team_name, red_team_points, blue_team_points, blue_team_name
    timeToClickOnc4o(f"{red_team_name} : {red_team_points} - {blue_team_points} : {blue_team_name}", 2.5, True)
    # Obtener el input del usuario y convertir a mayúsculas para que coincida con la clave del JSON
    mode_Pick = pickMessage("Pick \u0016")
    # Verificar si la clave existe en el JSON
    global currentTeam, mappool_data
    if mode_Pick in mappool_modes:
    #if mode_Pick in mappool_modes:
        if (isPickable(mappool_modes, mode_Pick)):
            displayRemainingPicks()
            timeToClickOnc4o("", 2)
            # Obtener el índice del elemento deseado (restar 1 ya que los índices comienzan desde 0)
            mode_PickID = int(mode_Pick[2:]) - 1
            if (len(mode_Pick) < 2):
                mode_PickID = 0
            # Número de mod
            timeToClickOnc4o(f"!mp mods {mods_data['NF'][mode_Pick[0:2]][mode_PickID]}", 0.45, True)
            # Valor correspondiente del modo
            timeToClickOnc4o(f"!mp map {mappool_data[mode_Pick[0:2]][mode_PickID]}", 0.45, True)

            addPoint(input("Quien ganó? Red o Blue team: ").lower())
            return teamTurn(currentTeam)
        else:
            print(f"No se puede pickear el {mode_Pick}")
            return teamTurn(teamTurn(currentTeam))
    else:
        print(f"No se puede pickear el {mode_Pick}")
        selectMap()

def addPoint(teamWin):
    global red_team_points, blue_team_points
    if (teamWin == red()):
        red_team_points=red_team_points+1
    elif (teamWin == blue()):
        blue_team_points=blue_team_points+1


#============================================
#              Flujo de Referi
#============================================
print(f"\n{"######"*10}\n\nImportante: Esto simula directamente la pulsación de teclas !\n Siendo prudente tener el foco de escritura el campo del chat4osu\n\t  para la digitación de PyAutoGUI.\n  En caso no tuvieran foco en algún area para texto, mover inmediatamente\n\t el cursor del mouse hacia alguna de las esquinas de la pantalla.\n\n{"######"*9}\n\n\n")
titleDivider("Preparación de la match")
# Definir Caster
enumerationPlayer(caster)
currentCaster = setNumber(currentCaster, input("\n> Reasignar caster: "))
# Ingresar el acronimo de sala
mpTimer = setNumber(90, input("El !mp timer para esta match será 90s automáticamete\n Se puede cambiar con el valor de "))
match_slots = setNumber(3, input("TeamVS Sv2 Slots Formato de "))
match_point = setNumber(5, input("> El MatchPoint es al punto 5to punto si no se define un numero diferente "))
match_acronym = input("> Ingrese el acronimo de sala: ").upper()

timeToClickOnc4o("", 0.45)


# Cargar el JSON desde un archivo externo
with open("data/mods.json", encoding="utf-8") as json_file:
    mods_data = json.load(json_file)

with open("data/teams.json", encoding="utf-8") as json_file:
    teams_data = json.load(json_file)

with open("data/mapPool.json", encoding="utf-8") as json_file:
    mappool_data = json.load(json_file)

mappool_modes = findModes(mappool_data)

currentTeam = set_team()

timeToClickOnc4o(f"!mp clearhost", 5, True)
print(f"\tMapPool: {mappool_modes}")
titleDivider("Comienzo del enfrentamiento")

timeToClickOnc4o(f"", 2)
previusPick()
while (red_team_points < match_point or blue_team_points < match_point):
    currentTeam = selectMap()
print(f"{currentTeam} ha ganado la Partida !\n Terminando proceso.")
time.sleep(10)