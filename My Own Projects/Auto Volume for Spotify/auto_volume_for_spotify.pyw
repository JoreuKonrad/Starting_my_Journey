import time
import threading
import os
import comtypes
from PIL import Image, ImageDraw
import pystray
from pycaw.pycaw import AudioUtilities, IAudioMeterInformation

# Configurações Iniciais
config = {
    "VOLUME_REDUZIDO": 0.6,
    "VOLUME_NORMAL": 1.0,
    "APP_ALVO": "spotify.exe",
    "APPS_GATILHO": ["chrome.exe", "msedge.exe", "firefox.exe", "brave.exe", "opera.exe"],
    "TOLERANCIA_SEGUNDOS": 3.0,
    "STANDBY": False
}

def monitorar_audio():
    comtypes.CoInitialize()
    try:
        ultimo_som_navegador_time = 0.0
        
        while True:
            sessions = AudioUtilities.GetAllSessions()
            spotify_session = None
            navegador_fazendo_barulho = False
            
            for session in sessions:
                if not session.Process:
                    continue
                
                process_name = session.Process.name().lower()
                
                # Identifica a sessão do Spotify
                if process_name == config["APP_ALVO"]:
                    spotify_session = session
                
                # Identifica se a sessão pertence a QUALQUER navegador da lista
                elif process_name in config["APPS_GATILHO"]:
                    try:
                        meter = session._ctl.QueryInterface(IAudioMeterInformation)
                        if meter.GetPeakValue() > 0.001: 
                            navegador_fazendo_barulho = True
                    except Exception:
                        pass

            # Lógica de Standby
            if config["STANDBY"]:
                if spotify_session and spotify_session.SimpleAudioVolume:
                    if round(spotify_session.SimpleAudioVolume.GetMasterVolume(), 2) != round(config["VOLUME_NORMAL"], 2):
                        spotify_session.SimpleAudioVolume.SetMasterVolume(config["VOLUME_NORMAL"], None)
                time.sleep(0.3)
                continue
            
            # Atualiza o cronômetro se algum navegador estiver tocando som agora
            if navegador_fazendo_barulho:
                ultimo_som_navegador_time = time.time()
            
            # Aplica a lógica de volume no Spotify
            if spotify_session and spotify_session.SimpleAudioVolume:
                tempo_decorrido = time.time() - ultimo_som_navegador_time
                
                if tempo_decorrido < config["TOLERANCIA_SEGUNDOS"]:
                    novo_vol = config["VOLUME_REDUZIDO"]
                else:
                    novo_vol = config["VOLUME_NORMAL"]
                
                if round(spotify_session.SimpleAudioVolume.GetMasterVolume(), 2) != round(novo_vol, 2):
                    spotify_session.SimpleAudioVolume.SetMasterVolume(novo_vol, None)
            
            time.sleep(0.3)
    finally:
        comtypes.CoUninitialize()

def set_volume_config(v):
    config["VOLUME_REDUZIDO"] = v / 100.0

def toggle_standby(icon, item):
    config["STANDBY"] = not config["STANDBY"]

def fechar_aplicacao(icon):
    icon.stop()
    os._exit(0)

def criar_menu_volumes():
    itens = []

    def make_action(v):
        return lambda icon, item: set_volume_config(v)

    def is_checked(v):
        return lambda item: config["VOLUME_REDUZIDO"] == v / 100.0

    for i in range(10, 100, 10):
        itens.append(pystray.MenuItem(
            f"{i}%",
            make_action(i),
            checked=is_checked(i)
        ))
    return itens

def criar_icone():
    image = Image.new('RGB', (64, 64), (0, 0, 0))
    dc = ImageDraw.Draw(image)
    dc.ellipse((10, 10, 54, 54), fill=(30, 215, 96))

    menu_volumes = pystray.Menu(*criar_menu_volumes())
    
    main_menu = pystray.Menu(
        pystray.MenuItem("Modo Standby", toggle_standby, checked=lambda item: config["STANDBY"]),
        pystray.MenuItem("Configurar Volume Reduzido", menu_volumes),
        pystray.MenuItem("Fechar Aplicação", fechar_aplicacao)
    )

    icon = pystray.Icon("AutoVolumeForSpotify", image, "Auto Volume for Spotify", menu=main_menu)

    def setup_inicial(icon):
        icon.visible = True
        icon.notify("O Auto Volume for Spotify foi iniciado com sucesso.", "Auto Volume for Spotify")

    icon.run(setup=setup_inicial)

if __name__ == "__main__":
    t = threading.Thread(target=monitorar_audio, daemon=True)
    t.start()
    criar_icone()
