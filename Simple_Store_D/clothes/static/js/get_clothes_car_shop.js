async function add_item_to_car_shop(id)
{
    const response = await fetch("/car-shop/add/"+id,{
        method:"GET",
    });

    const data = await response.json();
    
    let empy_div = document.getElementById("empty-items");


    if (empy_div!=null)
    {
        while(empy_div.hasChildNodes())
        {
            empy_div.removeChild(empy_div.firstChild);
        }
    }

    id = String(id);



    if (data.units == 1)
    {
        const col = document.getElementById("Items-car")

        const div_Item = document.createElement("div");

        div_Item.classList.add("card","bg-dark","text-light","my-2");
        div_Item.style.width = "23rem";
        div_Item.id = data.clothe_id

        let item_body = document.createElement("div");

        item_body.classList.add("card-body");

        let Item_desc = document.createTextNode("Item: "+data.desc);

        let para = document.createElement("p");

        para.appendChild(Item_desc);
        item_body.appendChild(para);

        let item_units = document.createTextNode("Units: "+data.units);
        
        let para2 = document.createElement("p");
        para2.appendChild(item_units);
        para2.id = "U-"+data.clothe_id
        item_body.appendChild(para2);

        let items_price = document.createTextNode("Price: "+data.price);
        let para3 = document.createElement('p');
        para3.appendChild(items_price);
        para3.id = "P-"+data.clothe_id;
        item_body.appendChild(para3);
        

        let button = document.createElement("button");
        button.type="button";
        button.classList.add("btn","btn-outline-dark","text-light");
        button.style.fontSize = "13px";
        button.setAttribute("onclick","increment_decrement("+data.clothe_id+",'low')");
        
        button.textContent = "-";

        item_body.appendChild(button);

        button = document.createElement("button");
        button.type="button";
        button.classList.add("btn","btn-outline-dark","text-light");
        button.style.fontSize = "13px";
        button.setAttribute("onclick","increment_decrement("+data.clothe_id+",'add')");

        button.textContent = "+";

        item_body.appendChild(button);

        button = document.createElement("button");
        button.type="button";
        button.classList.add("btn","btn-outline-warning","p-1","my-2");
        button.style.fontSize = "13px";
        button.setAttribute("onclick","delete_item("+data.clothe_id+")");
        button.textContent = "Delete Item"

        item_body.appendChild(button);

        div_Item.appendChild(item_body);

        col.appendChild(div_Item);

    }
    else{
        document.getElementById("U-"+id).innerHTML ="Units";
        document.getElementById("U-"+id).innerHTML = "Units: "+data.units;
        document.getElementById("P-"+id).innerHTML="Price";
        document.getElementById("P-"+id).innerHTML = "Price: "+data.price;
    }


}