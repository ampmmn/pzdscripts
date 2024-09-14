# code:utf-8

import os
import sys
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pzd

# seiyanohanazono.py
# 星夜の花園 修練の灯路

class scenario:

    def __init__(self, pzd):
        self.pzd = pzd
        # 連戦モードON
        self.rensenMode = True
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
        pzd.wait(6, msg="[1/7]フレイヤ先制エフェクト待ち")
        pzd.useSkill(4,msg="ニーズヘッグスキル使用", wait=3)
        self.useSkillAndMove(1, msg="ノア1スキル使用", wait=5.5)
    
    # 2Fの処理
    def battle2(self, pzd):
        pzd.wait(8, msg="[2/7]宝玉先制攻撃完了待ち")
        self.useSkillAndMove(1,msg="ノア1スキル使用", wait=5.5)
    
    # 3Fの処理
    def battle3(self, pzd):
        pzd.wait(12, msg="[3/7]番人先制エフェクト待ち")
        pzd.useSkill(4, msg="サレーネスキル使用", wait=4)
        self.useSkillAndMove(2,msg="ノア2スキル使用", wait=5.5)

    # 4Fの処理
    def battle4(self, pzd):
        pzd.wait(15, msg="[4/7]妖精みたいなやつ先制エフェクト待ち")
        self.useSkillAndMove(2,msg="ノア2スキル使用", wait=5.5)

    # 5Fの処理
    def battle5(self, pzd):
        pzd.wait(15, msg="[5/7]たまドラ先制エフェクト待ち")
        self.useSkillAndMove(3,msg="ノア3スキル使用", wait=5.5)

    # 6Fの処理
    def battle6(self, pzd):
        pzd.wait(15, msg="[6/7]花咲いてるやつ先制エフェクト待ち")
        pzd.useSkill(5, msg="上杉謙信スキル使用", wait=4)
        self.useSkillAndMove(3,msg="ノア3スキル使用", wait=5.5)

    # 7F(ボス)の処理
    def battleBoss(self, pzd):
        pzd.wait(16, msg="[7/7]プリシラ敵のスキル使用を待つ")
        self.useSkillAndMove(1,msg="ノア1スキル使用", wait=5.5)
        pzd.wait(13, msg="敵のスキル使用を待つ")
        pzd.useSkill(0, msg="ニーズヘッグスキル使用", wait=3)
        self.useSkillAndMove(1,msg="ノア1スキル使用", wait=5.5)
    
    # 周回のメイン処理
    def loop(self):

        pzd = self.pzd
        while True:

            # 4時になったら終了
            if time.strftime("%H") == "04":
                print("日付が変わったので終了")
                break

            # 連戦モードOFF時の処理
            if self.rensenMode == False:
                pzd.wait(1)
                pzd.tap(532, 583, msg="ダンジョン選択", wait=0.5)
                pzd.tap(532, 583, msg="助っ人選択", wait=0.5)

            # スタミナ不足していたら回復
            #pzd.kaifuku()

            if self.rensenMode == False:
                # 助っ人選択
                pzd.selectFriend(0)

            # 潜入確認
            pzd.enterQuest()
    
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

            pzd.skipResult()

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

