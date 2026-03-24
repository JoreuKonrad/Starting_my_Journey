import time
import threading
import os
import pythoncom
from PIL import Image, ImageDraw
import pystray
from pycaw.pycaw import AudioUtilities

# Configurações Iniciais
config = {
    "VOLUME_REDUZIDO": 0.6,
    "VOLUME_NORMAL": 1.0,
    "APP_ALVO": "Spotify.exe"
}

def monitorar_audio():
    pythoncom.CoInitialize()
    try:
        while True:
            sessions = AudioUtilities.GetAllSessions()
            spotify_session = None
            outros_fazendo_barulho = False
            
            for session in sessions:
                if session.Process and session.Process.name().lower() == config["APP_ALVO"].lower():
                    spotify_session = session
                elif session.Process and session.Process.name() != config["APP_ALVO"] and session.Process.name() != "System Idle Process":

                    # Se o pico for maior que 0.001, significa que há som saindo DE FATO
                    meter = session._ctl.QueryInterface(pythoncom.IID_IUnknown).QueryInterface(AudioUtilities.IAudioMeterInformation)
                    if meter.GetPeakValue() > 0.001: 
                        outros_fazendo_barulho = True
            
            if spotify_session and spotify_session.SimpleAudioVolume:
                novo_vol = config["VOLUME_REDUZIDO"] if outros_fazendo_barulho else config["VOLUME_NORMAL"]
                
                # Ajuste instantâneo se houver diferença
                if round(spotify_session.SimpleAudioVolume.GetMasterVolume(), 2) != round(novo_vol, 2):
                    spotify_session.SimpleAudioVolume.SetMasterVolume(novo_vol, None)
            
            # Diminuímos o sleep para 0.8 segundos para uma resposta mais rápida
            time.sleep(0.8)
    finally:
        pythoncom.CoUninitialize()

def set_volume_config(v):
    config["VOLUME_REDUZIDO"] = v / 100.0

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
    # Criação do ícone visual
    image = Image.new('RGB', (64, 64), (0, 0, 0))
    dc = ImageDraw.Draw(image)
    dc.ellipse((10, 10, 54, 54), fill=(30, 215, 96))

    menu_volumes = pystray.Menu(*criar_menu_volumes())
    
    main_menu = pystray.Menu(
        pystray.MenuItem("Configurar Volume Reduzido", menu_volumes),
        pystray.MenuItem("Fechar Aplicação", fechar_aplicacao)
    )

    icon = pystray.Icon("SpotifyDuck", image, "Spotify Auto-Volume", menu=main_menu)
    icon.run()

if __name__ == "__main__":
    t = threading.Thread(target=monitorar_audio, daemon=True)
    t.start()
    criar_icone()