//Date picker
$('.date').datepicker({dateFormat:'yy-mm-dd'});
i=1;

document.getElementById('addSpare').addEventListener('click',function(){
	var value=document.getElementById('spare').value
		if (value) addSpare(value);
		document.getElementById('spare').value=''; //Once machine created we empty the item field

});

spare_list=[];
function addSpare(item){
	spare_list.push(item);
	console.log(spare_list);
	var textarea = document.getElementById("sparelist");
	textarea.value=spare_list.join("\n");

}

function deleteSpare(){
	$(this).closest("tr").remove();
}