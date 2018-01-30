#!/usr/bin/env python

from selenium import webdriver

import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get("http://localhost:8000")

        self.assertIn('To-Do',self.browser.title)
        self.fail("finish the test!")

if __name__ == "__main__":
    unittest.main(warnings="ignore")

# browser = webdriver.Chrome()
#
# #伊迪斯听说有一个很酷的在线办事项应用
# #他去看了这个首页
#
# browser.get("http://localhost:8000")
#
# #她注意到网页标题的头部包含todo'这个词
#
# assert 'To-Do' in browser.title
#
# #应用邀请她输入一个待办事项
#
# #她在一个文本框中输入"buy peacock feathers"(购买孔雀羽毛)
# #伊迪斯的爱好是使用假蝇做鱼饵 钓鱼
# #
# #他按照回车键后，页面更新了
# #代办是想表格中显示了“1、buy peacock feathers”
#
#
# #页面有显示了一个文本框。可以输入其他的代办事项
#
# #她输入了“use peacock feathers to make a fly ”
#
# # 伊迪斯做事很有条理
#
# # 页面再次更新，他的清单中显示了两条待办事项
# #伊迪斯想知道这个网站是否会记住他的清单
# #他看到网站为他生成了一个唯一的url
# #而且页面中有一些文字解说这个功能
#
# #他访问那个url，发现他的待办事项列表还在
# #他很满意，去睡觉了
#
#
# browser.quit()