from flask import Flask, render_template, request, redirect
from Mahjong import Mahjong_settle
from trans_html import create_html_table 

app = Flask(__name__,template_folder='./templates')

# 配置路由，获取用户提交的登录信息



# 指定请求方式，如果不指定，则无法匹配到请求
@app.route("/Mahjong", methods=("GET", "POST"))
def Mahjong_calculate():
    # GET请求
    if request.method == "GET":
        return render_template("get_form.html")
    # POST请求
    if request.method == "POST":
        print('request.form.to_dict():',request.form.getlist('card_type'))
    # 获取数据并转化成字典
        card_type = request.form.getlist('card_type')
        print('card_type:',card_type)
        if len(card_type)==0:
            return "请选择胡牌类型"
        else:
            result = Mahjong_settle(card_type)
            print("result is :",result)
            heads = ["角色类型","输赢额"]
            #heads = '''<tr><th>角色类型</th><th>输赢额</th></tr>'''
            return render_template("result.html",heads = heads,results = result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)