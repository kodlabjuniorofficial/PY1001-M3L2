import json

class Assistant:
    def __init__(self, name):
        self.name = name
        self.filename = f"{self.name}.json"
        self.command_count = 0
        self.battery = 100 
        self.memory = [] 
        self.load_memory() 
        
        self.commands = {
            "merhaba": self.greet,
            "yardım": self.help,
            "istatistik": self.show_stats,
            "şarj": self.charge
        }

    def greet(self):
        if self.battery > 0:
            self.command_count += 1
            self.battery -= 5
            self.save_memory()
            return f"Merhaba! Ben {self.name}. Telegram bedenimle emrindeyim! 🤖 (Pil: %{self.battery})"
        return "🪫 Enerjim bitti! Lütfen beni /sarj et."

    def help(self):
        self.command_count += 1
        return "Desteklenen komutlar: /start, /yardim, /istatistik, /sarj, /isim_degistir, /not_al"

    def show_stats(self):
        return f"--- {self.name} İstatistikleri ---\n🔢 Komut: {self.command_count}\n🔋 Pil: %{self.battery}\n📝 Notlar: {len(self.memory)}"

    def charge(self):
        self.battery = 100
        self.save_memory()
        return "🔌 Şarj kablosu takıldı. Pil: %100! ⚡"

    def set_name(self, new_name):
        old = self.name
        self.name = new_name
        self.save_memory()
        return f"✅ İsmim '{old}' iken '{self.name}' olarak güncellendi."

    def add_note(self, note_text):
        self.memory.append(note_text)
        self.save_memory()
        return f"📝 '{note_text}' notunu hafızama ekledim."

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