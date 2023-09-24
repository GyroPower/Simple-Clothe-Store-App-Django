async function query_pagiator(page_number){

    const response = await fetch("/colors/"+page_number,{
        method:"GET",
    })

    const data = await response.json()

    let ul_colors = document.getElementById("list_colors")
    let color_list = []
    console.log(data.values,"V")

    for (let i = 0; i < data.page_objs.length; i++) {
        
        let check = (data.values.includes(String(data.page_objs[i].color_id))) ? 'checked' : '' 
        color_list.push('<li class="list-group-item text-light bg-dark">')
        color_list.push('   <input type="radio" name="colors" class="btn-check" id="colors_'+String(data.page_objs[i].color_id)+'" value="'+String(data.page_objs[i].color_id)+'" '+check+' >')
        color_list.push('   <label class="stretched-link btn text-light" for="colors_'+String(data.page_objs[i].color_id)+'" >')
        color_list.push('       <span style="display: inline-block; width: 30px; height: 30px; background-color: '+data.page_objs[i].color_hex+';  border: 1px solid black;"></span>')
        color_list.push('       '+data.page_objs[i].color_name+'')
        color_list.push('   </label>')
        color_list.push('</li>')
    }
    
    ul_colors.innerHTML = color_list.join("")
    

    let span = document.getElementById("paginator")

    
   
    let onclick_prev = ''
    if (data.page_number>1){
       onclick_prev = "query_pagiator("+String(data.page_number-1)+")"
    }


    let onclick_next = ''
    if (data.page_number<data.pages_number){
        onclick_next = 'query_pagiator('+String(data.page_number+1)+')'
    }

    let next_button=['<button type="button" class="btn btn-outline-dark" style="margin-left:5px;" onclick="'+onclick_next+'">></button>',]


    let previous_button=[
        '<button type="button" class="btn btn-outline-dark" onclick="'+onclick_prev+'"><</button>',
    ]

    let index_buttons = []

    for (let i = 1; i <= data.pages_number; i++) {
        
        if (data.page_number != i)
        {
            index_buttons.push('<button type="button" class="btn btn-outline-dark" style="margin-left:5px;" onclick="query_pagiator('+i+')">'+i+'</button>')
        }
        else{
            index_buttons.push('<button type="button" style="margin-left:5px;" class="btn btn-dark" >'+i+'</button>')
        }
    }

    
    index_buttons.unshift(previous_button)
    index_buttons.push(next_button)
    span.innerHTML = index_buttons.join("")

} 