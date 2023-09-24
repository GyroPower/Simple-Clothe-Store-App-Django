async function add_img(){
    let new_window = open('/images/add',"Add Image",'width=800,height=500');
    
    //This opens a window for the adding of an img and then create an input and display
    // the img and create buttons for actions to do with that img

    new_window.focus();

    const timer = setInterval(async()=>{
        if (new_window.closed){
            clearInterval(timer);

            const response = await fetch("/get-list-img",{
                method:"GET"
            })
            
            const data = await response.json()

            if (data.response == "v"){

                
                let new_input_hidden = document.createElement('input');
                new_input_hidden.type='checkbox';
                new_input_hidden.name='images';
                new_input_hidden.hidden=true;
                new_input_hidden.checked = true;
                new_input_hidden.value = data.id;
    
                let div_img_parent = document.getElementById("image_for_clothe");
                
                
                let col_img = document.createElement("div");
                col_img.classList.add("col-6");
                col_img.id="col_"+String(data.id);
                
                let card_img = document.createElement('div');
                card_img.classList.add("card-body","my-2");
    
    
                div_img_parent.appendChild(new_input_hidden);
                
                const img = document.createElement("img");
                img.src = data.path;
                img.classList.add("card-img");
                img.style.height="20rem";
                img.id=String(data.id)
    
                let button_delete = document.createElement('button');
                button_delete.type="button";
    
                let delete_text = document.createTextNode('Delete');
    
                button_delete.classList.add("btn",'btn-dark');
                
                
                button_delete.appendChild(delete_text);
                button_delete.addEventListener('click',function(){
                    delete_img(data.id);
                })
    
                let update_button = document.createElement('button');
                update_button.type="button";
                update_button.classList.add('btn','btn-dark');

                update_button.addEventListener('click',function(){
                    update_img(data.id);
                })
                update_button.appendChild(document.createTextNode('Update'));
                update_button.style.marginLeft="5px";

                card_img.appendChild(img);
                card_img.appendChild(button_delete);
                card_img.appendChild(update_button);
                col_img.appendChild(card_img);
    
                div_img_parent.appendChild(col_img);
    
            }
        }
    })

    
}