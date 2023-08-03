from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
# ...
a1 = TouchAction()
a1.press(10, 20)
a1.move_to(10, 200)
a1.release()

a2 = TouchAction()
a2.press(10, 10)
a2.move_to(10, 100)
a2.release()

ma = MultiAction(driver)
ma.add(a1, a2)
ma.perform()

