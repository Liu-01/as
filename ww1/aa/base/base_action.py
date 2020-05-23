import os,sys
sys.path.append(os.getcwd())
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
class BaseAction:
    # 引用driver对象
    def __init__(self, driver):
        self.driver = driver
        # 先借用一下init_driver方便编写函数
        # self.driver = init_driver()
        # 查找元素
    def find_element(self, log):
        # ele = self.driver.find_element(log[0],log[1])
        # return ele
        by = log[0]
        value = log[1]
        # if by == By.XPATH:
        #     value = self.find_xpath_result(value)
        return WebDriverWait(self.driver, 10, 0.5).until(lambda x:x.find_element(by, value))

    def find_elements(self, log):
        by = log[0]
        value = log[1]
        # if by == By.XPATH:
        #     value=self.find_xpath_result(value)
        return WebDriverWait(self.driver, 10, 0.5).until(lambda x:x.find_elements(by, value))

    def find_xpath(self, log):
        key1 = 0
        key2 = 1
        key3 = 2
        result = ''
        list = log.split(',')
        if len(list) == 2:
            result = 'contains(@' + list[key1] + ',"' + list[key2] + '")' + 'and' + ' '
        elif len(list) == 3:
            if list[2] == '1':
                result = list[key1] + '="' + list[key2] + '"' + 'and' + ' '
            elif list[2] == '0':
                result = 'contains(@' + list[key1] + ',"' + list[key2] + '")' + 'and' + ' '
        return result
    # xpath快捷获取
    def find_xpath_result(self, log):
        result = ''
        start = '//*['
        end = ']'
        if isinstance(log, str):
            result = self.find_xpath(log)
        else:
            for i in log:
                result += self.find_xpath(i)
        result = result.rstrip("and ")

        end_result = start + result + end
        return end_result
    # 点击元素
    def click(self, log):
        self.find_element(log).click()
    def send_keys(self, log, data):
        self.find_element(log).send_keys(data)
    # 打开app
    def open_app(self, package, activity):
        self.driver.start_activity(package, activity)
    # 获取页面的大小
    def get_size(self):
        z = self.driver.get_window_size()
        return z
    # 滑动屏幕
    def swip_screen(self):
        self.driver.swipe(start_x=(self.get_size().get('width'))*0.5,start_y=(self.get_size().get('height'))*0.9\
                          ,end_x=(self.get_size().get('width'))*0.5,end_y=(self.get_size().get('height'))*0.2,duration=1000)
    # 返回键
    def back_keyevent(self):
        self.driver.keyevent(4)
    # 菜单键
    def menu_keyevent(self):
        self.driver.keyevent(82)
    # 关闭虚拟机
    def quit(self):
        self.driver.quit()
    # 获取页面元素
    def get_window_source(self):
        return self.driver.page_source
    # 获取元素坐标
    def ele_location(self,log):
       return self.find_element(log).location
    # 按住屏幕
    def press_srceen(self,log):
        TouchAction(self.driver).press(self.find_element(log)).perform()
        # 点击屏幕
    def tap_screen(self,log):
        TouchAction(self.driver).tap(self.find_element(log)).perform()
        # 长按屏幕
    def long_press(self,log,time):
        TouchAction(self.driver).long_press((self.find_element(log)),duration=time).perform()
    # def move_to(self,value,log):
    #     TouchAction(self.driver).press(self.find_element(value)).wait(1000).move_to(self.find_element(log)).perform()
    # 移动
    def drag_and_down(self,log,log2):
        self.driver.drag_and_drop(self.find_element(log),self.find_element(log2))
    # 截图
    def get_screenshot_as_file(self):
        self.driver.get_screenshot_as_file('../report/pic.png')
    # 下拉通知栏
    def open_notifications(self):
        self.driver.open_notifications()
    # 查看网络
    def network_connection(self):
        return self.driver.network_connection


# a=BaseAction()
# a.open_app('com.android.settings','.Settings')
# button =By.XPATH,'//*[contains(@text,"应用")]'
# a.click(button)
# button2=By.CLASS_NAME,"android.widget.TextView"

