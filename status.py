class FuncStatus:
    """機能の実行状態を管理するクラス

    機能の実行状態を管理する。
    複数回やり取りする必要がある機能ごとに変数を定義しbool値で管理する。

    Attributes:
        calc_flg(bool): 足し算機能の継続判定フラグ

    """

    def __init__(self):
        # TODO 実行状態のフラグ（各機能の実行状態フラグ拡張エリア）
        self.record_flg = False
        self.calc_flg = False
        self.payroll_flg = False
        self.dutch_treat_flg = False
        self.hitgame_flg = False
        self.hitblow_flg = False
        self.week_flg = False
        self.zipcode_flg = False
        self.event_flg = False
        self.salary_flg = False
        self.exam_flg = False
        self.condition_flg = False
        self.jyanken_flg = False
        self.translator_flg = False
