PTT-backup
==========
###Introuction
平常在使用PTT的時候我習慣依照固定的搜尋方式來看看有沒有新文章  
所以我希望有一個機器人可以幫我整理好文章，節省一些搜尋的時間

####使用範例：
* 喜歡看<作者>的文章
* 喜歡看八卦版爆文

###Usage
python main.py

###Write Config
####Part 1: 更改檔名 config.ini.sample 成為 'config.ini'  
####Part 2: 填入帳號資訊
[Account]  
account  = <帳號>  
password = <密碼>  

####Part 3: 寫下規則
[<規則名稱>]  
board  = <看板名稱>  
Type   = <搜尋類型>  
Target = <目標>  

###目前支援的搜尋類型  
| Type          | Target        | 
| ------------- |:-------------:| 
| num           | 推文數量      | 
| author        | AuthorID      |

###未來支援的搜尋類型
* ~~author~~
* title  
* update read article

###未來會開發的功能
* 寄信
* 排程


