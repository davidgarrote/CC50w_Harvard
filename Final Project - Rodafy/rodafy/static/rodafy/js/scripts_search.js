document.addEventListener('DOMContentLoaded', function (){

if(document.querySelector("#find_parking")){
    document.querySelector("#find_parking").addEventListener('click', load_find);
    document.addEventListener('DOMContentLoaded', load_page);
    
    load_page();

    
    // Functions
    
    function load_page() {
    document.querySelector(".options").style.display = 'block';
    document.querySelector(".search").style.display = 'none';
    }
    
    function load_find() {
    document.querySelector(".options").style.display = 'none';
    document.querySelector(".search").style.display = 'block';
    }
}
else{
}
});