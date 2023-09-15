# 我的 Git 使用cheat sheet


!!! note "开发流程"
    改，发pr，检视，合入main。

!!! note "Git 当前分支落后主干分支的解决办法"
    当前的开发分支：feat-one，主线分支：main


    1.  切换到主线分支main：

    ```shell
    git checkout main
    ```

    2.  拉取远程主线分支main到本地的主线分支main ：

    ```shell
    git pull --rebase
    ```

    3.  切回到当前的开发分支feat-one：

    ```shell
    git checkout feat-one
    ```

    4.  拉取远程分支main 的代码：

    ```shell
    git rebase main
    ```

    5.  将当前开发分支分支feat-one提交到远程分支feat-one：

    ```shell
    git push origin feat-one -f
    ```


!!! note "把main分支同步到自己的分支"

    1. 创建自己分支：

    ```shell
    git checkout -b my-branch
    ```

    2. 提交到自己分支

    ```shell
    git add .
    git commit -m "Commit message"
    ```

    3. 一段时间后发现要合并主分支的修改

    ```shell
    git checkout main
    git pull origin main
    ```

    （切换到main分支，然后把main分支pull下来）

    4. 切换到自己的分支进行合并操作

    ```shell
    git checkout my-branch
    git merge master
    ```

    5. 如果有冲突，git status 查看冲突的文件

    ```shell
    git add conflict-file.txt
    git commit -m "Merge changes from master into my-branch"
    ```


