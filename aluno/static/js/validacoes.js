$('#cpf').on('keyup' , function(){
	mascaraCpf($('#cpf'));
});

$('#form-cadastro-aluno').on('submit' , function(){
	var cpf = $('#cpf').val();
	$('#cpf').val(removeMascaraCpf(cpf));
});

$('#cadastrar-aluno').on('click' , function(){
	redirecionaPagina('aluno/cadastro');
});

$('#dataNasc').on('keyup' , function(){
	var dataNasc = $('#dataNasc').val();
	$('#dataNasc').val(mascaraData(dataNasc));
});

$('#anoEntrada').on('keyup' , function(){
	var anoEntrada = $('#anoEntrada').val();
	$('#anoEntrada').val(mascaraAnoEntrada(anoEntrada));
});

$('.escurece-pagina').on('click' , function(){
	$('.escurece-pagina').fadeOut(200);
	$('.div-erro').fadeOut(200);
});

$('#listar-aluno').on('click' , function(){
	redirecionaPagina('aluno/lista');
});

$('.linha').on('dblclick' , function(){
	var linha = $(this)
	var id = linha.find('.id_aluno').text();
	redirecionaPagina('aluno/editar/' + id);
});

$('#remover-aluno').on('click' , function(event){
	event.preventDefault();
	var id_aluno = $('#idAluno').val();
	redirecionaPagina('aluno/remover/' + id_aluno);
});