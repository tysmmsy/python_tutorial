import re

# \S =空白を除く全ての文字列の抽出
url_pattern = "https?://\S+"

# 半角英数と_/:%#$&~=?().+- を文字列の抽出
url_pattern2 = "https?://[\w/:%#&~=\$\?\(\)\.\+\-]+"

text1 = "Axross のURLは、 https://axross-recipe.com/recipes です。"

url_list = re.findall(url_pattern, text1)
print(url_list)
