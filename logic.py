import requests

from chat import Chat
from status import FuncStatus

import random


class ChatLogic:
    """チャットロジッククラス

    チャットコントロールから呼び出され、チャットの各機能を実行する。

    Attributes:
        calc(:obj:Calc): 計算機能
        status(:obj:FuncStatus): 機能継続状態管理
    """

    def __init__(self):
        self.status = FuncStatus()
        # TODO 入力パラメータの追加
        self.x = None
        self.y = None
        self.hit_answer = None
        self.guess_counter = 0

    def replay(self, message):
        """チャットの応答

        引数で受け取ったmessageにしたがって、戻り値を返す。
        処理の継続が必要な機能の場合は、機能実行状態の更新を行う。

        Args:
            message (str): 処理対象のメッセージ.

        Returns:
            obj:Chat: チャットの応答情報

        """

        chat = Chat()  # 返答用オブジェクト
        # TODO メッセージ分岐（チャット拡張エリア）
        if "足し算" in message:
            self.x, self.y = (None, None)
            self.status.calc_flg = True
            chat.set_replay_data("足したい値を入力してください")

        elif "給与計算" in message:
            self.x, self.y = (None, None)
            self.status.payroll_flg = True
            chat.set_replay_data("労働時間：")
        elif "名言" in message:
            url = "http://127.0.0.1:8000/good_words/"
            param = {"message": message}
            res = requests.get(url, param)
            replay_message = res.json()["result"]
            image_idx = res.json()["image_idx"]
            chat.set_replay_data(replay_message, image_idx, True)
        elif "おみくじ" in message:
            url = "http://127.0.0.1:8000/omikuji/"
            param = {"message": message}
            res = requests.get(url, param)
            replay_message = res.json()["result"]
            image_idx = res.json()["image_idx"]
            chat.set_replay_data(replay_message, image_idx, True)

        elif "数当てゲーム" in message:
            url = "http://127.0.0.1:8000/hitgame/"
            self.hit_answer = random.randint(1, 100)
            self.guess_counter = 0
            self.status.hitgame_flg = True
            chat.set_replay_data("予想を入力してください")
        elif "何時" in message:
            url = "http://127.0.0.1:8000/get_datetime/"
            param = {"message": message}
            res = requests.get(url)
            replay_message = "{}だよん".format(res.json()["result"])
            image_idx = res.json()["image_idx"]
            chat.set_replay_data(replay_message, image_idx, True)
        elif "郵便番号" in message:
            url = "http://127.0.0.1:8000/zipcode/"
            self.status.zipcode_flg = True
            chat.set_replay_data("郵便番号を入力してください")

        else:
            # WebAPIリクエストURI
            url = "http://127.0.0.1:8000/replay/"
            param = {"message": message}
            res = requests.get(url, param)
            replay_message = res.json()["result"]
            image_idx = res.json()["image_idx"]
            chat.set_replay_data(replay_message, image_idx, True)

        return chat

    def calc_func(self, message):
        """計算機能

        足し算APIを呼び出し、チャットの応答メッセージを作成する。
        計算処理が終わった場合は、計算クラスのインスタンス、機能実行状態の更新を行う。

        Args:
            message (str): 処理対象のメッセージ.

        Returns:
            Chat: チャットの応答情報

        """
        chat = Chat()
        if self.x == None:
            replay_message1 = "もう一つの値は？"
            try:
                self.x = int(message)
            except ValueError:
                chat.set_replay_data("数字以外を入力しないでください")
                return chat
            chat.set_replay_data(replay_message1)
        else:
            try:
                self.y = int(message)
            except ValueError:
                chat.set_replay_data("数字以外を入力しないでください")
                return chat

            # chat.set_replay_data(replay_message1)
            url = "http://127.0.0.1:8000/add/"
            param = {"x": self.x, "y": self.y}
            res = requests.get(url, param)
            result = res.json()["result"]
            replay_message2 = "合計は、{0}です。"
            self.status.calc_flg = False
            chat.set_replay_data(
                replay_message2.format(result), image_idx=1, init_flg=True
            )
        return chat

    def payroll_func(self, message):
        chat = Chat()
        if self.x == None:
            replay_message1 = "時給："
            try:
                self.x = int(message)
            except ValueError:
                chat.set_replay_data("数字以外を入力しないでください")
                return chat

            chat.set_replay_data(replay_message1)
        else:
            try:
                self.y = int(message)
            except ValueError:
                chat.set_replay_data("数字以外を入力しないでください")
                return chat
            url = "http://127.0.0.1:8000/payroll/"
            param = {"x": self.x, "y": self.y}
            res = requests.get(url, param)
            result = res.json()["result"]
            replay_message2 = "給料は、{0}です。"
            self.status.payroll_flg = False
            chat.set_replay_data(replay_message2.format(result), image_idx=1, init_flg=True)
        return chat

    def hitgame_func(self, message):
        chat = Chat()

        self.guess_counter  += 1
        try:
            guess = int(message)
        except ValueError:
            chat.set_replay_data("数字以外を入力しないでください")
            return chat

        url = "http://127.0.0.1:8000/hitgame/"
        param = {
            "answer": self.hit_answer,
            "guess": guess
        }

        res = requests.get(url, param)
        result = res.json()["result"]

        if result == "hit":
            replay_message = "🎉 正解！おめでとう！{}回で正解！".format(self.guess_counter)
            self.status.hitgame_flg = False
            self.hit_answer = random.randint(1, 10)
            chat.set_replay_data(replay_message, image_idx=6, init_flg=True)

        elif result == "near":
            replay_message = "おしい！かなり近いです！（±2）"
            chat.set_replay_data(replay_message, 8)

        elif result == "low":
            replay_message = "もっと大きい数です"
            chat.set_replay_data(replay_message, 9)

        elif result == "high":
            replay_message = "もっと小さい数です"
            chat.set_replay_data(replay_message, 10)

        return chat
    def zipcode_func(self, message):
        chat = Chat()

        url = "http://127.0.0.1:8000/zipcode/"
        param = {"code": message}

        res = requests.get(url, params=param)

        result = res.json()["result"]
        replay_message = "住所は\n{}です。\nえ、ここに住んでるの？？".format(result)

        chat.set_replay_data(replay_message,1, init_flg=True)

        self.status.zipcode_flg = False

        return chat


def calc_func(self, message):
    """計算機能

    足し算APIを呼び出し、チャットの応答メッセージを作成する。
    計算処理が終わった場合は、計算クラスのインスタンス、機能実行状態の更新を行う。

    Args:
        message (str): 処理対象のメッセージ.

    Returns:
        Chat: チャットの応答情報

    """
    chat = Chat()
    if self.x == None:
        replay_message1 = "もう一つの値は？"
        self.x = int(message)
        chat.set_replay_data(replay_message1)

   
    else:
        self.y = int(message)
        url = "http://127.0.0.1:8000/add/"
        param = {"x": self.x, "y": self.y}
        res = requests.get(url, param)
        result = res.json()["result"]
        replay_message2 = "合計は、{0}です。"
        self.status.calc_flg = False
        chat.set_replay_data(replay_message2.format(result), image_idx=1, init_flg=True)
    return chat
