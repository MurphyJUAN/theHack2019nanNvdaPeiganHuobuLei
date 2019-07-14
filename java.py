from jpype import *
import os

#指定jar包位置
jarpath = os.path.join(os.path.abspath('.'), '/EngStudy/')
#开启JVM，且指定jar包位置
jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.ext.dirs=%s" % jarpath)
#引入java程序中的类.路径应该是项目中的package包路径
javaClass = jpype.JClass('cilin.CiLin')
#这一步就是具体执行类中的函数了
javaInstance = javaClass.calcWordsSimilarity(u"杯子", u"盆子")
print(javaInstance)
jpype.shutdownJVM()
