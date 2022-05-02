---
# Python：网络爬虫入门
这只是一个最最最基础版本的Python爬虫入门，代码是我两年前写的，最近两天没事翻出来再写(shui)一篇博客。就是爬取王者荣耀英雄的皮肤。然后备注也是写的十分的详细，所以就不做过多的解释，如果想提高自己Python水平的同学可以照着敲一遍。
<!-- more -->
## 获取加载文件

打开[王者荣耀官网](http://pvp.qq.com/web201605/herolist.shtml)。
然后随便点一个英雄的界面，然后按f12打开开发者调试工具。
![阿离](https://img-blog.csdnimg.cn/img_convert/bbca0585b3d22061eceacbb5fe0b27b2.png)
然后我们把这个花间舞的头像指向的地址复制出来，就是后面那个地址，然后把它粘贴在地址栏，就可以看到我们得到了一张花间舞的高清图片，我们要爬取的就是这张图片。

## 获取图片地址信息

我们一般会多打开几张图片，然后观察他们的共性。
![add](https://img-blog.csdnimg.cn/img_convert/b8fe80f44b27300abf1003be4c7eaf14.png)
![add](https://img-blog.csdnimg.cn/img_convert/216dee37490778f0634f5ce08f9f7c9a.png)

我们可以发现，就只有上面的141和bigskin后面的代码不一样，那我们就可以猜测414和199应该就是英雄的代号，2和3就是指第几张图片，这就好办了，那我们又怎么知道英雄的代码和皮肤的代号呢。
我们先返回到这个英雄界面，我们知道，网页要加载这些图片，肯定不是一开始就这样排好的，肯定有一个文件里面存了这些图片的信息，所以一般只需要更新那个文件就可以更新这个网页的内容了，我们先把那个文件找出来，一般这种文件都是json或者js为后缀的。

![text](https://img-blog.csdnimg.cn/img_convert/65ccfd3192ee3a122c33c118cb1c8696.png)

先按F12，然后刷新网页，就可以看到network下面加载出一堆的文件，然后把json一个个都找一遍。
![text](https://img-blog.csdnimg.cn/img_convert/9b7ebef411063c98a2ecfd37b830fc4e.png)

我们把它下载下来。
![text](https://img-blog.csdnimg.cn/img_convert/c99a01c31c06c4953099d6d6f87346f8.png)

右键，copy，第一个，然后复制链接地址，再粘贴到地址栏，就可以下载了。
![text](https://img-blog.csdnimg.cn/img_convert/81cdde74b82360762ce12eab4ce7fac2.png)

可以看到里面的东西都非常详细，第一个ename就是英雄的代码了，第二个是英雄的中文名字，第三个就是默认皮肤的意思，第四个不知道啥玩意，别理他，第五个，好像是英雄的属性，法师坦克射手之类的，最后一个就是皮肤的名字啦。

## 编写代码
现在我们既然可以得到文件的准确地址，那么只要能够组合出图片地址就可以直接下载下来了。下面直接写代码。因为是古老的代码了，而且有些不全，我就不贴代码了，直接给图片吧。
![text](https://img-blog.csdnimg.cn/img_convert/bf3790fbdf9fd6cc728d906a3de39cbd.png)
![text](https://img-blog.csdnimg.cn/img_convert/c2aed603ddc49a62bf13acfcdd3f3871.png)
然后就是我们关键的地方了，下载皮肤。
其实为了我们以后更加方便的下载，我这里是写了一个GUI界面。
![text](https://img-blog.csdnimg.cn/img_convert/62b8598a0674aee4d7923e59398dd9b5.png)
![text](https://img-blog.csdnimg.cn/img_convert/69f044e174a29d8f12fedc2eaf5ea562.png)
![text](https://img-blog.csdnimg.cn/img_convert/f5cfae0e1716702f9772253d3c651b7f.png)
然后新上架的皮肤不会及时更新到官网上面，但是可以组合出他们的图片地址，就暂时叫他们为隐藏皮肤，其实叫新皮肤会更合适。
![text](https://img-blog.csdnimg.cn/img_convert/4c21592e1f8dfd929043ed7ecf352591.png)

然后最后我这里是用pyinstaller打包成exe文件了，如果你用的win10 x64的系统的话，可以直接运行，我也把源码贴上去。
下载地址：[百度云](https://pan.baidu.com/s/1LimeHAvQakr9id4jBLxzqQ) 提取码：nos3

非常非常简单的爬虫，可以用作Python入门级的教程了。
