#websocket

简介
  这个项目是写的一个简单的语音答复功能,采用的是flask框架,实现的一个小功能,主要的实现分为以下三个模块
    1.websocket 
    2.语音合成,语音处理,,自然语言的识别 
    3.智能机器人的简单对答
    4.调用浏览器的麦克风功能
    
    
   
1.websocket 
  采用的是flask 框架,用WSGIServer 替换掉原生的app.run,来引入websocket,前端实例化websockt对象,连接后端,来实线相互之间的数据通信
  
  
2.语音识别
  采用的百度提供的接口  ai.baidu.com 里面的功能很强大,只是玩了一个很简单的操作,如果有需要,可以去看看
  
  
3.智能机器人
  这里只是我自己闲来无事,调用接口逗自己玩呢,所以采用的是免费的里面,我觉得最好的的一个 tuling123.com(图灵机器人),里面的很多功能也是收费的,具体怎么玩
  就是自己来动手了
  
  
 4.浏览器的麦克风
    这个倒是在写代码的时候卡住了,没什么头绪,最后也是自己查阅资料,和寻求帮助的情况下完成的,前端的页面垃圾的不行,好在实现了功能,倒也还是个不错的选择
  
  
pip3 install pyopenssl
环境 python3 + flask 和响应的包即可

clone 此项目, 然后在 myapp.py run起来即可.
