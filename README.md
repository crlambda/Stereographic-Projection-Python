# Stereographic-Projection-Python

keywords: Stereographic Projection, python, 物理冶金, 晶體缺陷


## 簡述

利用python的`matplotlib`及`tkinter`模組畫出stereographic projection

![100](https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fd2vlcm61l7u1fs.cloudfront.net%2Fmedia%252F639%252F6396459d-d57d-4ed1-9887-dde34db11a03%252FphpzwhKq3.png&f=1&nofb=1)

▲ **圖一、(100) stereographic projection。**

## 原理

### (一)找出落在軸面之向量

先用3個 for loop 將所有符合條件的向量暴力解出來，再用matplotlib模組將算出的向量呈現出來。



#### 繪製 (100) 投影圖

實際上的操作，我是將向量先放置在半徑為 1 圓心在圓點的球體表面，接著將投影點設為 (-1,0,0)，將投影點與球體上的向量連線，最終投影至 x = 1 平面上，繪製結果如圖六。

![100sp](https://scontent.ftpe7-3.fna.fbcdn.net/v/t1.15752-9/105964361_598601674395597_336815407516572358_n.png?_nc_cat=108&_nc_sid=b96e70&_nc_ohc=4MXc-7j1qzMAX9YKD61&_nc_ht=scontent.ftpe7-3.fna&oh=74a84f61ff6c4f1b9e52ee74a7ae04a8&oe=5F95A883)

▲ **(100) 投影圖繪製結果**

<br>

#### 繪製 (110) 投影

![110sp](https://scontent.ftpe7-1.fna.fbcdn.net/v/t1.15752-9/105328006_691133118102999_1382517231252798342_n.png?_nc_cat=110&_nc_sid=b96e70&_nc_ohc=34HOsVA-E3IAX85dkFV&_nc_ht=scontent.ftpe7-1.fna&oh=be48381fb4b3ed48f8fa31a2e037f77e&oe=5F95BA1F)

▲ **(110) 投影圖繪製結果**

<br>

#### 繪製 (111) 投影

先將向量伸縮至球體表面，使用矩陣：

[[ 2/3, -1/3, -1/3],
 [-1/3,  2/3, -1/3],
 [-1/3, -1/3,  2/3]]

將向量投影至[111]面上，最終將`Axes3D` 的屬性 view_init 設定為 `view_init(elev=45,azim=45)`，即x軸沿z軸順時針旋轉45°；固定原點將z軸往出紙面方向旋轉45°，繪製結果如圖。

![111sp](https://scontent.ftpe7-3.fna.fbcdn.net/v/t1.15752-9/83477996_1150650755292956_15575585439126339_n.png?_nc_cat=102&_nc_sid=b96e70&_nc_ohc=_JvjaUUtJ-oAX9sva5B&_nc_ht=scontent.ftpe7-3.fna&oh=89acb19ce928120493cdc2aba8d7d9ca&oe=5F979172)

▲ **(100) 投影圖繪製結果**

---

### 可旋轉球體投影

雖然和stereographic projection投影圖有差距，但利用球體投影，旋轉的座標軸移動清晰可見。為了方便使用者操作，引入 tkinter 模組，可以呈現與使用者互動的3d圖，座標圖上的文字方便使用者找到現在的位置。

---

![100ball](https://scontent.ftpe7-1.fna.fbcdn.net/v/t1.15752-9/106296387_296256185113570_4120106733186470162_n.png?_nc_cat=110&_nc_sid=b96e70&_nc_ohc=WPOgEJQyCewAX9d5ro4&_nc_ht=scontent.ftpe7-1.fna&oh=b09a7b94029fad16857d8e3b6bb4cfcb&oe=5F975640)

▲ **(100) 投影圖於球體**

![110ball](https://scontent.ftpe7-1.fna.fbcdn.net/v/t1.15752-9/106398188_274806526909701_8217067908496273162_n.png?_nc_cat=106&_nc_sid=b96e70&_nc_ohc=EQoouuZu7cEAX9zaqhd&_nc_ht=scontent.ftpe7-1.fna&oh=284cd80902a66e6304bf4bfe13fc2de3&oe=5F95337F)

▲ **(110) 投影圖於球體**

![111ball](https://scontent.ftpe7-1.fna.fbcdn.net/v/t1.15752-9/105947616_316367839368518_3239856020578297935_n.png?_nc_cat=100&_nc_sid=b96e70&_nc_ohc=fbFdKJVnC3IAX9FDC-A&_nc_ht=scontent.ftpe7-1.fna&oh=0abd30325e4e1aeeb672e7ccdad6da86&oe=5F981A4C)

▲ **(111) 投影圖於球體**

## Usage

1. install package `tkinter`
2. Download all the files and put them in the same folder
3. See Projections open `Projection1xx.ipynb` and run the code inside
4. See Sphere Projections open `Project_sphere_tkinter.py`
