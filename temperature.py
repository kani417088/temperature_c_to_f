#攝氏('C')轉換成華氏('F')程式
#F=9/5 C + 32
#讓使用者輸入攝氏溫度，然後印出華氏溫度
temperature_C = input('請輸入攝氏溫度:')
temperature_C = float(temperature_C)
temperature_F = temperature_C * 9 / 5 + 32
print('華氏溫度為:', temperature_F)
