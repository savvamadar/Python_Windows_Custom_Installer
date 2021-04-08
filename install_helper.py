#from Savva to Liza
#savva.madar@gmail.com

#!/usr/bin/env python
import subprocess
import os
import ctypes
import sys
import easygui
import pyautogui
import time


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


game_arr = [
    {
        'name': 'Freddi Fish 1 - Case of the Missing Kelp Seeds',
        'install': './Ffish1/Setup.exe',
        'install_command': '',
        'compatibility':'',
        'default_loc': '/Program Files (x86)/Freddi Fish/Freddi1/',
        'default_exe': 'FREDDI.EXE',
        'needs_commands': True,
        'monitor': True,
        'commands': [
                'cmd /c "rename \"%dir%%exe%\" \"%exe%.BAK\""',
                'cmd /c "rename \"%dir%FREDDI.W32\" \"FREDDI.EXE\""'
        ]
    },
    {
        'name': 'Freddi Fish 2 - Case of the Haunted Schoolhouse',
        'install': './Ffish2/Setup.exe',
        'install_command': '',
        'compatibility':'',
        'default_loc': '/Program Files (x86)/Freddi Fish/Freddi2/',
        'default_exe': 'FreddiCHSH.exe',
        'needs_commands': False,
        'monitor': True,
        'commands': []
    },
    {
        'name': 'Freddi Fish 3 - Case of the Stolen Conch Shell',
        'install': './Ffish3/Setup.exe',
        'install_command': '',
        'compatibility':'',
        'default_loc': '/Program Files (x86)/Freddi Fish/Freddi3/',
        'default_exe': 'FreddiSCS.EXE',
        'needs_commands': False,
        'monitor': True,
        'commands': []
    },
    {
        'name': 'Freddi Fish 4 - Case of the Hogfish Rustlers of Briny Gulch',
        'install': './Ffish4/Setup.exe',
        'install_command': '',
        'compatibility':'',
        'default_loc': '/Program Files (x86)/Freddi Fish/Freddi4/',
        'default_exe': 'Freddihrbg.exe',
        'needs_commands': False,
        'monitor': True,
        'commands': []
    },
    {
        'name': 'Freddi Fish 5 - Case of the Creature of Coral Cove',
        'install': './Ffish5/Setup.exe',
        'install_command': '',
        'compatibility':'',
        'default_loc': '/Program Files (x86)/Freddi Fish/Freddi5/',
        'default_exe': 'FreddiCCC.EXE',
        'needs_commands': False,
        'monitor': True,
        'commands': []
    },
    {
        'name': 'Freddi Fish 6 - Water Worries',
        'install': './Ffish6/Setup.exe',
        'install_command': '',
        'compatibility':'',
        'default_loc': '/Program Files (x86)/Freddi Fish/Freddi6/',
        'default_exe': 'WATER.EXE',
        'needs_commands': True,
        'monitor': True,
        'commands': [
                'cmd /c "rename \"%dir%%exe%\" \"%exe%.BAK\""',
                'cmd /c "rename \"%dir%WATER.W32\" \"WATER.EXE\""'
        ]
    },
    {
        'name': 'LEGO Island 2',
        'install': './LegoIsland2/LEGO Island 2/Setup.exe',
        'install_command': '',
        'compatibility':'',
        'default_loc': '/Program Files (x86)/LEGO Media/LEGO Island 2/',
        'default_exe': 'LEGO Island 2.exe',
        'needs_commands': True,
        'monitor': True,
        'commands': [
                'cmd /c "rename \"%dir%%exe%\" \"%exe%.BAK\""',
                'cmd /c "copy \".\LegoIsland2\LEGO Island 2.exe.PATCHED\" \"%dir%LEGO Island 2.exe\""',
                'cmd /c "start \"%dir%\""'
        ]
    },
    {
        'name': 'Cliffords Birthday',
        'install': '',
        'install_command': 'cmd /c "cd .\Clifford & setup.exe"',
        'compatibility':'',
        'default_loc': "/Program Files/Scholastic's Clifford/Clifford Adventure/",
        'default_exe': 'Clifford.exe',
        'needs_commands': True,
        'monitor': True,
        'commands': [
            'cmd /c "start \"%dir%\""'
        ]
    },
    {
        'name': 'Lego Racers 2',
        'install': './LegoRacers2/Install/Setup.exe',
        'install_command': '',
        'compatibility':'WinXP',
        'default_loc': "/Program Files (x86)/LEGO Media/LEGO Racers 2/",
        'default_exe': 'LEGO Racers 2.exe',
        'needs_commands': True,
        'monitor': True,
        'commands': [
            'cmd /c "rename \"%dir%%exe%\" \"%exe%.BAK\""',
            'cmd /c "copy \".\LegoRacers2\Patch\LEGO Racers 2.exe\" \"%dir%LEGO Racers 2.exe\""',
            'cmd /c "rd /s /q \"%dir%game data\""',
            'cmd /c "Xcopy /E /I \".\LegoRacers2\Patch\game data\" \"%dir%game data\""',
            'cmd /c "start \"%dir%\""'
        ]
    },
    {
        'name': "American McGee's Alice",
        'install': '',
        'install_command': 'cmd /c "copy \".\Alice\Alice.zip\" \"%temp%\Alice.zip\" & unzip.bat \"%temp%\Alice.zip\" \"%dir%\" & delete.bat \"%temp%\Alice.zip\""',
        'compatibility':'',
        'default_loc': "/Program Files (x86)/Alice/",
        'default_exe': 'alice.exe',
        'needs_commands': True,
        'monitor': True,
        'commands': [
            'cmd /c "start \"%dir%\""'
        ]
    },
    {
        'name': "The ClueFinders 4th Grade Adventures: Puzzle of the Pyramid",
        'install': './ClueFinders4/Play.exe',
        'install_command': '',
        'compatibility':'',
        'default_loc': "/Program Files (x86)/The Learning Company/ClueFinders(R) 4th Grade Adventures/",
        'default_exe': '4thadv32.exe',
        'needs_commands': False,
        'monitor': False,
        'commands': [
        ]
    },
    {
        'name': "The ClueFinders 5th Grade Adventures: Secret of the Living Volcano",
        'install': './ClueFinders5/INSTALL/setup32.exe',
        'install_command': '',
        'compatibility':'',
        'default_loc': "/Program Files (x86)/The Learning Company/The ClueFinders 5th Grade Adventures/",
        'default_exe': '5thad32.exe',
        'needs_commands': False,
        'monitor': False,
        'commands': [
        ]
    },
    {
        'name': "Pet Racer",
        'install': './PetRacer/Setup.exe',
        'install_command': '',
        'compatibility':'',
        'default_loc': "/Program Files (x86)/Big City Games/Pet Racer/",
        'default_exe': 'PetRacer.exe',
        'needs_commands': True,
        'monitor': True,
        'commands': [
            'cmd /c "start \"%dir%\""'
        ]
    }
]


if is_admin():
    did_choose_exit = False
    removed_options = []
    while not did_choose_exit:
        
        original_compat = os.environ.get("__COMPAT_LAYER",None)
        if original_compat:
            os.environ.pop("__COMPAT_LAYER")
            
        print("\n\nChoose a game to Install:\n")
        choice_itter = 0
        for game in game_arr:
            choice_itter += 1
            if not choice_itter in removed_options:
                print(f"{choice_itter}) {game['name']}\n")

        print("99) Exit\n")

    
        choice = 0
        while choice <= 0 or choice > len(game_arr):
            try:
                choice = input(f"Game to install (1-99): ")
                choice = int(choice)
            except:
                choice = 0

            if choice in removed_options:
                choice = 0
                
            if choice <= 0 or choice > len(game_arr):
                if choice == 99:
                    did_choose_exit = True
                    sys.exit("Bye!")
                else:
                    print("Invalid choice")
        if True: #too lazy to untab
            choice = choice - 1

            os.environ.update({"__COMPAT_LAYER": game_arr[choice]['compatibility']})

            default_drive = os.getenv('SystemDrive')

            install_loc = default_drive + game_arr[choice]['default_loc']
            install_exe = game_arr[choice]['default_exe']
            abs_dir = os.getcwd()

            if game_arr[choice]['install_command'] != '':
                install_loc_altered = install_loc.replace('/', '\\')
                altered_command = game_arr[choice]['install_command'].replace('%dir%', install_loc_altered)
                altered_command = altered_command.replace('%exe%', install_exe)
                altered_command = altered_command.replace('%diskdir%', abs_dir)
                altered_command = altered_command.replace(':\\\\',':\\')
                print(altered_command)
                print(abs_dir)
                print("Please wait...")
                os.system(altered_command)
            else:
                process = subprocess.Popen(game_arr[choice]['install'], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                should_monitor = game_arr[choice]['monitor']
                while should_monitor:
                    output, err = process.communicate()
                    status = process.returncode
                    if not status:
                        time.sleep(0.5)
                        break

                if not should_monitor:
                    time.sleep(2)


            attempts = 0
            if game_arr[choice]['needs_commands']:
                files_found = False
                while not files_found:
                    files_found = (os.path.isdir(install_loc) and os.path.isfile(install_loc+install_exe))
                    if not files_found:
                        pyautogui.alert(text=f"{game_arr[choice]['default_exe']} NOT FOUND\n\n\nPlease select {game_arr[choice]['default_exe']} from where you installed the game.\n\n\nNormally this would be:\n{install_loc+game_arr[choice]['default_exe']}", title=f"Can't find {game_arr[choice]['default_exe']}")
                        selected_exe = easygui.fileopenbox(default=f'{install_loc}*.exe', filetypes=["*.exe"])
                        if selected_exe:
                            install_exe = selected_exe[selected_exe.rfind("\\")+1:]
                            install_loc = selected_exe[:selected_exe.rfind("\\")+1]
                        else:
                            attempts += 1
                            if attempts >= 2:
                                pyautogui.alert(text=f"{game_arr[choice]['name']} was not successfully installed.\n\nRefer to manual_install.txt", title=f"Can't find {game_arr[choice]['default_exe']}")
                                sys.exit("manual_install.txt")

                install_loc_altered = install_loc.replace('/', '\\')
                for command in game_arr[choice]['commands']:
                    altered_command = command.replace('%dir%', install_loc_altered)
                    altered_command = altered_command.replace('%exe%', install_exe)
                    altered_command = altered_command.replace('%diskdir%', abs_dir)
                    altered_command = altered_command.replace(':\\\\',':\\')
                    print("Please wait...")
                    os.system(altered_command)

                print("Please wait...")
                subprocess.Popen(f'explorer /select,"{install_loc_altered+game_arr[choice]["default_exe"]}"')

            removed_options.append(choice+1)
            print(f"\n\nFinished installing {game_arr[choice]['name']}\n")

else:
    print("Is not admin")
    argv = sys.argv

    if len(argv) > 1:
        argv = argv[1:]
        print("Standalone")

    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(argv), None, 1)
    sys.exit("Starting as admin...")
