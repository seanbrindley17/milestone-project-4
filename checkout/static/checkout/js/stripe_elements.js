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
    // If user has saved info checked, retrieve from id-save-info 
    const saveInfo = Boolean($("#id-save-info").attr("checked"));
    // Get csrf token from form
    const csrfToken = $("input[name='csrfmiddlewaretoken']").val();
    // collate data to be sent to form in postData object
    const postData = {
        "csrfmiddlewaretoken": csrfToken,
        "client_secret": clientSecret,
        "save_info": saveInfo,
    };
    const url = "/checkout/cache_checkout_data";
    // Post data to url above using postData above
    // Uses .done to call function that will be executed if view has success response
    // Basically means execute stripe function if all goes to plan
    $.post(url, postData).done(function() {
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
    // If view returns 400 response, reload page and django will show error message
    }).fail(function() {
        location.reload();
    });  
});