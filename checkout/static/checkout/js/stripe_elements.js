const stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
const clientSecret = $('#id_client_secret').text().slice(1, -1);
const stripe = stripe(stripePublicKey);

const appearance = { /* appearance */ };
const options = { layout: 'accordion', /* options */ };
const elements = stripe.elements({ clientSecret, appearance });
const paymentElement = elements.create('payment', options);
paymentElement.mount('#payment-element');

//Handle errors
card.addEventListener("change", function(event) {
    // Error detected
    const errorDiv = document.getElementById("card-errors");
    // Show alert
    if (event.error) {
        const html = `
        <span class="icon" role="alert">
            <i class="fas fa-times"></i>
        </span>
        <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = "";
    }
});

// Handle form submit

const form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            // Shows error message in html
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            // re enables card update and submit button for user to fix issue
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            // If the status of the payment attempt is succeeded, then submit form
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});