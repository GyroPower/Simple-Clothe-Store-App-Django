async function clear_car()
{
    const empy_div = document.getElementById("empty-items");

    console.log("clear");
    if (empy_div==null)
    {
        console.log("V")
        const response = await fetch("/car-shop/clear",{
            method:"GET",
        });
    
        const data = await response.json();
    
        
        
        if (data.response ==="V")
        {

            let items_div = document.getElementById("Items-car");
    
            while(items_div.hasChildNodes())
            {
                items_div.removeChild(items_div.firstChild);
            }
        }
    }
    else {
        console.log("Nothing happend")
    }

}