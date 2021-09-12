import json
import os
import subprocess
# import argparse # eventually make it so that this can be run from terminal, then eventually from Discord


# Loads the .json file for modlist
with open('mods.json', 'r') as f:
    mods = json.load(f)

steamcmd = 'D:/SteamCMD/steamcmd.exe'
username = 'capt_krakah'
	
# Checks if symlink already exists, if not creates the symlink for the mod and it's ID.
def create_link(src, tgt, mod, mod_id):
    if not os.path.islink(tgt):
        print(f"\nCreating symlink for {mod}, ID: {mod_id}")
        os.symlink(src, tgt, target_is_directory=True)
    else:
        print(f'\nSymlink for {mod}, ID: {mod_id} exists')


# Downloads the mod from SteamCMD, then uses create_link() to create a symlink
def update_mods(modlist=dict):
    for mod, mod_id in modlist.items():
        print(f"\nMod: {mod} (ID: {mod_id})\n")
        path = f'D:/SteamCMD/steamapps/workshop/content/107410/{mod_id}'
        target = f'D:/ArmaServer/@{mod}'
        subprocess.run([steamcmd, '+login', username, '+workshop_download_item', '107410', mod_id, 'validate', '+quit'], shell=True)
        create_link(path, target, mod, mod_id)


# allows you to update the mods.json file from the program itself
def modlist_update(name=str, mod_id=str):
	with open('mods.json', 'r') as readfile:
		data = json.load(readfile)

	x = {name: mod_id}
	data.update(x)
	readfile.close()
	
	with open('mods.json', 'w') as outfile:
		json.dump(data, outfile, indent=2)
	outfile.close()
	
	path = f'D:/SteamCMD/steamapps/workshop/content/107410/{mod_id}'
	target = f'D:/ArmaServer/@{name}'
	subprocess.run([steamcmd, '+login', username, '+workshop_download_item', '107410', mod_id, 'validate', '+quit'], shell=True)
	create_link(path, target, name, mod_id)

# modlist_update("Community Factions Project (CFP)",  "1369691841")
update_mods(mods)
