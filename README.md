# vastrelv9
Vastrel v9 - Termux için gelişmiş hacker aracı (SMS, CMD vb. içerir)

# Vastrel v9

**Termux ve Kali Linux için güçlü siber güvenlik aracı**

Vastrel, CMD tabanlı araçlar ve SMS fonksiyonları içeren gelişmiş bir hacking aracıdır.

---

## ⚠️ ÖNEMLİ UYARI

**Bu araç son derece tehlikeli ve güçlü özellikler içermektedir.**  
Bu scripti kullanmak tamamen sizin sorumluluğunuzdadır. 

Yazar ve geliştiriciler, bu aracın kötüye kullanımı sonucunda oluşabilecek **hiçbir yasal, maddi veya manevi sorumluluğu kabul etmez.**  

Bu araç **sadece eğitim amaçlı**, etik hacking, siber güvenlik öğrenimi ve izinli testler için geliştirilmiştir. Yasadışı faaliyetlerde kullanmak kesinlikle yasaktır ve hukuki sonuçlar doğurabilir.

---

## Kurulum

### 1. Termux için

pkg update && pkg upgrade -y
pkg install python git -y

1 git clone https://github.com/eralpdalikirik14-design/vastrelv9.git
2cd vastrelv9
3sed -i 's/Style\.LIGHTCYAN_EX/Fore.CYAN/g' vastrel.py
4pip install -r requirements.txt
5python vastrel.py

## Kurulum

### 2. Kali linux için

sudo apt update && sudo apt upgrade -y
sudo apt install python3 git -y

2 git clone https://github.com/eralpdalikirik14-design/vastrelv9.git
2cd vastrelv9
3pip3 install -r requirements.txt
4sed -i 's/Style\.LIGHTCYAN_EX/Fore.CYAN/g' 5vastrel.py
6python3 vastrel.py

