from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Create a list to store shopping items
shopping_list = []

# Route to display the shopping list
@app.route('/')
def show_list():
    return render_template('index.html', items=shopping_list)

# Route to add items to the shopping list
@app.route('/add', methods=['POST'])
def add_item():
    item = request.form['item'].strip()  # Remove leading/trailing whitespace
    if item:  # Check if item is not empty
        shopping_list.append(item)
    return redirect(url_for('show_list'))

# Route to remove items from the shopping list
@app.route('/delete/<int:item_id>', methods=['GET'])
def delete_item(item_id):
    if 0 <= item_id < len(shopping_list):
        del shopping_list[item_id]
    else:
        return "Item does not exist"  # Error handling for invalid item index
    return redirect(url_for('show_list'))

if __name__ == '__main__':
    app.run(debug=True)

