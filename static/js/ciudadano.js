var number_document;
var number_book;
var paternal_surname;
var mother_surname;
var name;
var birth_date;
var sex;
var degree_instruction;
//var region_code;
//province_code
//district_code

function getCiudadano(dni){
	$.getJSON('/ciudadano/'+dni+'/json/', function(data){
		if(data.length > 0){
				number_document = $("#id_number_document").val(data[0].fields.).attr('',);
				number_book = $("#id_number_book");
				paternal_surname = $("#id_paternal_surname");
				mother_surname = $("#id_mother_surname");
				name = $("#id_name");
				birth_date = $("#id_birth_date");
				sex = $("#id_sex");
				degree_instruction = $("#id_degree_instruction");
			}
		});
}
