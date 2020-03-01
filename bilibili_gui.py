import json
import os
import tkinter as tk
import tkinter.filedialog
from bilibili_downloader import Bilibili


class BilibiliGui(tk.Frame):
    url_entry = None
    url_button = None
    hint_text = None
    file_dialog_button = None
    save_dir_label = None
    msg = None

    def __init__(self, master=None):
        super().__init__(master)

        self.config_file = 'config.json'
        self.config = {}
        self.read_config()

        self.bilibili = Bilibili(self.config.get('save_dir', os.getcwd()))

        self.master = master
        self.pack()
        self.create_widgets()

    def read_config(self):
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf8') as f:
                    self.config = json.loads(f.read())
            except Exception:
                pass

    def dump_config(self):
        with open(self.config_file, 'w', encoding='utf8') as f:
            f.write(json.dumps(self.config))

    def create_widgets(self):
        fm1 = tk.Frame(self)
        fm1.pack(anchor='w')
        label = tk.Label(fm1, text='视频网址')
        label.pack(padx=10, pady=5, side=tk.LEFT)

        self.url_entry = tk.Entry(fm1, width=40)
        self.url_entry.pack(pady=5, side=tk.LEFT)

        self.url_button = tk.Button(fm1, text='下载', command=self.download)
        self.url_button.pack(padx=5, pady=10)

        fm2 = tk.Frame(self)
        fm2.pack(anchor='w')
        self.file_dialog_button = tk.Button(fm2, text='选择要保存的目录', command=self.select_save_dir)
        self.file_dialog_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.save_dir_label = tk.Label(fm2, text=self.config.get('save_dir', os.getcwd()))
        self.save_dir_label.pack(side=tk.LEFT, padx=10, pady=5)

        fm3 = tk.Frame(self)
        fm3.pack(anchor='w')
        self.msg = tk.Message(fm3, text='', width=370)
        self.msg.pack(side=tk.LEFT, padx=10, pady=10)

    def select_save_dir(self):
        path = tkinter.filedialog.askdirectory()
        if path:
            self.bilibili.set_save_dir(path)
            self.save_dir_label['text'] = path
            self.config['save_dir'] = path
            self.dump_config()

    def download(self):
        url = self.url_entry.get()
        self.msg['text'] = f'开始下载 {url}'
        self.bilibili.get_video(url)


def main():
    root = tk.Tk()
    root.minsize(450, 100)
    root.title('bilibili下载器')
    app = BilibiliGui(root)
    app.mainloop()


if __name__ == '__main__':
    main()