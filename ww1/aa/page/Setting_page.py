import os,sys
sys.path.append(os.getcwd())
import pytest
from selenium.webdriver.common.by import By
from ww1.aa.base.base_action import BaseAction
from ww1.aa.base.base_yml import yml_data_with_file

class Settings(BaseAction):
    search_button=By.ID,'com.android.settings:id/search'
    input_button=By.ID,'android:id/search_src_text'
    result=By.ID,'com.android.settings:id/title'
    def open_app_s(self):
        self.open_app('com.android.settings','.Settings')
    # 点击搜索按钮
    def click_ele(self):
        self.click(self.search_button)
    # 输入文字
    @pytest.mark.parametrize("data",['1','12'])
    def input(self,data):
        self.send_keys(self.input_button,data)
    # 判断
    def panduan(self):
        a=self.find_element(self.result)
        if a.text =='设置时间':
            assert 1
        else:
            assert 0