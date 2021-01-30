document.addEventListener('DOMContentLoaded', function (){

    if(document.querySelector(".msg_history")){
        document.addEventListener('DOMContentLoaded', scroll_down);
        
        scroll_down();


        if ( window.history.replaceState ) {
            window.history.replaceState( null, null, window.location.href );
          }
    
        
        // Functions
        
        function scroll_down() {
            var objDiv = document.querySelector(".msg_history");
            objDiv.scrollTop = objDiv.scrollHeight;
        }
        
    }
    else{
    }
    });