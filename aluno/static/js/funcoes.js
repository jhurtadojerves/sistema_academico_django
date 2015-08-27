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

function mascaraData(dataNasc){
	var mascara = '';
	for(var c = 0 ; c < dataNasc.length ; c++){
		if(c === 2 && dataNasc[2] !== '/' || c === 5 && dataNasc[5] !== '/')
			mascara += '/';
		mascara += dataNasc[c]
	}
	return mascara;
}

function mascaraAnoEntrada(anoEntrada){
	var mascara = '';
	for(var c = 0 ; c < anoEntrada.length ; c++){
		if(c === 4 && anoEntrada[4] !== '-')
			mascara += '-';
		mascara += anoEntrada[c];
	}
	return mascara;
}