document.addEventListener('DOMContentLoaded', function () {

        if (document.querySelector('#dark-mode').innerHTML === "Enable dark mode"){
            document.querySelector('#dark-mode').addEventListener('click', dark_mode);
        } 
        else{
            document.querySelector('#dark-mode').addEventListener('click', light_mode);
        }
  
    // Dark mode function

    function dark_mode() {
        document.body.style.color = 'white';
        document.body.style.backgroundColor = 'black';
        document.querySelector('#dark-mode') = "Enable light mode";
    };

    // Light mode function
    
    function light_mode() {
        document.body.style.color = 'black';
        document.body.style.backgroundColor = 'white';
        document.querySelector('#dark-mode').innerHTML = "Enable dark mode";
    }
});
