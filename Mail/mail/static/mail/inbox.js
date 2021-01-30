document.addEventListener('DOMContentLoaded', function () {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  //until there is a message, keep the alert hidden
  document.querySelector('.alert').style.display = 'none';

  // By default, load the inbox
  load_mailbox('inbox');
});

// FUNCTION Compose email

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#full-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';

  document.querySelector('#compose-form').onsubmit = () => {
    fetch('/emails', {
      method: 'POST',
      body: JSON.stringify({
        recipients: document.querySelector('#compose-recipients').value,
        subject: document.querySelector('#compose-subject').value,
        body: document.querySelector('#compose-body').value
      })
    })
      .then(response => response.json())
      .then(result => {
        if (result["error"]) {
          document.querySelector('#message').innerHTML = result["error"];
          document.querySelector('.alert').style.display = 'block';
          document.body.scrollTop = document.documentElement.scrollTop = 0;
        }
        else {
          document.querySelector('.alert').style.display = 'none';
          load_mailbox('sent')
        }
      });

    return false;
  };
}

// FUNCTION Load mailbox

function load_mailbox(mailbox) {

  // make a fetch call to load the mailbox

  fetch(`emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {

    // For each email inside the array of emails, create a DIV constant called email_div
    for (let email of emails) {
      if (email["archived"] && mailbox === "inbox") {
        //it should show archived emails in "sent" and "archived" only
        continue;
      }


      const email_div = document.createElement('div');
      // Set the atribute false/true read to set a different class atribute and load a different looking div
      email_div.setAttribute("class", `email-holder row d-flex read-${email["read"]}`);

      // Complete the div with the data from the email
      email_div.innerHTML = `
        <div class="p-2">${email["sender"]}</div>
        <div class="p-2">${email["subject"]}</div>
        <div class="ml-auto p-2">${email["timestamp"]}</div>
      `;

      // Once the email is clicked, load the email
      email_div.addEventListener('click', () => load_email(email));

      // Append the emails to the emails-view to complete the creation of the emails view
      document.querySelector('#emails-view').append(email_div);
    };
  });

  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#full-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
}


// FUNCTION Load email

function load_email(email) {
  document.querySelector('#full-view').style.display = 'block';
  document.querySelector('#emails-view').style.display = 'none';

  fetch(`/emails/${email["id"]}`, {
    method: 'PUT',
    body: JSON.stringify({
      read: true
    })
  })

  document.querySelector('#full-view').innerHTML = /*html*/`
    <span style="font-weight: bold">From: </span>${email["sender"]}<br>
    <span style="font-weight: bold">To: </span>${email["recipients"]}<br>
    <span style="font-weight: bold">Subject: </span>${email["subject"]}<br>
    <span style="font-weight: bold">Timestamp: </span>${email["timestamp"]}<br><br>
    <div class="email-buttons row">
      <button class="btn btn-sm btn-outline-primary" id="reply">Reply</button>
      <button class="btn btn-sm btn-outline-primary" id="archive">${email["archived"] ? "Unarchive" : "Archive"}</button>
    </div>
    <hr>
    ${email["body"]}
  `;

   // Archive / Unarchive email

  document.querySelector('#archive').addEventListener('click', () => {
    fetch(`/emails/${email["id"]}`, {
      method: 'PUT',
      body: JSON.stringify({
        archived: !email["archived"]
      })
    })
      .then(() => load_mailbox("inbox"));
  });

  // Reply email

  document.querySelector('#reply').addEventListener('click', () => {
    compose_email();

    if(email["subject"].slice(0,4) != "Re: "){
      email["subject"] = `Re: ${email["subject"]}`;
    }

    document.querySelector('#compose-recipients').value = email["sender"]; //reply to the sender
    document.querySelector('#compose-subject').value = `${email["subject"]}`;
    document.querySelector('#compose-body').value = `On ${email["timestamp"]} ${email["sender"]} wrote:\n${email["body"]}\n\n`;
  });
}