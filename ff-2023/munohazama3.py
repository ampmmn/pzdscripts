# code:utf-8

import os
import sys
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pzd

# munohazama3.py
# 無の狭間 上級 周回
#  2023/10/12

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
        pzd.wait(9, msg="移動可能になるまで待機")
    
    # 1Fの処理
    def battle1(self, pzd):
        pzd.useSkill(1, msg="シヴィニア1変身", wait=3)
        pzd.useSkill(2, msg="シヴィニア2変身", wait=3)
        pzd.useSkill(3, msg="木ゼローグスキル使用", wait=2)
        pzd.useSkill(0, msg="サレーネスキル使用", wait=3)
        self.useSkillAndMove(1,msg="シヴィニア1スキル使用")
    
    # 2Fの処理
    def battle2(self, pzd):
        pzd.wait(10, msg="セリフまち")
        self.useSkillAndMove(2,msg="シヴィニア2スキル使用")
    
    # 3Fの処理
    def battle3(self, pzd):
        pzd.wait(10, msg="セリフまち")
        self.useSkillAndMove(1,msg="シヴィニア1スキル使用")
    
    # 4Fの処理
    def battle4(self, pzd):
        pzd.wait(10, msg="セリフまち")
        self.useSkillAndMove(2,msg="シヴィニア2スキル使用")
    
    # 5Fの処理
    def battle5(self, pzd):
        pzd.wait(10, msg="セリフまち")
        self.useSkillAndMove(1,msg="シヴィニア1スキル使用")
    
    # 6Fの処理
    def battle6(self, pzd):
        pzd.wait(10, msg="セリフまち")
        self.useSkillAndMove(2,msg="シヴィニア2スキル使用")
    
    # 7Fの処理
    def battleBoss(self, pzd):
        pzd.wait(10, msg="セリフまち")
        pzd.useSkill(1, msg="シヴィニア1スキル使用", wait=2.5)
        # 最終フロアなので次のフロアの表示待ちは不要
        pzd.swipe(120, 1410, 276, 1410, msg="ずらす", duration=230)
        # なんだけど、崩れ去るエフェクトがあるのでタップしてスキップ
        pzd.tap(120, 1410, msg="エフェクト飛ばす", wait=5)
        pzd.tap(120, 1410, msg="エフェクト飛ばす", wait=5)
    
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
            self.battle6(pzd)
            self.battleBoss(pzd)

            # TIPS画面と結果画面のスキップ
            pzd.skipTips()
            pzd.skipResult()

if __name__ == "__main__":

    pzd = pzd.pzd()

    # adb.exeが見つからない場合は終了
    if pzd.isAvailable() == False:
        print(f"adb.exe does not exist. [{kyokuren.pzd.ADBPath()}]")
        quit()

    try:
        kyokuren = scenario(pzd)
        kyokuren.loop()
    except KeyboardInterrupt:
        pass

