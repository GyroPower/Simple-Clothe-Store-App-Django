async function update_img(id){
    
    //This is for call the window for updating an image instance
    let new_update_window = open('/images/update/'+id,'Update image','width=800,height=500');

    new_update_window.focus();

    const timer = setInterval(async()=>{
        if (new_update_window.closed){
            clearInterval(timer);

            //Once the update happens, it get the last image updated or added, in this case 
            //is a updated one
            const response = await fetch("/get-list-img",{
                method:"GET",
            });

            const data = await response.json();

            //If there is not a problem, it change the src for the preview
            if (data.response=="v"){

                let img = document.getElementById(id);
    
                img.src = data.path
            }

        }
    })

}