async function delete_img(id)
{   
    csfr_token = document.getElementsByName("csrfmiddlewaretoken")
    
    //This is for deleting an img, this if use a confirm to ensure the admin wanna delete it
    if (confirm('Do you wanna delete it?')){
        const response = await fetch('/image/delete/'+id,{
            method: "DELETE",
            headers: {"X-CSRFToken":csfr_token[0].value},
            credentials: 'same-origin'
        });
    
        const data = await response.json();
        
        //if there is not a problem, it removes the div containing the preview of the img
        if (data.response == "v"){
            const col_img = document.getElementById('col_'+data.id);
    
            while(col_img.firstChild){
                col_img.removeChild(col_img.firstChild);
            }
            col_img.remove();

        }
    }

    


}