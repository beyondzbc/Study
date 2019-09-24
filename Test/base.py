'''
python面向对象，解释型语言
标识符：字母、数字、下划线，不能以数字开头
数据类型：数值、字符串、列表、元组（不可改）、集合（不重复）、字典
控制流：
    顺序结构
    条件分支结构  if
    循环结构  while、for
    中断结构  break（中断一个程序） continue（中断一次运行）
函数：本质是封装
模块：多个函数组合在一起 （系统自带模块在lib文件夹下面）
'''

for i in range(1, 10):
    for j in range(1, i + 1):
        print(str(i) + '*' + str(j) + '=' + str(i * j), end=' ')
    print('')

print('-------------------------------------------------------------')

for i in range(9, 0, -1):
    for j in range(i, 0, -1):
        print('%d*%d=%2d' %(i,j,i*j), end=' ')
    print()

print('-------------------------------------------------------------')

n=9
for i in range(n,0,-1):
    for j in range(1,n+1):
        print(str(j) + '*' + str(i) + '=' + str(j * i), end=' ')
        # m-=1
    n-=1
    print()

print('-------------------------------------------------------------')

for i in range(0,11):
    for j in range(0,i+1):
        print(str(i) + '+' + str(j) + '=' + str(i+j), end=' ')
    print()

i=0
j=1
while j<200:
    print(j)
    i,j=j,i+j


def abc():
    for i in range(0,200):
        if i <=1:
            print(i)
    else:
            print(abc(i-1))

文件读取
f=open('D:/pydata/file.txt','w')
contents='我是文件内容'
f.write(contents)
f.write('\n这是另外的内容')
f.close()

f=open('D:/pydata/file.txt','r')
# data=f.read()
# print(data)
data1=f.readlines()
print(data1)


异常处理
try:
    print('hello')
    prints('hi')
except Exception as er:
    print(er)
    print('error')

'''
数据分析：已知、提取、统计、数据量小
数据挖掘：未知、探索、规律、数据量大
numpy +（mkl）  （下载安装） 基础、数组支持
pandas    核心 数据探索、分析
matplotlib   可视化
scipy   （下载安装）    数值计算   高等数据处理、矩阵
statsmodels   统计分析
Gensim    文本挖掘
sklearn、keras    机器学习、深度学习
其余都可通过网络安装

numpy
创建一维数组：
numpy.array([元素1,元素2,元素3,...,元素n])
创建二维数组：
numpy.array([[元素1,元素2,元素3,...,元素n],[元素1,元素2,元素3,...,元素n],[元素1,元素2,元素3,...,元素n],...[元素1,元素2,元素3,...,元素n]])
排序sort()
极值max()、min()
切片  数组[起始下标：最终下标+1]


pandas
Series      pd.Series([1,2,3,4,...])
            pd.Series([13,5,7,2],index=['one','two','three','four')
DataFrame   pd.DataFrame([[2,3,4,5],[4,5,6,7],[4,3,2,8],[7,8,9,5]])
            pd.DataFrame([[2,3,4,5],[4,5,6,7],[4,3,2,8],[7,8,9,5]],columns=['one','two','three','four'])
            pd.DataFrame({
            'one':2,
            'two':[3,4,5],
            'three':list(str(232))
            })
head()  头部数据，默认前五行
tail()  尾部数据，默认后五行
describe()  统计数据基本情况
info()   数据信息
T   转置


data=pd.reac_csv()
    sort_values(by='')排序
data=pd.read_excel()

连接mysql数据库
import pymysql
conn=pymysql.connect(host='127.0.0.1',user='root',passwd='root,db='test')
sql="select * from xxx "
data=pd.read_sql(sql,conn)

直接从网页中加载对应的table表格中的数据，需要先安装html5lib库与BeautifulSoup库
data=pd.read_html('本地网页')
data=pd.read_html('网页链接')

data=read_table('文件路径')

可视化
直方图hist
散点图/折线图plot(x,y,'o'(默认为折线图))

线条样式：
-直线
--虚线
-.
：细小虚线

点的样式：
s  方形
h H  六角形
*  星形
+  加号
x  x形
d D  菱形
p  五角形

plt.title('标题')
plt.xlable('横轴')
plt.ylable('纵轴')
plt.xlim(0,20)
plt.ylim(5,30)  范围设置
plt.subplot(2,2,3)  (行，列，当前区域)
data=np.random.normal(均数,西格玛,个数,)  随机正态分布
data.values[][]   读取第几行第几列数据

'''

'''
数据探索
核心：
1、质量分析
2、特征分析（分布、对比、周期性、相关性、常见统计量）
数据清洗：
1、缺失值处理（通过describe与len直接发现，通过0数据发现）
2、异常值处理（通过散点图发现）
一般遇到缺失值，处理方式为（删除、插补、不处理）
    插补的主要方式有：均值插补、中位数、众数、固定值、最近数据、回归插补、拉格朗日插补、牛顿插补、分段插补等
    异常值一般视为缺失值、删除、修补、不处理等


数据集成：
把不同来源的数据放在一起，但是一定要做好实体识别与冗余属性识别，避免数据整合错误及数据重复
技巧：
1、观察数据，发现其中关系，详细查看是否有同名不同意，同意不同名的情况
2、进行数据读取与整合
3、去除重复数据

数据变换：
简单变换
    目的是将数据转换为更方便分析的数据
    简单变换通常使用函数变换的方式进行，常见的函数包括：开方、平方、对数等
数据规范化
    离差标准化（最小-最大标准化）  消除量纲（单位）影响以及变异大小因素的影响  x1=(x-min)/(max-min)
    标准差标准化（零-均值标准化）  消除单位影响以及变量自身变异影响   x1=（x-平均数)/标准差   平均数为0，标准差为1
    小数定标规范化  消除单位影响  x1=x/10**(k)   k=log10(x的绝对值的最大值)
连续型数据离散化
    等宽离散化  pd.cut(data,k(等分为几份），labels=["小","中","大"])
        非等宽离散化  pd.cut(data,[3,6,10,19]，labels=["多","适中","少"])
    等频率离散化（相同数量的数据放到每个区间内）
    一维聚类离散化 
属性构造
属性规约（与数值规约一样都是为了精简数据）
    主成分分析PCA：主要用作数据降维
    from sklearn.decomposition import PCA
数值规约

文本挖掘  中文jieba库
文本相似度分析  tf-idf   封装在Gensim
    稀疏向量
    相似度计算的步骤：
        1、读取文档
        2、对要计算的文档进行分词
        3、对文档进行整理成指定格式，方便后续进行计算
        4、计算出词语的频率
        5[可选]、对频率低的词语进行过滤
        6、通过语料库建立词典
        7、加载要对比的文档
        8、将要对比的文档通过doc2bow转化为稀疏向量
        9、对稀疏向量进行进一步处理，得到新语料库
        10、将新语料库通过tf-idf model进行处理，得到tf-idf
        11、通过token2id得到特征数
        12、稀疏矩阵相似度，从而建立索引
        13、得到最终相似度结果
        
        
python数据建模
模型的建立一般依赖于算法，常见的有：分类、聚类、关联、回归

数据分类实现过程：
    1、首先明确需求并对数据进行观察
    2、其次，确定算法
    3、确定步骤
    4、编程实现
    
常见的分类算法：
        1、KNN
        2、贝克斯方法
        3、决策树
        4、人工神经网络
        5、支持向量机（SVM）
        
KNN
算法实现步骤：
    1、处理数据
    2、数据向量化
    3、计算欧几里得距离
    4、根据距离进行分类
    #tile（）扩展数据
'''
