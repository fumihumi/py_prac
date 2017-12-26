# 穴埋めするような形でコードを記述してください。
class YenToCurrency:
    def __init__(self,yen):
        #ここを埋めてください。
        self.yen = yen


#2. 1ドル=100円, 1ユーロ=120円で換算してください。
    def doll(self):
        #ここを埋めてください。
        return  f"{self.yen / 100}ドル"


    def euro(self):
        #ここを埋めてください。
        return f"{self.yen * 1.2}ユーロ"

#正しくできているか確認するために1200円をドル・ユーロに換算して例のように出力してください。
exchange = YenToCurrency(1200)

print(f"{exchange.yen}円は{exchange.doll()}です。")
print(f'{exchange.yen}円は→{exchange.euro()}です。')
