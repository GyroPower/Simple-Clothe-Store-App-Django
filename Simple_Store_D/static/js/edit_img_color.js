async function edit_img_color(id,clothe_id=0,color_id){
    
    //This scripts open a new window to a form for updating a Colorimage instance

    let new_window = open('/color-image/update/'+id+'/'+clothe_id,'Edit images and color','width=1280,height=720');

    new_window.focus();

    const timer = setInterval(async()=>{
        if (new_window.closed){

            clearInterval(timer);

            let div_img = document.getElementById("images_"+id);

            //get the last updated ColorImage to put his data in a html document
            let response = await fetch('/color-image/last/update',{
                method:"GET"
            });

            let data = await response.json();

            //if there is not a problem we start editing the html document
            if (data.response=="v"){

                //If there is not conflict with other instance having the same color, this goes
                //and edit the info
                if (document.getElementById(data.color_id) != null && document.getElementById(id+"_"+data.color_id)==null){
                    set_warning_message_for_repeated_color('div_errors_'+id,'update');
                }


                //There is a div containig an id with the ColorImage id and the color id
                //This is a unique key that can't be repeated
                let div_ColorImageId_colorId = document.getElementById(id+"_"+color_id);
                div_ColorImageId_colorId.id=id+'_'+data.color_id;

                //remove all the preview of the images
                while(div_img.firstChild){
                    div_img.removeChild(div_img.firstChild);
                }
                
                //Put every image for the user to watch
                data.images_src.forEach(image => {
                    let col_img = document.createElement('div');
                    col_img.classList.add('col-4');
                    
                    let card_body_img = document.createElement('div');
    
                    card_body_img.classList.add('card-body');
    
                    let img = document.createElement('img');
                    img.classList.add('card-img');
                    img.src = image;
    
                    col_img.appendChild(card_body_img);
                    card_body_img.appendChild(img);
    
                    div_img.appendChild(col_img);
    
                });
    
                let div_color = document.getElementById("color_"+id);
                
                //remove the color
                while(div_color.firstChild){
                    div_color.removeChild(div_color.firstChild);
                }
    
                //Put it the 'new' color
                let col_color = document.createElement('div');
    
                col_color.classList.add('col');
    
                let span_color = document.createElement('span');
    
                console.log(data.color);
                span_color.style.width="30px";
                span_color.style.height="30px";
                span_color.id=data.color_id;
                span_color.style.display="inline-block";
                span_color.style.backgroundColor=data.color;
                span_color.style.border="1px solid black";
    
                let p = document.createElement('p');
                p.classList.add('text-light');
    
                p.appendChild(document.createTextNode(data.color_name))
    
                div_color.appendChild(col_color);
    
                col_color.appendChild(span_color);
                col_color.appendChild(p);
            }
        }
    })
}