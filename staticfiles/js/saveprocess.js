
//send data to the database
$(document).on('click','#saveProcess',function(e){
	e.preventDefault();
	//List down anchors and connections and jsonifiy the data
	var processo=[];
	$(".machine").each(function(){
		processo+=$(this).get(0).outerHTML;
	})

	var nodes = []
    $(".machine").each(function (idx, elem) {
    	var $elem = $(elem);
        var endpoints = jsPlumb.getEndpoints($elem.attr('id'));
        /*console.log('endpoints of '+$elem.attr('id'));
        console.log(endpoints);*/
        nodes.push({
          	blockId: $elem.attr('id'),
            nodetype: $elem.attr('data-nodetype'),
            positionX: parseInt($elem.css("left"), 10),
            positionY: parseInt($elem.css("top"), 10)
        });
    });


	var connections=[];
	$.each(jsPlumb.getConnections(),function(idx,connection){
	connections.push({
		connectionId: connection.id,
		pageSourceId:connection.sourceId,
		pageTargetId:connection.targetId,
		anchors: $.map(connection.endpoints, function(endpoint) {
	        return [[endpoint.anchor.x, 
    	    endpoint.anchor.y, 
        	endpoint.anchor.getOrientation()[0], 
        	endpoint.anchor.getOrientation()[1],
        	endpoint.anchor.offsets[0],
        	endpoint.anchor.offsets[1]]];
     	 })
		})
	});

	var connections=JSON.stringify(connections);
	/*console.log(connections);*/
	var nodes=JSON.stringify(nodes);
    /*console.log(nodes);*/
    
	//Send data to DB
	$.ajax({
		type:'POST',
		url:'/map/saveprocess/',
		dataType: 'html',
		data:{
			process:processo,
			nodes:nodes,
			connections:connections,
			csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
		},
		success:function(){
			var $el = $('body'),
    		x = 500,
    		originalColor = $el.css("background");
			$el.css("background", "#ccffcc");
			setTimeout(function(){
  			$el.css("background", originalColor);
			}, x);

		}
	})
})
