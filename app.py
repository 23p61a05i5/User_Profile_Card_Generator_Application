from flask import Flask, render_template, request
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    profile=None
    if request.method=="POST":
        profile={"name":request.form.get("name","").strip(),"bio":request.form.get("bio","").strip(),
                 "image_url":request.form.get("image_url","").strip(),"role":request.form.get("role","").strip()}
        if not profile["name"]: profile=None
    return render_template("index.html",profile=profile)
if __name__=="__main__": app.run(debug=True)
