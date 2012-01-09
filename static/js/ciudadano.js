function getCiudadano(dni){
	$.getJSON('/ciudadano/'+dni+'/json/', function(data){
		$.each(data, function(key, value){
			$("#id_citizen").val(value.pk);
			$("#id_number_document").val(value.pk);
			$("#id_number_book").val(value.fields.number_book);
			$("#id_paternal_surname").val(value.fields.paternal_surname);
			$("#id_mother_surname").val(value.fields.mother_surname);
			$("#id_name").val(value.fields.name);
			nacimiento = value.fields.birth_date.split("-");
			$("#id_birth_date_day").val(nacimiento[2]);
			$("#id_birth_date_month").val(Number(nacimiento[1]));
			$("#id_birth_date_year").val(nacimiento[0]);
			$("#id_ubigeo_0").val(value.fields.region_code+'0000');
			getProvincias(value.fields.region_code+'0000', value.fields.region_code+value.fields.province_code+'00',value.fields.region_code+value.fields.province_code+value.fields.district_code);
			if(value.fields.sex == 1)
				$("#id_sex_0").attr('checked','checked');
			else
				$("#id_sex_1");
			$("#id_degree_instruction").val(value.fields.degree_instruction);
			});
		});
}
