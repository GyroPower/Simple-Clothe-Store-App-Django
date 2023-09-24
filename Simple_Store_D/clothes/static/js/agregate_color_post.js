async function agreagate_color(){
    const color_name = document.getElementById("color_name").value; 
    const color_hexa = document.getElementById("color_hexa").value;
    
    console.log(color_name);

    let data = new FormData();
    csfr_token = document.getElementsByName("csrfmiddlewaretoken")
    data.append('color_name',color_name);
    data.append('color_hexa',color_hexa);

    //This script is for add a new color and close the window with the form 

    let response = await fetch("/colors/add",{
        method:'POST',
        body: data,
        headers: {"X-CSRFToken":csfr_token[0].value},
        credentials: 'same-origin',
    });

    let data_res = await response.json();

    console.log(data_res.response);

    if (data_res.response=="V"){
        close();
    }

    
}