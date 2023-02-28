$(document).ready(function(){
    $("#addModal").modalForm({
        formUrl: "{% url 'core:add' %}"
    });
});
