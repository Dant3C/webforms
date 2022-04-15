from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)
@app.route("/answer", methods=['GET', 'POST'])
def render_answer():
    bill = (float(request.args['text1']))/100
    real_val = request.args['rad1']
    tip_prsnt = "0"
    plus_tip = 0.0
    if real_val == "radio1":
        plus_tip = bill * 1.15
        tip_prsnt = "15%"
    elif real_val == "radio2":
        plus_tip = bill * 1.20
        tip_prsnt = "20%"
    else: 
        plus_tip = bill * 1.25
        tip_prsnt = "25%"
    
    tip = plus_tip - bill
    ans1 = "Total: " + str(bill) + " x " + tip_prsnt + " = " + str(plus_tip)
    ans2 = "tip: " + str(tip)
    return render_template('answer.html', answer1 = ans1, answer2 = ans2)
    
@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/p1")
def render_page1():
    food_type = []
    r_string = ""
    r_list = []
    all_rest_list = []
    try:
        fast = request.args['fast_food']
        if fast == "yes":
            all_rest_list = ["lilys tacos", "taqueria el buen gusto", "la Super-Rica", "in n out", "habit", "kyle's kitchen", "california pasta" ]
        elif fast == "no":
            all_rest_list = ["los agaves", "flor de maiz", "los Arroyos", "eurika", "kyles kitchen", "Mesa Burger", "The Shop"]
        else:
            all_rest_list = ["nothing","nothing","nothing","nothing","nothing","nothing"]
        
    except:
        print("gdh")
    try:
        food_type.append(request.args['foodtype1'])
    except:
        print(food_type)
    try: 
        food_type.append(request.args['foodtype2'])
    except:
        print(food_type)
    try: 
        food_type.append(request.args['foodtype3'])
    except:
        print(food_type)

    print (food_type)
    
    # 0-2 is mexican // 3-5 is buger // 6-10 is other 
    for x in range(0, len(food_type)):
        if food_type[x] == "mexican":
            r_list.append(all_rest_list[0])
            r_list.append(all_rest_list[1])
            r_list.append(all_rest_list[2])
            print (r_list)
            if food_type[x] == "burger":
                r_list.append(all_rest_list[3])#buger
                r_list.append(all_rest_list[4])#buger
                r_list.append(all_rest_list[5])#buger
                if food_type[x] == "seafood":
                    r_list.append(all_rest_list[6]) ## diffrent foods
                else:
                    pass
            else:
                if food_type[x] == "seafood":
                    r_list.append(all_rest_list[6]) ## other foes
                else:
                    pass
        else:
            if food_type[x] == "burger":
                r_list.append(all_rest_list[3])#buger
                r_list.append(all_rest_list[4])#buger
                r_list.append(all_rest_list[5])#buger
                if food_type[x] == "seafood":
                    r_list.append(all_rest_list[6]) ## foods
            else:
                if food_type[x] == "seafood":
                    r_list.append(all_rest_list[6]) #other foes
                else:
                    r_list.append("nothing, i cant give you a recommendation if you don't give me information")
            
    for x in r_list:
        r_string = r_string + x + ", "
    print (r_string)
    return render_template('page1.html', restaurants = r_string)

@app.route("/p2")
def render_page2():
    return render_template('page2.html')
    
if __name__=="__main__":
    app.run(debug=True)
