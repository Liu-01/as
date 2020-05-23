import os,sys
sys.path.append(os.getcwd())

from ww1.aa.page.Setting_page import Settings
from ww1.aa.base.driver import init_driver
import pytest
from ww1.aa.base.base_yml import yml_data_with_file


# 读取yml文件
def read_yml(filename,key):
    return yml_data_with_file(filename)[key]
class Test_settings():
    def setup(self):
        self.driver=init_driver()
        self.setting_page_driver=Settings(self.driver)

    @pytest.mark.parametrize("data",read_yml('settings','input'))
    def test_01(self,data):
        # 启动设置
        self.setting_page_driver.open_app_s()
        # 点击搜索按钮
        self.setting_page_driver.click_ele()
        # 输入文字
        self.setting_page_driver.input(data)
        # 判断
        self.setting_page_driver.panduan()

    def teardown(self):
        self.driver.quit()

