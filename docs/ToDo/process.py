import os

if __name__ == "__main__":
    paths = os.walk('/Users/apple/Desktop/mkdocs-site/docs/ToDo/LeetCode')
    files = []
    for path, dir_lst, file_lst in paths:

        for file_name in file_lst:
            if "_" in file_name and not file_name.startswith("0"):
                files.append((file_name, file_name.split("_")[0]))
                # print(file_name)
    files.sort(key=lambda x: x[1])
    # print(files)
    for (a, b) in files:
        # print(i)
        # print("- " + "" + "ToDo/LeetCode/" + a[0] + "/" + a)

        # 输出在mkdocs目录里的情况
        # print(f"- {a} : ToDo/LeetCode/{a[0]}/{a}")

        # 输出处理后的表格的情况（自动脚本）
        print(
            f"| {b} | {str(a).split('_')[1][:-3]} | [Link](./{a[0]}/{a}) | Unknown | Unknown | Unknown |")


# | Index | Intro | Solution | Difficulty | Keywords | Notes |
# | :---: | :---: | :------: | :--------: | :------: | :---: |
