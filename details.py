from flask import Flask,request
app=Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Home page"

  ###  calling through URL -----> /api/name/or data

# @app.route('/api/<name>')
# def name(name):
#     # length=len(name)
#     # if length>5:
#     #     return "name is too long"
#     # else:
#     #     return "Nice Name."
#     result= "hello " + name + "!"
#     return result



# @app.route('/add/<a>/<b>')
# def add(a,b):
#     answer= int(a) + int(b)
#     result={
#         'ans' : answer
#     }
#     return result



######### calling through json   ----> api/?name=....&age=...
####giving value through url position matter but in json does'nt

@app.route('/api')
def name():
    name = request.values.get('name')
    age = request.values.get('age')
    
    # result={
    #     'name':name,
    #     'age':age
    # }
    # return result
    
    age=int(age)
    if age>18:
        return f"Nice {name} you can use this site."
    else:
        return f"Sorry! {name} you are too young to use this site!"


if __name__ == "__main__":
    app.run(debug=True)