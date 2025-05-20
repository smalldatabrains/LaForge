//variables
i=$('.machine').length;
console.log(i);
var common={
	isSource:true,
	isTarget:true,
	maxConnections: -1
}

//JsPlumb Properties
jsPlumb.setContainer(document.getElementById("diagramContainer"));
jsPlumb.draggable($('.machine'));


var informationForm=`
<form class="information">
	<li class="info">Supplier</li>
	<li class="info">Installation date</li>
	<li class="info">History</li>
	<li class="info">Spare parts</li>
	<li class="info">Last maintenance</li>
</form>

`

//Add Machine function
function addMachine(item){
	$('#diagramContainer').append(
	'<ul class="machine" id="'+item+'" style="position:absolute; top: 150px; left: 90px;">'
	+'<div class="machinetitle">'+item+'</div>'
	+'<img src="/static/images/default.jpg" id="image'+i+'" class="image-machine" align="right">'
	+'<div id="model'+i+'"><div class="subtitle">Model</div></div>'
	+'<div class="subtitle">Status <form><input type="radio" name="status" value="Ok" checked>OK <input type="radio" name="status" value="Nok">NOK</form></div>'
	+'<button class="addinformation" type="button" onclick="toggleInformation()">Informations</button>'
	+ informationForm
	+'<button class="addMaintenance" type="button" onclick="toggleMaintenance()">Add maintenance</button>'
    +'<form id="addmaintenanceform" class="maintenance">'
	+'<input type="date" id="datestart'+i+'" class="date" placeholder="Start date">'
	+'<input type="date" id="dateend'+i+'" class="date" placeholder="End date">'
	+'<input type="text" id="name" placeholder="machine">'
	+'<input type="text" id="technician" placeholder="Technician">'
	+'<input type="text" id="spare" placeholder="Spare part">'
	+'<textarea id="detail" placeholder="Intervention details"></textarea>'
	+'<button type="submit" class="post-form" id="saveMaintenance">Save</button>'
	+'</form>'
    +'<button id="removeMachine" type="button" onclick="removeTheMachine()">Remove</button>'
	+'</ul>');
	var model=document.getElementById('model'+i);
	var selectList=document.createElement('select');
	model.appendChild(selectList);
	for (var j = 0; j < categoryList.length; j++) {
    var option = document.createElement("option");
    option.value = categoryList[j];
    option.text = categoryList[j];
    selectList.appendChild(option);
	};
	$('select').on('change', function() {
  	var selected=$(this).val();
  	selected= selected.replace(/\s/g, '');
  	console.log(selected);
  	var item=$(":focus").parent().parent().find('img').attr('id');
  	console.log(item);
  	document.getElementById(item).src = "../media/"+selected+".jpg"
	})
    $('.date').datepicker({dateFormat:'yy-mm-dd'});
    $('.machine').draggable({grid:[30,30],cursor:'pointer',opacity:0.6});
	jsPlumb.addEndpoint($('#'+item),{anchors:["Right"]},common);
	jsPlumb.addEndpoint($('#'+item),{anchors:["Left"]},common);
	jsPlumb.draggable($('#'+item));
	i++;
	console.log(i);
};

//Remove machine and connectins to this machine
function removeTheMachine(){
	$(":focus").each(function() {
		jsPlumb.deleteConnectionsForElement($(this).parent());
		jsPlumb.removeAllEndpoints($(this).parent());
		$(this).parent().remove();
	});
}

//Edit machine
function toggleMaintenance(){

    $(":focus").parent().each(function(){
        $(this).find('.maintenance').toggle();
    });


}

//Toggle Information
function toggleInformation(){
    $(":focus").parent().each(function(){
        $(this).find('.information').toggle();
    });

}

//Date picker for time sliding
$('.date').datepicker({dateFormat:'yy-mm-dd'});

//Event listener on Add Button
document.getElementById('addMachine').addEventListener('click',function(){
    var value=document.getElementById('item').value
        if (value) addMachine(value);
        document.getElementById('item').value=''; //Once machine created we empty the item field

});

