import json

class Assistant:
    def __init__(self, name):
        self.name = name
        self.filename = f"{self.name}.json"
        self.command_count = 0
        self.battery = 100 
        self.memory = [] 
        self.load_memory() 
        
        # SÖZLÜK YAPISI: Bu yapı aynen kalıyor!
        self.commands = {
            "merhaba": self.greet,
            "yardım": self.help,
            "istatistik": self.show_stats,
            "şarj": self.charge,
            # NOT: isim değiştir ve not al bot tarafından özel yönetilecek.
        }
        print(f"'{self.name}' beyni hazır.")

    def greet(self):
        if self.battery > 0:
            self.command_count += 1
            self.battery -= 10
            # GÖREV-1: print'i sil, mesajı 'return' et. save_memory() çağırmayı unutma.
            print(f"Merhaba! Ben {self.name}. Pil: %{self.battery}")
        else:
            # GÖREV-2: print'i sil, return yap.
            print("⚠️ HATA: Şarj bitti!")

    def help(self):
        self.command_count += 1
        # GÖREV-3: print'i sil, return yap.
        print("Komutlar: merhaba, yardım, istatistik, şarj, isim değiştir, not al")

    def show_stats(self):
        # GÖREV-4: print'i sil, return yap.
        print(f"--- {self.name} İstatistikleri ---")

    def charge(self):
        self.battery = 100
        self.save_memory()
        # GÖREV-5: print'i sil, return yap.
        print("🔌 Şarj dolduruldu! %100")

    def set_name(self, new_name):
        # GÖREV-6: input()'u SİL. Veriyi 'new_name' parametresinden al. 
        # return ile başarı mesajı döndür.
        pass

    def add_note(self, note_text):
        # GÖREV-7: input()'u SİL. Veriyi 'note_text' parametresinden al.
        # return ile başarı mesajı döndür.
        pass

    def save_memory(self):
        data = {"battery": self.battery, "count": self.command_count, "memory": self.memory}
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False)

    def load_memory(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.battery = data.get("battery", 100)
                self.command_count = data.get("count", 0)
                self.memory = data.get("memory", [])
        except FileNotFoundError: pass

    def run_command(self, command):
        if command in self.commands:
            action = self.commands[command]
            return action() # Telegram için return ekledik!
        else:
            return "Bu komutu anlamadım. 🤖"