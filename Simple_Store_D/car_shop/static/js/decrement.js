function decrement(id){
    fetch("/car-shop/low/"+id,{
        method: "GET",
    })
    .then(response => response.json())
    .then(docuement.getElementById("U-"+id).innerHTML = "Units")
    .then(data => document.getElementById("U-"+id).innerHTML = "Units: "+data.units)
}