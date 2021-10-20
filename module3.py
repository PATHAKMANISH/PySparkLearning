import module2

print("the name of this module is ",__name__)

#"C:\Trendy Tech\PySpark\PySparkLearning\venv\Scripts\python.exe" "C:/Trendy Tech/PySpark/PySparkLearning/module3.py"
#the name of this module is  module2
#the name of this module is  __main__

# because it has been executed indirectly not directly from that file

a= 5
print(a)

#Python is a dynamically typed language. There is no need to specifically declare data type of variable .
# In python interpreter itself predict the data type

# declare function in python
# named function
def sum(a,b) :
    return a+b
total = sum(3,4)

print(total)

# just like in scala in python also we can define a function without a name ( anonumous function in scala )
# same annonymous function in scala are called LAMDA FUNCTION IN PYTHON
