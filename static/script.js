
// function myFunction() {
//     var x = document.getElementById("password");
//     if (x.type === "password") {
//         x.type = "text";
//     } else {
//         x.type = "password";
//     }
// }








var remove_cart_item_button = document.getElementsByClassName('btn-danger')
console.log(remove_cart_item_button)
for (var i = 0; i < remove_cart_item_button; i++){
    var button = remove_cart_item_button[i]
    button.addEventListener('click', function(){
        console.log('clicled')
    })
}