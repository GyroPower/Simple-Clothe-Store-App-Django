async function create_order()
{
    let items_div = document.getElementById("Items-car");

    if (items_div.hasChildNodes())
    {
        
        const response = await fetch("/car-shop/order",{
            method:"GET",
        });

        const data = await response.json();

        if (data.response =="V")
        {
            
            while(items_div.hasChildNodes())
            {
                items_div.removeChild(items_div.firstChild);
            }

            items_div.innerHTML = [
                '<div class="card bg-dark text-light" id="empty-items" style="width: 23rem;">',
                '   <div class="card-body">',
                '       <p class="card-text">Item: None</p>',
                '       <p class="card-text">Units: 0</p>',
                '</div>'
            ].join("")

            const aletPlaceholder = document.getElementById("success-car-shop");

        
            const wrapper = document.createElement("div")
            wrapper.innerHTML = [
                "<div class='alert alert-success alert-dismissible' role='alert'>",
                "   <div>Order made it without a problem</div>",
                "   <button type='button' class='btn-close' data-bs-dismiss='alert' aria-label='close'></button>",
                "</div>"
            ].join('')
        
            aletPlaceholder.append(wrapper)
        
        }
    }


}