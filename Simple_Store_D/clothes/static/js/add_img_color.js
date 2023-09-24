async function add_img_color(){

    //This scripts opens a window for addig a ImagesColor instance and adding an input of
    //the instance for the clothe instance to create 

    let new_window = open('/color-image/add','Add images-colors','width=1280,height=720');

    new_window.focus();

    const timer = setInterval(async()=>{
        if (new_window.closed){
            clearInterval(timer);
            const response = await fetch('/color-image/last/add',{
                method:"GET"
            })

            const data = await response.json();

            if (data.response=="v"){
                console.log("See what it gives if not exists an element:",document.getElementById(data.color_id))
                
                // If a ImageColor instance already have the color we are adding, it will send
                // an error message, it would not be logic that the same color is reapeated for
                // a clothe, and it will delete the ImageColor instance 
    
                if (document.getElementById(data.color_id) != null){
                    set_warning_message_for_repeated_color('div_add');
                }
                else{

                    let div_containig_images_color = document.getElementById('images_color');
    
                    let div_image_color_new = document.createElement('div');
        
                    div_image_color_new.id = String(data.id);
        
                    let input_images_color = document.createElement('input');
                    input_images_color.type="checkbox";
                    input_images_color.value=data.id;
                    input_images_color.checked=true;
                    input_images_color.hidden=true;
                    input_images_color.name = 'ColorImages';
                    
        
                    div_image_color_new.appendChild(input_images_color);
        
        
                    let div_row_images = document.createElement('div');
                    div_row_images.classList.add('row');
                    div_row_images.id = "images_"+String(data.id);
        
                    data.images_src.forEach(image => {
        
                        let col_card = document.createElement('div')
                        col_card.classList.add('col-4')
        
                        let col_card_body = document.createElement('div');
                        col_card_body.classList.add('card-body');
        
                        let img = document.createElement('img');
                        img.classList.add('card-img');
                        img.src = image;
        
                        col_card_body.appendChild(img);
                        col_card.appendChild(col_card_body);
                        div_row_images.appendChild(col_card);
                    });
                    div_image_color_new.appendChild(div_row_images);
        
        
                    let div_color_row = document.createElement('div');
                    div_color_row.classList.add('row');
        
                    let div_col_color = document.createElement('div');
                    div_col_color.classList.add('col');
                    div_col_color.classList.add('text-light');
        
                    let span_color = document.createElement('span');
                    span_color.style.width="30px";
                    span_color.style.height="30px";
                    span_color.style.display="inline-block";
                    span_color.style.backgroundColor=data.color;
                    span_color.style.border="1px solid black";
                    span_color.id = data.color_id
        
                    let color_text = document.createTextNode(' '+data.color_name);
                    
                    div_col_color.appendChild(span_color);
                    div_col_color.appendChild(color_text);
        
                    div_color_row.appendChild(div_col_color);
        
                    div_image_color_new.appendChild(div_color_row);
        
                    div_containig_images_color.appendChild(div_image_color_new)
        
                    //Row for the button edit and delete
                    let div_buttons_edit_delete_row = document.createElement('div');
                    div_buttons_edit_delete_row.classList.add('row',"my-2");
        
                    let div_col_edit = document.createElement('div');
                    div_col_edit.classList.add('col');
                    
                    let button_edit = document.createElement('button');
                    button_edit.type="button";
                    button_edit.classList.add('btn','btn-dark');
                    button_edit.appendChild(document.createTextNode('Edit'));
                    
                    button_edit.addEventListener('click',function(){
                        edit_img_color(data.id);
                    })
        
        
                    div_col_edit.appendChild(button_edit);
        
                    div_buttons_edit_delete_row.appendChild(div_col_edit)
        
        
                    let div_col_delete = document.createElement('div');
                    div_col_delete.classList.add('col');
        
                    let button_delete = document.createElement('button');
                    button_delete.type="button";
                    
                    button_delete.classList.add('btn','btn-dark')
                    button_delete.appendChild(document.createTextNode('Delete'));
                    button_delete.addEventListener('click',function(){
                        // This creates a modal of confirmation, to confirm if the admin
                        // wants to delete the instance if it is created
                        let div_modal = document.createElement('div');
                        div_modal.classList.add('modal','fade');
        
                        let div_modal_dialog = document.createElement('div');
                        div_modal_dialog.classList.add('modal-dialog');
        
                        div_modal.appendChild(div_modal_dialog);
        
                        let div_modal_content = document.createElement('div');
                        div_modal_content.classList.add('modal-content');
        
                        div_modal_dialog.appendChild(div_modal_content);
        
                        let div_modal_header = document.createElement('div');
                        div_modal_header.classList.add('modal-header');
        
                        div_modal_content.appendChild(div_modal_header);
        
                        let h1 = document.createElement('h1'); 
                        h1.classList.add('modal-title','fs-5');
        
                        div_modal_header.appendChild(h1);
        
                        h1.appendChild(document.createTextNode('Are you sure?'));
        
                        let div_modal_body = document.createElement('div');
                        div_modal_body.classList.add('modal-body');
                        div_modal_content.appendChild(div_modal_body);
        
                        let p = document.createElement('p');
        
                        p.appendChild(document.createTextNode('If you delete it, you will not able to recover the data'));
        
                        div_modal_body.appendChild(p);
        
                        let div_modal_footer = document.createElement('div');
                        div_modal_footer.classList.add('modal-footer');
                        div_modal_content.appendChild(div_modal_footer)
        
                        let close_button = document.createElement('button');
                        close_button.type="button";
                        close_button.classList.add('btn','btn-dark');
                        close_button.addEventListener('click',()=>{
                            div_modal.remove();
                        });
        
                        div_modal_footer.appendChild(close_button);
        
                        let delete_button = document.createElement('button');
                        delete_button.type="button";
                        delete_button.classList.add('btn',"btn-dark");
                        delete_button.addEventListener('click',async()=>{
                            delete_img_color(data.id);
                        })
                        console.log("Button")
                    });
        
                    div_col_delete.appendChild(button_delete);
        
                    div_buttons_edit_delete_row.appendChild(div_col_delete);
        
                    div_image_color_new.appendChild(div_buttons_edit_delete_row);
                }
            }

        }
    })

}


async function set_warning_message_for_repeated_color(id,type_str="add"){
    //This funtion is used for a recent added ImageColor or for an update, if it is 
    // added, it's going to delete the instance, if it is updated and it is a conflict
    // of repeated color, it just going to display a message warning 
    
    let div_for_error_message = document.getElementById(id);
    
    let div_warning_message = document.createElement('div');
    div_warning_message.classList.add('alert','alert-warning','alert-dismissible','fade','show')
    div_warning_message.role="alert";

    
    div_warning_message.appendChild(document.createTextNode('The color is alredy added for the clothe'));

    let button_close = document.createElement('button');

    button_close.type='button';
    button_close.classList.add('btn-close');

    button_close.addEventListener('click',function(){
        div_warning_message.remove();
    });

    div_warning_message.appendChild(button_close);

    
    div_for_error_message.appendChild(div_warning_message);

    //If it is add action it's going to be deleted the instance
    if (type_str=="add"){

        csfr_token = document.getElementsByName("csrfmiddlewaretoken")
    
        const response = await fetch('/delete-img-color/'+id,{
            method:"DELETE",
            headers: {"X-CSRFToken":csfr_token[0].value},
            credentials: 'same-origin'
        })
    } 

    const data = await response.json();

    console.log(data.response)
}