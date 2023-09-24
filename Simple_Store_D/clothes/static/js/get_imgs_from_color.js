async function get_images_from_color(id,clothe_id){
    const response = await fetch('/get-imgs-from-colorImage/'+id+'/'+clothe_id,{
        method:"GET"
    })

    const data = await response.json()

    console.log(data.response);

    let div_imgs = document.getElementById('images')

    while(div_imgs.firstChild){
        div_imgs.removeChild(div_imgs.firstChild);
    }

    data.imgs_src.forEach(img => {

        let div_col = document.createElement('div');
        div_col.classList.add('col-6');

        let div_card_body = document.createElement('div');
        div_card_body.classList.add('card-body');

        let new_img = document.createElement('img');
        new_img.src = img;
        new_img.classList.add('card-img','my-2');
        new_img.style.border="1px solid black";

        div_col.appendChild(div_card_body);
        div_card_body.appendChild(new_img);

        div_imgs.appendChild(div_col);


    });

}