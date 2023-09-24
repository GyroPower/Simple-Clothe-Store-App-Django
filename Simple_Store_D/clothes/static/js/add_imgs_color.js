//There is gonna be some scripts with funtions that only send form data, or try to fetch 
//some urls with others method than GET, and be sure that the data was correctly precessed
//and it is a positive response

async function save_images_color(id,clothe_id){

    //This funtion calls a url and pass in a form data, the data for the creation of 
    //a ImagesColor instance or for updating 
    const images = document.getElementsByName("images");
    const color = document.querySelector('input[name="color"]:checked');


    const formData = new FormData();

    csfr_token = document.getElementsByName("csrfmiddlewaretoken");

    images.forEach(img => {
        console.log(img.value)
        formData.append('images',img.value);
        
    });

    
    formData.append('color',color.value);
    let response 

    console.log("ADD")

    if (id!='0'){
        //This is for updating a created ImageColor instance, the clothe id is for know
        //if it has a clothe parent instance, to see 
        response = await fetch("/color-image/update/"+id+"/"+clothe_id,{
            method:"POST",
            body: formData,
            headers: {"X-CSRFToken":csfr_token[0].value},
            credentials: 'same-origin'
        })
    }
    else{
        //This is for adding a new instance
        response = await fetch("/color-image/add",{
            method:"POST",
            body: formData,
            headers: {"X-CSRFToken":csfr_token[0].value},
            credentials: 'same-origin'
        })
    }

    const data = await response.json();

    if (data.response=="v"){
        close();
    } 

    //If there is an error, create a div error and put in the error
    let alert_div = document.createElement('div');
    alert_div.classList.add('alert','alert-danger','d-flex','align-items-center');

    alert_div.role="alert";
    alert_div.id = 'alert_div'

    alert_div.innerHTML=data.errors;

    let button_dismiss = document.createElement('button');

    button_dismiss.type="button";
    button_dismiss.classList.add('btn-close');
    button_dismiss.addEventListener('click',function(){
        alert_div.remove();
    })

    alert_div.appendChild(button_dismiss);

    let alert_div_father = document.getElementById('alert');

    alert_div_father.appendChild(alert_div);



}

