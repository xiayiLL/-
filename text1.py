import unittest
from sizeyunsuanxiaoxue import newint

class TestFun(unittest.TestCase):
    times = 0

    @classmethod
    def setUpClass(self):
        print('Test begining:setUpclass........')
 
    def setUp(self):
        # 每个测试用例执行之前都会执行该方法
        TestFun.times += 1
        print('setUp', TestFun.times)
 
    def tearDown(self):
        # 每个测试用例执行之后都会执行该方法
        TestFun.times += 1
        print('tearDown', TestFun.times)
 
    def test1(self):  #运算测试
        test = newint(2,5,4)
        result = 20
        self.assertEqual(test,result)
    
    @unittest.skipIf(True, 'no')
    def test5(self):
        print('跳过!')
    @classmethod
    def tearDownClass(cls):  #测试结束
        print('Test End:tearDownClass.......')



if __name__ == '__main__':
    for i in range(3):
        unittest.main()
