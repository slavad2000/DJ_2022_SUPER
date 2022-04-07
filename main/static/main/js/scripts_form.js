//Процедура выбора картинки
$('.img_select').on('click', function (even) {
    even.preventDefault();

    $target = $(even.target);

    console.log($('#id_'+$target.data('input')));

    $('#id_'+$target.data('input')).on('change',(even2) => {

        var file = even2.target.files[0]; 
        var files = even2.target.files;

        $('#id_'+$target.data('input')).prop("files",files);

        var reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = readerEvent => {
           var content = readerEvent.target.result;
           $target.prop('src',content);
        }
    })

    $('#id_'+$target.data('input')).click()  
})
//Очистка картинки
$('.img_clear').on('change', function (even) {
    even.preventDefault();

    $target = $(even.target);

    console.log($('#id_'+$target.data('input')));
    console.log($('#img_'+$target.data('input')));

    $target = $(even.target);
    $('#id_'+$target.data('input')).val('');
    $('#img_'+$target.data('input')).prop("src","static/main/images/photo.png");
})

function saveForms(e, dop_command={}) {
    if (e)
        e.preventDefault();

    var formData = new FormData(document.querySelector('#my-form'));
    for (var key in dop_command) {
        formData.append(key, dop_command[key])
    };

    $.ajax({
        type : $("#my-form").attr('method'),
        url :  '/tabl/' + $("#my-form").data('typespr') + '/' + $("#my-form").data('id'),
        data : formData,
        processData: false,
        contentType: false,        
        success : function(response){
            $('article').html(response);
            if ('copy' in dop_command) {
                setChanged();
                visibility();
            }
        },
        error : function(response){
             $('article').html(response);
             setChanged();
        }
    })
}

$('button.close').on('click', function(e) {
    if (e)
        e.preventDefault();

    if ($('#caption_form').hasClass('changed'))
        if (!confirm("Данные формы изменены, вы действительно хотите закрыть форму?"))
            return;

    $.ajax({
        type : 'GET',
        url :  '/tabl/' + $("#my-form").data('typespr') + '?parent=' + $("#id_parent_old").val() + '&owner=' + $("#id_owner_old").val(),
        data : {},
        success : function(response){
            $('article').html(response);
        },
        error : function(response){
            $('article').html(response);
            alert("Ошибка создания элемента")
        }
    })                    
});

$("#bn-save-close").on('click', (e)=>{saveForms(e,{'close': true})});
$("#bn-save").on('click', (e)=>{saveForms(e)});
$("#bn-save-copy").on('click', (e)=>{saveForms(e,{'copy': true})});

function setChanged() {
    if ($('#bn-save-close').hasClass('disabled')) {
        $('#bn-save-close').removeClass('disabled'); 
        $('#bn-save').removeClass('disabled');    
        $('#caption_form').addClass('changed');
    }
};  

$(':input',document.getElementById('my-form')).bind("keyup", setChanged);
$(':input',document.getElementById('my-form')).bind("change", setChanged);

function setDelete() {
    $("#id_deleted").val(!($("#id_deleted").val().toLowerCase() == "true"));

    setChanged();
    visibility();
}

function visibility() {
    if ($("#my-form").data('id') != 'add')
        $('#bn-save-copy').removeClass('disabled');   
        
    str = 'static/main/images/bullet-green.png';

    group = false;
    
    if ($('#id_group').length > 0)
        group = ($("#id_group").val().toLowerCase() == "true") 

    del = ($("#id_deleted").val().toLowerCase() == "true");

    if (group)
        str = del ? 'static/main/images/folder_closed-delete.png':'static/main/images/folder_closed.png'
    else 
        str = del ? 'static/main/images/bullet-red.png':'static/main/images/bullet-green.png'

    $("#image-delete").prop('src',str)
}


visibility()
