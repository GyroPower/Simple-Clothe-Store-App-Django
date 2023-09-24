async function add_or_update_image(id=""){
    
    
    file = input.files[0];
    
    //This is for update a image or add an image, if the function recieve an id 
    // id for update an image

    const formData = new FormData();
    formData.append("image_for",file);

    csfr_token = document.getElementsByName("csrfmiddlewaretoken")
    
    let response

    if (id==""){
        
        response = await fetch('/images/add',{
            method: 'POST',
            body: formData,
            headers: {"X-CSRFToken":csfr_token[0].value},
            credentials: 'same-origin',
        });
        
    }
    else{

        
        response = await fetch('/images/update/'+id,{
            method: 'POST',
            body: formData,
            headers: {"X-CSRFToken":csfr_token[0].value},
            credentials: 'same-origin',
        })
    }


    
    let data = await response.json();


    if (data.response == "v")
    {
        console.log("V Close");
        close();
    }

    
}


function preview_image(){
    //This is for preview the image to add or update
    while(preview.firstChild){
        preview.removeChild(preview.firstChild);
    }

    file = input.files[0];

    const image = document.createElement('img');
    image.src = URL.createObjectURL(file);
    image.classList.add("card-img")
    image.style.height="300px";
    preview.appendChild(image);
    
}

//Get the input and the div for preview the image
const input = document.getElementById("image_for");
console.log(input)
const preview = document.getElementById("img_for_clothe");


input.addEventListener("change",preview_image);