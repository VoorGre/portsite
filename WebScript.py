from flask import Flask, render_template, request, redirect
import csv



app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('./index.html')






@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


@app.route("/submit_form",methods=['POST',"GET"])
def submit_form():
    if request.method== 'POST':
        try:
            data= request.form.to_dict()
            write_to_csv(data)

            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return "Error"



def write_to_csv(data):
    with open('db.csv',mode='a',newline='') as database2:
        email =data["email"]
        subject= data["subject"]
        message=data["message"]
        csv_writer = csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])



# @app.route("/about.html")
# def about():
#     return render_template('./about.html')
#
#
# @app.route("/components.html")
# def components():
#     return render_template('./components.html')
#
# @app.route("/contact.html")
# def contact():
#     return render_template('./contact.html')
#
# @app.route("/thankyou.html")
# def thankyou():
#     return render_template('./thankyou.html')
#
# @app.route("/work.html")
# def work():
#     return render_template('./work.html')
#
# @app.route("/works.html")
# def works():
#     return render_template('./works.html')