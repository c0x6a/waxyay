$(function() {
	$("#bt_base").button({
		icons: {
			primary: "ui-icon-search"
		},
		text: false
	})
	.css('height', 25)
	.click(function(){
		$("#dialog-base").dialog( "open" );
		});
	$("#dialog-base").dialog({
						autoOpen: false,
						height: 600,
						width: 500,
						modal: true});
});
