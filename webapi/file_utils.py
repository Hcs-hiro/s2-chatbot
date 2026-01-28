def file_append(file_path, value):
  """ファイル追記
  引数で指定されたファイルに引数で受け取った値を追記する。
  Attributes:
  file_path (str): 追記対象のファイルパス.
  value (str): 追記する値
  Raises:
  IOError: ファイルをほかのプロセスで使用している場合に発生
  """

  try:
    with open(file_path, mode="a", encoding="utf-8") as f:
      f.write(value.rstrip("\n") + "\n")
  except IOError as e:
    raise IOError("ファイルへの追記に失敗しました") from e

def file_readlines(file_path):
    lines = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            lines.append(line.rstrip("\n"))

    return lines


def file_read(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            value = f.read().strip()
            if value == "":
                return None
            return int(value)

    except FileNotFoundError:
        return None


def file_write(file_path, value):
  try:
    with open(file_path, mode = "w", encoding="utf-8") as f:
      f.write(str(value))
  except IOError as e:
    raise IOError("失敗") from e
