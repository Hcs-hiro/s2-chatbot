class Chat():
    """チャットクラス

        チャットの応答情報を管理する
        
        Attributes:
            replay_message(str): 応答メッセージ
            image_idx(int):出力画像のindex
            init_flg(bool):初期化flg
            
    """
    def __init__(self):
        self.replay_message = ""
        self.image_idx = 0
        self.init_flg = False

    def set_replay_data(self,replay_message,image_idx=0,init_flg=False):
        # TODO 返答用メッセージ設定
        self.replay_message = replay_message
        self.image_idx = image_idx
        self.init_flg = init_flg
