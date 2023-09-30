# code:utf-8

import os
import sys
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pzd

# loop-dengeki-1.py
# 電撃文庫コラボ2023初級
#  2023/09/26
# スクリプト開始時の前提: 
#  - スペシャルダンジョン選択画面を表示していること
#  - 「電撃文庫」が一番上に見えていること
#  - スキブバッジ
# メンバ構成:
#	L:モモタロス
#     超転生ルシファーx4
#	F:モモタロス
# 1周の目安時間: ?
#
# メモ:
#   - 1Fから4Fまで、ルシファーのスキル使用→ずらす
#   - 5FでLモモタロスのスキル使用→ずらす
#   - 6Fでルシファーのスキル使用→ずらす

class scenario:

    def __init__(self, pzd):
        self.pzd = pzd
        pass

    # メンバのスキルをポチって、ドロップをずらす
    def useSkillAndMove(self, index,*,msg=""):

        pzd = self.pzd

        # スキル使用
        pzd.useSkill(index, msg=msg, wait=3)
        # ずらして、次を待つ
        pzd.swipe(120, 1410, 120, 1560, msg="ドロップをずらす", duration=230)
        pzd.wait(10, msg="移動可能になるまで待機")
    
    # 1Fの処理
    def battle1(self, pzd):
        self.useSkillAndMove(1,msg="ルシファー1スキル使用")
    
    # 2Fの処理
    def battle2(self, pzd):
        self.useSkillAndMove(2,msg="ルシファー2スキル使用")
    
    # 3Fの処理
    def battle3(self, pzd):
        self.useSkillAndMove(3,msg="ルシファー3スキル使用")
    
    # 4Fの処理
    def battle4(self, pzd):
        self.useSkillAndMove(4,msg="ルシファー4スキル使用")
    
    # 5Fの処理
    def battle5(self, pzd):
        self.useSkillAndMove(0,msg="モモタロススキル使用")
    
    # 6F(ボス)の処理
    def battleBoss(self, pzd):
        pzd.useSkill(1, msg="シヴィニア1スキル使用", wait=2.5)
        # 最終フロアなので次のフロアの表示待ちは不要
        pzd.swipe(120, 1410, 120, 1560, msg="ずらす", duration=230)
    
    # 周回のメイン処理
    def loop(self):

        pzd = self.pzd

        # ダンジョン選択
        # (1つ目を選択、画面上の一番上に電撃文庫が見えている状態を想定)
        pzd.selectDangeon1(0, msg="「電撃文庫」を選択")
    
        while True:

            # 4時になったら終了
            if time.strftime("%H") == "04":
                print("日付が変わったので終了")
                break

            # (5つ目を選択、画面上の一番下に初級が見えている状態を想定)
            pzd.selectDangeon2(4, msg="「初級」を選択")
    
            # スタミナ不足していたら回復
            pzd.kaifuku()
    
            # 助っ人選択
            pzd.selectFriend(0)
    
            # 各フロアの処理
            self.battle1(pzd)
            self.battle2(pzd)
            self.battle3(pzd)
            self.battle4(pzd)
            self.battle5(pzd)
            self.battleBoss(pzd)

            # TIPS画面と結果画面のスキップ
            pzd.skipTips()

            pzd.tap(600, 1582, duration=1900, msg="結果をスキップ", wait=3)
            pzd.tap(600, 1416)
            pzd.tap(600, 1416, msg="売却しないのでスキップ")

if __name__ == "__main__":

    pzd = pzd.pzd()

    # adb.exeが見つからない場合は終了
    if pzd.isAvailable() == False:
        print(f"adb.exe does not exist. [{dengeki.pzd.ADBPath()}]")
        quit()

    try:
        dengeki = scenario(pzd)
        dengeki.loop()
    except KeyboardInterrupt:
        pass

