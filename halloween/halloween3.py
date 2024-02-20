# code:utf-8

import os
import sys
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pzd

# halloween3.py
# ハロウィーン 上級

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
        pzd.swipe(120, 1410, 276, 1410, msg="ドロップをずらす", duration=230)
        pzd.wait(11, msg="移動可能になるまで待機")
    
    # 1Fの処理
    def battle1(self, pzd):
        pzd.wait(7, msg="敵のスキル使用を待つ")
        pzd.useSkill(1, msg="シヴィニア1変身", wait=3)
        pzd.useSkill(2, msg="シヴィニア2変身", wait=3)
        pzd.useSkill(3, msg="ゼローグ", wait=3)
        pzd.useSkill(4, msg="サレーネ", wait=3)
        self.useSkillAndMove(1,msg="シヴィニアスキル使用")
    
    # 2Fの処理
    def battle2(self, pzd):
        pzd.wait(7, msg="敵のスキル使用を待つ")
        self.useSkillAndMove(2,msg="シヴィニアスキル使用")
    
    # 3Fの処理
    def battle3(self, pzd):
        pzd.wait(7, msg="敵のスキル使用を待つ")
        self.useSkillAndMove(1,msg="シヴィニアスキル使用")

    # 4Fの処理
    def battle4(self, pzd):
        pzd.wait(7, msg="敵のスキル使用を待つ")
        self.useSkillAndMove(2,msg="シヴィニアスキル使用")

    # 5Fの処理
    def battle5(self, pzd):
        pzd.wait(7, msg="敵のスキル使用を待つ")
        self.useSkillAndMove(1,msg="シヴィニアスキル使用")

    # 5F(ボス)の処理
    def battleBoss(self, pzd):
        pzd.wait(7, msg="敵のスキル使用を待つ")
        pzd.useSkill(2, msg="シヴィニア1スキル使用", wait=2.5)
        # 最終フロアなので次のフロアの表示待ちは不要
        pzd.swipe(120, 1410, 120, 1560, msg="ずらす", duration=230)
    
    # 周回のメイン処理
    def loop(self):

        pzd = self.pzd
        while True:

            # 4時になったら終了
            if time.strftime("%H") == "04":
                print("日付が変わったので終了")
                break
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
        print(f"adb.exe does not exist. [{obj.pzd.ADBPath()}]")
        quit()
    try:
        snro = scenario(pzd)
        snro.loop()
    except KeyboardInterrupt:
        pass

