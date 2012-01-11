$(function() {
	$("#bt_base").button({
		icons: {
			primary: "ui-icon-search"
		},
		text: false
	})
	.css('height', 25)
	.click(function(){
		$("#base_select").attr('src','/base/compatriota/')
		$("#dialog-base").dialog( "open" );
		});
	$("#dialog-base").dialog({
						autoOpen: false,
						height: 600,
						width: 500,
						modal: true});
});

function closeDialog(){
	$("#dialog-base").dialog( "close" );
	$("#bt_base").attr('enabled',false)
}
