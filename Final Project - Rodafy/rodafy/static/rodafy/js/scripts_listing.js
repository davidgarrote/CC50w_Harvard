document.addEventListener('DOMContentLoaded', function () {

    if(document.querySelector('#Edit_listing')){
    document.querySelector('#Edit_listing').addEventListener('click', load_edit);
    document.querySelector('#Save_listing').addEventListener('click', save_page);
    document.addEventListener('DOMContentLoaded', load_page);

    //By default show all categories and hide forms

    load_page();



    // Functions

    // Hides all the information and loads an input form instead
    function load_edit() {
        
        // Price
        price = document.querySelector('.listing-text-price').textContent
        document.querySelector('.listing-text-price').style.display = 'none';
        document.querySelector('#form-control-price').textContent = price
        document.querySelector('#form-control-price').style.display = 'block';


        // Measurements
        document.querySelector('.listing-text-width').style.display = 'none';
        document.querySelector('#form-control-width').style.display = 'block';

        document.querySelector('.listing-text-length').style.display = 'none';
        document.querySelector('#form-control-length').style.display = 'block';

        // Address
        document.querySelector('.listing-text-address').style.display = 'none';
        document.querySelector('#form-control-address').style.display = 'block';

        // Availability
        document.querySelector('.listing-text-availability').style.display = 'none';
        document.querySelector('#form-control-availability').style.display = 'block';

        // Description
        document.querySelector('.listing-text-description').style.display = 'none';
        document.querySelector('#form-control-description').style.display = 'block';


        document.querySelector('#Edit_listing').style.display = 'none';
        document.querySelector('#Save_listing').style.display = 'block';
    }

    // Default function to run, and to run after saving the changes made

    function load_page(){

        // Price
        document.querySelector('.listing-text-price').style.display = 'block';
        document.querySelector('#form-control-price').style.display = 'none';

        // Measurements
        document.querySelector('.listing-text-width').style.display = 'block';
        document.querySelector('#form-control-width').style.display = 'none';

        document.querySelector('.listing-text-length').style.display = 'block';
        document.querySelector('#form-control-length').style.display = 'none';

        // Address
        document.querySelector('.listing-text-address').style.display = 'block';
        document.querySelector('#form-control-address').style.display = 'none';

        // Availability
        document.querySelector('.listing-text-availability').style.display = 'block';
        document.querySelector('#form-control-availability').style.display = 'none';

        // Description
        document.querySelector('.listing-text-description').style.display = 'block';
        document.querySelector('#form-control-description').style.display = 'none';

        document.querySelector('#Save_listing').style.display = 'none';
        document.querySelector('#Edit_listing').style.display = 'block';
    }

    function save_page(){

        // Price
        document.querySelector('.listing-text-price').style.display = 'block';
        document.querySelector('#form-control-price').style.display = 'none';

        // Measurements
        document.querySelector('.listing-text-width').style.display = 'block';
        document.querySelector('#form-control-width').style.display = 'none';

        document.querySelector('.listing-text-length').style.display = 'block';
        document.querySelector('#form-control-length').style.display = 'none';

        // Address
        document.querySelector('.listing-text-address').style.display = 'block';
        document.querySelector('#form-control-address').style.display = 'none';

        // Availability
        document.querySelector('.listing-text-availability').style.display = 'block';
        document.querySelector('#form-control-availability').style.display = 'none';

        // Description
        document.querySelector('.listing-text-description').style.display = 'block';
        document.querySelector('#form-control-description').style.display = 'none';

        document.querySelector('#Save_listing').style.display = 'none';
        document.querySelector('#Edit_listing').style.display = 'block';
    }
}else{
    
}
});
