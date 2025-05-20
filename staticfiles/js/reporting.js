//Print to pdf
var specialElementHandlers = {
    '#editor': function (element, renderer) {
        return true;
    }
};

function exportTopdf(){
	var doc = new jsPDF()
	doc.fromHTML($('#content').html(), 15, 15, {
        'width': 170,
            'elementHandlers': specialElementHandlers
    });
    doc.save('sample-file.pdf');
	console.log("document saved as pdf");
}





//Data retrieving


//Chart creation