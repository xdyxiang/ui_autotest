# viabtc_ui_autotest
> 项目技术栈：
* python3 
* selenium 
* pymsql
* 


UI自动化相关知识：

- 1.强制等待:sleep()

- 2.隐式等待:implicitly_wait():即在定位元素时，需要等待页面全部元素加载完成，才会执行下一个语句。如果超出了设置时间的则抛出异常。

    当页面某些js无法加载，但是想找的元素已经出来了，它还是会继续等待，直到页面加载完成（浏览器标签左上角圈圈不再转），才会执行下一句。某些情况下会影响脚本执行速度。

- 3.显示等待:WebDriverWait():---WebDriverWait与expected_conditions结合使用
    * from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.support.wait import WebDriverWait
        wait = WebDriverWait(driver,10,0.5)
        element =waite.until(EC.presence_of_element_located((By.ID,"kw"),message="")
        此处注意，如果省略message=“”，则By.ID外面是两层()

    * expected_conditions类提供的预期条件判断的方法
        方法	说明
        title_is	判断当前页面的 title 是否完全等于（==）预期字符串，返回布尔值
        title_contains	判断当前页面的 title 是否包含预期字符串，返回布尔值
        presence_of_element_located	判断某个元素是否被加到了 dom 树里，并不代表该元素一定可见
        visibility_of_element_located	判断元素是否可见（可见代表元素非隐藏，并且元素宽和高都不等于 0）
        visibility_of	同上一方法，只是上一方法参数为locator，这个方法参数是 定位后的元素
        presence_of_all_elements_located	判断是否至少有 1 个元素存在于 dom 树中。举例：如果页面上有 n 个元素的 class 都是’wp’，那么只要有 1 个元素存在，这个方法就返回 True
        text_to_be_present_in_element	判断某个元素中的 text 是否 包含 了预期的字符串
        text_to_be_present_in_element_value	判断某个元素中的 value 属性是否包含 了预期的字符串
        frame_to_be_available_and_switch_to_it	判断该 frame 是否可以 switch进去，如果可以的话，返回 True 并且 switch 进去，否则返回 False
        invisibility_of_element_located	判断某个元素中是否不存在于dom树或不可见
        element_to_be_clickable	判断某个元素中是否可见并且可点击
        staleness_of	等某个元素从 dom 树中移除，注意，这个方法也是返回 True或 False
        element_to_be_selected	判断某个元素是否被选中了,一般用在下拉列表
        element_selection_state_to_be	判断某个元素的选中状态是否符合预期
        element_located_selection_state_to_be	跟上面的方法作用一样，只是上面的方法传入定位到的 element，而这个方法传入 locator
        alert_is_present	判断页面上是否存在 alert
    
    * 封装：
        def find_elements(self, *locator):
            WebDriverWait(self.driver, 10).until(lambda the_driver: len(the_driver.find_elements(*locator)) > 0)




- 判断：
1.标题title
2.页面固定text
3.页面列表元素大于0
4.检查元素是否可见
5.走流程检查前后数据库数据
