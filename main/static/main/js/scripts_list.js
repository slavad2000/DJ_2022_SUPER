function addEl(e) {
    e.preventDefault();
    console.log($(e));

    var $but = $(e.target);

    var $owner = $(".select_owner")

    var parent = $("#" + $but.data('table') + " thead tr:last a");

    $.ajax({
        type : 'GET',
        url :  '/tabl/' + $but.data('typespr') + '/add',
        data : {'group': + $but.data('group'),
                'owner': ($owner.length != 0) ? $owner.val():'',
                'parent':(parent.length != 0) ? $(parent[0]).data('id'):''},
        success : function(response){
            $("article").html(response);
        },
        error : function(response){
            alert(response)
        }
    })
}    

$(".bn_addGrTabl").on('click', addEl);
$(".bn_addElTabl").on('click', addEl);
//*
function listEl(e) {
    e.preventDefault();

    let $parent = $(e.target); 

    if ($parent.hasClass('gr_list'))  {
        $typespr = $parent.data('typespr') 
        var $owner = $(".select_owner")

        if ($parent.closest('thead').hasClass('list_gr'))
            $parent = $parent.parent().parent().prev().find('td a:first'); 

        $.ajax({
            type : 'GET',
            url :  '/tabl/' + $typespr,
            data : {'parent': ($parent.data('id') === undefined) ? '':$parent.data('id'), 
                    'owner': ($owner.length != 0) ? $owner.val():''},
            success : function(response){
                $("article").html(response);
            },
            error : function(response){
                alert(response)
            }
        })
    }
}

$(".list_el").on('click', listEl);
$(".list_gr").on('click', listEl);
//*
$(".select_edit").on('click', function(e) {
    if (e)
        e.preventDefault();

    var $select = $(e.target)

    if ($select.data('type') === 'li') {
        if ($select.data('id') === 1) { //Редактирование
            var $parent = $(".list_gr tr:last a");
            var $owner = $(".select_owner")

            var select_edit = $select.closest('.select_edit')

            $.ajax({
                type : 'GET',
                url :  '/tabl/' + select_edit.data('typespr') + '/' + select_edit.data('id'),
                data : {'owner': ($owner.length != 0) ? $owner.val():'',
                        'parent':($parent.length != 0) ? $($parent[0]).data('id'):''},
                success : function(response){
                    $("article").html(response);
                },
                error : function(response){
                    alert(response)
                }
            })
        } else if ($select.data('id') === 2) { //Пометка на удаление
            var select_edit = $select.closest('.select_edit')

            $.ajax({
                type : 'POST',
                url :  '/tabl/' + select_edit.data('typespr') + '/' + select_edit.data('id'),
                data : {'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'delete': true},
                success : function(response){

                    var $i = $select.closest('tr').children('th').children('img');

                    if (response.group){
                        if (response.deleted)
                            $i.attr("src","/static/main/images/folder_closed-delete.png");
                        else
                            $i.attr("src","/static/main/images/folder_closed.png");

                    }else {
                        if (response.deleted)
                            $i.attr("src","/static/main/images/bullet-red.png");
                        else
                            $i.attr("src","/static/main/images/bullet-green.png");
                    }
                },
                error : function(response){
                    alert(response)
                }
            })
        } else { //Копирование
            var select_edit = $select.closest('.select_edit')

            $.ajax({
                type : 'post',
                url :  '/tabl/' + select_edit.data('typespr') + '/' + select_edit.data('id'),
                data : {'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'copy': true},
                 success : function(response){
                    $('article').html(response);
                    setChanged();
                    visibility();
                },
                error : function(response){
                    alert(response)
                }
            })
        }   
    }
 });

$(".select_owner").on('change', function(e){
    var $select = $(e.target)
    $.ajax({
        type : 'GET',
        url :  '/tabl/' + $select.data('typespr') ,
        data : {'owner': $select.val(),
                'parent':''},
        success : function(response){
            $("article").html(response);
        },
        error : function(response){
            alert(response)
        }
    })
});


