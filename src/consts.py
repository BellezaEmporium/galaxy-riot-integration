import os, winreg


class GameID:
    league_of_legends = "league_of_legends"
    legends_of_runeterra = "bacon"
    valorant = "valorant"
    vanguard = "vanguard"  # anti-cheat for valorant & league
    twoxko = "project-l" # closed beta, wait oct. 7 for public beta. potential name, not sure


GAME_IDS = [GameID.legends_of_runeterra, GameID.league_of_legends, GameID.valorant, GameID.twoxko]
# Registry info is still needed to detect Vanguard.
REGISTRY_START_PATHS = [winreg.HKEY_CURRENT_USER, winreg.HKEY_LOCAL_MACHINE]
SOFTWARE_PATHS = ["SOFTWARE\\", "SOFTWARE\\WOW6432Node\\"]
UNINSTALL_REGISTRY_PATH = "Microsoft\\Windows\\CurrentVersion\\Uninstall\\"
GAME_REGISTRY_PATH = {
    GameID.league_of_legends: "Riot Game league_of_legends.live",
    GameID.legends_of_runeterra: "Riot Game bacon.live",
    GameID.valorant: "Riot Game valorant.live",
    GameID.twoxko: "Riot Game project-l.live",
    "vanguard": "Riot Vanguard",
}
UNINSTALL_STRING_KEY = "UninstallString"
INSTALL_LOCATION_KEY = "InstallLocation"
DOWNLOAD_URL = {
    GameID.league_of_legends: "https://lol.secure.dyn.riotcdn.net/channels/public/x/installer/current/live.na.exe",  # noqa: E501
    GameID.legends_of_runeterra: "https://bacon.secure.dyn.riotcdn.net/channels/public/x/installer/current/live.exe",  # noqa: E501
    GameID.valorant: "https://valorant.secure.dyn.riotcdn.net/channels/public/x/installer/current/live.live.eu.exe",  # noqa: E501
    GameID.twoxko: "https://project-l.secure.dyn.riotcdn.net/channels/public/x/installer/current/live.exe" # invalid link for now, noqa: E501
}
LOCAL_FILE_CACHE = os.path.expandvars(
    "%LOCALAPPDATA%\\GOG.com\\Galaxy\\plugins\\installed\\riot_play_time_cache.txt"
)

# path of the Riot Client settings yaml file.
RIOT_CLIENT_INSTALLS_PATH = os.path.expandvars("%PROGRAMDATA%\\Riot Games\\RiotClientInstalls.json")

VANGUARD_INSTALL_LOCATION = os.path.abspath(os.path.expandvars("%programfiles%/Riot Vanguard"))
