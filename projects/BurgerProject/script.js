// Header
const dateSpan = document.getElementById('date-span');

// Menu
const menu = document.getElementById('menu');

// Modal
const cartModal = document.getElementById('cart-modal');
const cartItemsContainer = document.getElementById('cart-items');
const cartTotal = document.getElementById('cart-total');
const addressInput = document.getElementById('adress');
const addressWarn = document.getElementById('adress-warn');
const closeModalBtn = document.getElementById('close-modal-btn');
const checkoutBtn = document.getElementById('checkout-btn');

// Cart Footer
const cartBtn = document.getElementById('cart-btn');
const cartCount = document.getElementById('cart-count');

let cart = [];

//
// Opening Modal
cartBtn.addEventListener('click', function() {
    updateCartModal();
    cartModal.style.display = "flex"
})

// Closing Modal
cartModal.addEventListener("click", function(event){
    if(event.target === cartModal){
        cartModal.style.display = "none"
    }
})

closeModalBtn.addEventListener("click", function(){
    cartModal.style.display = "none"
})

// Get Cart Button Attributes
menu.addEventListener("click", function(event){
    let parentButton = event.target.closest(".add-to-cart-btn")  // Se você clicou nele ou se o elemento em volta dele (pai) tem "btn". o '.' é pra classem ' # ' é pra ID

    if(parentButton){
        const name = parentButton.getAttribute("data-name")
        const price = parseFloat(parentButton.getAttribute("data-price"))
    
        addToCart(name, price)
    
    }
})

// Add to cart function
function addToCart(name, price){
    const existingItem = cart.find(item => item.name === name)

    if(existingItem){
        // If item already exists in cart then increment quantity by 1
        existingItem.quantity += 1
        return;
    }else{
        cart.push({
            name,
            price,
            quantity: 1,
        })
    }

    updateCartModal()


}

//Update cart
function updateCartModal(){
    cartItemsContainer.innerHTML = "";
    let total = 0;

    cart.forEach(item => {
        const cartItemElement = document.createElement("div");
        cartItemElement.classList.add("flex", "justfy-between", "mb-4", "flex-col")

        cartItemElement.innerHTML = `
        <div class="flex items-center justify-between">
            <div>
                <p class="font-medium">${item.name}</p>
                <p>Amount: ${item.quantity}</p>
                <p class="font-medium mt-2">$ ${item.price.toFixed(2)}</p>
            </div>

            <button class="remove-from-cart-btn" data-name="${item.name}">
                Remove
            </button>
        </div>
        `
        
        total += item.price * item.quantity;

        cartItemsContainer.appendChild(cartItemElement)
    })

    cartTotal.textContent = total.toLocaleString("pt-BR", {
        style: "currency",
        currency: "USD"
    });

    cartCount.innerHTML = cart.length;

}


// Remove chart item
cartItemsContainer.addEventListener("click", function(event){
    if(event.target.classList.contains("remove-from-cart-btn")){
        const name = event.target.getAttribute("data-name")

        removeItemCart(name);
    }
})

function removeItemCart(name){
    const index = cart.findIndex(item => item.name === name);

    if(index !== -1){
        const item = cart[index];

        if(item.quantity > 1){
            item.quantity -= 1;
            updateCartModal();
            return;
        }

        cart.splice(index, 1);
        updateCartModal();

    }

}

//Get adress
addressInput.addEventListener("input", function(event){
    let inputValue = event.target.value;

    if(inputValue !== ""){
        addressInput.classList.remove("border-red-500")
        addressWarn.classList.add("hidden")
    }
})

//Finish order
checkoutBtn.addEventListener("click", function(){
    const isOpen = checkRestaurantOpen();
    if(!isOpen){

    Toastify({
        text: "Sorry, we're closed.",
        duration: 3000,
        close: true,
        gravity: "top", // `top` or `bottom`
        position: "left", // `left`, `center` or `right`
        stopOnFocus: true, // Prevents dismissing of toast on hover
        style: {
            background: "#ef4444",
        },
        }).showToast();

    }

    if(cart.length === 0) return;

    if(addressInput.value === ""){
        addressWarn.classList.remove("hidden")
        addressInput.classList.add("border-red-500")
        return;
    }

    //Send to WhatsappWeb API
    const cartItems = cart.map((item) => {
        return(
            `${item.name} Quantity: (${item.quantity}) Price: $(${item.price}) |`
        )
    }).join("")

    const message = encodeURIComponent(cartItems)
    const phone = "47999675582"

    window.open(`https://wa.me/${phone}?text=${message} Address: ${addressInput.value}`, "_blank")

    cart = [];
    updateCartModal();
})


//Verify if restaurant is open
function checkRestaurantOpen(){
    const date = new Date();
    const hora = date.getHours();
    return hora >= 18 && hora < 22; //true = open
    
}

const spanItem = document.getElementById("date-span")
const isOpen = checkRestaurantOpen();

if(isOpen){
    spanItem.classList.remove("bg-red-500")
    spanItem.classList.add("bg-green-600")
}else{
    spanItem.classList.remove("bg-green-600")
    spanItem.classList.remove("bg-red-500")
}