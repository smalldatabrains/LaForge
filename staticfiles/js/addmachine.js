$(document).on('submit','#addmachineform',function(e){
	e.preventDefault();
	var data=new FormData();
	data.append('picture',$('input[type=file]')[0].files[0])
	data.append('spare_list[]',JSON.stringify(spare_list));
	data.append('supplier',$('#id_supplier').val());
	data.append('category',$('#id_category').val());
	data.append('csrfmiddlewaretoken',$('input[name=csrfmiddlewaretoken]').val())
	$.ajax({
		type:'POST',
		url:'/map/addmachine/',
		enctype:'multipart/form-data',
		data:data,
		processData:false,
		contentType:false,
		success:function(data){
			console.log(data)
			alert("Machine added")
			document.getElementById("addmachineform").reset();

		}
	})
})

