from flask import Flask, render_template
# from forms import ContactForm
# import contact2.html
from flask import request
import pandas as pd

app = Flask(__name__)
app.secret_key = 'secretKey'

@app.route('/contact2', methods=["GET","POST"])
def get_contact():
    form = ContactForm()
    # here, if the request type is a POST we get the data on contact
    #forms and save them else we return the contact forms html page
    if request.method == 'POST':
        name =  request.form["fisrt name"]
        last = request.form["last name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        res = pd.DataFrame({'name':name,"last name":last, 'email':email, 'subject':subject ,'message':message}, index=[0])
        res.to_csv('./contactusMessage.csv')
        print("The data are saved !")
    else:
        return render_template('contact2.html', form=form)

        if __name__ == '__main__':

         app.run(debug=True)
