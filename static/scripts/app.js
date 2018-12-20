$( function() {
    function split( val ) {
      return val.split( /,\s*/ );
    }
    function extractLast( term ) {
      return split( term ).pop();
    }
 
    $( "#hostname" )
      // don't navigate away from the field on tab when selecting an item
      .on( "keydown", function( event ) {
        if ( event.keyCode === $.ui.keyCode.TAB &&
            $( this ).autocomplete( "instance" ).menu.active ) {
          event.preventDefault();
        }
      })
      .autocomplete({
        source: function( request, response ) {
          $.getJSON( "/searchhost", {
            hostname: extractLast( request.term )
          }, response );
        },
        search: function() {
          // custom minLength
          var term = extractLast( this.value );
          if ( term.length < 4 ) {
            return false;
          }
        },
        focus: function() {
          // prevent value inserted on focus
          return false;
        },
        select: function( event, ui ) {
          var terms = split( this.value );
          // remove the current input
          terms.pop();
          // add the selected item
          terms.push( ui.item.value );
          // add placeholder to get the comma-and-space at the end
          terms.push( "" );
          this.value = terms.join( ", " );
          return false;
        }
      });

      

  
  

  //var doc = new jsPDF('p', 'pt', 'letter');
  /*var doc = new jsPDF('p', 'mm', 'a4');
  var specialElementHandlers = {
      '#editor': function (element, renderer) {
          return true;
      }
  };
  
  $('#pdfBtn').click(function () {
    //doc.canvas.height = 72 * 11;
      //      doc.canvas.width = 72 * 8.5;
      doc.fromHTML($('#hostinfoDiv').html(), 15, 15, {
          'width': 550,
              'elementHandlers': specialElementHandlers
      });
      doc.save('sample-file.pdf');
  });*/
  $('#csvBtn').click(function () {
    console.log("kkkkkk");
  
    $('#hostTable').csvExport({
      title:'HostTables'
    });

/*  let options = {
    "separator": ",",
    "newline": "\n",
    "quoteFields": true,
    "excludeColumns": "",
    "excludeRows": "",
    "trimContent": true,
    "filename": "table.csv"
  }
  
  $('#example').table2csv('download', options);*/
});
});
  