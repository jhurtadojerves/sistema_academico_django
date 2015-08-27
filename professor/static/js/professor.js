$('#cpf').on('keyup' , function(){
	mascaraCpf($('#cpf'));
});


$('#form-cadastro-professor').on('submit' , function(){
	var cpf = $('#cpf').val();
	$('#cpf').val(removeMascaraCpf(cpf));
});

$('#lista-professor').on('click' , function(){
	redirecionaPagina('professor');
});

$('#cadastra-professor').on('click' , function(){
	redirecionaPagina('professor/cadastro');
});

$('#form-edita').on('submit' , function(event){
	var cpf = $('#cpf').val();
	$('#cpf').val(removeMascaraCpf(cpf));
});

$('.linha').on('dblclick' , function(){
	var id = $(this).find('.id-professor').text()
	redirecionaPagina('professor/edita/' + id);
});

$('#btn-remover-professor').on('click' , function(event){
	event.preventDefault();
	var id = $('#id-professor').val();
	redirecionaPagina('professor/remove/' + id);
});