$('#buscar').keyup(function(e){
consulta = $("#buscar").val().trim();
$.ajax({
    data: {'consulta': consulta},
    url: '/lista/',
    type: 'get',
    success : function(data) {
        $("#resultados").empty();
        for (i=0;i<data.length;i++){
            $("#resultados").append("<p>" + data[i].first_name + "</p>");
        }
    },
});
});

function buscar(e) {

}