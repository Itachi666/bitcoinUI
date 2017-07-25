主界面&主程序  ui.py
运行后有一个登陆界面，输入一组对应的比特币地址和私钥登陆
exm：'mhqNzF5fQGpeVHpestNbxz8mPDyjzUcSuJ', 'cNUz3hRMLEq2BXNyG1RunyrFXhYeucdC2sg5buxsWcu2AAG3Gd6q'
对应类   LoginDialog

主界面有一个表格table，后台会调用（生成）数据库INFO.db，见initDB函数
SkPk.py文件中的函数主要为计算比特币系统中的各种私钥公钥地址之间的转化函数，以及对合同文本的转化函数。

ui界面分四个功能模块：
1.合同文本转换translate函数,点击translate按钮调用，  主要功能：完成合同文本转化
    调用ui_input文件，其中主体是Ui_input类，其中setupUi和retranslateUi为qt窗口设置参数不用考虑，几个getdata_*函数用来回传参数，使用方法：
        myapp = input()
        myapp.show()
        myapp.exec_()
        data = myapp.ui.getdata_all()
    getpandq：生成两个1024位的素数p，q并显示在ui上面，算法调用SkPk.py
    Require：require按钮功能，弹出一个提示窗，没太大作用
    file_click：实现选择文件的功能（目前不支持中文文件名）
    createkey：拥有p，q，文件之后调用SkPk完成转换，并调用下一个窗口ui_generate
        ui_generate:将生成公私钥显示出来，调用ui_details显示更多参数细节
    最后在translate函数中将全部参数加入INFO

2.交换1中生成的数据exchange         主要功能：完成双方的合同文本数据交换
    需要主窗口选定一行参数
    调用ui_exchange文件，使之弹出exchange窗口
    上方文本框为显示用
    需要在这里输入交易对方的名称（作为一个识别标记）和这一交易预计提交押金
    showHint_*:为弹出提示窗口用
    putindata： 将在 1 中生成的各种参数传进来
    set_a_server： 对应第一个按钮Set a Server ，调用setserver函数建立服务器
    connect_ip： 第二个按钮，无太大实际意义，用以表示连接成功
    exchangedata： 第三个按钮，客户端向服务端发送数据，同时服务端回传对应数据
    getdata：向主窗口传送数据
    checking：没写出来，无实际功能，只弹出成功窗口
    在关闭exchange窗口之后，ui.py文件通过getdata函数获取数据，并记入数据库

3.创建交易单并发送createandsend         主要功能：创建发送交易单
    需要主窗口选定一行参数
    调用ui_send文件
    也分为四个模块：create，sign，exchange，send
    create：调用ui_createtx文件，通过tx.py和此前两步中的数据来创建五个交易单
        特别的，createfundingtransaction函数需要提供两笔（且只能是两笔）总钱数足够双方总押金的txid。
    sign：调用ui_signtx文件，通过tx.py和此前交换得到的私钥来签名五个交易单
    exchange：无功能
    send：调用ui_up2bit文件，无实际功能，靠server在后台传输数据保持同步，核心在checking按钮，用以表示当前交换进度（有哪几笔交易已经被发送）

4.删去某一笔交易delele
    主窗口选中一行，直接删除。