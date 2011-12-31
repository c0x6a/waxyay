function getProvincias(id){
	var provincia = $("#id_ubigeo_now_1");
	provincia.find('option').remove();
	$.getJSON('/ubigeo/provincia/json/?r='+id, function(data){
		$.each(data, function(key,value){
			if(key == 0)
				getDistritos(value.pk);
			provincia.append("<option value='"+value.pk+"'>"+value.fields.name+"</option>");
			});
		});
}

function getDistritos(id){
	var distrito = $("#id_ubigeo_now_2");
	distrito.find('option').remove();
	$.getJSON('/ubigeo/distrito/json/?d='+id, function(data){
		$.each(data, function(key,value){
			distrito.append("<option value='"+value.fields.ubigeo+"'>"+value.fields.name+"</option>");
			});
		});
}
