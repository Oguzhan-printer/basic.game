
# ✊📄✂️ Rock-Paper-Scissors Oyunu

Bu eğlenceli Python projesi, bilgisayar tarafından oynanan bir **Taş-Kağıt-Makas** oyununu simüle eder. Oyuncular (bilgisayar kontrollü) belirli sayıda tur oynar ve her turda rastgele seçimler yaparak kazanan belirlenir. 🧠🎲

---

## 🕹️ Oyunun Kuralları

- **Taş** makası yener 🪨 > ✂️  
- **Makas** kağıdı yener ✂️ > 📄  
- **Kağıt** taşı yener 📄 > 🪨  
- Aynı seçim yapılırsa, **beraberlik** olur ⚖️

---

## 🔁 Oyun Akışı

1. Kullanıcıdan kaç tur oynanacağı sorulur.
2. Her turda:
   - Her iki oyuncu için rastgele seçim yapılır.
   - Kazanan belirlenir ve skora eklenir.
   - Skorlar yazdırılır.
3. Tüm turlar sonunda toplam skor yazdırılır ve kazanan duyurulur. 🏆

---

## 🧠 Kullanılan Python Özellikleri

- `random.choice()` ve `random.randint()` ile rastgele seçim
- `if-elif` yapıları ile oyun mantığı
- `while` döngüsü ile tur sayısı kadar oyun oynatma
- `input()` ile kullanıcı etkileşimi
- `int()` dönüşümü ile kullanıcıdan alınan veriyi sayıya çevirme

---

## 📌 Koddan Bir Kesit

```python
action_list = ['rock', 'paper', 'scissors']
player1_choice = random.choice(action_list)
player2_choice = action_list[random.randint(0,2)]

if player1_choice == player2_choice:
    print("Tie! Both player chose same action.")
elif player1_choice == 'rock' and player2_choice == 'scissors':
    print("Winner is: Player 1")
```

---

## 🧪 Örnek Oyun Çıktısı

```
How many rounds do you want to play? : 3
Round number: 1
Player1: paper
Player2: rock
Winner is: Player 1
Score: Player1 = 1 Player2 = 0
...
Player 1 won with score 2 : 1
```

---

## 🚀 Nasıl Çalıştırılır?

1. Python yüklü olmalı.
2. Kodları `.py` dosyasına yapıştır.
3. Terminalde çalıştır:
```bash
python rock_paper_scissors.py
```

---

## 🎮 Geliştirme Fikirleri

- Kullanıcının da seçim yapabildiği bir sürüm oluştur.
- Grafik arayüz (GUI) ile daha görsel bir deneyim yarat.
- Oyunun sonunda en çok hangi seçimin yapıldığını analiz et.

---

👾 **Klasik oyunun dijital haliyle Python öğrenmeyi eğlenceli hale getir!**
