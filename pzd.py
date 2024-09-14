# code:utf-8
import os
import subprocess
import time

class ADB:

    def __init__(self):
        # 前回のswipe時の移動時間
        self.lastDuration = 100
        pass

    def path(self):
        # 実行環境によりパスは異なるので適宜設定する
        return r"C:\Program Files (x86)\Android\android-sdk\platform-tools\adb.exe"

    # タップ処理
    def tap(self, x, y, *, msg="", duration=200, wait=0):

        if msg != "":
            print(msg)

        cmd = [ self.path(), "shell", "input", "swipe", f'{x}', f'{y}', f'{x}', f'{y}', f"{duration}" ]
        subprocess.run(cmd)

        if wait>0:
            self.wait(wait)

    # スワイプ処理
    def swipe(self, x1, y1, x2, y2,*, msg="", duration = 0, wait=0):

        if msg != "":
            print(msg)

        d = duration
        if d == 0:
            d = self.lastDuration

        cmd = [ self.path(), "shell", "input", "swipe", f'{x1}', f'{y1}', f'{x2}', f'{y2}', f"{duration}" ]
        subprocess.run(cmd)

        self.lastDuration = d

        if wait>0:
            self.wait(wait)

    # 待ち
    def wait(self, sec, msg = ""):
        if msg != "":
            print(msg)

        time.sleep(sec)

    # 戻るキー押下
    def backKey(self,*,msg = "", wait=0):

        if msg != "":
            print(msg)

        cmd = [ self.path(), "shell", "input", "keyevent", '4' ]
        subprocess.run(cmd)

        if wait > 0:
            self.wait(wait)

class pzd:

    def __init__(self):
        self.adb = ADB()
        pass

    def ADBPath(self):
        return self.adb.path()

    def isAvailable(self):
        return os.path.exists(self.adb.path())

    # タップ
    def tap(self, x, y, *, msg="", duration=200, wait=0):
        self.adb.tap(x, y, msg=msg, duration=duration, wait=wait)

    # スワイプ
    def swipe(self, x1, y1, x2, y2,*, msg="", duration = 0, wait=0):
        self.adb.swipe(x1, y1, x2, y2, msg=msg, duration=duration, wait=wait)

    # 待つ
    def wait(self, sec, msg = ""):
        self.adb.wait(sec, msg=msg)

    # 戻るキー押下
    def backKey(self,*,msg = "", wait=0):
        self.adb.backKey(msg=msg, wait=wait)

    # メンバーのスキル使用
    def useSkill(self, index, *, msg="", wait=0):
        self.adb.tap(100+index*180, 1155, msg=msg, wait=wait)

    # ダンジョン選択(1階層目)
    def selectDangeon1(self, index, msg=""):
        self.adb.tap(600, 640 + index * 280, msg=msg, wait=1)
    
    # ダンジョン選択(2階層目)
    def selectDangeon2(self,index, msg=""):
        self.adb.tap(600, 640 + index * 280, msg=msg, wait=1)

    # スタミナ回復
    def kaifuku(self):

        # スタミナ足りません画面かどうかにかかわらずとりあえず押す
        # (助っ人選択画面だった場合は、行間なので何も起こらない)
        self.adb.tap(532, 1065, msg="魔法石で回復するボタンを押す", wait=1)
        self.adb.tap(532, 1080, msg="魔法石で回復するボタンを押す", wait=1)

        # ダミー処理
        # (スタミナが足りていて助っ人選択画面になってた場合に自助っ人を選択)
        self.adb.tap(500, 570)
    
        # スタミナが足りていた場合、この時点で潜入確認画面になっていて何も起こらない
        self.adb.tap(394, 1353, msg="回復するボタンを押す", wait=2)

        # スタミナ回復を実施した場合は回復しましたボタンをスキップ
        # 回復をせず、潜入確認画面に進んでいた場合は助っ人選択に戻る
        # (どちらにせよ、次の状態は助っ人選択画面になる)
        self.adb.backKey(msg="OKボタンをスキップ", wait=1)

    # 助っ人を選択
    def selectFriend(self, index):

        # 助っ人を選択
        self.adb.tap(520, 525 + index * 182, msg=f'助っ人を選択', wait=0.3)
    
        # 確定
        self.adb.tap(424, 1097, wait=1)
    

    def enterQuest(self):
        # 潜入確認
        self.adb.tap(520, 1757, msg="潜入確認→1Fが始まるまで待機",wait=12)

    
    # Tips画面をスキップする
    def skipTips(self,prewait=10):
        self.adb.wait(prewait, msg="TIPS画面がでるまで待機")
        self.adb.backKey(msg="OKボタンをクリックし待機", wait=9)
    
    # 結果画面をスキップ
    def skipResult(self, skipLevelup = True):
        self.adb.tap(600, 1582, duration=1900, msg="結果をスキップ", wait=3)
        if skipLevelup:
            self.adb.tap(600, 1416, msg="レベルアップがあったときのエフェクトまち", wait=3)
            self.adb.tap(600, 1416)
    
        self.adb.tap(600, 1416, msg="売却しないのでスキップ", wait=1)
        # 念のため
        self.adb.tap(520, 1757, wait=0.5)

