# GIT-DEMO
12/26-
版本 : 
>git --version

建立全域端使用者 : 
>git config --global user.name [your name]
>git config --global user.email [your email]

檢視細節設定:
>git config --list

(in vscode: Terminal 終端機)
#vscode指令: 
  	#ctrl+shift+p > default >Tterminal :select default >connend prumpt > 刪掉舊的terminal 開啟新terminal
  
	控管專案folder:
	>git init
 	(讓.git的檔案夾跑出來:prefer >seting >搜尋ex >git刪除隱藏 )

	檔案加入控管: 
	>git add [file name]  => "U"ntrack變成"A"dded >"M"dify >"D"eleted
	檢視誰是否被控管:
	>git status

	>git cat-file
	-t看格式 [目錄名稱+檔案編號4碼(sha-1)]
	-s 看size
	-p看內容
		git cat-file -t sha1(2+4)
      		git cat-file -p sha1(2+4)
	>>修改過內容後確認修改:git add [filename] (確認修改/確認新增/確認刪除)
  	   反悔修改:git restore [filename]  (M變回A) (確認刪除跟恢復刪除同理)

	檢視object暫存區(仍可反悔)中的控管內容是屬於哪一個file的:
	>git ls-files -s

	記錄到倉儲區(reporter):
	>git commit -m "message" (裡面填想寫的memo)

	>git add . (所有)
	檢視目前有幾個儲存點:
	>git log
	>git log --oneline (濃縮在一行看)

12/28-
自動格式化: 搜尋插件>black formatter(microsoft) 回原編輯檔按ctrl+S

#內建編輯器:
	new Terminal 輸入
      >git commit    按enter開啟vim編輯器 
	>> 打小寫i用insert開始記錄
	寫完之後按esc取消記錄模式
	:wq (紀錄後離開) **一定要加冒號
	:q! (不紀錄後離開)
		就會記錄到commit
合併上一次的commit:
>git comit --amend   (會開啟上一次的 commit/編輯器指令 進行修改的動作)

 -使用指令刪除: (手動刪除按delet>git add .)
 >git rm -f [filename]  (f是全功能的意思full)
 >git restore --staged [filename] (恢復刪除檔)
 >git rm --cached [filename]  (從"A"變回"U",移出暫存區/倉庫區不被控管)
 
#在sorce control中:
	>+ : 確認add的意思
	>向返回的箭頭: restore救回檔案
#vscode指令: 
	>git checkout [分支名稱] (切換到分支操作)

	檢視分支:
	>git branch (*字號是正在操作的)
	
	新增分支:
	>git branch [分支名稱]

	進行分支合併: (要先切換到要合併的主分支(通常是master))
	>git merge [branchfile name]

	刪除分支:
	>git branch -D [branchfile name]  **不能在自己的分支刪除自己
	
	自動切換新增分支: (新增+切換2合一)
	>git checkout -b [branchfile name]

	add+commit二合一: git add . + git commit -m" "
	>git commit -am"memo"

 ##合併衝突:
	-不同分支改動同一個檔案(選擇合併方式)
	反悔指令:
	>git merge --abort
 	 
	想看當初的commit當下的情境寫的程式碼:
	>先用git log --oneline
	>git checkout [commit-sha1(2+4)] (回到過去的修正)
		-新增分支跟commit
     		-切回master進行合併
	重置指令..回到最原始點(真正恢復回到過去的commit): reset
	--三種模式mixed/soft/hard
	>git reset [commit-sha1(2+4)]   (在那之後的全部會變成不被控管的)
	>git reset --soft [commit-sha1(2+4)]   (刪除其中一個commit)
	>git reset --hard [commit-sha1(2+4)]   (刪除選定的commit之後的所有修改動作)

	>git reset ORIG_HEAD  (恢復到上一動)

	>git reset --hard HEAD (重置到最新commit)
	>git reset --hard HEAD~1  (重置到最新commit的前一個)


2024/01/02-

   #檢視所有歷程:
	>git reflog

#程式碼控管 : github
- echo "# git-demo1" >> README.md
- git init
- git add README.md
- git commit -m "first commit"
- git branch -M main
- git remote add origin https://github.com/SandyChen1201/git-demo1.git  (本地端跟遠端URL連動)+
	>git remote -v (查看本地專案綁訂的雲端倉庫(v=view))
	  >第一次需要git push --set-upstream origin master
		 或是git push --set-u origin master   
	>git push (資料同步到雲端)
- git push -u origin main


複製雲端專案
- git clone https://github.com/SandyChen1201/git-demo1.git