async function delete_item(id)
{
    console.log("IN")
    const response = await fetch("/car-shop/del/"+id,{
        method:"GET",
    });

    const data = await response.json();

    let div = document.getElementById(id);
    
    while (div.hasChildNodes()){
        div.removeChild(div.firstChild);
    }

    div.remove();
}