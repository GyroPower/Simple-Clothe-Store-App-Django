async function increment_decrement(id,action){

    const response = await fetch("/car-shop/"+action+"/"+id,{
        method: "GET",
    });

    const data = await response.json();

    document.getElementById("U-"+id).innerHTML ="Units";
    document.getElementById("U-"+id).innerHTML = "Units: "+data.units;
    document.getElementById("P-"+id).innerHTML="Price";
    document.getElementById("P-"+id).innerHTML = "Price: "+data.price;
}

