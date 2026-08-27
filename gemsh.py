#py:python_OS_win_linux_android_shell_cmd
__doc__ = """
gemsh by AS - www.adelinosaldanha.site for gemini by google ✦

# This Python script is licensed under the GNU General Public License, version 2.
# See the LICENSE file for more details: https://www.gnu.org/licenses/gpl-2.0.en.html
# Copyright (C) 2023 Adelino Saldanha

# The code is open, but the conscience is not.
# Remember: Many charge monthly for a mountain I built for free.
"""
ETHICS_STATEMENT = """

# 💡 Ethics and the Spirit of gemsh (GPL v2)
# This script is shared under the **GNU GPL v2** to promote learning and freedom. The license permits commercial use, but the spirit of Open Source requires integrity.
# While some may choose to profit without contributing, the ultimate truth remains:
# > **"Laugh at the ledger, but know this: While you charge for the fish, I still hold the deed to the sea. The credit for creation is the only currency that never depreciates."**
# Please respect the lineage of this project. Contribute back if you can, and always preserve the original
# **Copyright (C) 2026 Adelino Saldanha** in all distributed source code.
"""

import os
import sys
import random
import socket
import time
import subprocess
import threading
import importlib
import locale

# some static global cybele variables
version = '1.0'
_title_ = 'gemsh'
_spchar_ = '⚝〉“”—❛❜⧗✔🦖🔗𝒊️💡😊🏆🐧🎯🐚❝❞💬💾🌐🌡️🪐🌊🧬🖳'
_revise_ = '27.08.2026'
_author_ = 'Adelino Saldanha'
_gmodel_ = 'gemini-3.6-flash'
_apikey_ = ''
dblrconn = ''
_pydr3_ = False

REQUIRED_PACKAGES = {
    'google.genai': 'google-genai',
}
#-----------------------------------------------------------
kolor = {
	'BOLD_WHITE':'\033[1;37m','BOLD_YELLOW':'\033[1;33m','BOLD_GREEN':'\033[1;32m','BOLD_BLUE':'\033[1;34m',
	'BOLD_CYAN':'\033[1;36m','BOLD_RED':'\033[1;31m','BOLD_MAGENTA':'\033[1;35m','BOLD_BLACK':'\033[1;30m',
	'WHITE':'\033[0;37m','YELLOW':'\033[0;33m','GREEN':'\033[0;32m','BLUE':'\033[0;34m','CYAN':'\033[0;36m',
	'RED':'\033[0;31m','MAGENTA':'\033[0;35m','BLACK':'\033[0;30m',
	'VIVID_RED':'\033[91m','VIVID_GREEN':'\033[92m','VIVID_YELLOW':'\033[93m','VIVID_BLUE':'\033[94m',
	'VIVID_MAGENTA':'\033[95m','VIVID_CYAN':'\033[96m','VIVID_WHITE':'\033[97m',
	'DARK_BLACK':'\033[30m','DARK_RED':'\033[31m','DARK_GREEN':'\033[32m','DARK_YELLOW':'\033[33m',
	'DARK_BLUE':'\033[34m','DARK_MAGENTA':'\033[35m','DARK_CYAN':'\033[36m','DARK_WHITE':'\033[37m',
	'DIM_BLACK':'\033[2;30m','DIM_RED':'\033[2;31m','DIM_GREEN':'\033[2;32m','DIM_YELLOW':'\033[2;33m',
	'DIM_BLUE':'\033[2;34m','DIM_MAGENTA':'\033[2;35m','DIM_CYAN':'\033[2;36m','DIM_WHITE':'\033[2;37m',
	'ORANGE': '\033[38;5;208m','OFF':'\033[0m','RESET':'\033[0m','SW_CRAWL': '\033[93m','SABER_BLUE': '\033[96m',
    'GRAY': '\033[90m',
    # Cores Google oficiais para o autómato do prompt
    'G_BLUE': '\033[38;5;33m',
    'G_RED': '\033[38;5;196m',
    'G_YELLOW': '\033[38;5;220m',
    'G_GREEN': '\033[38;5;46m'
}
#------------------------------------------------------------
_pydr3_ = 'pydroid' in sys.executable.lower()
if _pydr3_:
    print(f"\n{kolor['RED']}[ERROR]{kolor['RESET']} System not supported.")
    print(f"{kolor['YELLOW']}The system on which you are trying to run me is not (or not yet) supported.{kolor['RESET']}\n")
    sys.exit(1)
#------------------------------------------------------------
def get_system_lang():
    try:
        lang_env = os.environ.get('LANG') or os.environ.get('LC_ALL') or os.environ.get('LANGUAGE')
        if lang_env:
            # Corta logo nos primeiros 2 caracteres (ex: 'pt_PT.UTF-8' -> 'pt')
            return lang_env[:2].lower()

        loc = locale.getlocale()[0]
        if loc:
            return loc[:2].lower()
    except Exception:
        pass
    return 'en'

#------------------------------------------------------------
lang_code = get_system_lang()
active_lang = 'pt' if lang_code == 'pt' else 'en'

#------------------------------------------------------------
def install_and_check():
    needed = []
    for module, pip_name in REQUIRED_PACKAGES.items():
        try:
            importlib.import_module(module)
        except ImportError:
            needed.append((module, pip_name))

    if not needed:
        return

    print(f"\n\033[38;5;208mInitializing { _title_ } - Setting up dependencies...\033[0m")
    total = len(needed)
    for i, (module, pip_name) in enumerate(needed):
        progress = (i / total)
        bar_len = 20
        filled = int(bar_len * progress)
        bar = '━' * filled + ' ' * (bar_len - filled)
        print(f"\r\033[1;36m[{bar}]\033[0m Installing {pip_name}...\033[K", end="", flush=True)
        with open(os.devnull, 'w') as fnull:
            subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name], stdout=fnull, stderr=fnull)
    print(f"\r\033[1;32m[{'━' * 20}] Ready!\033[0m\n")

install_and_check()

from google import genai

#------------------------------------------------------------
def internet_onoff():
    try:
        socket.setdefaulttimeout(1)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("8.8.8.8", 53))
        s.close()
        return True
    except OSError:
        pass
    return False

#-----------------------------------------------------------
online = internet_onoff()
dblrconn = "online" if online else "offline"

if not online:
    print(f"\n{kolor['RED']}[OFFLINE ERROR]{kolor['RESET']} No internet connection detected.")
    print(f"{kolor['YELLOW']}The offline neural model version is not yet available. Please check your connection and try again.{kolor['RESET']}\n")
    sys.exit(1)

#-----------------------------------------------------------
def print_statusline(msg: str):
    last_msg_length = len(getattr(print_statusline, 'last_msg', ''))
    print(' ' * last_msg_length, end='\r')
    print(msg, end='\r')
    sys.stdout.flush()
    setattr(print_statusline, 'last_msg', msg)

class Spinner:
    def __init__(self, message="A pensar"):
        self.message = message
        self.anim_frames = ["⏳", "⌛", "🪐", "💡", "✨", "🌊", "🐧"]
        self.spinner_chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        self.is_running = False
        self.thread = None

    def _spin(self):
        i = 0
        while self.is_running:
            frame = self.anim_frames[i % len(self.anim_frames)]
            spin_char = self.spinner_chars[i % len(self.spinner_chars)]
            text = f"\r{kolor['VIVID_CYAN']}{frame} {spin_char} {self.message}...{kolor['RESET']}"
            print_statusline(text)
            time.sleep(0.12)
            i += 1

    def start(self):
        self.is_running = True
        self.thread = threading.Thread(target=self._spin)
        self.thread.daemon = True
        self.thread.start()

    def stop(self):
        self.is_running = False
        if self.thread:
            self.thread.join()
        print_statusline("")
        sys.stdout.write("\033[K")

#-----------------------------------------------------------
art_gem = [
        [32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,46,95,95,32,32,32,32,32,32,32,46,95,95],
        [32,32,32,95,95,95,95,32,32,32,95,95,95,95,32,32,32,95,95,95,95,95,32,124,95,95,124,32,95,95,95,95,32,124,95,95,124,32],
        [32,32,47,32,95,95,95,92,95,47,32,95,95,32,92,32,47,32,32,32,32,32,92,124,32,32,124,47,32,32,32,32,92,124,32,32,124],
        [32,47,32,47,95,47,32,32,62,32,32,95,95,95,47,124,32,32,89,32,89,32,32,92,32,32,124,32,32,32,124,32,32,92,32,32,124],
        [32,92,95,95,95,32,32,47,32,92,95,95,95,32,32,62,95,95,124,95,124,32,32,47,95,95,124,95,95,95,124,32,32,47,95,95,124],
        [32,92,95,95,95,32,32,47,32,92,95,95,95,32,32,62,95,95,124,95,124,32,32,47,95,95,124,95,95,95,124,32,32,47,95,95,124],
        [47,95,95,95,95,95,47,32,32,32,32,32,32,92,47,32,32,32,32,32,32,92,47,32,32,32,32,32,32,32,32,92,47]
]
art_kx64 = [98,121,32,107,101,114,110,101,108,120,54,52]
art_byas = [129150,32,98,121,32,65,83]

#----------------------------------------------------
core = {
    "intromsg": {
        "en": [
            "Welcome.", "Greetings.", "Entertain.", "Glad you're here!", "Delighted to have you!",
            "Fantastic to see you!", "Awesome you're here!", "Stoked you're here!", "Pleasure to have you!",
            "Delighted to welcome you!", "Is a privilege to host you!", "Honored to have you join us.",
            "A warm welcome to you.", "Truly a pleasure to meet you.", "So glad you could make it!",
            "Great to see you in the mix!", "Look who decided to drop by!", "Hi! Let’s get started.",
            "Make yourself at home!", "Step right in!", "The legend has arrived!",
            "Your presence makes this better.", "Welcome to the party."
        ],
        "pt": [
            "Bem-vindo.", "Saudações.", "Entra e diverte-te.", "Ainda bem que estás aqui!",
            "É um gosto ter-te cá!", "Fantástico ver-te!", "Excelente ter-te por cá!",
            "Que bom ver-te!", "É um prazer receber-te!", "É um privilégio hospedar-te!",
            "Honrado por te juntares a nós.", "Uma calorosa boas-vindas.", "Verdadeiramente um prazer conhecer-te.",
            "Ainda bem que conseguiste vir!", "Bom ver-te no ativo!", "Olha quem decidiu aparecer!",
            "Olá! Vamos começar.", "Sente-te em casa!", "Sente-te à vontade!",
            "A lenda acabou de chegar!", "A tua presença torna isto melhor.", "Bem-vindo à festa."
        ]
    },
    "exitmsg": {
        "en": [
            'It was a pleasure.', 'Until next time!', 'Until we meet again!', 'Looking forward.',
            'Have a good one.', 'Take care.', 'Catch you later!', 'Peace Out.', 'Farewell.'
        ],
        "pt": [
            'Foi um prazer.', 'Até à próxima!', 'Até nos voltarmos a ver!', 'Fico a aguardar.',
            'Passa um bom dia.', 'Toma cuidado.', 'Ate logo!', 'Força e paz.', 'Adeus.'
        ]
    },
    "spinner": {
        "en": ["Thinking", "Consulting neural matrix", "Processing data"],
        "pt": ["A pensar", "A consultar a matriz neural", "A processar dados"]
    },
    "deactivate": {
        "en": "Deactivating neural connection...",
        "pt": "A desativar a ligação neural..."
    },
    "ctrl": {
        "en": "Interrupted by the user by CTRL+C ...",
        "pt": "Interrompido pelo utilizador via Ctrl+C ..."
    }
}
#----------------------------------------------------
website = {
	"home": "https://www.adelinosaldanha.site",
	"mystory": "https://www.adelinosaldanha.site/mystory",
	"github": "https://github.com/kernelx64/",
	"amoc_db": "https://baserow.io/public/grid/qo5AByxLIe2Ny53BsIfuyogo5vrJb4AzaPESGP8llPs"
}
#----------------------------------------------------
def drawart(artname):
    print(kolor['OFF'])
    art_data = {
            'art_gem': {'art': art_gem, 'exclude_colors': ['BOLD_BLACK', 'DARK_BLACK', 'DIM_BLACK', 'BLACK'],
            'fallback_colors': ['RED', 'DIM_RED', 'BOLD_RED'], 'special_line': 6, 'special_suffix': art_byas,
            'special_suffix_color': 'BOLD_YELLOW'},
    }
    if artname not in art_data:
        print(f"Error: Art '{artname}' not found in my code to handle'it. Fix'it!\n")
        print(kolor['OFF'])
        return
    config = art_data[artname]
    art = config['art']
    if 'color' in config:
        art_color = kolor[config['color']]
    else:
        available_colors = [c for c in list(kolor.keys()) if c not in config.get('exclude_colors', []) and not c.startswith('G_')]
        if not available_colors:
            art_color_name = random.choice(config['fallback_colors'])
        else:
            art_color_name = random.choice(available_colors)
        art_color = kolor[art_color_name]
    for i, line_bytes in enumerate(art):
        res = ''.join(map(chr, line_bytes))
        if artname == 'art_gem' and i == config['special_line']:
            suffix_res =''.join(map(chr, config['special_suffix']))
            start_of_line = res[:7]
            new_content = kolor['DIM_YELLOW'] + dblrconn + kolor['OFF']
            final_line = art_color + start_of_line + new_content + art_color + res[13:-5]
            print(final_line + kolor[config['special_suffix_color']] + suffix_res)
        else:
            print(art_color + res)
    print(kolor['OFF'])

#---------------------------------------------------
def symb_prompt():
	global _spchar_
	primary_icon = _spchar_[1]
	alternative_icon = "\u27e9"
	safety_icon = "\u276f"

	def update_global(new_icon):
		global _spchar_
		_spchar_ = _spchar_[0] + new_icon + _spchar_[2:]
		return new_icon

	try:
		primary_icon.encode(sys.stdout.encoding)
		return update_global(primary_icon)
	except (UnicodeEncodeError, AttributeError):
		try:
			alternative_icon.encode(sys.stdout.encoding)
			return update_global(alternative_icon)
		except:
			return update_global(safety_icon)
#-----------------------------------------------------------
def get_google_styled_gemini():
    return (
        f"{kolor['G_RED']}g{kolor['RESET']}"
        f"{kolor['G_YELLOW']}e{kolor['RESET']}"
        f"{kolor['G_BLUE']}m{kolor['RESET']}"
        f"{kolor['G_GREEN']}i{kolor['RESET']}"
        f"{kolor['G_RED']}n{kolor['RESET']}"
        f"{kolor['G_YELLOW']}i{kolor['RESET']}"
    )
#-----------------------------------------------------------
def main():
    api_key = os.environ.get("GEMINI_API_KEY") or _apikey_

    if not api_key or api_key.strip() == "":
        print(f"\n{kolor['YELLOW']}[WARNING]{kolor['RESET']} No GEMINI_API_KEY configured.")
        print(f"To get an API Key go to [https://aistudio.google.com/api-keys], create one and insert it in the var _apikey_ .")
        print(f"Run in the terminal: export GEMINI_API_KEY='your api key'\n")
        return

    client = genai.Client(api_key=api_key)
    drawart('art_gem')
    wms = random.choice(core['intromsg'][active_lang])
    print(f"{wms}\n")

    try:
        chat = client.chats.create(model=_gmodel_)
    except Exception as e:
        print(f"{kolor['YELLOW']}Error initiating the chat: {e}{kolor['RESET']}")
        return

    while True:
        try:
            # Nome do utilizador num verde vivo e estético, seguido de '@' em branco e o gemini com as cores da Google
            username = os.getlogin()
            prompt_line = (
                f"{kolor['BOLD_GREEN']}{username}{kolor['RESET']}"
                f"{kolor['WHITE']}@{kolor['RESET']}"
                f"{get_google_styled_gemini()} "
                f"{kolor['VIVID_MAGENTA']}{symb_prompt()}{kolor['RESET']}"
            )

            user_input = input(prompt_line)

            if user_input.strip().lower() in ["sair", "exit", "quit", "q", "x", ":q" ,":x"]:
                print(f"{kolor['GRAY']}\n{core['deactivate'][active_lang]}{kolor['RESET']}")
                print(f"{random.choice(core['exitmsg'][active_lang])} {random.choice(['',' Bye.'])}\n")
                break

            if user_input.strip().lower() == "author":
                print(f"\n{kolor['BOLD_YELLOW']}✦ Script Author:{kolor['RESET']} {kolor['BOLD_WHITE']}{_author_}{kolor['RESET']}")
                print(f"{kolor['CYAN']}{website['home']}{kolor['RESET']}\n")
                continue

            if user_input.strip().lower() == "model":
                print(f"\n{kolor['BOLD_YELLOW']}Gemini Model:{kolor['RESET']} {kolor['BOLD_WHITE']}{_gmodel_}{kolor['RESET']}")
                print(f"{kolor['CYAN']}Is Google's high-efficiency workhorse multimodal AI model released in July 2026.{kolor['RESET']}\n")
                continue

            if not user_input.strip():
                continue

            spinner_msg = random.choice(core['spinner'][active_lang])
            spinner = Spinner(message=spinner_msg)
            spinner.start()

            try:
                response = chat.send_message(user_input)
            finally:
                spinner.stop()

            print(f"\n{kolor['VIVID_WHITE']}{response.text}{kolor['RESET']}\n")

        except (KeyboardInterrupt, EOFError):
            try:
                msg = core['ctrl'][active_lang]
            except Exception:
                msg = "Interrupted by user."
            print(f"\n{kolor['GRAY']}{msg}{kolor['RESET']}\n")
            break

#-----------------------------------------------------------
if __name__ == "__main__":
    main()
    globals().clear()
