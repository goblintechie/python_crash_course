在`test_survey.py`中每个测试方法都创建了一个`AnonymousSurvey`实例，每个方法都创建了答案。
使用`unittest.TestCase`的`setUp()`方法可以让我们只创建对象一次就可以在每个测试方法中使用。
在`TestCase`类中包含了方法`setUp()`，Python会先运行它，再运行各个以`test_`开头的方法。这样每个测试方法都会用到这个对象。
