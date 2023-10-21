#在這篇教學中，你將會學到如何定義函式，函式會讓程式變簡潔易懂，來個對比
#沒有函式的情況
numbers = [2, 4, 6, 8, 10]
total = 0

for num in numbers:
        if num % 2 == 0:
                    total += num

                    if total > 0:
                            average = total / len([x for x in numbers if x % 2 == 0])
                        else:
                                average = 0

                                print("偶数的平均值是：" + str(average))
#有函式的話
def calculate_even_average(nums):
        even_numbers = [x for x in nums if x % 2 == 0]
        if even_numbers:
            return sum(even_numbers) / len(even_numbers)
        else:
            return 0

numbers = [2, 4, 6, 8, 10]
average = calculate_even_average(numbers)
print("偶数的平均值是：" + str(average))

#現在來學定義函式吧
#函式的結構

def your_function_name():
    #your codes
#def:告訴python你要定義一個函式名叫your_function_name,其中your_function_name要改什麼都可以（中文也OK)

#如果要有函式輸入值的話也OK
def function(value1:int,value2:float):
    #your code
#輸入值也可以指定類別喔

def functions(value1:int, value2:int) -> int:
    return value1+value2
#如果要規定函式輸出的話就可以用->來規定喔(但是基本上沒有特別的需求不會去定義）

#小範例：製作計算機
def add(a:float,b:float):
    return a+b

def minus(a:float,b:float):
    return a-b

def times(a:float, b:float):
    return a*b

def div(a:float,b:float):
    if b == 0:
        raise ZeroDivisionError("connot div by 0")
    else:
        return a/b

 >>> print(add(2,3))
 >>> 5
