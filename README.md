## Python Spider使用的一些经验
## 任务为：采集豆瓣影评。
1. 好评为：percent_type = h，中评为：percent_type = m，差评为：percent_type = l
2. statue = P表示为：看过，statue = F表示为：未看过
3. 具体的数据接口为：https://movie.douban.com/subject/20435622/comments?start=20&limit=20&sort=new_score&status=P&percent_type=l&comments_only=1
4. 可以使用Request.get进行拼接，对于采集后的json格式要进行清洗，json只认识双引号格式，单引号格式进行转化，使用格式化json工具进行在线校验：https://www.bejson.com/，
5. 总结：先观察json的格式，然后观察json中的Ture和Fault，有的话就替换为数字
#### 数据截图如下所示。
### ![数据截图](https://github.com/CarryChang/-/blob/master/%E8%B1%86%E7%93%A3%E5%BD%B1%E8%AF%84%E9%87%87%E9%9B%86/%E6%95%B0%E6%8D%AE%E6%88%AA%E5%9B%BE/%E6%95%B0%E6%8D%AE%E6%88%AA%E5%9B%BE.png)
