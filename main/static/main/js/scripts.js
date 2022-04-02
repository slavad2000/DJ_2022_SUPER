window.onload = function() {
    document.querySelectorAll('.dropdown-item').forEach(function(item) {
        new Menu_select(item,{
            onSelect(item) {
                $.ajax({
                    type : 'GET',
                    url :  "tabl/" + item,
                    data : {},
                    success : function(response){
                        $('article').html(response);
                    },
                    error : function(response){
                        console.log(response)
                    }
                })
            }            
        });    
    })
};