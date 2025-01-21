const stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
const clientSecret = $("#id_client_secret").text().slice(1, -1);
const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();
const style = {
};
const card = elements.create("card", {style: style});
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener("change", function (event) {
    const errorDiv = document.getElementById("card-errors");
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
const form = document.getElementById("payment-form");

form.addEventListener("submit", function(ev) {
    ev.preventDefault();
    card.update({ "disabled": true});
    $("#submit-button").attr("disabled", true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            // billing details and shipping from form data to be used with webhooks
            billing_details: {
                name: $.trim(form.name.value),
                surname: $.trim(form.surname.value),
                phone: $.trim(form.phone_number.value),
                email: $.trim(form.email.value),
                address: {
                    line_one: $.trim(form.address_line_one.value),
                    line_two: $.trim(form.address_line_two.value),
                    town: $.trim(form.town_or_city.value),
                    country: "GB",
                }
            }
        },
        shipping: {
           name: $.trim(form.name.value),
            surname: $.trim(form.surname.value),
            phone: $.trim(form.phone_number.value),
            address: {
                line_one: $.trim(form.address_line_one.value),
                line_two: $.trim(form.address_line_two.value),
                town: $.trim(form.town_or_city.value),
                postcode: $.trim(form.postcode.value),
                country: "GB", 
            }
        }
    }).then(function(result) {
        if (result.error) {
            const errorDiv = document.getElementById("card-errors");
            const html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({ "disabled": false});
            $("#submit-button").attr("disabled", false);
        } else {
            if (result.paymentIntent.status === "succeeded") {
                form.submit();
            }
        }
    });
});