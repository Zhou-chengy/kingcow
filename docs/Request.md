  # Request
  Request是kingcow的一个类，您可以用它来发送网页请求，获得网页后使用解析方法对其解析
  ## 请求方法
  Request类的构造函数就是请求方法，您需要提供一些参数发送请求，可能会有些延迟。
  
  ### 参数
  
 url:必选参数，为请求网页的链接
 
 data:需要向网页发送的数据(注意：网页要求的类型为表单类型）
 
 header:请求头，网站用此验证你的身份
 
 code：默认为UTF-8，他会把data加密成此编码，再标准化
 
 method：如果有data,默认是POST，没有则为GET
 
 cafile、capath、cadefault：用于实现可信任的CA证书的HTTP请求。（不常用）
 
 context：实现SSL加密传输。（不常用）
 
 ip：代理IP，默认不启用（dict)
 
 ### 解析方法
 
 #### html_analysis
 
 ###### 参数
 lab：网页的标签
 
 attrs:默认不启用，网页所需的属性值
 
 code:默认UTF-8
 ###### 作用和好处
 
 可以获取网页数据，比使用正则表达式快。获取的网页数据用于统计、搜索等。
 
 #### html_tag
 ##### 参数
 tag:网页标签
 
 attrs:必选参数，网页属性（如href,src)
 
 ##### 作用
 可以用于提取链接，爬取图片
 
 #### json
 提取json
 
 
