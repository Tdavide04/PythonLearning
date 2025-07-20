import requests
import json

# Configurazione
API_KEY = ""  # Sostituisci con la tua chiave API
STEAM_ID = "" # Sostituisci con il tuo Steam ID
APP_ID = 236850 # ID di Europa Universalis IV su Steam
OUTPUT_FILE = "ScrapingSteam/missing_achievements.txt"

# Funzione per ottenere gli achievement del giocatore
def get_player_achievements(api_key, steam_id, app_id):
    url = "https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v1/"
    params = {
        "key": api_key,
        "steamid": steam_id,
        "appid": app_id,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Errore: {response.status_code} - {response.text}")
        return None

# Funzione per ottenere i dettagli degli achievement globali
def get_global_achievements(api_key, app_id):
    url = "https://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/"
    params = {
        "key": api_key,
        "appid": app_id,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Errore: {response.status_code} - {response.text}")
        return None

# Funzione principale
def main():
    print("Recupero gli achievement del giocatore...")
    player_data = get_player_achievements(API_KEY, STEAM_ID, APP_ID)
    if not player_data or "playerstats" not in player_data or "achievements" not in player_data["playerstats"]:
        print("Impossibile recuperare gli achievement del giocatore.")
        return

    print("Recupero i dettagli globali degli achievement...")
    global_data = get_global_achievements(API_KEY, APP_ID)
    if not global_data or "game" not in global_data or "availableGameStats" not in global_data["game"] or "achievements" not in global_data["game"]["availableGameStats"]:
        print("Impossibile recuperare i dettagli globali degli achievement.")
        return

    player_achievements = {ach["apiname"]: ach["achieved"] for ach in player_data["playerstats"]["achievements"]}
    global_achievements = {ach["name"]: ach["displayName"] for ach in global_data["game"]["availableGameStats"]["achievements"]}

    # Trova gli achievement mancanti
    missing_achievements = [
        global_achievements[api_name]
        for api_name, achieved in player_achievements.items()
        if achieved == 0 and api_name in global_achievements
    ]

    # Scrivi i risultati in un file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("Achievement mancanti in Europa Universalis IV:\n\n")
        for achievement in missing_achievements:
            f.write(f"- {achievement}\n")

    print(f"File generato: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
