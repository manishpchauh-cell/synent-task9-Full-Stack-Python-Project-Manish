// Delete Confirmation

const deleteLinks = document.querySelectorAll(".delete-link");

deleteLinks.forEach(link => {

    link.addEventListener("click", function(e){

        if(!confirm("Are you sure you want to delete this task?")){

            e.preventDefault();

        }

    });

});


// Auto-hide messages

const message = document.querySelector(".message");

if(message){

    setTimeout(()=>{

        message.style.display="none";

    },3000);

}


// Form Validation

const forms = document.querySelectorAll("form");

forms.forEach(form=>{

    form.addEventListener("submit",function(e){

        const required = form.querySelectorAll("input[required]");

        let valid = true;

        required.forEach(input=>{

            if(input.value.trim()===""){

                valid=false;

            }

        });

        if(!valid){

            alert("Please fill all required fields.");

            e.preventDefault();

        }

    });

});


// Search Tasks

const searchInput = document.getElementById("searchTask");

if(searchInput){

searchInput.addEventListener("keyup",function(){

let filter=this.value.toLowerCase();

let cards=document.querySelectorAll(".card");

cards.forEach(card=>{

let title=card.querySelector("h3").innerText.toLowerCase();

if(title.includes(filter)){

card.style.display="block";

}else{

card.style.display="none";

}

});

});

}


// Dark Mode

const darkBtn=document.getElementById("darkMode");

if(darkBtn){

darkBtn.addEventListener("click",()=>{

document.body.classList.toggle("dark");

});

}
