🐍 今天的 Python 小筆記：計算圓面積！

今天我們學了一些神奇的程式語言 Python 的指令，來幫我們計算圓的面積。一起來看看是怎麼做的吧！

🧠 我們要做的事是什麼？
我們要做的事情是：
👉「讓電腦幫我們算出一個圓的面積！」

💻 今天學到的程式碼
import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi \* radius\*\*2
print("The area of the circle is ", area)
🧩 每一行的意思是什麼？
1️⃣ import math

我們請電腦幫我們「叫出數學工具箱」。
因為我們要用到圓周率 π（唸作「派」）這個數字。
2️⃣ radius = float(input("Enter the radius of the circle: "))

我們讓使用者輸入圓的半徑。
input() 是請人輸入資料。
float() 是讓電腦知道，這是一個小數。
radius（唸作「瑞迪耶斯」）是「半徑」的英文。
3️⃣ area = math.pi \* radius\*\*2

我們用公式來算圓的面積：
👉 面積 = π × 半徑 × 半徑
math.pi 就是 π（約等於 3.14159）。
radius\*\*2 的意思是「半徑平方」就是半徑 × 半徑。
4️⃣ print("The area of the circle is ", area)

這行會把答案印出來給我們看！
它會說：「圓的面積是…」然後顯示出數字。
✅ 小小總結：
今天學到的重點是：

怎麼讓電腦問我們一個問題（像是「請輸入半徑」）。
怎麼用公式算圓的面積。
怎麼把答案印出來。
