# code:utf-8
import os
import sys
import time

import pzd

# loop-kyokuren.py
# 極練周回
#  2023/09/23
# スクリプト開始時の前提: 
#  - ノーマルダンジョン選択画面を表示していること
#  - 「獄連の闘技場」が一番上に見えていること(獄連,極連ともに解放済であること)
#  - 経験値バッジ
# メンバ構成:
#	L:サレーネ + スキブアシスト
#     シヴィニア + スキブアシスト
#     シヴィニア + スキブアシスト
#	  木ゼローグ
#	  万極 + フェイタン装備
#	F:サレーネ
# 1周の目安時間: 3分20秒程度(1時間に18-19周程度)
#
# メモ:
#   - 初手でシヴィニアx2変身、木ゼローグの10ターン落ちコンなし→サレーネでヘイスト+2
#   - 1Fから最後まで、2体のシヴィニアx2のスキルを交互に使ってずらす、で進む
#   - 万極は火力要員
#   - 落ちコンなしの効果が切れるので途中(9F)で再度木ゼローグのスキルを使用している
#   - 完全ノーパズル+落ちコンなし編成なので画面状態で判断せずに単純なsleepによる待ちで処理している
#     - とはいえコンボが多く発生した場合に、見切り発車によるずれが生じる可能性あり
#   - 04:00の「日付が変わりました」スキップは実装してないので4時で流れが止まる一方、
#     このスクリプト自体は実行し続けるため、誤操作の恐れあり(というかした)
#
#   - 現在使用している機種している機種を前提としてタップ/スワイプする座標値をハードコードしているのでどうにかする

class loop_kyokuren:

    def __init__(self):
        self.pzd = pzd.pzd()
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
        self.useSkillAndMove(2,msg="シヴィニア2スキル使用")
    
    # 3Fの処理
    def battle3(self, pzd):
        self.useSkillAndMove(1,msg="シヴィニア1スキル使用")
    
    # 4Fの処理
    def battle4(self, pzd):
        self.useSkillAndMove(2,msg="シヴィニア2スキル使用")
    
    # 5Fの処理
    def battle5(self, pzd):
        self.useSkillAndMove(1,msg="シヴィニア1スキル使用")
    
    # 6Fの処理
    def battle6(self, pzd):
        self.useSkillAndMove(2,msg="シヴィニア2スキル使用")
    
    # 7Fの処理
    def battle7(self, pzd):
        self.useSkillAndMove(1,msg="シヴィニア1スキル使用")
    
    # 8Fの処理
    def battle8(self, pzd):
        self.useSkillAndMove(2,msg="シヴィニア2スキル使用")
    
    # 9Fの処理
    def battle9(self, pzd):
        pzd.useSkill(3, msg="木ゼローグスキル使用", wait=2)
        self.useSkillAndMove(1,msg="シヴィニア1スキル使用")
    
    # 10Fの処理
    def battle10(self, pzd):
        self.useSkillAndMove(2,msg="シヴィニア2スキル使用")
    
    # 11F(ボス)の処理
    def battleBoss(self, pzd):
        pzd.useSkill(1, msg="シヴィニア1スキル使用", wait=2.5)
        # 最終フロアなので次のフロアの表示待ちは不要
        pzd.swipe(120, 1410, 276, 1410, msg="ずらす", duration=230)
    
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
            self.battle7(pzd)
            self.battle8(pzd)
            self.battle9(pzd)
            self.battle10(pzd)
            self.battleBoss(pzd)

            # TIPS画面と結果画面のスキップ
            pzd.skipTips()
            pzd.skipResult()

if __name__ == "__main__":
    kyokuren = loop_kyokuren()

    # adb.exeが見つからない場合は終了
    if kyokuren.pzd.isAvailable() == False:
        print(f"adb.exe does not exist. [{kyokuren.pzd.ADBPath()}]")
        quit()

    try:
        kyokuren.loop()
    except KeyboardInterrupt:
        pass

