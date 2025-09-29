from pyscript import document

def clear_output():
    document.getElementById("output").innerHTML = ""

def generate_message(event=None):
    clear_output()
    name = document.getElementById("name").value
    address = document.getElementById("address").value
    contnumb = document.getElementById("contnumb").value

    foods = document.getElementsByName("food")
    total = 0
    items = []
    for f in foods:
        if f.checked:
            total += float(f.value)
            label = f.nextSibling.textContent.strip()
            items.append(f"{label} (₱{float(f.value):.2f})")

    if not items:
        items_text = "No items selected"
    else:
        items_text = "<br>".join(items)

    message = f"""
    <p><b>Order for:</b> {name if name else '[Not Provided]'}</p>
    <p><b>Address:</b> {address if address else '[Not Provided]'}</p>
    <p><b>Contact number:</b> {contnumb if contnumb else '[Not Provided]'}</p>
    <p><b>Items:</b><br>{items_text}</p>
    <p><b>Total:</b> ₱ {total:.2f}</p>
    """
    document.getElementById("output").innerHTML = message