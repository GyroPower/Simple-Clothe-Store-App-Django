async function increment_decrement(id,action){
    console.log(typeof id)
    const response = await fetch("/car-shop/"+action+"/"+id,{
        method: "GET",
    });

    const data = await response.json();

    if (data.response=="V")
    {
        document.getElementById("U-"+id).innerHTML ="Units";
        document.getElementById("U-"+id).innerHTML = "Units: "+data.units;
        document.getElementById("P-"+id).innerHTML="Price";
        document.getElementById("P-"+id).innerHTML = "Price: "+data.price;
    }
    else
    {
        delete_item(id);
    }

}

