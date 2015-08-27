function mascaraCpf(campo){
	var cpf = campo.val();
	var mascara = '';
	for(var c = 0 ; c < cpf.length ; c++){
		if(c == 3 && cpf[3] !== '.' || c == 7 && cpf[7] !== '.')
			mascara += '.';
		else if(c == 11 && cpf[11] != '-')
			mascara += '-'
		mascara += cpf[c];
	}
	campo.val(mascara);
}

function removeMascaraCpf(cpf){
	var cpfLimpo = '';
	for(var c = 0 ; c < cpf.length ; c++){
		if(c !== 3 && c !== 7 && c !== 11)
			cpfLimpo += cpf[c];
	}
	return cpfLimpo;
}

function redirecionaPagina(endereco){
	window.location.assign("http://localhost:8000/" + endereco);
}