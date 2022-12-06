# 二乗を返すバリエーション
def square(x):
    return x * x


# 無名関数 lambda 引数: 返り値
lambda x: x * x

# square = lambda x : x * xのように名前をつけて呼び出すこともできるが、Pythonのコーディング規約に違反している。
# 構文上はエラーがでないが、推奨されていない。
# 一部の組み込み関数の引数として使うことにある。
#
student = [
    {"Name": "Alice", "Math": 75},
    {"Name": "Carles", "Math": 85},
    {"Name": "Bob", "Math": 45},
]

print(sorted(student, key=lambda x: x["Math"], reverse=True))

# formatメソッド
site_name = "Test"
site_url = "http://sample:1010/"
print("{name}のURLは{url}です.".format(name=site_name, url=site_url))
print(f"{site_name}のURLは{site_url}です")
