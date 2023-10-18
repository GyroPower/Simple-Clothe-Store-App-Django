function add_color()
{
    //this script adds a new color, opening a end point with a form to add it
    //after submit the form, the window close and the script calls a endpoint to 
    //retrieve a json response to give the data of the color and add an input for the color
    

    let new_window = open('/colors/add',"Add Color",'width=800,height=500');
    
    new_window.focus();

    const timer = setInterval(async()=>{
        if (new_window.closed){
            clearInterval(timer);
            let div = document.getElementById("list_colors");
            const response = await fetch("/color/get",{
                method:"GET",
            });
            
            const data = await response.json();
            
            let input = document.getElementById("colors_"+String(data.color_id));
            
            console.log(data.color_id)
            
            if (input == undefined){
                let list_add_color = document.createElement("li"); 
                list_add_color.classList.add("list-group-item",'bg-dark','text-light');

                let input_color = document.createElement("input");
                input_color.type="radio";
                input_color.name="color";
                input_color.id = "colors_"+String(data.color_id);
                input_color.value=String(data.color_id);
                input_color.classList.add("btn-check")


                let general_label = document.createElement('label');
                general_label.classList.add('stretched-link','btn',"text-light");
                general_label.htmlFor="colors_"+String(data.color_id);

                let color_name = document.createTextNode(" "+data.color_name)
                

                let span_color = document.createElement("span");
                span_color.style.display="inline-block";
                span_color.style.width="30px";
                span_color.style.height="30px";
                span_color.style.backgroundColor=String(data.color);
                span_color.style.marginRight="5px";
                span_color.style.border="1px solid black";
                span_color.style.borderColor="black";

    
                general_label.appendChild(span_color);
                general_label.appendChild(color_name);
                
                list_add_color.appendChild(input_color);
                list_add_color.appendChild(general_label)
                div.appendChild(list_add_color);

            }

        }
    });

}