document.addEventListener('DOMContentLoaded', function () {

    // Use buttons to toggle between views

    document.querySelector('#submit_post').addEventListener('click', submit);
    document.querySelector('#feed').addEventListener('click', load_feed);
    document.querySelector('#following').addEventListener('click', load_following_feed);


    // Functions

    function submit() {

        //Only show the submit and feed views
        document.querySelector('#new_post').style.display = 'block';
        document.querySelector('#feed_posts').style.display = 'block';
        document.querySelector('#following_posts').style.display = 'none';
        document.querySelector('#profile_posts').style.display = 'none';
    }

    function load_feed() {

        //Only show the submit and feed views

        document.querySelector('#new_post').style.display = 'block';
        document.querySelector('#feed_posts').style.display = 'block';
        document.querySelector('#following_posts').style.display = 'none';
        document.querySelector('#profile_posts').style.display = 'none';

        // Effectively load feed

        

    }

    function load_following_feed() {
        
        //Only show the submit and following views

        document.querySelector('#new_post').style.display = 'none';
        document.querySelector('#feed_posts').style.display = 'none';
        document.querySelector('#following_posts').style.display = 'block';
        document.querySelector('#profile_posts').style.display = 'none';

    }
  });