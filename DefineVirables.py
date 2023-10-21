#這一篇會教妳如何定義變數。變數在程式裡面是在常見不過的東西，因為變數的出現，讓程式變的人性化許多。
#在python裡面不用特別宣告變數是什麼類型的，他會自動判別，例如
something = 123
>>> print(type(something))
>>> int
something_float = 123.456
 >> print(type(something_float))
 >>>float
something_bool = True
>>>print(type(something_bool))
>>>bool
#基本上這樣已經很方便了，如果想要固定變數的類別的話可以用這個方式
some_int:int = 123
some_float:float = 123.456
#這樣就可以定義他的變數類別，其他的類別也是如此

#變數的類別
ints:int = 123 #int:整數，就是定義整整數
floats:float = 123.456 #float:小樹，跟整數一樣
booleans:bool = True #bool：布林值，只有對（True)跟錯（False)兩種資料內容
tuples:tuple = (123,345) #這個東西定義之後就不可以被修改，所以又稱為只讀列表
lists:list = ["123","456"] #list:清單，或是說串列，可以多個資料一起儲存，當然也可以多個類別混在一起
dicts:dict = {"123":"345"} #Dict:字典，每個鑰匙都有相對應的值對應，所以怎麼寫是有規定的，但是鑰匙跟值的類別可以不一樣
sets:set = {123,345} #set:集合，跟list很像，但是set不能重複，沒有排序，意指不能要讀就要全部一起讀
something = None #沒有，就是沒有

#下一章我們會學到如何定義函式來讓程式變簡潔、易懂與較容易維護
