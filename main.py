from pyscript import document   # Imports the 'document' object (interface to HTML DOM in PyScript)

def clear_output():  
    document.getElementById("output").innerHTML = ""  
    # Clears the content of the <div id="output"> by setting its HTML string to empty
    # "output" is a DOM element, innerHTML is a string

def generate_message(event=None):  
    # event (default None) → passed automatically if button is clicked in browser
    clear_output()   # Calls the function above to reset output area

    name = document.getElementById("name").value  
    # name: str → input value from <input id="name">  

    address = document.getElementById("address").value  
    # address: str → input value from <input id="address">  

    contnumb = document.getElementById("contnumb").value  
    # contnumb: str → input value from <input id="contnumb">  

    foods = document.getElementsByName("food")  
    # foods: list-like object of DOM elements (<input type="checkbox" name="food">)  

    total = 0  
    # total: float (starting at 0, will store total price)  

    items = []  
    # items: list[str] → each selected food item string goes here  

    for f in foods:  
        # f: DOM element → each checkbox in "foods"  

        if f.checked:  
            # f.checked: bool → True if checkbox is ticked  

            total += float(f.value)  
            # f.value: str → converted to float and added to total  

            label = f.nextSibling.textContent.strip()  
            # label: str → gets the text next to the checkbox (e.g., "Classic Burger")  

            items.append(f"{label} (₱{float(f.value):.2f})")  
            # formatted string with item + price (2 decimals), appended to list  

    if not items:  
        items_text = "No items selected"  
        # items_text: str → fallback if no items chosen  
    else:  
        items_text = "<br>".join(items)  
        # items_text: str → joins list into one string separated by <br> (line breaks in HTML)  

    message = f"""  
    <p><b>Order for:</b> {name if name else '[Not Provided]'}</p>  
    <p><b>Address:</b> {address if address else '[Not Provided]'}</p>  
    <p><b>Contact number:</b> {contnumb if contnumb else '[Not Provided]'}</p>  
    <p><b>Items:</b><br>{items_text}</p>  
    <p><b>Total:</b> ₱ {total:.2f}</p>  
