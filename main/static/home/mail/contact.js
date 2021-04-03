document.getElementById("sendMessageButton").addEventListener("click",function(){
    console.log("sender_name")
    let sender_name=document.getElementById("name").value
    let sender_email=document.getElementById("email").value
    let sender_phone=document.getElementById("phone").value
    let sender_message=document.getElementById("message").value
    Email.send({
      Host: "smtp.gmail.com",
      Username: "spotr.iiita@gmail.com",
      Password: "spotr1234",
      To: "spotr.iiita@gmail.com",
      From:`${sender_email}` ,
      Subject: `${sender_name} `,
      Body: `${sender_message}   

           Contact number= ${sender_phone} 
      `,
    }).then(
      function (message) {
        console.log(message);
        alert("mail sent successfully");
      },
      function (error) {
        console.log(error);
      }
    );
  }
)

//   console.log("hey paras")
//     <form method="post">
//       <input type="button" value="Send Email" onclick="sendEmail()" />
//     </form>
//   </body>
// </html>
