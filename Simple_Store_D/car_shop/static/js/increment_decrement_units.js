function increment_decrement(id,action){
    fetch("/car-shop/"+action+"/"+id,{
        method: "GET",
    })
    .then(response=>response.json())
    .then(document.getElementById("U-"+id).innerHTML= "Units")
    .then(data => document.getElementById("U-"+id).innerHTML = "Units: "+data.units)
    .then(document.getElementById("P-"+id).innerHTML="Price")
    .then(data => document.getElementById("P-"+id).innerHTML = "Price: "+data.price)
}

