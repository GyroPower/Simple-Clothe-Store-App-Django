function test_string(string)
{
    console.log(typeof string);
    console.log(string);
}

async function add_item_to_car_shop(id)
{
    let colors = document.getElementsByName('options-color');
    let color;
    let sizes = document.getElementsByName("options-size");
    let size;

    for (i=0;i<colors.length;i++)
    {
        if (colors[i].checked)
        {
            color = colors[i];
            break;
        }
    }

    for (i=0; i < sizes.length;i++)
    {
        if (sizes[i].checked)
        {
            size = sizes[i];
            break;
        }
    }
    
    
    const id_string = String(id)+"-"+String(color.value)+"-"+String(size.value); 

    
    
    const response = await fetch("/car-shop/add/"+id_string,{
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

        //Creating the container for the item info 
        const div_Item = document.createElement("div");

        div_Item.classList.add("card","bg-dark","text-light","my-2");
        div_Item.style.width = "23rem";
        div_Item.id = id_string;

        let item_body = document.createElement("div");

        item_body.classList.add("card-body");

        //Desc of the item
        let Item_desc = document.createTextNode("Item: "+data.desc);

        let para = document.createElement("p");

        para.appendChild(Item_desc);
        item_body.appendChild(para);
        
        
        //Units info text
        let item_units = document.createTextNode("Units: "+data.units);
        
        let para2 = document.createElement("p");
        para2.appendChild(item_units);
        para2.id = "U-"+data.clothe_id+"-"+data.color_id+"-"+data.size_id
        item_body.appendChild(para2);

        //Total
        let items_price = document.createTextNode("Total: "+data.price);
        let para3 = document.createElement('p');
        para3.appendChild(items_price);
        para3.id = "P-"+data.clothe_id+"-"+data.color_id+"-"+data.size_id;
        item_body.appendChild(para3);
        
        //Color
        let Item_color_text = document.createTextNode("Color:");
        let Color_para = document.createElement("p");
        Color_para.appendChild(Item_color_text);
        item_body.appendChild(Color_para);
        let Item_color = document.createElement('div');
        Item_color.style.height="30px";
        Item_color.style.width="30px";
        Item_color.style.borderRadius = "50%";
        Item_color.style.backgroundColor = data.color;

        item_body.appendChild(Item_color);

        //Minus button
        let button = document.createElement("button");
        button.type="button";
        button.classList.add("btn","btn-outline-dark","text-light");
        button.style.fontSize = "13px";
        button.setAttribute("onclick","increment_decrement("+data.clothe_id+"+'-'+"+data.color_id+"+'-'+"+data.size_id+",'low')");
        
        button.textContent = "-";

        item_body.appendChild(button);

        //Plus button
        button = document.createElement("button");
        button.type="button";
        button.classList.add("btn","btn-outline-dark","text-light");
        button.style.fontSize = "13px";
        console.log(data.clothe_id+"-"+data.color_id+"-"+data.size_id)
        button.setAttribute("onclick","increment_decrement("+data.clothe_id+"+'-'+"+data.color_id+"+'-'+"+data.size_id+",'add')");

        button.textContent = "+";

        item_body.appendChild(button);

        //Delete button
        button = document.createElement("button");
        button.type="button";
        button.classList.add("btn","btn-outline-warning","p-1","my-2");
        button.style.fontSize = "13px";
        button.setAttribute("onclick","delete_item("+data.clothe_id+"+'-'+"+data.color_id+"+'-'+"+data.size_id+")");
        button.textContent = "Delete Item"

        item_body.appendChild(button);
        
        
        
        div_Item.appendChild(item_body);

        col.appendChild(div_Item);

    
    }
    else{
        //if alredy exists just increment the units and the total for the Item
        document.getElementById("U-"+id_string).innerHTML ="Units";
        document.getElementById("U-"+id_string).innerHTML = "Units: "+data.units;
        document.getElementById("P-"+id_string).innerHTML="Total:";
        document.getElementById("P-"+id_string).innerHTML = "Total: "+data.price;
    }


}

