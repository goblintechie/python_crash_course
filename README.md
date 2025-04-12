# Python_Crash_Course

参考资料：[Python编程：从入门到实践（第2版）](https://weread.qq.com/web/bookDetail/08232ac0720befa90825d88)

[02 变量和简单数据类型](https://github.com/baoyg/Python_Crash_Course/tree/main/02%20%E5%8F%98%E9%87%8F%E5%92%8C%E7%AE%80%E5%8D%95%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B) 

> 在本章学习在Python程序中使用各种数据，还将学习如何在程序中使用变量表示这些数据。

本章小结：
1. 如何使用变量；
2. 如何创建描述性变量名以及如何消除名称错误和语法错误；
3. 字符串是什么，以及如何使用小写、大写和首字母大写方式显示字符串；
4. 使用空白来显示整洁的输出，以及如何剔除字符串中多余的空白；
5. 如何使用整数和浮点数；
6. 一些使用数值数据的方式。
7. 还学习了如何编写说明性注释，让代码对你和其他人来说更容易理解。
8. 了解了让代码尽可能简单的理念。

---

[03 列表简介](https://github.com/baoyg/Python_Crash_Course/tree/main/03%20%E5%88%97%E8%A1%A8%E7%AE%80%E4%BB%8B)

> 本章和下一章学习列表式什么以及如何使用列表元素。列表让你能够在一个地方存储成组的信息，其中可以包含几个元素，也可以包含数百万个元素。

本章小结：
1. 列表是什么以及如何使用其中的元素；
2. 如何定义列表以及如何增删元素；
3. 如何对列表进行永久性排序，以及如何为展示列表而进行临时排序；
3. 如何确定列表的长度，以及在使用列表时如何避免索引错误。

---

[04 操作列表](https://github.com/baoyg/Python_Crash_Course/tree/main/04%20%E6%93%8D%E4%BD%9C%E5%88%97%E8%A1%A8)

> 第3章学习了如何创建简单的列表，以及如何操作列表元素。
> 本章将学习如何遍历整个列表。循环能让你对列表的每个元素采取一种或一系列相同的措施，从而高效地处理任何长度的列表，包括数千乃至数百万个的列表。

本章小结：
1. 如何高效地处理列表中的元素；
2. 如何使用`for`循环遍历列表，Python如何根据缩进来确定程序的结构，以及如何避免一些常见的缩进错误；
3. 如何创建简单的数字列表，以及可对数字列表执行的一些操作；
4. 如何通过切片来使用列表的一部分和复制列表。
5. 还学习了元组（它对不应变化的值提供了一定程度的保护）​，以及在代码变得越来越复杂时如何设置格式，使其易于阅读。

---

[05 if语句](https://github.com/baoyg/Python_Crash_Course/tree/main/05%20if%E8%AF%AD%E5%8F%A5)

> 编程时经常要检查一系列条件，并据此决定采取什么措施。
> 本章将学习条件测试，以检查关心的任何条件。将学习简单的`if`语句，创建一系列复杂的`if`语句来确定当前处于什么情形。
> 将学到的知识应用于列表，编写一个`for`循环，以一种方式处理列表中大多数元素，并以另一种方式处理包含特定值的元素。

本章小结：
1. 如何编写结果要么为`True`要么为`False`的条件测试；
2. 如何编写简单的`if`语句、`if-else`语句和`if-elif-else`结构，并且在程序中使用这些结构来测试特定的条件，以确定这些条件是否满足；
3. 如何在利用高效的for循环的同时，以不同于其他元素的方式对特定的列表元素进行处理。
4. 再次学习了Python就代码格式提出的建议，从而确保即便编写的程序越来越复杂，其代码依然易于阅读和理解。

---

[06 字典](https://github.com/baoyg/Python_Crash_Course/tree/main/06%20%E5%AD%97%E5%85%B8)

> 本章学习能够将信息关联起来的Python字典，以及如何访问和修改字典中的信息。
> 字典可存储的信息量几乎不受限制，因此会演示如何遍历字典中的数据。
> 还将学习存储字典的列表、存储列表的字典和存储字典的字典。
> 理解字典后就能更准确地为各种真实物体建模。可以创建一个表示人的字典，其中存储他的各种信息：姓名、年龄、地址、职业等等。
> 你还能存储任意两种相关的信息，如一系列单词及其含义，一系列人名及其喜欢的数，山脉及其海拔等。

本章小结：
1. 如何定义字典，以及如何使用存储在字典中的信息；
2. 如何访问和修改字典中的元素，以及如何遍历字典中的所有信息；
3. 如何遍历字典中所有的键值对、所有的键和所有的值；
4. 如何在列表中嵌套字典、在字典中嵌套列表以及在字典中嵌套字典。

---

[07 用户输入和while循环](https://github.com/baoyg/Python_Crash_Course/tree/main/07%20%E7%94%A8%E6%88%B7%E8%BE%93%E5%85%A5%E5%92%8Cwhile%E5%BE%AA%E7%8E%AF)

> 本章学习如何接受用户输入，以便程序进行处理。程序需要一个名字时，需要提示用户输入该名字；程序需要一个名单时，需要提示用户输入一系列名字。为此将使用函数`input()`。
> 还将学习如何让程序不断运行，以便用户根据需要输入信息，并在程序中使用这些信息。为此将使用`while`循环让程序不断运行，直到指定的条件不满足为止。
> 通过获取用户输入并学会控制程序的运行时间，就能编写交互式程序。

本章小结：
1. 如何在程序中使用`input()`来让用户提供信息；
2. 如何处理文本和数的输入，以及如何使用`while`循环让程序按用户的要求不断运行；
3. 多种控制`while`循环流程的方式：设置活动标志、使用`break`语句以及使用`continue`语句；
4. 如何使用`while`循环在列表之间移动元素，以及如何从列表中删除所有包含特定值的元素；
5. 如何结合使用`while`循环和字典。

> 在本章中学习编写函数。函数是带名字的代码块，用于完成具体工作。
> 要执行函数定义的特定任务，可调用该函数。需要在程序中多次执行同一项任务时，无需反复编写完成该任务的代码，只需要多次调用函数。
> 还将学习向函数传递信息的方式；学习如何编写主要任务是显示信息的函数，以及用来处理数据并返回一个或一组值的函数；
> 最后学习如何将函数存储在称为模块的独立文件中，让主程序文件的组织更为有序。