async function delete_img_color(id){

    csfr_token = document.getElementsByName("csrfmiddlewaretoken")
    
    //This is for delete an Colorimage, is there is an error it raise an div containing an error
    //message
    
    const response = await fetch('/color-image/update/'+id,{
        method: "DELETE",
        headers: {"X-CSRFToken":csfr_token[0].value},
        credentials: 'same-origin'

    });

    const data = await response.json();

    if (data.response == "v"){
        let div_contain_image_color = document.getElementById(id);
    
        div_contain_image_color.remove();
        return 
    }
    else{
        let div_errors = document.createElement('div');

        div_errors.classList.add('alert','alert-danger','alert-dismissible','fade','show');

        div_errors.role="alert";

        div_errors.appendChild(data.errors);

        let button_dismiss = document.createElement('button');
        button_dismiss.type="button";
        button_dismiss.classList.add('btn','btn-close');

        div_errors.appendChild(button_dismiss);

        button_dismiss.addEventListener('click',function(){
            div_errors.remove();
        })
    }

}