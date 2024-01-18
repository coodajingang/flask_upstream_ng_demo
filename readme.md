# 功能 
使用flask实现应用demo，作为nginx的上游 ， 验证nginx的相关配置 

## 功能列表 
1. get /  ： 返回一段html 
2. get /echo-etag ： 返回一段html 带etag 和 last-modified 
3. get /echo-realip ： 返回一段html ，带realip 
4. get /echo-headers ： 返回一段html ，参数中带各种headers， 响应时设置这些headers 
5. post /echo-post ： 返回一段json ， 参数中带各种headers， 响应时设置这些headers 
6. head /echo-head ： 
7. option /echo-option ： 


# develop  
`python main.py` 

# prod 
`pip install gunicorn`
`gunicorn -w 4 -b 0.0.0.0:8801 your_app_module:app --log-level debug --timeout 60`
`gunicorn -w 1 -b 0.0.0.0:8801 main:app`