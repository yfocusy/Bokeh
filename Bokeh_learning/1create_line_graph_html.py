from bokeh.plotting import figure, output_file, show

# data
x=[1,2,3,4,5]
y=[6,7,2,4,5]

# output a html file
output_file("lines.html")

# set x,y and labels
p = figure(title="simple line example", x_axis_label='x',y_axis_label='y')

# draw a line
p.line(x,y,legend="Temp.", line_width=2)

# generate html file and open it in the browser
show(p)


'''
通过这个示例，可以大致了解bokeh.plotting绘图的基本流程：

准备数据；
通过output_file指定输出文件；
调用figure方法生成画布，指定标题、坐标标签等信息；
添加数据绘制图，可以指定颜色、图例、粗细等参数；
调用show方法生成结果文件。
https://zhuanlan.zhihu.com/p/28334595

'''
