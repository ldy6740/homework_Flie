from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


articles = []



## HTML을 주는 부분
@app.route('/')
def home():
    return 'This is Home!'


@app.route('/mypage')
def mypage():
    return render_template('index.html')

@app.route('/subpage')
def subpage():
    return render_template('subpage.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')



## API 역할을 하는 부분
@app.route('/post', methods=['POST'])
def post():
    global articles  # 이 함수 안에서 나오는 articles 글로벌 변수를 가리킵니다.

    name_receive = request.form['name_give']  # 주문자 name을 받는 부분
    quantity_receive = request.form['quantity_give']  # 주문할 수량을 받는 부분
    address_receive = request.form['address_give']  # 배송할 address 받는 부분
    phone_receive = request.form['phone_give']  # 고객 phone 받는 부분


    article = {'name': name_receive,'quantity': quantity_receive, 'address': address_receive, 'phone': phone_receive}  # 받은 걸 딕셔너리로 만들고,

    articles.append(article)  # 넣는다

    return jsonify({'result': 'success'})


@app.route('/post', methods=['GET'])
def view():
    return jsonify({'result': 'success', 'articles': articles})

'''
@app.route('/delete', methods=['post'])
def delete():
    global articles  # 이 함수 안에서 나오는 articles 글로벌 변수를 가리킵니다.
    no_receive = request.form['no_give']  # 클라이언트로부터 no를 받는 부분

    for article in articles:  # 반복문: articles를 돌면서,
        if str(article['no']) == no_receive:  # 조건문: 받은 no와 같은 번호의 아티클을 찾아서 (단, 문자열 == 문자열로!)
            articles.remove(article)  # 해당 article을 지우고,
            return jsonify({'result': 'success'})  # 결과를 주고 함수를 끝낸다.

    return jsonify({'result': 'fail', 'msg': '아티클이 없습니다'})  # 만약 반복문을 다 돌아도 결과를 주지 않았으면, 아티클이 없다고 한다.
'''

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)