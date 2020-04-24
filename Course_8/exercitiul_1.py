import curs_7_ex_1
import curs_7_ex_2

from flask import Flask, request
app = Flask(__name__)
my_deck = None

@app.route('/')
def hello():
    return "hello"
    
@app.route('/exercitiul_1/<method_name>/<param>')
def ex1(method_name, param):
    global my_deck
    if method_name == "create_full_deck":
        my_deck = curs_7_ex_1.create_full_deck()
    if method_name == "add_card":
        try:
            my_deck.add_card(extract_card(param))
        except (curs_7_ex_1.DuplicateCardError, arg):
            print(arg)
    return str(my_deck.cards)
        
def extract_card(card_string):
    parts = card_string.split("_")
    value = parts[0]
    symbol = parts[1]
    if len(parts) == 3:
        symbol += " " + parts[2]
    return curs_7_ex_1.Card(value, symbol)
    
if __name__ == "__main__":
   app.run(debug = True, port=5000)