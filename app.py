import tkinter as tk
import tkinter.font as font
from time import sleep

from control import ChatControl


from PIL import Image, ImageTk


class Application(tk.Frame):
    """メインウィンドウ作成クラス

        フレームを作成し、画面の各種設定を行う。
        フレーム上にラベルやボタンなどのウィジェットを配置し、メインウィンドウを作成する。
        画面に表示する部品に対する処理や部品を追加する際などは、このクラスを修正する。

        Attributes:
            master (Tkinter): メインウィンドウ


    """
    def __init__(self, master):
        # スーパークラスFrameの__init__() を呼び出して初期化に必要な処理を実施
        super().__init__(master)
        # フレームをメインウィンドウに配置し
        self.pack()
        # 画面サイズの設定
        self.master.geometry("470x630")
        # TODO タイトルの設定
        self.master.title("AIボット")
        # フォントの設定
        self.master.option_add("*font", ["MSゴシック", 24])
        # 部品の配置
        self.create_widgets()
        # ChatControlのインスタンス
        self.chatControl = ChatControl()

    def create_widgets(self):
        """ウィジェットの設定

            メインウィンドウにキャンバスを設定し、ウィジェットを設置する。
            表示する画像を変更する場合は、このメソッドを修正する。

            Attributes:
                canvas:(:obj:Canvas):キャンバス（ウィジェットを設置する土台）のオブジェクト
                img_list (list): 画面に表示する画像のリスト
                frame_img:(:obj:PhotoImage):画像の設定を行うオブジェクト
                askbutton:(:obj:Button):ボタンのオブジェクト
                answer_font:(:obj:Font):フォント
                answer:(:obj:Label):ラベル
                inputarea:(:obj:Entry):入力フィールド

        """
        # 画像表示
        self.canvas = tk.Canvas(bg="white", width=470, height=630)
        self.canvas.place(x=0, y=0)

        # TODO チャットボットイメージ画像の設定（表示画像拡張エリア）
        from PIL import Image, ImageTk

        self.img_list = []

        for name in [
            "ryu.png",
            "image.png",
            "riku2.png",
            "ryu2.png",
            "riku3.png",
            "riku4.png",
            "riku.png",
            "riku8.png",
            "riku9.png",
            "riku10.png",
            "riku11.png"
        ]:
            
            img = Image.open(f"images/{name}").resize((200, 200))
            photo = ImageTk.PhotoImage(img)
            self.img_list.append(photo)

        self.canvas.create_image(
            235, 280, image=self.img_list[0], anchor="center", tag="ai-bot"
        )

        self.canvas.create_image(235, 280, image=self.img_list[0], tag="ai-bot")

        # フレームに画像の設定
        self.frame_img = tk.PhotoImage(file="images/tablet.png")
        self.canvas.create_image(235, 315, image=self.frame_img)

        # ボタン
        self.askbutton = tk.Button(text="▲", font=("", 18))
        self.askbutton.place(x=386, y=511)
        # ボタンに紐づけ
        self.askbutton["command"] = self.ask_click

        # 出力エリア
        self.canvas.create_rectangle(40, 420, 430, 500, outline = "pink", fill = "white")
        self.answer_font = font.Font(self.master,family="HG創英角ﾎﾟｯﾌﾟ体",size=16)
        self.answer = tk.Label(text="(話しかけられるのを待ってる)", bg="white", font=self.answer_font,justify='left')
        self.answer.place(x=50, y=430)

        # 入力エリア
        self.inputarea = tk.Entry(width=21, bd=4)
        self.inputarea.place(x=34, y=511)
        self.inputarea.focus()

        # リターンキー対応
        self.inputarea.bind('<Return>', self.ask_enter)

    # エンターキー押した
    def ask_enter(self,event):
        self.ask_click()

    # ボタン押した
    def ask_click(self):
        """ボタン押下時の動作制御

            入力メッセージを取得し実行する処理の制御を行う。
            ChatControlクラスのメソッドからの戻り値にしたがって、以下の処理を行う。
            ・応答メッセージの設定
            ・画面表示画像の切り替え
            ・画面の初期化

        """
        # 入力値の取得
        message = self.inputarea.get()
        # 入力欄クリア
        self.inputarea.delete(0, tk.END)

        # チャット制御
        chat = self.chatControl.control(message)
        replay_message = chat.replay_message
        image_no = chat.image_idx
        init_flg = chat.init_flg

        self.answer["text"] = "connecting"
        for i in range(3):
            self.master.update()
            self.answer["text"] += "."
            sleep(0.5)

        self.canvas.itemconfig("ai-bot", image=self.img_list[image_no])
        self.answer["text"] = replay_message
        self.master.update()

        if init_flg:
            sleep(3)
            self.canvas.itemconfig("ai-bot", image=self.img_list[0])
            self.answer["text"] = "(話しかけられるのを待ってる)"
