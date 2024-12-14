from flask import Flask, render_template, request

# ایجاد یک برنامه Flask
app = Flask(__name__)

# مسیر اصلی برای نمایش صفحه HTML
@app.route('/')
def index():
    return render_template('index.html')  # فایل index.html از پوشه templates بارگذاری می‌شود

# مسیر برای پردازش فرم ارسال‌شده
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']  # دریافت داده فیلد "name" از فرم
    email = request.form['email']  # دریافت داده فیلد "email" از فرم
    return f"Form submitted! Name: {name}, Email: {email}"  # نمایش داده‌های دریافت‌شده

# اجرای سرور Flask
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # سرور روی پورت 5001 اجرا می‌شود