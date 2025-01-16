const stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
const client_secret = $('#id_client_secret').text().slice(1, -1);
const stripe = Stripe(stripe_public_key);

const appearance = { /* appearance */ };
const options = { layout: 'accordion', /* options */ };
const elements = stripe.elements({ clientSecret, appearance });
const paymentElement = elements.create('payment', options);
paymentElement.mount('#payment-element');