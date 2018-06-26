<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'DejaVu Sans Mono'; font-size:10pt; font-weight:400; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 10:22:32) [MSC v.1900 64 bit (AMD64)]</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Type &quot;copyright&quot;, &quot;credits&quot; or &quot;license&quot; for more information.</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">IPython 6.2.1 -- An enhanced Interactive Python.</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">1</span><span style=" color:#000080;">]:</span> import numpy as np</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> import matplotlib.pyplot as plt</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> import pandas as pd</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">2</span><span style=" color:#000080;">]:</span> dataset = pd.read_csv('Position_Salaries.csv')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">3</span><span style=" color:#000080;">]:</span> X = dataset.iloc[:, 1:2].values</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> y = dataset.iloc[:, 2].values</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">4</span><span style=" color:#000080;">]:</span> from sklearn.linear_model import LinearRegression</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> lin_reg = LinearRegression()</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> lin_reg.fit(X, y)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#8b0000;">Out[</span><span style=" font-weight:600; color:#8b0000;">4</span><span style=" color:#8b0000;">]:</span> LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">5</span><span style=" color:#000080;">]:</span> from sklearn.preprocessing import PolynomialFeatures</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> poly_reg = PolynomialFeatures(degree = 4)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> X_poly = poly_reg.fit_transform(X)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">6</span><span style=" color:#000080;">]:</span> lin_reg2 = LinearRegression()</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> lin_reg2.fit(X_poly, y)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#8b0000;">Out[</span><span style=" font-weight:600; color:#8b0000;">6</span><span style=" color:#8b0000;">]:</span> LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">7</span><span style=" color:#000080;">]:</span> from sklearn.preprocessing import PolynomialFeatures</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> poly_reg = PolynomialFeatures(degree = 2)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> X_poly = poly_reg.fit_transform(X)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">8</span><span style=" color:#000080;">]:</span> lin_reg2 = LinearRegression()</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> lin_reg2.fit(X_poly, y)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#8b0000;">Out[</span><span style=" font-weight:600; color:#8b0000;">8</span><span style=" color:#8b0000;">]:</span> LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">9</span><span style=" color:#000080;">]:</span> plt.scatter(X, y, colour = 'red')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> plt.plot(X, lin_reg.predict(X), colour = 'blue')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> plt.title('Truth or Bluff(Linear Regression)')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> plt.xlabel('Position level')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> plt.ylabel('Salary')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> plt,show()</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Traceback <span style=" color:#4682b4;">(most recent call last)</span>:</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;&lt;ipython-input-9-8280f873d1cd&gt;&quot;</span>, line <span style=" color:#00ff00;">1</span>, in <span style=" color:#ff00ff;">&lt;module&gt;</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    plt.scatter(X, y, colour = 'red')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;C:\Users\admin\Anaconda3\lib\site-packages\matplotlib\pyplot.py&quot;</span>, line <span style=" color:#00ff00;">3378</span>, in <span style=" color:#ff00ff;">scatter</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    edgecolors=edgecolors, data=data, **kwargs)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;C:\Users\admin\Anaconda3\lib\site-packages\matplotlib\__init__.py&quot;</span>, line <span style=" color:#00ff00;">1717</span>, in <span style=" color:#ff00ff;">inner</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    return func(ax, *args, **kwargs)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;C:\Users\admin\Anaconda3\lib\site-packages\matplotlib\axes\_axes.py&quot;</span>, line <span style=" color:#00ff00;">4035</span>, in <span style=" color:#ff00ff;">scatter</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    collection.update(kwargs)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;C:\Users\admin\Anaconda3\lib\site-packages\matplotlib\artist.py&quot;</span>, line <span style=" color:#00ff00;">902</span>, in <span style=" color:#ff00ff;">update</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    for k, v in props.items()]</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;C:\Users\admin\Anaconda3\lib\site-packages\matplotlib\artist.py&quot;</span>, line <span style=" color:#00ff00;">902</span>, in <span style=" color:#ff00ff;">&lt;listcomp&gt;</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    for k, v in props.items()]</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#4682b4;">  File </span><span style=" color:#006400;">&quot;C:\Users\admin\Anaconda3\lib\site-packages\matplotlib\artist.py&quot;</span><span style=" color:#4682b4;">, line </span><span style=" color:#006400;">895</span><span style=" color:#4682b4;">, in </span><span style=" color:#9400d3;">_update_property</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#8b0000;">    raise AttributeError('Unknown property %s' % k)</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#8b0000;">AttributeError:</span> Unknown property colour</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="data:image/png;base64,
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
4ZxzZ86ccevXr3fr1q1zf/3rX8swafHlsxdDQ0NuzZo17quvvnLOOff555+X
Y9Siy2cvfv3rX7s333zTOefcsWPH3A033FCGSYvvwIED7m9/+5traGiY8/wf
/vAHd99997nJyUl38OBB9/Of/zyvxy3qK3w+lmFaPnvR3NysJUuWSJKampqU
zWbLMWrR5bMXkrR9+3Zt27ZNV199dRmmLI189mLXrl1qb2+f+s23qqqqcoxa
dPnsRSAQ0JkzZyRJp0+fnvWeoMvFnXfe+b3vZUomk9q0aZMCgYCampr09ddf
69SpU76PW9Tgz/WxDLlc7pJrvvuxDJebfPbiu7q7u3X//feXYrSSy2cvjh49
qpGRET344IOlHq+k8tmLoaEhDQ0N6Y477lBTU5P6+/tLPWZJ5LMXO3bs0O7d
uxUMBvXAAw9o586dpR7zB2G+Pfkf349WKMRcr9QX+rEMP3bz+Tl3796tVCql
AwcOFHussvDbi8nJSW3dulXvvfdeCacqj3z+Xly8eFGZTEb79+9XNpvV+vXr
NTg4qGuuuaZUY5ZEPnuRSCS0efNm/eY3v9HBgwf15JNPanBwUFdcYev3Txba
zaLuEh/LMC2fvZCkffv26eWXX1Zvb6+uuuqqUo5YMn57cfbsWQ0ODuruu+/W
jTfeqEOHDikajV6WN27z/Tfy0EMP6corr9TKlStVW1urTCZT6lGLLp+96O7u
VmtrqyTptttu07lz5zQ2NlbSOX8I8u3JLItxg+FSLly44FauXOn+/e9/T92E
GRwcnLGmq6trxk3bRx99tJgjlU0+e3HkyBEXCoXc0NBQmaYsjXz24rvuuuuu
y/ambT570dfX5zZt2uScc250dNQFg0E3NjZWjnGLKp+9uO+++9y7777rnHMu
nU67FStWuMnJyTJMW3zDw8OXvGn70Ucfzbhp29jYmNdjFjX4zv33bvLNN9/s
QqGQe+mll5xzzm3fvt0lk0nnnHPffvut27hxo7vppptcY2Oj++yzz4o9Utn4
7cWGDRtcVVWVW716tVu9erX7xS9+Uc5xi8pvL77rcg6+c/57MTk56bZu3erq
6urcqlWrXCKRKOe4ReW3F8eOHXO33367i0QibvXq1e6Pf/xjOcctmra2NvfT
n/7UVVRUuOuvv96988477q233nJvvfWWc+6/fyeeffZZFwqF3KpVq/L+98FH
KwCAEbbudACAYQQfAIwg+ABgBMEHACMIPgAYQfABwAiCDwBG/D9DsD9sUGWV
jAAAAABJRU5ErkJggg==
" /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">10</span><span style=" color:#000080;">]:</span> </p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">10</span><span style=" color:#000080;">]:</span> plt.scatter(X, y, colour = 'red')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.plot(X, lin_reg.predict(X), colour = 'blue')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.title('Truth or Bluff(Linear Regression)')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.xlabel('Position level')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.ylabel('Salary')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.show()</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Traceback <span style=" color:#4682b4;">(most recent call last)</span>:</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;&lt;ipython-input-10-fb8bba579e52&gt;&quot;</span>, line <span style=" color:#00ff00;">1</span>, in <span style=" color:#ff00ff;">&lt;module&gt;</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    plt.scatter(X, y, colour = 'red')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;C:\Users\admin\Anaconda3\lib\site-packages\matplotlib\pyplot.py&quot;</span>, line <span style=" color:#00ff00;">3378</span>, in <span style=" color:#ff00ff;">scatter</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    edgecolors=edgecolors, data=data, **kwargs)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;C:\Users\admin\Anaconda3\lib\site-packages\matplotlib\__init__.py&quot;</span>, line <span style=" color:#00ff00;">1717</span>, in <span style=" color:#ff00ff;">inner</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    return func(ax, *args, **kwargs)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;C:\Users\admin\Anaconda3\lib\site-packages\matplotlib\axes\_axes.py&quot;</span>, line <span style=" color:#00ff00;">4035</span>, in <span style=" color:#ff00ff;">scatter</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    collection.update(kwargs)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;C:\Users\admin\Anaconda3\lib\site-packages\matplotlib\artist.py&quot;</span>, line <span style=" color:#00ff00;">902</span>, in <span style=" color:#ff00ff;">update</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    for k, v in props.items()]</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;C:\Users\admin\Anaconda3\lib\site-packages\matplotlib\artist.py&quot;</span>, line <span style=" color:#00ff00;">902</span>, in <span style=" color:#ff00ff;">&lt;listcomp&gt;</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    for k, v in props.items()]</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#4682b4;">  File </span><span style=" color:#006400;">&quot;C:\Users\admin\Anaconda3\lib\site-packages\matplotlib\artist.py&quot;</span><span style=" color:#4682b4;">, line </span><span style=" color:#006400;">895</span><span style=" color:#4682b4;">, in </span><span style=" color:#9400d3;">_update_property</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#8b0000;">    raise AttributeError('Unknown property %s' % k)</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#8b0000;">AttributeError:</span> Unknown property colour</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="data:image/png;base64,
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
4ZxzZ86ccevXr3fr1q1zf/3rX8swafHlsxdDQ0NuzZo17quvvnLOOff555+X
Y9Siy2cvfv3rX7s333zTOefcsWPH3A033FCGSYvvwIED7m9/+5traGiY8/wf
/vAHd99997nJyUl38OBB9/Of/zyvxy3qK3w+lmFaPnvR3NysJUuWSJKampqU
zWbLMWrR5bMXkrR9+3Zt27ZNV199dRmmLI189mLXrl1qb2+f+s23qqqqcoxa
dPnsRSAQ0JkzZyRJp0+fnvWeoMvFnXfe+b3vZUomk9q0aZMCgYCampr09ddf
69SpU76PW9Tgz/WxDLlc7pJrvvuxDJebfPbiu7q7u3X//feXYrSSy2cvjh49
qpGRET344IOlHq+k8tmLoaEhDQ0N6Y477lBTU5P6+/tLPWZJ5LMXO3bs0O7d
uxUMBvXAAw9o586dpR7zB2G+Pfkf349WKMRcr9QX+rEMP3bz+Tl3796tVCql
AwcOFHussvDbi8nJSW3dulXvvfdeCacqj3z+Xly8eFGZTEb79+9XNpvV+vXr
NTg4qGuuuaZUY5ZEPnuRSCS0efNm/eY3v9HBgwf15JNPanBwUFdcYev3Txba
zaLuEh/LMC2fvZCkffv26eWXX1Zvb6+uuuqqUo5YMn57cfbsWQ0ODuruu+/W
jTfeqEOHDikajV6WN27z/Tfy0EMP6corr9TKlStVW1urTCZT6lGLLp+96O7u
VmtrqyTptttu07lz5zQ2NlbSOX8I8u3JLItxg+FSLly44FauXOn+/e9/T92E
GRwcnLGmq6trxk3bRx99tJgjlU0+e3HkyBEXCoXc0NBQmaYsjXz24rvuuuuu
y/ambT570dfX5zZt2uScc250dNQFg0E3NjZWjnGLKp+9uO+++9y7777rnHMu
nU67FStWuMnJyTJMW3zDw8OXvGn70Ucfzbhp29jYmNdjFjX4zv33bvLNN9/s
QqGQe+mll5xzzm3fvt0lk0nnnHPffvut27hxo7vppptcY2Oj++yzz4o9Utn4
7cWGDRtcVVWVW716tVu9erX7xS9+Uc5xi8pvL77rcg6+c/57MTk56bZu3erq
6urcqlWrXCKRKOe4ReW3F8eOHXO33367i0QibvXq1e6Pf/xjOcctmra2NvfT
n/7UVVRUuOuvv96988477q233nJvvfWWc+6/fyeeffZZFwqF3KpVq/L+98FH
KwCAEbbudACAYQQfAIwg+ABgBMEHACMIPgAYQfABwAiCDwBG/D9DsD9sUGWV
jAAAAABJRU5ErkJggg==
" /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">11</span><span style=" color:#000080;">]:</span> </p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">11</span><span style=" color:#000080;">]:</span> plt.scatter(X, y, color = 'red')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.plot(X, lin_reg.predict(X), color = 'blue')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.title('Truth or Bluff (Linear Regression)')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.xlabel('Position level')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.ylabel('Salary')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.show()</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="data:image/png;base64,
iVBORw0KGgoAAAANSUhEUgAAAaEAAAEWCAYAAADPZygPAAAACXBIWXMAAAsS
AAALEgHS3X78AAAAO3pUWHRTb2Z0d2FyZQAACJnLTSwpyMkvyclMUihLLSrO
zM9TMNIz1DPSUcgoKSmw0tfPhSvQyy9K1wcApwMQ8Tj1nCgAACAASURBVHic
7d15XFXV/v/xFwKaM5qoIIIiaIRTjo1aGGql+E1JJfylqZdSy4abZdlt7sq1
byM2kcPF0rTrN6XCMbWbN0fUummmpKAylITghJjA+v2x8ygKCApshvfz8eBh
LM7Za51zuefN2nvt9XEyxhhERERsUMvuAYiISM2lEBIREdsohERExDYKIRER
sY1CSEREbKMQEhER2yiEpFL55ZdfcHJysnsYDl9//TVt2rQp8eNnzpxJ8+bN
adCgAUePHmX9+vX4+fnRoEEDvvrqq0KfM2XKFGbOnHnJY48fP56///3vJR6L
FO3ll1/mwQcfvOLjbN++nVtuuaUMRlSDGZESql+/vuPLycnJXHXVVY7vP/nk
k8s6ZqtWrcy6desc3yckJJiK/LWcNm2acXFxcbyOgIAAs2TJEsfPV69ebXx8
fEp0rFOnTpk6deqYnTt3Otr69OljZs6cWeRz0tLSTKtWrcypU6dK3Z+dWrVq
5fjfv0WLFmbs2LHmxIkTdg/LFsHBwWbZsmV2D6PK0kxISuzEiROOL29vb778
8kvH9+Hh4Rc9Pjc314ZRFq2o8YSHhztex//+7/8SFhbG77//Xurj//rrr5w+
fZrAwEBH24EDBwp8f6G5c+cyePBgrrrqqlL3VxHy8/PJz88v9GfLly/nxIkT
bN++nc2bNzNjxoxyGUNeXl65HLeshIeH8+GHH9o9jCpLISRl5tlnn2XEiBGE
hYXRsGFDPvnkE0aNGsULL7zgeMz5p7fCwsJITU3ljjvuoEGDBrzxxhuOx82b
Nw8vLy/c3d2JjIwsss+srCxGjRqFu7s7bdq0Yfr06Zg/NwGZNWsWffr0YfLk
yTRt2pRXXnnlkq/hzjvvpG7duuzfv/+in+Xm5uLk5ERSUpKj7ezr2717tyNs
GjRoQP/+/WnTpg0HDx50vL7CPkyXL19O3759Lzmu8/uCc+/jjBkzcHd3x9PT
k3nz5jkem5OTw+OPP07r1q1p0aIFEydOJCcnB4CMjAzuvPNO3N3dadKkCYMH
DyYlJcXx3Jtvvpm//e1v3HDDDdSvX5+DBw8WOy5PT0/69+/P999/X6L+AaZP
n07Lli1p1aoVH330UYH3ddSoUUyaNImBAwdSv3591q9fX+zxDh8+zJ133omb
mxtNmzalT58+jn7+/ve/4+npSaNGjbjmmmv45ptvAOt3dcyYMY7HLV26lMDA
QNzc3AgKCmLPnj2On3l5efHGG2/QqVMnGjduTFhYGKdPn3b8/NZbb2X16tWc
OXOm2PdJCqcQkjK1ZMkS7r33Xo4ePcqIESOKfeynn36Kp6en4y/qxx9/3PGz
DRs28Msvv7By5Uqef/55EhISCj3GxIkTyc7OZv/+/axdu5bZs2cX+DDesGED
AQEBpKen89RTTxU7HmMMX3zxBcYYrrnmmlK8aggICOCHH34ArBnjqlWrSEpK
KvD6nJ2dL3rejz/+SIcOHUrV11nJycmcOnWK1NRUPvjgAyZMmMCxY8cAeOKJ
J0hMTOS///0vCQkJJCUl8eqrrwLW7OYvf/kLBw8e5MCBA7i6uvLII48UOPbH
H3/MnDlzOHbsGF5eXsWO49ChQ6xYsQI/Pz9HW3H9f/XVV0RFRbFu3Tr27t3L
2rVrLzrmggULeP755zl+/Dg33HBDscd77bXX8PX1JT09nV9//ZWXX34ZgF27
dvHhhx+yfft2jh07xvLly/H29r6or927dzNq1CiioqJIT0/n9ttvZ/DgwQVC
5bPPPmP16tXs37+fbdu28fHHHzt+5uPjgzGmyN9RKZ5CSMrUzTffzODBg6lV
qxZ169a97OO88MILXHXVVXTr1o3AwEDHB/z5zpw5w2effUZkZCQNGzbE19eX
xx57rMAHhLe3NxMmTMDZ2bnI8SxYsAA3Nzfq16/P3XffzbPPPkujRo0ue+yl
cfToURo2bHhZz73qqqt49tlncXV1JSQkhDp16rB3717y8/OZNWsWb731Fk2a
NKFRo0Y8/fTTLFy4EAB3d3fuvvtu6tatS6NGjXjmmWf497//XeDYY8eOJSAg
AFdXV1xcXArtf9CgQTRs2BBvb2+8vLx47rnnAC7Z/2effca4ceMICAigfv36
PP/88xcd++677+aGG26gVq1auLq6Fns8V1dXUlNTOXjwILVr13bMLF1cXMjJ
yWHXrl3k5ubStm1bfH19L+pr4cKFhISEEBQUhKurK1OnTuXYsWNs3rzZ8ZhH
H32Uli1bcvXVVzNo0KACsz6Ahg0bkpWVVaL/3aQghZCUqdatW5fJcVq2bOn4
73r16nHixImLHnP48GHy8vLw8fFxtPn4+BQ4tVSS8dx7771kZWWRnZ1NQkIC
s2bNYvbs2Vf4CkrGzc2N48ePX9ZzmzVrVmB2dfZ9OnttqkuXLri5ueHm5sag
QYM4fPgwACdPnmT8+PF4e3vTqFEjgoKCLroGVpL37auvvuL48eOsWbOGXbt2
ceTIEYBL9p+amlrg+IX1dX7bpY43depUfHx86NevH+3ateO1114DoEOHDrz+
+us899xzNG/enLCwMH799deL+kpNTS3wO1SrVi28vLwK/B5d6vfx+PHjuLm5
XfI9k4sphKRMXbi8un79+mRnZzu+v/BD4EqWYzdv3hxnZ2cOHDjgaDt48CCt
WrW67OP7+voycOBAvvzyy4t+5uLiQp06dYp9PaXVuXNn9u7de0XHuFCLFi2o
Xbs2e/bsISsri6ysLI4ePcrRo0cBmDFjBomJiWzZsoVjx44VejqsNO9bUFAQ
o0aNYsqUKSXq38PDg+TkZMfzDx06VGz/lzpeo0aNePPNN0lKSmLp0qX84x//
cMzsRo0axXfffUdiYiJ5eXk8/fTTF/Xl6elZ4HcoPz+f5OTkAr9HxTn7XH9/
/xI9XgpSCEm56tq1K3FxcWRmZpKWlsY777xT4OctWrQodBFASbi6uhIaGsoz
zzzDiRMnSExM5M0332TUqFGXPd5Dhw6xcuXKIle0denShfnz55OXl0dcXBz/
+c9/LrsvsBZCXHgqzBhDTk5OgS9Tioorzs7OjB8/nkcffZT09HSMMSQnJ7Nq
1SrA+qu9Xr16NGnShIyMDF566aUreg0Ajz32GMuWLWPnzp2X7H/48OHMnj2b
PXv2kJ2d7biGc7mv58svv2Tfvn0YY2jcuDHOzs44Ozuze/du1q1bx+nTp6lb
ty5169Yt9Lrc8OHD+eKLL/jmm284c+YMr732Gg0bNqR3794leu3//ve/uf32
23F1dS3luyagEJJyNmbMGAICAvDx8WHgwIGMHDmywM+feeYZnn/+edzc3Hjr
rbdKffz33nuP2rVr07ZtW/r27cvo0aO57777SnWM+fPn06BBAxo0aEDv3r25
9dZbefbZZwt97DvvvMOSJUtwc3PjX//6FyEhIaUe8/lGjx7Nl19+WWC11cGD
Bx0fmme/zv9LvSRef/11fHx86NWrF40bN6Z///6OC+ePP/44R48e5eqrr+bG
G2/kjjvuuKLXANbpqvDwcEegFNf/4MGDmTBhAn369MHf35+bbroJgDp16lzW
69mzZw9BQUE0aNCAm266iUceeYSbb76Z06dP8+STT9KsWTNatmxJZmZmoSsk
AwMDiYmJYcKECbi7u7NixQq++OKLEofK/Pnzy+TG15rKyZTmTywRKXNPPvkk
3t7ePPTQQ3YPxRY//vgj3bp14/Tp09SqVbX+Lt6xYwcPP/zwFc+IazKFkIhU
uCVLlnDXXXdx/Phx7rvvPurWrcvixYvtHpbYoGr92SEi1cK7775Ls2bN8Pf3
56qrruLdd9+1e0hiE82ERETENpoJiYiIbQq/FVocmjVrVqqt/EVEBJKSkkq0
EbBC6BLatGlDfHy83cMQEalSevToUaLH6XSciIjYRiEkIiK2UQiJiIhtFEIi
ImIbhZCIiNim3EJo7NixNG/enI4dOzrajhw5QnBwMP7+/gQHB5OZmQlYuwZP
njwZPz8/OnfuzPbt2x3PiYmJwd/fH39/f2JiYhzt27Zto1OnTvj5+TF58mTH
LsOX04eIiPxp/nxo0wZq1bL+nT+/XLsrtxAaM2YMK1asKNAWGRlJv379SEhI
oF+/fkRGRgKwfPlyEhISSEhIIDo6mgkTJgBWoLz44ots3ryZLVu28OKLLzpC
ZcKECURHRzued7av0vYhIiJ/mj8fIiLgwAEwxvo3IqJcg6jcQqhPnz40bdq0
QFtsbCyjR48GrC3sly5d6mi/7777cHJy4vrrrycrK4u0tDRWrlxJcHAwTZs2
pUmTJgQHB7NixQrS0tI4duwYN9xwA05OTtx3330FjlWaPkRE5E/TpsF5RRsB
6/tp08qtywq9JvTbb7/h4eEBWNUVz5bnTUlJKVDO92xp3eLavby8Lmq/nD4K
Ex0dTY8ePejRowfp6ell8dJFRCq/gwdL114GKsXChML2UHVycip1++X0UZiI
iAji4+OJj4/H3d292OOKiFQb3t6lay8DFRpCLVq0cJwCS0tLo3nz5oA1Kzm/
znxycjKenp7Ftp9fo/5s++X0ISIif3r1VahXr2BbvXpWezmp0BAKCQlxrHCL
iYlhyJAhjvZ58+ZhjGHTpk00btwYDw8PBgwYwKpVq8jMzCQzM5NVq1YxYMAA
PDw8aNiwIZs2bcIYw7x58wocqzR9iIjIn8LDIToafHzAycn6Nzraai8vppyM
HDnStGzZ0ri4uJhWrVqZWbNmmd9//90EBQUZPz8/ExQUZDIyMowxxuTn55uJ
EycaX19f07FjR7N161bHcWbPnm3atWtn2rVrZ+bMmeNo37p1qwkMDDS+vr5m
0qRJJj8/3xhjLquP4nTv3r2s3hIRkRqjpJ+dKmp3CT169NAu2iIipVTSz85K
sTBBRERqJoWQiIjYRiEkIiK2UQiJiIhtFEIiImIbhZCIiNhGISQiIrZRCImI
iG0UQiIiYhuFkIiI2EYhJCIitlEIiYiIbRRCIiJiG4WQiIjYRiEkIiK2UQiJ
iIhtFEIiImIbhZCIiNhGISQiIrZRCImIiG0UQiIiYhuFkIiI2EYhJCIitlEI
iYiIbRRCIiJiG4WQiIjYRiEkIiK2sSWE3nzzTQIDA+nYsSNhYWHk5OSQmJhI
79698ff3Z8SIEfzxxx8AnD59mhEjRuDn50fv3r1JSkpyHGf69On4+fnRoUMH
Vq5c6WhfsWIFHTp0wM/Pj8jISEd7UX2IiIg9KjyEUlJSeOedd4iPj2fnzp3k
5eWxcOFCnnrqKR577DESEhJo0qQJs2fPBmD27Nk0adKEX375hccee4ynnnoK
gJ9++omFCxeya9cuVqxYwcSJE8nLyyMvL49JkyaxfPlyfvrpJz799FN++ukn
gCL7EBERe9gyE8rNzeXUqVPk5uaSnZ2Nh4cHa9euJTQ0FIDRo0ezdOlSAGJj
Yxk9ejQAoaGhrFmzBmMMsbGxjBw5kjp16tC2bVv8/PzYsmULW7Zswc/PD19f
X2rXrs3IkSOJjY3FGFNkHyIiYo8KD6FWrVrxxBNP4O3tjYeHB40bN6Z79+64
ubnh4uICgJeXFykpKYA1c2rdujUALi4uNG7cmIyMjALt5z+nqPaMjIwi+7hQ
dHQ0PXr0oEePHqSnp5fL+yAiIjaEUGZmJrGxsSQmJpKamsrJkydZvnz5RY9z
cnICwBhT6M/Kqr0wERERxMfHEx8fj7u7+yVfk4iIXJ4KD6Gvv/6atm3b4u7u
jqurK0OHDmXDhg1kZWWRm5sLQHJyMp6enoA1Yzl06BBgncY7evQoTZs2LdB+
/nOKam/WrFmRfYiIiD0qPIS8vb3ZtGkT2dnZGGNYs2YN1157LbfddhuLFy8G
ICYmhiFDhgAQEhJCTEwMAIsXLyYoKAgnJydCQkJYuHAhp0+fJjExkYSEBHr1
6kXPnj1JSEggMTGRP/74g4ULFxISEoKTk1ORfYiIiE2MDZ577jnToUMHExgY
aEaNGmVycnLMvn37TM+ePU27du1MaGioycnJMcYYc+rUKRMaGmratWtnevbs
afbt2+c4ziuvvGJ8fX1N+/btzbJlyxztcXFxxt/f3/j6+ppXXnnF0V5UH8Xp
3r17Gb5yEZGaoaSfnU7GFHKxRBx69OhBfHy83cMQEalSSvrZqR0TRETENgoh
ERGxjUJIRERsoxASERHbKIRERMQ2CiEREbGNQkhERGyjEBIREdsohERExDYK
IRERsY1CSEREbKMQEhER2yiERETENgohERGxjUJIRERsoxASERHbKIRERMQ2
CiEREbGNQkhERGyjEBIREdsohERExDYKIRERsY1CSEREbKMQEhER2yiERETE
NgohERG5yIkTFdOPLSGUlZVFaGgo11xzDQEBAWzcuJEjR44QHByMv78/wcHB
ZGZmAmCMYfLkyfj5+dG5c2e2b9/uOE5MTAz+/v74+/sTExPjaN+2bRudOnXC
z8+PyZMnY4wBKLIPEREBY2DDBggLA09PyMgo/z5tCaFHHnmEgQMH8vPPP/PD
Dz8QEBBAZGQk/fr1IyEhgX79+hEZGQnA8uXLSUhIICEhgejoaCZMmABYgfLi
iy+yefNmtmzZwosvvugIlQkTJhAdHe143ooVKwCK7ENEpCbLyYG5c6FHD7jp
Jli2DMaNg7y8CujcVLCjR4+aNm3amPz8/ALt7du3N6mpqcYYY1JTU0379u2N
McZERESYBQsWXPS4BQsWmIiICEf72celpqaaDh06ONrPf1xRfRSne/ful/lK
RUQqtwMHjJk61ZirrzYGjLn2WmPee8+Y48ev/Ngl/ex0qYCcK2D//v24u7tz
//3388MPP9C9e3fefvttfvvtNzw8PADw8PDg8OHDAKSkpNC6dWvH8728vEhJ
SSm23cvL66J2oMg+LhQdHU10dDQA6enpZfjqRUTsZQx88w3MnAlLl1ptISHw
8MNw223g5FSx46nw03G5ubls376dCRMmsGPHDurXr1/saTHz5/Wc8zk5OZW6
vTQiIiKIj48nPj4ed3f3Uj1XRKQyOnkSPvwQOneGoCAriJ54AvbtgyVLrLaK
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
1zzwwAPGGGM+/fRTM3z4cGOMMbt27TKdO3c2OTk5Zv/+/cbX19fk5uaa3Nxc
4+vra/bt22dOnz5tOnfubHbt2lVsH8Xp3r172b5wEbki+fnGfPONMcOGGePs
bEytWsYMGWLM119bP5PKoaSfnSU+QxoXF8eMGTN46aWXHF+XKzk5mbi4OMfi
BmMMa9euJTQ0FIDRo0ezdOlSAGJjYxk9ejRglY5Ys2YNxhhiY2MZOXIkderU
oW3btvj5+bFlyxa2bNmCn58fvr6+1K5dm5EjRxIbG1tsHyJS+WVnw0cfQZcu
cOutsG4d/PWv1vLqpUuhX7/LLKEgtrLlZtVHH32UGTNmcPz4cQAyMjJwc3PD
xcUajpeXFykpKQCkpKTQunVra7AuLjRu3JiMjAxSUlK4/vrrHcc8/zlnH3+2
ffPmzcX2caHo6Giio6MBSE9Pv+zXKSJX7sKicV26WDea3ntvKYvGSaVU4Ter
fvXVVzRv3pzu3bs72kwhC/Sc/vyTpqiflVV7YSIiIoiPjyc+Ph53d/eiX4yI
lIuzReNCQs4tre7fH9avhx07rJ0NFEDVw2XdrNq0adPLvln1u+++44svvmDZ
smXk5ORw7NgxHn30UbKyssjNzcXFxYXk5GQ8PT0Ba8Zy6NAhvLy8yM3N5ejR
ozRt2tTRftb5zymsvVmzZkX2ISKVQ2FF46ZNgwcfLMOaPVKplGgmdPZm1Sef
fJLu3bvTtm1bRo4ceVkdTp8+neTkZJKSkli4cCFBQUHMnz+f2267jcWLFwMQ
ExPDkCFDAAgJCSEmJgaAxYsXExQUhJOTEyEhISxcuJDTp0+TmJhIQkICvXr1
omfPniQkJJCYmMgff/zBwoULCQkJwcnJqcg+RMRexRWNe/llBVC1VtyqhS1b
tpi0tDTH9zExMSY4ONg8/PDDJiMj4/KWTJxn3bp1jtVx+/btMz179jTt2rUz
oaGhJicnxxhjzKlTp0xoaKhp166d6dmzp9m3b5/j+a+88orx9fU17du3N8uW
LXO0x8XFGX9/f+Pr62teeeUVR3tRfRRHq+NEykdenjFffmnMgAHGgDGursaM
GmXM5s12j0zKQkk/O4vdMaFbt258/fXXNG3alG+//ZaRI0cSFRXF999/z+7d
ux2ziupMOyaIlK2sLJgzp2DRuAcfhIgIFY2rTspkx4S8vDyaNm0KwKJFi4iI
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
dg9LKomoqCjCw8Pp3Lkz33//Pc8884zdQ7JF7969CQ0NpVu3bnTq1In8/Hwi
IiLsHlaFCgsL44YbbmDPnj14eXkxe/Zspk6dyurVq/H392f16tVMnTq1XPrW
tj0iImIbzYRERMQ2CiEREbGNQkhERGyjEBIREdsohERExDYKIZHL5OzsTNeu
XenYsSP33HMP2dnZpT7G+PHjHZvK/v3vfy/wsxtvvLFMxjlmzBgWL15cJscq
z2NKzaQQErlMdevW5fvvv2fnzp3Url2bDz74oNTHmDVrluMm0QtDSHftS02g
EBIpA7fccgu//PILAG+88QYdO3akY8eOvPXWWwCcPHmSu+66iy5dutCxY0cW
LVoEwK233kp8fDxTp07l1KlTdO3alfDwcAAaNGgAWDtfTJkyhY4dO9KpUyfH
c7/55htuvfVWR02g8PBwLnXb37Zt2+jbty/du3dnwIABpKWlsXv3bnr16uV4
TFJSEp07dy7y8SJlycXuAYhUdbm5uSxfvpyBAweybds25s6dy+bNmzHG0Lt3
b/r27cv+/fvx9PQkLi4OgKNHjxY4RmRkJDNnzuT777+/6Piff/4533//PT/8
8AO///47PXv2pE+fPgDs2LGDXbt24enpyU033cR3333HzTffXOg4z5w5w8MP
P0xsbCzu7u4sWrSIadOmMWfOHP744w/279+Pr68vixYtYvjw4cU+XqSsKIRE
LtPZmQtYM6Fx48bx/vvvc/fdd1O/fn0Ahg4dyvr16xk4cCBPPPEETz31FIMG
DeKWW24pcT//+c9/CAsLw9nZmRYtWtC3b1+2bt1Ko0aN6NWrF15eXgB07dqV
pKSkIkNoz5497Ny5k+DgYMCqMnt2q/7hw4fz2WefMXXqVBYtWsSiRYuKfbxI
WVEIiVyms9eEzlfU6bD27duzbds2li1bxtNPP03//v157rnnStRPcafY6tSp
4/hvZ2dncnNziz1OYGBgoWW8R4wYwT333MPQoUNxcnLC39+fH3/8scjHi5QV
XRMSKUN9+vRh6dKlZGdnc/LkSZYsWcItt9xCamoq9erVY9SoUTzxxBOFlk1w
dXXlzJkzhR5z0aJF5OXlkZ6ezrffflvgGk5JdejQgfT0dEeonDlzhl27dgHQ
rl07nJ2defnllxkxYsQlHy9SVjQTEilD3bp1Y8yYMY6QGD9+PNdddx0rV65k
ypQp1KpVC1dXV95///2LnhsREUHnzp3p1q0b8+fPd7TffffdbNy4kS5duuDk
5MSMGTNo2bIlP//8c6nGVrt2bRYvXszkyZM5evQoubm5PProowQGBgLWbGjK
lCkkJiaW6PEiZUG7aIuIiG10Ok5ERGyjEBIREdsohERExDYKIRERsY1CSERE
bKMQEhER2yiERETENv8f8hHTioUCylMAAAAASUVORK5CYII=
" /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">12</span><span style=" color:#000080;">]:</span> plt.scatter(X,y, color = 'red')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.plot(X, lin_reg2.predict(poly_reg.fit_transform(X)), color ='blue')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.title('Truth or Bluff(Polynomial Rregression)')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.xlabel('Position level')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.ylabel('Salary')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.show()</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="data:image/png;base64,
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
towxY8YYX2/YsKHxOktISAgNGjTgv//9b6WOoZeXF2PGjMHKyooRI0Zw6tQp
5s6dS4MGDRg0aBBAmS1HJycnhg4dSqNGjWjatCmzZ88udZK9meLfi62tLTEx
MaxduxYrKyvj69bW1rzyyivUr1+fRo0aERUVxaRJkwgICMDKyorx48cDkJCQ
wK5du6hXrx7PPPMMNjY2PProo/j5+ZWqryr7s7a2Jj8/nyNHjlBQUIC7uzse
Hh6A1nJLSkoiKysLOzs7AgMDb/hsycnJxMfHExkZafw7f/LJJ0sd9759+zJg
wACsrKwYM2YMhw4dKrUPOzs7cnJyKn086yJJQuIGbdq0qZb9lLxmYmtrW+YF
3TNnzlBYWEi7du2MZe3atSvV5VOZeB5//HFycnLIy8sjKSmJxYsXEx0dfZuf
oGyOjo7873//u6E8JyeH7Oxsjh07xuTJkwFIT08v9dngxs9X7J577sHa2pof
f/yRw4cPc+rUKR566CHj6y1atCh1Ai8+ppU5hq1atTL+u1GjRlhZWRlbWMVl
Zf1+Ll68yIQJE2jbti1NmzYlKCioStfain8vf/zxBx07duTgwYOlXm/VqhX1
69c3Pj958iRvvPEGDg4OxkdGRgZpaWmkp6fj6upa6v3X/21UZX8dO3bkrbfe
4uWXX6Zly5aMGjWKP/74A4AlS5Zw9OhROnbsSK9evdi4ceMNny09PZ0WLVrQ
uHFjY9n1x/36/wMXL14stY///e9/ODg43PQ41mWShMQNrh9e3bhx41JdNcX/
UcvbvipatmyJlZUVJ0+eNJadOnWKO+6445b37+HhwcCBA/nqq69ueM3a2poG
DRpU+HlupmvXrvz3v/+t1LYuLi6lPhvc+PlKGjt2LMuXL2fZsmU89thjNGjQ
4KZ1VOYY3qqFCxcav/Hn5uayffv2W9qPk5MTn376KXPmzOHPP/80ll//u23T
pg1z584lJyfH+MjLy+Oxxx7D2dmZ1NTUUtufPn261POq7A+061+7du0iOTmZ
wsJCXnzxRQA6duzI6tWrOXPmDM8//zzDhw8nPz+/1L5dXFw4e/ZsqcRS1eN+
7NgxunXrVunt6yJJQuKmunfvTlxcHNnZ2WRkZLBo0aJSr7dq1arMrpzKsLGx
ITQ0lNmzZ3PhwgWSk5N55513GD169C3He/r0abZs2VJqRFtJ3bp1Y8WKFRQW
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
P/2kJZ6MDK3e1q1LJ51OnSTpCGEuFtUSKiwspEOHDnzzzTe4uroSEBDAqlWr
6Ny5c7nvkZZQ5WVmlr6+FB+vXXMCaNhQ65W8WcIwB2fnawnnvvugQwdJOkJU
N2kJlSE+Ph5PT088PDwAGDlyJLGxsRUmIVF5Tk4waJD2gGsX9+PjYd8+SE/X
WkM2NlrrqvjflXlene9p3FiSjhA1hUUlobS0NNq0aWN87urqyr59+3SMqG4z
GMDDQ3uMHKl3NEKImsiiklBZPY+GMr4SR0VFERUVBUBmZqbJ4xJCCEtlUQNN
XV1dOV087hZITU3FxcXlhu3Cw8NJTEwkMTERJycnc4YohBAWxaKSUEBAAElJ
SSQnJ3PlyhVWr15NSEiI3mEJIYTFsqjuOGtraz744AMGDBhAYWEh48ePx8fH
R++whBDCYllUEgIYNGgQg4qHbwkhhNCVRXXHCSGEqFkkCQkhhNCNJCEhhBC6
sahpe25FixYtcHNz0zuM25KZmSlDzUuQ43GNHIvS5Hhcc7vHIiUlhbNnz950
O0lCFkDmvytNjsc1cixKk+NxjbmOhXTHCSGE0I0kISGEELqxeuWVV17ROwhh
en5+fnqHUKPI8bhGjkVpcjyuMcexkGtCQgghdCPdcUIIIXQjSUgIIYRuJAnV
YadPn6Zfv354e3vj4+PDe++9p3dIuissLKRHjx4MHjxY71B0l5OTQ2hoKJ06
dcLb25s9e/boHZJu3nnnHXx8fPD19WXUqFHk5+frHZJZjR8/npYtW+Lr62ss
O3fuHMHBwXh5eREcHEx2drZJ6pYkVIdZW1vz1ltvcezYMfbu3cuHH37I0aNH
9Q5LV++99x7e3t56h1EjPPfccwwcOJBff/2Vn376yWKPS1paGosWLSIxMZHD
hw9TWFjI6tWr9Q7LrJ544gk2b95cqiwyMpL+/fuTlJRE//79iYyMNEndkoTq
MGdnZ3r27AmAnZ0d3t7epKWl6RyVflJTU4mLi2PChAl6h6K73Nxcdu7cyVNP
PQVA/fr1cXBw0Dkq/RQUFHDp0iUKCgrIy8src7HLuqxPnz40a9asVFlsbCzj
xo0DYNy4caxfv94kdUsSshApKSkcPHiQwMBAvUPRzZQpU1i4cCH16smf/YkT
J3BycuLJJ5+kR48eTJgwgYsXL+odli7uuOMOpk+fTtu2bXF2dsbe3p4HHnhA
77B09+eff+Ls7AxoX2jPnDljknrkf6MFuHDhAsOHD+fdd9+ladOmeoeji6+/
/pqWLVvKPSB/KSgo4MCBA0ycOJGDBw/SuHFjk3W31HTZ2dnExsaSnJxMeno6
Fy9eZPny5XqHZTEkCdVxV69eZfjw4YSFhTFs2DC9w9HNrl272LBhA25ubowc
OZLt27czevRovcPSjaurK66ursaWcWhoKAcOHNA5Kn18++23uLu74+TkhI2N
DcOGDWP37t16h6W7Vq1akZGRAUBGRgYtW7Y0ST2ShOowpRRPPfUU3t7eTJs2
Te9wdLVgwQJSU1NJSUlh9erVBAUFWfS33datW9OmTRt+++03ALZt20bnzp11
jkofbdu2Ze/eveTl5aGUYtu2bRY7SKOkkJAQYmJiAIiJiWHIkCEmqUeSUB22
a9culi1bxvbt2+nevTvdu3dn48aNeoclaoj333+fsLAwunbtyqFDh5g9e7be
IekiMDCQ0NBQevbsSZcuXSgqKiI8PFzvsMxq1KhR3HXXXfz222+4uroSHR3N
rFmz+Oabb/Dy8uKbb75h1qxZJqlbpu0RQgihG2kJCSGE0I0kISGEELqRJCSE
EEI3koSEEELoRpKQEEII3UgSEuIWWVlZ0b17d3x9fXn00UfJy8ur8j4mTJhg
nFR2/vz5pV67++67qyXOJ554grVr11bLvky5T2GZJAkJcYsaNWrEoUOHOHz4
MPXr1+eTTz6p8j4WL15svEn0+iQkd+0LSyBJSIhqcO+993L8+HEA3n77bXx9
ffH19eXdd98F4OLFizz00EN069YNX19f1qxZA8B9991HYmIis2bN4tKlS3Tv
3p2wsDAAmjRpAmgzX8yYMQNfX1+6dOlifO93333HfffdZ1wTKCwsjJvd9rd/
/3769u2Ln58fAwYMICMjg2PHjtGrVy/jNikpKXTt2rXc7YWoTtZ6ByBEbVdQ
UMCmTZsYOHAg+/fvZ8mSJezbtw+lFIGBgfTt25cTJ07g4uJCXFwcAOfPny+1
j8jISD744AMOHTp0w/6//PJLDh06xE8//cTZs2cJCAigT58+ABw8eJAjR47g
4uLCPffcw65du+jdu3eZcV69epVnn32W2NhYnJycWLNmDS+99BKfffYZV65c
4cSJE3h4eLBmzRoee+yxCrcXorpIEhLiFhW3XEBrCT311FN8/PHHDB06lMaN
GwMwbNgwfvjhBwYOHMj06dOZOXMmgwcP5t577610PT/++COjRo3CysqKVq1a
0bdvXxISEmjatCm9evXC1dUVgO7du5OSklJuEvrtt984fPgwwcHBgLbKbPFU
/Y899hiff/45s2bNYs2aNaxZs6bC7YWoLpKEhLhFxdeESiqvO6xDhw7s37+f
jRs38uKLL/LAAw/w8ssvV6qeirrYGjRoYPy3lZUVBQUFFe7Hx8enzGW8R4wY
waOPPsqwYcMwGAx4eXnxyy+/lLu9ENVFrgkJUY369OnD+vXrycvL4+LFi6xb
t457772X9PR0bG1tGT16NNOnTy9z2QQbGxuuXr1a5j7XrFlDYWEhmZmZ7Ny5
s9Q1nMrq2LEjmZmZxqRy9epVjhw5AkD79u2xsrLiH//4ByNGjLjp9kJUF2kJ
CVGNevbsyRNPPGFMEhMmTKBHjx5s2bKFGTNmUK9ePWxsbPj4449veG94eDhd
u3alZ8+erFixwlg+dOhQ9uzZQ7du3TAYDCxcuJDWrVvz66+/Vim2+vXrs3bt
WiIiIjh//jwFBQVMmTIFHx8fQGsNzZgxg+Tk5EptL0R1kFm0hRBC6Ea644QQ
QuhGkpAQQgjdSBISQgihG0lCQgghdCNJSAghhG4kCQkhhNCNJCEhhBC6+X8W
1C+8nI8YJAAAAABJRU5ErkJggg==
" /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">13</span><span style=" color:#000080;">]:</span> from sklearn.preprocessing import PolynomialFeatures</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> poly_reg = PolynomialFeatures(degree = 3)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> X_poly = poly_reg.fit_transform(X)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> lin_reg2 = LinearRegression()</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> lin_reg2.fit(X_poly, y)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#8b0000;">Out[</span><span style=" font-weight:600; color:#8b0000;">13</span><span style=" color:#8b0000;">]:</span> LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">14</span><span style=" color:#000080;">]:</span> plt.scatter(X,y, color = 'red')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.plot(X, lin_reg2.predict(poly_reg.fit_transform(X)), color ='blue')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.title('Truth or Bluff(Polynomial Rregression)')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.xlabel('Position level')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.ylabel('Salary')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.show()</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">15</span><span style=" color:#000080;">]:</span> from sklearn.preprocessing import PolynomialFeatures</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> poly_reg = PolynomialFeatures(degree = 4)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> X_poly = poly_reg.fit_transform(X)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> lin_reg2 = LinearRegression()</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> lin_reg2.fit(X_poly, y)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#8b0000;">Out[</span><span style=" font-weight:600; color:#8b0000;">15</span><span style=" color:#8b0000;">]:</span> LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">16</span><span style=" color:#000080;">]:</span> plt.scatter(X,y, color = 'red')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.plot(X, lin_reg2.predict(poly_reg.fit_transform(X)), color ='blue')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.title('Truth or Bluff(Polynomial Rregression)')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.xlabel('Position level')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.ylabel('Salary')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.show()</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="data:image/png;base64,
iVBORw0KGgoAAAANSUhEUgAAAaEAAAEWCAYAAADPZygPAAAACXBIWXMAAAsS
AAALEgHS3X78AAAAO3pUWHRTb2Z0d2FyZQAACJnLTSwpyMkvyclMUihLLSrO
zM9TMNIz1DPSUcgoKSmw0tfPhSvQyy9K1wcApwMQ8Tj1nCgAACAASURBVHic
7d1/XM33///x21EykQqhJMpJUn5HthnDuzHzzpCf+c3aG++12ZgNn5nPe8N8
3vs9+9GX7R1FbbbJ5ufGNpvf+bEN8c6U9GMkxZKien7/eOkoKkX1qs7jerl0
Sc/zOq/X47zk3D2f5/l6vgxKKYUQQgihgzp6FyCEEMJ8SQgJIYTQjYSQEEII
3UgICSGE0I2EkBBCCN1ICAkhhNCNhJCocKdPn8ZgMOhdhsn3339PmzZtyrz9
Bx98QLNmzWjYsCGXL1/m559/xmg00rBhQ7799lsAVqxYwZw5c+67tt69e/Of
//znvvdTkaZPn86SJUvKtG11rL8ynTlzhoYNG973fpRS+Pj4cPLkyQqoqmaT
EDIzDRs2NH3VqVOH+vXrm34ODw+/p306Ozvz448/Vmyh5bBw4ULq1q1reh0d
OnRgw4YN97Sv7Oxs5syZww8//EBmZia2trYsXLiQ2bNnk5mZyZAhQ8jJyWHJ
kiWmECoI3YLju7q6snz58op8iVVq5cqVzJ8//773U/jvxc7OjocffpgDBw5U
QIX6cXNzIzMz8773YzAYeP7551m0aFEFVFWzSQiZmczMTNOXi4sL33zzjenn
wMDAO7bPzc3VocqSlVRPYGCg6XX8+9//ZuzYsVy8eLHc+//zzz/JycnBy8vL
1Hb27NkiP3/11Vd06tSJFi1aFHluwfHXrFnDokWL+P7778t9/Nqm4O8lNTWV
Rx55hJEjR5a4bUX/rlW3393bPfnkk2zfvp0LFy7oXYquJIREEQsXLmT06NGM
HTsWGxsbwsLCGD9+PK+++qppm8LDW2PHjiU5OZnHH3+chg0b8tZbb5m2W716
Nc7Ozjg4OLBs2bISj5mRkcH48eNxcHCgTZs2LF26lIKFPFauXEmfPn0IDg6m
cePGvPbaa3d9DYMHD6Z+/fqcOXPmjsdyc3MxGAzEx8eb2gpeX0xMjClsGjZs
yGOPPUabNm1ISEgwvb68vDy2bNlC3759Szx+7969ad++PceOHQPgl19+wcfH
B1tbW3r27Mn+/fvveE52djZ2dnbExMSY2lJSUrC2tiYtLc10zpcvX46DgwNO
Tk6sXr26zOewb9++BAcHY2dnh9FoZP/+/axatYpWrVrRvHlzwsLC7jgfAGlp
aQwePBgHBwfs7e35+9//TlJS0l3/Dm5Xt25dxo0bR0JCAunp6cCt36MlS5bQ
okULnnrqKQA2btxI586dsbOzo3fv3qbzCBAdHU2XLl2wsbFhzJgxjBw50lTr
vexvyZIlODk50ahRI9q3b2/q0e/bt49u3brRqFEjmjdvzty5c4E7h5oTExMZ
MmQIjRs3xt3dnU8//dT02MKFCxk7dizjx4/HxsYGb29vDh8+bHrc2tqaLl26
8N1335X7fNYmEkLiDl9//TXjxo3j8uXLjB49utRt161bh5OTE1u2bCEzM5Pn
n3/e9NiePXs4ffo027ZtY9GiRcTGxha7j5kzZ5KVlcWZM2fYuXMnq1atKvIG
u2fPHjw9PUlNTWXevHml1qOUYuPGjSilaN++fTleNXh6evLrr78CWq9m+/bt
xMfHF3l9FhYW/P7773h4eJR4/J9//pmYmBi6du3KxYsXeeKJJ3jhhRdIS0sj
ODiYwYMHm96ICzzwwAOMGjWqSBisXbuWgQMH0qRJE0B7w7t27RrJycl8/PHH
zJgxgytXrpTpHO7evZsePXqQlpZGQEAAo0aN4tdff+X06dN89tlnzJo1i6ys
rDteT35+Pk899RQJCQmcPXuWunXr8uyzz5brvALk5OSwevVqHBwcaNSokak9
MTGRzMxMEhIS+PDDDzl48CBPPfUUK1euJC0tjalTpzJ06FCuX79OTk4OTz75
JNOnT+fSpUuMGDHijmHX8uzv+PHjfPLJJxw+fJgrV66wZcsWXFxcAHjmmWeY
O3cuV65c4fTp0wQEBBT7ukaPHo2rqyvJyclERkby4osv8tNPP5ke37BhAxMm
TCAjI4PHH3+c4ODgIs8v/DtnriSExB169+7N3//+d9NnRvfq1Vdf5YEHHqBb
t254eXkV+4/txo0bfP755yxbtgwbGxvc3NyYPXs2a9asMW3j4uLCjBkzsLCw
KLGetWvXYmdnR4MGDRg2bBgLFy4s8mZXkTIyMrCxsbmj3c7OjsaNGxMUFMSb
b75J3759+eabb/Dy8mLs2LFYWloyfvx43Nzc2LRp0x3PnzRpEmvXrjX1YNas
WcOECRNMjz/wwAOmz1n8/f2pV68e//3vf8t0Dt3d3ZkwYQIWFhaMHj2ahIQE
Fi1aRL169Rg8eDBAsT1HBwcHhg0bRv369WnUqBHz588v8iZ7NwV/L9bW1oSG
hrJ+/XosLCxMj1taWvLqq69iZWVF/fr1CQkJYebMmfTo0QMLCwumTp0KwMGD
B9m9ezd16tThn//8J3Xr1mXkyJF07969yPHKsz9LS0uys7M5fvw4ubm5uLq6
4ubmBmg9t9jYWNLS0rCxscHX1/eO1xYXF8eBAwdYtmyZ6fd8ypQpRc573759
GThwIBYWFkyYMIGjR48W2YeNjQ0ZGRllPp+1kYSQuEOrVq0qZD+FPzOxtrYu
9gPdCxcukJeXR+vWrU1trVu3LjLkU5Z6xo0bR0ZGBllZWcTGxrJy5UpWrVp1
n6+gePb29vz11193tGdkZJCenk5MTAyzZs0CIDk5uchrgztfX4GHH34YS0tL
fvnlF44dO0ZCQgJPPPGE6fGmTZsWeQMvOKdlOYfNmzc3/bl+/fpYWFiYelgF
bcX9/Vy9epXp06fj4uJCo0aN6N+/f7k+ayv4e/nzzz/x8PDgyJEjRR5v3rw5
VlZWpp/Pnj3LG2+8gZ2dnekrJSWFpKQkkpOTcXZ2LvL82383yrM/Dw8P3nzz
TV555RWaNWvG2LFj+fPPPwH47LPPOHHiBB4eHvTs2ZPNmzff8dqSk5Np2rQp
DRo0MLXdft5v/zdw9erVIvv466+/sLOzu+t5rM0khMQdbp9e3aBBgyJDNQX/
UEvavjyaNWuGhYUFZ8+eNbUlJCTQsmXLe96/m5sbgwYN4ptvvrnjMUtLS+rV
q1fq67mbTp068d///rdM2zo5ORV5bXDn6yts4sSJhIWFsWbNGkaNGkW9evXu
eoyynMN7tXz5ctP/+K9cucLOnTvvaT8ODg588sknLFy4kPPnz5vab/+7bdWq
FYsWLSIjI8P0lZWVxahRo3B0dCQxMbHI9ufOnSvyc3n2B9rnX7t37yYuLo68
vDxefvllADw8PIiIiODChQu88MILjBgxguzs7CL7dnJy4uLFi0WCpbznPSYm
hs6dO5d5+9pIQkjcVZcuXdi0aRPp6emkpKTw3nvvFXm8efPmxQ7llEXdunUJ
CAhg/vz5ZGZmEhcXx9tvv8348ePvud5z586xbdu2IjPaCuvcuTPh4eHk5eWx
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
jkgA1WTSExJC1Ahxcdo6b999Bw89BP/v/2m9IFGzVXlP6Ny5c/Tr1w9PT0+8
vLx49913Abh06RJ+fn64u7vj5+dHeno6AEopgoODMRqNdOrUicOHD5v2FRoa
iru7O+7u7oSGhpraDx06RMeOHTEajQQHB6OUKvUYQojqKzdXu9DU21ubAbdi
Bfz8swRQraGqWHJysjp06JBSSqkrV64od3d3dfz4cTV37ly1dOlSpZRSS5cu
VS+++KJSSqlNmzapQYMGqfz8fLV3717Vs2dPpZRSaWlpytXVVaWlpalLly4p
V1dXdenSJaWUUj169FB79uxR+fn5atCgQWrz5s1KKVXiMUrTvXv3ij0BQohb
wsKUat1aKYNB+x4WVuTho0eV8vFRCpQaMkSphARdqhT3oKzvnVUeQrfz9/dX
27dvV+3atVPJyclKKS2o2rVrp5RSKigoSK1du9a0fcF2a9euVUFBQab2gu2S
k5OVh4eHqb3wdiUdozQSQkJUkrAwpayttYQp+LK2ViosTF27ptT8+UpZWirV
rJlSERFK5efrXbAoj7K+d+o6MSE+Pp4jR47g6+vL+fPncXR0BMDR0ZELFy4A
kJSURKtWrUzPcXZ2JikpqdR2Z2fnO9qBEo8hhNDBggWQlVW0LSuLn17YSOfO
sGQJjB8PMTEwejQYDPqUKSqXbiGUmZnJiBEjeOedd2jUqFGJ26mbn+cUZjAY
yt1eHiEhIfj4+ODj40Nqamq5niuEKKOEhCI/ZmDL03zMo+cjuXFDm4Dw2WfQ
uLFO9YkqoUsI3bhxgxEjRhAYGMjw4cMBaN68OSkpKQCkpKTQ7Oblzs7Ozpw7
d8703MTERJycnEptT0xMvKO9tGPcLigoiOjoaKKjo3FwcKjAVy6EMHFxMf3x
a56kAydYyXTmNPqE33+Hv/1Nx9pElanyEFJKMW3aNDw9PXn++edN7f7+/qYZ
bqGhoQwdOtTUvnr1apRS7Nu3D1tbWxwdHRk4cCDbt28nPT2d9PR0tm/fzsCB
A3F0dMTGxoZ9+/ahlGL16tVF9lXcMYQQVSsjA74Z8R/mWL5Dd6IZztc04wIH
HujD/33YkAYN9K5QVJlK+1SqBD///LMCVMeOHVXnzp1V586d1aZNm9TFixdV
//79ldFoVP3791dpaWlKKaXy8/PVzJkzlZubm/L29lYHDx407WvVqlWqbdu2
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
EJXK7EJo69ateHh4YDQaWbZsmd7lCCGEWTOrEMrLy2PWrFls2bKFEydOsG7d
Ok6cOKF3WUIIYbbMKoQOHDiA0WjEzc0NKysrxowZQ1RUlN5lCSGE2TKrEEpK
SqJVq1amn52dnUlKSrpju5CQEHx8fPDx8SG14AY2QgghKpxZhVBx1+Uailm0
LSgoiOjoaKKjo3FwcKiK0oQQwiyZVQg5Oztz7tw508+JiYk4lXo7TiGEEJXJ
rEKoR48exMbGEhcXx/Xr14mIiMDf31/vsoQQwmyZ1cWqlpaWfPDBBwwcOJC8
vDymTp2K112u6oyPj8fHx6eKKqwcqampMqxYiJyPW+RcFCXn45b7PRfxZbxV
iyxgagbuaRHWWkzOxy1yLoqS83FLVZ0LsxqOE0IIUb1ICAkhhNCNxauvvvqq
3kWIyte9e3e9S6hW5HzcIueiKDkft1TFuZDPhIQQQuhGhuOEEELoRkJICCGE
biSEarFz587Rr18/PD098fLy4t1339W7JN3l5eXRtWtXhgwZoncpusvIyCAg
IID27dvj6enJ3r179S5JN2+//TZeXl54e3szduxYsrOz9S6pSk2dOpVmzZrh
7e1tart06RJ+fn64u7vj5+dHenp6pRxbQqgWs7S05M033yQmJoZ9+/axYsUK
s791xbvvvounp6feZVQLzz77LIMGDeLkyZP8+uuvZntekpKSeO+994iOjubY
sWPk5eURERGhd1lVavLkyWzdurVI27JlyxgwYACxsbEMGDCg0u6/JiFUizk6
OtKtWzcAbGxs8PT0LHbVcHORmJjIpk2bmD59ut6l6O7KlSvs2rWLadOmAWBl
ZYWdnZ3OVeknNzeXa9eukZubS1ZWltmtKdmnTx8aN25cpC0qKopJkyYBMGnS
JDZs2FApx5YQMhPx8fEcOXIEX19fvUvRzXPPPcfy5cupU0d+7c+cOYODgwNT
pkyha9euTJ8+natXr+pdli5atmzJnDlzcHFxwdHREVtbWx577DG9y9Ld+fPn
cXR0BLT/0F64cKFSjiP/Gs1AZmYmI0aM4J133qFRo0Z6l6OLb7/9lmbNmsk1
IDfl5uZy+PBhZsyYwZEjR2jQoIHZ3u4+PT2dqKgo4uLiSE5O5urVq4SFheld
ltmQEKrlbty4wYgRIwgMDGT48OF6l6Ob3bt3s3HjRtq0acOYMWPYuXMn48eP
17ss3Tg7O+Ps7GzqGQcEBHD48GGdq9LH999/j6urKw4ODtStW5fhw4ezZ88e
vcvSXfPmzUlJSQEgJSWFZs2aVcpxJIRqMaUU06ZNw9PTk+eff17vcnS1dOlS
EhMTiY+PJyIigv79+5v1/3ZbtGhBq1atOHXqFAA7duygQ4cOOlelDxcXF/bt
20dWVhZKKXbs2GG2kzQK8/f3JzQ0FIDQ0FCGDh1aKceREKrFdu/ezZo1a9i5
cyddunShS5cubN68We+yRDXx/vvvExgYSKdOnTh69Cjz58/XuyRd+Pr6EhAQ
QLdu3ejYsSP5+fkEBQXpXVaVGjt2LA8++CCnTp3C2dmZVatW8dJLL/Hdd9/h
7u7Od999x0svvVQpx5Zle4QQQuhGekJCCCF0IyEkhBBCNxJCQgghdCMhJIQQ
QjcSQkIIIXQjISTEPbKwsKBLly54e3szcuRIsrKyyr2P6dOnmxaVXbJkSZHH
HnrooQqpc/Lkyaxfv75C9lWZ+xTmSUJIiHtUv359jh49yrFjx7CysuLjjz8u
9z5Wrlxpukj09hCSq/aFOZAQEqICPPLII5w+fRqAt956C29vb7y9vXnnnXcA
uHr1Kk888QSdO3fG29ubyMhIAB599FGio6N56aWXuHbtGl26dCEwMBCAhg0b
AtrKF3PnzsXb25uOHTuanvvjjz/y6KOPmu4JFBgYyN0u+zt06BB9+/ale/fu
DBw4kJSUFGJiYujZs6dpm/j4eDp16lTi9kJUJEu9CxCipsvNzWXLli0MGjSI
Q4cO8dlnn7F//36UUvj6+tK3b1/OnDmDk5MTmzZtAuDy5ctF9rFs2TI++OAD
jh49esf+v/rqK44ePcqvv/7KxYsX6dGjB3369AHgyJEjHD9+HCcnJx5++GF2
795N7969i63zxo0bPPPMM0RFReHg4EBkZCQLFizg008/5fr165w5cwY3Nzci
IyMZNWpUqdsLUVEkhIS4RwU9F9B6QtOmTeOjjz5i2LBhNGjQAIDhw4fz888/
M2jQIObMmcO8efMYMmQIjzzySJmP88svvzB27FgsLCxo3rw5ffv25eDBgzRq
1IiePXvi7OwMQJcuXYiPjy8xhE6dOsWxY8fw8/MDtLvMFizVP2rUKD7//HNe
euklIiMjiYyMLHV7ISqKhJAQ96jgM6HCShoOa9euHYcOHWLz5s28/PLLPPbY
Y7zyyitlOk5pQ2z16tUz/dnCwoLc3NxS9+Pl5VXsbbxHjx7NyJEjGT58OAaD
AXd3d37//fcStxeioshnQkJUoD59+rBhwwaysrK4evUqX3/9NY888gjJyclY
W1szfvx45syZU+xtE+rWrcuNGzeK3WdkZCR5eXmkpqaya9euIp/hlJWHhwep
qammULlx4wbHjx8HoG3btlhYWPCvf/2L0aNH33V7ISqK9ISEqEDdunVj8uTJ
ppCYPn06Xbt2Zdu2bcydO5c6depQt25dPvroozueGxQURKdOnejWrRvh4eGm
9mHDhrF37146d+6MwWBg+fLltGjRgpMnT5arNisrK9avX09wcDCXL18mNzeX
5557Di8vL0DrDc2dO5e4uLgybS9ERZBVtIUQQuhGhuOEEELoRkJICCGEbiSE
hBBC6EZCSAghhG4khIQQQuhGQkgIIYRuJISEEELo5v8Dk/djNhfCv9QAAAAA
SUVORK5CYII=
" /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">17</span><span style=" color:#000080;">]:</span> lin_reg.predict(6.5)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#8b0000;">Out[</span><span style=" font-weight:600; color:#8b0000;">17</span><span style=" color:#8b0000;">]:</span> array([330378.78787879])</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">18</span><span style=" color:#000080;">]:</span> lin_reg_2.predict(poly_reg.fit_transform(6.5))</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Traceback <span style=" color:#4682b4;">(most recent call last)</span>:</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#4682b4;">  File </span><span style=" color:#006400;">&quot;&lt;ipython-input-18-37e3532bc52e&gt;&quot;</span><span style=" color:#4682b4;">, line </span><span style=" color:#006400;">1</span><span style=" color:#4682b4;">, in </span><span style=" color:#9400d3;">&lt;module&gt;</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#8b0000;">    lin_reg_2.predict(poly_reg.fit_transform(6.5))</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#8b0000;">NameError:</span> name 'lin_reg_2' is not defined</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">19</span><span style=" color:#000080;">]:</span> </p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">19</span><span style=" color:#000080;">]:</span> lin_reg2.predict(poly_reg.fit_transform(6.5))</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#8b0000;">Out[</span><span style=" font-weight:600; color:#8b0000;">19</span><span style=" color:#8b0000;">]:</span> array([158862.45265153])</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">20</span><span style=" color:#000080;">]:</span> </p></body></html>