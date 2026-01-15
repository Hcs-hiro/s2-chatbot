import requests

from chat import Chat
from status import FuncStatus


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
       
        
        elif "追加する機能の処理メッセージ" in message:
            pass
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
            chat.set_replay_data(
                replay_message2.format(result), image_idx=1, init_flg=True
            )
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



