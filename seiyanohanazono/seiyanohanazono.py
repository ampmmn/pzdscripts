# code:utf-8

import os
import sys
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pzd

# valentine2024.py
# スイートバレンタイン 甘美祭 上級

class scenario:

    def __init__(self, pzd):
        self.pzd = pzd
        pass

    # メンバのスキルをポチって、ドロップをずらす
    def useSkillAndMove(self, index,*,msg="", wait=6):

        pzd = self.pzd

        # スキル使用
        pzd.useSkill(index, msg=msg, wait=wait)
        # ずらして、次を待つ
        pzd.swipe(120, 1410, 276, 1410, msg="ドロップをずらす", duration=230)
        pzd.wait(11, msg="移動可能になるまで待機")
    
    # 1Fの処理
    def battle1(self, pzd):
        pzd.wait(6, msg="[1/7]先制エフェクト待ち")
        pzd.useSkill(4,msg="ニーズヘッグスキル使用", wait=3)
        self.useSkillAndMove(1, msg="ノア1スキル使用", wait=6)
    
    # 2Fの処理
    def battle2(self, pzd):
        pzd.wait(11, msg="[2/7]先制攻撃完了待ち")
        self.useSkillAndMove(1,msg="ノア1スキル使用", wait=6)
    
    # 3Fの処理
    def battle3(self, pzd):
        pzd.wait(15, msg="[3/7]先制エフェクト待ち")
        pzd.useSkill(4, msg="サレーネスキル使用", wait=4)
        self.useSkillAndMove(2,msg="ノア2スキル使用", wait=6)

    # 4Fの処理
    def battle4(self, pzd):
        pzd.wait(15, msg="[4/7]先制エフェクト待ち")
        self.useSkillAndMove(2,msg="ノア2スキル使用", wait=6)

    # 5Fの処理
    def battle5(self, pzd):
        pzd.wait(15, msg="[5/7]先制エフェクト待ち")
        self.useSkillAndMove(3,msg="ノア3スキル使用", wait=6)

    # 6Fの処理
    def battle6(self, pzd):
        pzd.wait(15, msg="[6/7]先制エフェクト待ち")
        pzd.useSkill(5, msg="上杉謙信スキル使用", wait=4)
        self.useSkillAndMove(3,msg="ノア3スキル使用", wait=6)

    # 7F(ボス)の処理
    def battleBoss(self, pzd):
        pzd.wait(18, msg="[7/7]敵のスキル使用を待つ")
        self.useSkillAndMove(1,msg="ノア1スキル使用", wait=6)
        pzd.wait(22, msg="敵のスキル使用を待つ")
        pzd.useSkill(0, msg="ニーズヘッグスキル使用", wait=3)
        self.useSkillAndMove(1,msg="ノア1スキル使用", wait=6)
    
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
            pzd.skipTips(prewait=4)

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

