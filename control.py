from logic import ChatLogic


class ChatControl:
    """チャットコントロールクラス

    チャットの処理を制御する

    Attributes:
    chat(:obj:Chat): チャットの応答情報
    chatLogic(:obj:ChatLogic):チャットの各機能の処理
    """

    def __init__(self):
        self.chatLogic = ChatLogic()

    def control(self, message):
        """チャットの制御を行う

        機能の実行状態に従って処理を振り分ける。
        機能実行状態のフラグがTrueであれば、該当機能を実行する。
        機能実行状態のフラグが全てFalseであれば、replayメソッドを実行する。

        Args:
            message (str): 処理対象のメッセージ.

        Returns:
            obj:Chat: チャットの応答情報

        Raises:
            ValueError: 数値入力が必要なケースで文字が入力された場合に発生


        """
        # TODO 機能継続チェック
        if self.chatLogic.status.calc_flg:
            chat = self.chatLogic.calc_func(message)
        elif self.chatLogic.status.record_flg:
            chat = self.chatLogic.record_func(message)
        elif self.chatLogic.status.payroll_flg:
            chat = self.chatLogic.payroll_func(message)
        elif self.chatLogic.status.dutch_treat_flg:
            chat = self.chatLogic.dutch_treat_func(message)
        elif self.chatLogic.status.hitgame_flg:
            chat = self.chatLogic.hitgame_func(message)
        elif self.chatLogic.status.hitblow_flg:
            chat = self.chatLogic.hitblow_func(message)
        elif self.chatLogic.status.week_flg:
            chat = self.chatLogic.get_day_of_week_func(message)
        elif self.chatLogic.status.zipcode_flg:
            chat = self.chatLogic.zipcode_func(message)
        elif self.chatLogic.status.event_flg:
            chat = self.chatLogic.event_func(message)
        elif self.chatLogic.status.salary_flg:
            chat = self.chatLogic.predict_salary_func(message)
        elif self.chatLogic.status.exam_flg:
            chat = self.chatLogic.predict_exam_func(message)
        elif self.chatLogic.status.condition_flg:
            chat = self.chatLogic.predict_condition_func(message)
        elif self.chatLogic.status.jyanken_flg:
            chat = self.chatLogic.jyanken_func(message)
        elif self.chatLogic.status.translator_flg:
            chat = self.chatLogic.translator_func(message)
        # elif self.chatLogic.status.log_flg:
        #     chat = self.chatLogic.record_output(message)
        else:
            chat = self.chatLogic.replay(message)
        return chat
