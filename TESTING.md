# Testing

> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| checkout | [checkout.html](https://github.com/seanbrindley17/milestone-project-4/blob/main/checkout/templates/checkout/checkout.html) | [link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmilestone-project-4-sb-1448d349aa27.herokuapp.com%2Fcheckout%2F#textarea) | ![screenshot](/readme-documentation/screenshots/validation/html/checkout-warning.png) | Used `<h1>` in the page title while it is also used for the site title that extends every page. Fixed by changing to `<h2>` element. |
| checkout | [checkout.html](https://github.com/seanbrindley17/milestone-project-4/blob/main/checkout/templates/checkout/checkout.html) | [link](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmilestone-project-4-sb-1448d349aa27.herokuapp.com%2Fcheckout%2F) | ![screenshot](/readme-documentation/screenshots/validation/html/checkout-page-success.png) | No errors |
| checkout | [checkout_success.html](https://github.com/seanbrindley17/milestone-project-4/blob/main/checkout/templates/checkout/checkout_success.html) | [Link](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmilestone-project-4-sb-1448d349aa27.herokuapp.com%2Fcheckout%2Fcheckout%2FC70AF50B9DEA45EE99B0A5EFB30B7448%2F) | ![screenshot](/readme-documentation/screenshots/validation/html/checkout-success-error.png) | Error not specifically on page, but on the toast-success page where there were a couple of stray `</div>` end tags. These have been removed |
| checkout | [checkout_success.html](https://github.com/seanbrindley17/milestone-project-4/blob/main/checkout/templates/checkout/checkout_success.html) | [Link](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmilestone-project-4-sb-1448d349aa27.herokuapp.com%2Fcheckout%2Fcheckout%2F15959F200CD14BFDB66FFB50D5B1EECD%2F) | ![screenshot](/readme-documentation/screenshots/validation/html/checkout-success-success.png) | No errors |
| home | [add_product.html](https://github.com/seanbrindley17/milestone-project-4/blob/main/home/templates/home/add_product.html) |  | ![screenshot](/readme-documentation/screenshots/validation/html/add-product-success.png) | No errors |
| home | [edit_product.html](https://github.com/seanbrindley17/milestone-project-4/blob/main/home/templates/home/edit_product.html) |  | ![screenshot](/readme-documentation/screenshots/validation/html/edit-product-success.png) | No errors |
| home | [product_display.html](https://github.com/seanbrindley17/milestone-project-4/blob/main/home/templates/home/product_display.html) |  | ![screenshot](/readme-documentation/screenshots/validation/html/index-errors.png) | Two errors, repeated. The duplicate class error was because on the confirm delete button in the model, there were two class attributes, one blank. This was removed. The other was an aria label error because I hadn't referenced what was being labelled. This was corrected by putting the id in the title and using the jinja templating to generate the correct ID  |
| home | [index.html](https://github.com/seanbrindley17/milestone-project-4/blob/main/home/templates/home/index.html) | [Link](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmilestone-project-4-sb-1448d349aa27.herokuapp.com%2F) | ![screenshot](/readme-documentation/screenshots/validation/html/index-success.png) | No errors |
| home | [product_detail.html](https://github.com/seanbrindley17/milestone-project-4/blob/main/home/templates/home/product_detail.html) |  | ![screenshot](/readme-documentation/screenshots/validation/html/product_detail-errors.png) | Repeat class attribute, removed extra one. aria-label error, no link to the delete element, fixed by correctly linking. Warning for using type=text/javascript. Didn't know this wasn't necessary as my walkthrough used it. |
| home | [product_detail.html](https://github.com/seanbrindley17/milestone-project-4/blob/main/home/templates/home/product_detail.html) | [Link](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmilestone-project-4-sb-1448d349aa27.herokuapp.com%2F6%2F) | ![screenshot](/readme-documentation/screenshots/validation/html/product_detail-success.png) | No errors. |
| profiles | [profile.html](https://github.com/seanbrindley17/milestone-project-4/blob/main/profiles/templates/profiles/profile.html) | [Link](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmilestone-project-4-sb-1448d349aa27.herokuapp.com%2Fprofile%2F) | ![screenshot of errors](/readme-documentation/screenshots/validation/html/profile-errors.png) | Unsure about this. The errors say there are missing closing tags but looking at the source code I see the open tags here and then corresponding close tags here: ![screenshot of open tags](/readme-documentation/screenshots/validation/html/profile-open-tags.png), ![screenshot of close tags](/readme-documentation/screenshots/validation/html/profile-close-tags.png). I am completely unsure what to do about this. |
| templates | [404.html](https://github.com/seanbrindley17/milestone-project-4/blob/main/templates/404.html) |  | ![screenshot](/readme-documentation/screenshots/validation/html/404-success.png) | No errors |
| trolley | [trolley.html](https://github.com/seanbrindley17/milestone-project-4/blob/main/trolley/templates/trolley/trolley.html) | [Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmilestone-project-4-sb-1448d349aa27.herokuapp.com%2Ftrolley%2F) | ![screenshot](/readme-documentation/screenshots/validation/html/trolley-success.png) | No errors |


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| profiles | [profiles.css](https://github.com/seanbrindley17/milestone-project-4/blob/main/profiles/static/profiles/css/profiles.css) |  | ![screenshot](/readme-documentation/screenshots/validation/css/profiles.css-success.png) | No errors |
| static | [base.css](https://github.com/seanbrindley17/milestone-project-4/blob/main/static/css/base.css) | [Link](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fmilestone-project-4-sb-1448d349aa27.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#warnings) | ![screenshot](/readme-documentation/screenshots/validation/css/base.css-success.png) | No errors |


### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| checkout | [stripe_elements.js](https://github.com/seanbrindley17/milestone-project-4/blob/main/checkout/static/checkout/js/stripe_elements.js) | N/A | ![screenshot](/readme-documentation/screenshots/validation/js/checkout-stripe-js-success.png) | No errors |


### Python

I used autopep8 to force my lines to be 79 maximum as designated by the CI Linter. God knows why you can't just stick with 88 as it was before but let's just hope everything still works.

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files. 

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| checkout | [admin.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/checkout/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/checkout/admin.py) | ![screenshot](/readme-documentation/screenshots/validation/python/checkout/admin.png) | No errors |
| checkout | [forms.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/checkout/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/checkout/forms.py) | ![screenshot](/readme-documentation/screenshots/validation/python/checkout/forms.png) | No errors |
| checkout | [models.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/checkout/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/checkout/models.py) | ![screenshot](/readme-documentation/screenshots/validation/python/checkout/models.png) | Had to use `#noqa`, as some of the lines were too long for the CI Linter, yet when I tried shortening them at brackets and saving, the automatic linter would put them back where they were originally. Using `#noqa` made the auto linter put brackets around some of the problem lines. |
| checkout | [signals.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/checkout/signals.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/checkout/signals.py) | ![screenshot](/readme-documentation/screenshots/validation/python/checkout/signals.png) | No errors |
| checkout | [urls.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/checkout/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/checkout/urls.py) | ![screenshot](/readme-documentation/screenshots/validation/python/checkout/urls.py.png) | No errors |
| checkout | [views.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/checkout/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/checkout/views.py) | ![screenshot](/readme-documentation/screenshots/validation/python/checkout/views.py.png) | Had to #noqa a couple of lines |
| checkout | [webhook_handler.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/checkout/webhook_handler.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/checkout/webhook_handler.py) | ![screenshot](/readme-documentation/screenshots/validation/python/checkout/webhook_handlers.py.png) | No errors |
| checkout | [webhooks.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/checkout/webhooks.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/checkout/webhooks.py) | ![screenshot](/readme-documentation/screenshots/validation/python/checkout/webhooks.py.png) | No errors |
|  | [custom_storages.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/custom_storages.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/custom_storages.py) | ![screenshot](/readme-documentation/screenshots/validation/python/root-level/custom-storages.py.png) | Notes (if applicable) |
| home | [admin.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/home/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/home/admin.py) | ![screenshot](/readme-documentation/screenshots/validation/python/home/admin.py.png) | No errors |
| home | [forms.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/home/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/home/forms.py) | ![screenshot](/readme-documentation/screenshots/validation/python/home/forms.py.png) | No errors |
| home | [models.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/home/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/home/models.py) | ![screenshot](/readme-documentation/screenshots/validation/python/home/models.py.png) | No errors |
| home | [urls.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/home/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/home/urls.py) | ![screenshot](/readme-documentation/screenshots/validation/python/home/urls.py.png) | No errors |
| home | [views.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/home/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/home/views.py) | ![screenshot](/readme-documentation/screenshots/validation/python/home/views.py.png) | No errors |
|  | [manage.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/manage.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/manage.py) | ![screenshot](/readme-documentation/screenshots/validation/python/root-level/manage.py.png) | No errors |
| profiles | [forms.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/profiles/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/profiles/forms.py) | ![screenshot](/readme-documentation/screenshots/validation/python/profiles/forms.py.png) | No errors |
| profiles | [models.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/profiles/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/profiles/models.py) | ![screenshot](/readme-documentation/screenshots/validation/python/profiles/models.py.png) | No errors |
| profiles | [urls.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/profiles/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/profiles/urls.py) | ![screenshot](/readme-documentation/screenshots/validation/python/profiles/urls.py.png) | No errors |
| profiles | [views.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/profiles/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/profiles/views.py) | ![screenshot](/readme-documentation/screenshots/validation/python/profiles/views.py.png) | No errors |
| trolley | [contexts.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/trolley/contexts.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/trolley/contexts.py) | ![screenshot](/readme-documentation/screenshots/validation/python/trolley/contexts.py.png) | No errors |
| trolley | [urls.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/trolley/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/trolley/urls.py) | ![screenshot](/readme-documentation/screenshots/validation/python/trolley/urls.py.png) | No errors |
| trolley | [views.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/trolley/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/trolley/views.py) | ![screenshot](/readme-documentation/screenshots/validation/python/trolley/views.py.png) | No errors |
| wnsc_shop | [settings.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/wnsc_shop/settings.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/wnsc_shop/settings.py) | ![screenshot](/readme-documentation/screenshots/validation/python/project-level/settings.py.png) | No errors |
| wnsc_shop | [urls.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/wnsc_shop/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/wnsc_shop/urls.py) | ![screenshot](/readme-documentation/screenshots/validation/python/project-level/urls.py.png) | No errors |


## Responsiveness

I've tested my deployed project to check for responsiveness issues.
I used my Acer laptop for desktop testing, a simulated galaxy s8 on dev tools for mobile and a simulated ipad mini on dev tools for tablet.

| Page | Mobile | Tablet | Desktop | Notes |
| --- | --- | --- | --- | --- |
| Sign Up | ![screenshot](/readme-documentation/screenshots/responsiveness/mobile/sign-up.png) | ![screenshot](/readme-documentation/screenshots/responsiveness/tablet/sign-up.png) | ![screenshot](/readme-documentation/screenshots/features/signup.png) | Works as expected |
| Log In | ![screenshot](/readme-documentation/screenshots/responsiveness/mobile/login.png) | ![screenshot](/readme-documentation/screenshots/responsiveness/tablet/login.png) | ![screenshot](/readme-documentation/screenshots/features/login.png) | Footer not pushed down far enough on tablet and desktop |
| Profile | ![screenshot](/readme-documentation/screenshots/responsiveness/mobile/profile.png) | ![screenshot](/readme-documentation/screenshots/responsiveness/tablet/profile.png) | ![screenshot](/readme-documentation/screenshots/features/profile-details.png) | Works as expected |
| Home | ![screenshot](/readme-documentation/screenshots/responsiveness/mobile/home-page.png) | ![screenshot](/readme-documentation/screenshots/responsiveness/tablet/home.png) | ![screenshot](/readme-documentation/screenshots/responsiveness/desktop/home.png) | Works as expected |
| Products | ![screenshot](/readme-documentation/screenshots/responsiveness/mobile/product-display.png) | ![screenshot](/readme-documentation/screenshots/responsiveness/tablet/product-display.png) | ![screenshot](/readme-documentation/screenshots/features/products.png) | Works as expected |
| Product Details | ![screenshot](/readme-documentation/screenshots/responsiveness/mobile/product-detail.png) | ![screenshot](/readme-documentation/screenshots/responsiveness/tablet/product-detail.png) | ![screenshot](/readme-documentation/screenshots/features/product-detail.png) | Works as expected |
| Trolley | ![screenshot](/readme-documentation/screenshots/responsiveness/mobile/trolley.png) | ![screenshot](/readme-documentation/screenshots/responsiveness/tablet/trolley.png) | ![screenshot](/readme-documentation/screenshots/features/trolley.png) | Footer not pushed far enough down on tablet |
| Checkout | ![screenshot](/readme-documentation/screenshots/responsiveness/mobile/checkout.png) | ![screenshot](/readme-documentation/screenshots/responsiveness/tablet/checkout-success.png) | ![screenshot](/readme-documentation/screenshots/features/checkout.png) | Works as expected |
| Checkout Success | ![screenshot](/readme-documentation/screenshots/responsiveness/mobile/checkout-success.png) | ![screenshot](/readme-documentation/screenshots/responsiveness/tablet/checkout-success.png) | ![screenshot](/readme-documentation/screenshots/features/order-confirmation.png) | Works as expected |
| Add Product | ![screenshot](/readme-documentation/screenshots/responsiveness/mobile/add-product.png) | ![screenshot](/readme-documentation/screenshots/responsiveness/tablet/add-product.png) | ![screenshot](/readme-documentation/screenshots/responsiveness/desktop/add-product.png) | Stretched on mobile due to the form fields, I'm not sure what to do to change them. Wasn't explained well. |
| Edit Product | ![screenshot](/readme-documentation/screenshots/responsiveness/mobile/edit-product.png) | ![screenshot](/readme-documentation/screenshots/responsiveness/tablet/edit-product.png) | ![screenshot](/readme-documentation/screenshots/responsiveness/desktop/edit-product.png) | Stretched on mobile due to the form fields, I'm not sure what to do to change them. Wasn't explained well. |
| Newsletter | ![screenshot](/readme-documentation/screenshots/responsiveness/mobile/newsletter.png) | ![screenshot](/readme-documentation/screenshots/responsiveness/tablet/newsletter.png) | ![screenshot](/readme-documentation/screenshots/features/newsletter.png) | Works as expected |
| 404 | ![screenshot](/readme-documentation/screenshots/responsiveness/mobile/404.png) | ![screenshot](/readme-documentation/screenshots/responsiveness/tablet/404.png) | ![screenshot](/readme-documentation/screenshots/features/404.png) | Works as expected |

## Browser Compatibility

I've tested my deployed project on Chrome, Firefox and Opera to check for compatibility issues.
I found nothing that impacted compatibility between the browsers.

| Page | Chrome | Firefox | Opera | Notes |
| --- | --- | --- | --- | --- |
| Register | ![screenshot](/readme-documentation/screenshots/features/signup.png) | ![screenshot](/readme-documentation/screenshots/compatibility/firefox/register.png) | ![screenshot](/readme-documentation/screenshots/compatibility/opera/register.png) | Works as expected |
| Login | ![screenshot](/readme-documentation/screenshots/features/login.png) | ![screenshot](/readme-documentation/screenshots/compatibility/firefox/login.png) | ![screenshot](/readme-documentation/screenshots/compatibility/opera/login.png) | Works as expected |
| Profile | ![screenshot](/readme-documentation/screenshots/features/profile-details.png) | ![screenshot](/readme-documentation/screenshots/compatibility/firefox/profile.png) | ![screenshot](/readme-documentation/screenshots/compatibility/opera/profile.png) | Works as expected |
| Home | ![screenshot](/readme-documentation/screenshots/responsiveness/desktop/home.png) | ![screenshot](/readme-documentation/screenshots/compatibility/firefox/home.png) | ![screenshot](/readme-documentation/screenshots/compatibility/opera/home.png) | Works as expected |
| Products | ![screenshot](/readme-documentation/screenshots/features/products.png) | ![screenshot](/readme-documentation/screenshots/compatibility/firefox/products.png) | ![screenshot](/readme-documentation/screenshots/compatibility/opera/products.png) | Works as expected |
| Product Details | ![screenshot](/readme-documentation/screenshots/features/product-detail.png) | ![screenshot](/readme-documentation/screenshots/compatibility/firefox/product-detail.png) | ![screenshot](/readme-documentation/screenshots/compatibility/opera/product-detail.png) | Works as expected |
| Trolley | ![screenshot](/readme-documentation/screenshots/features/trolley.png) | ![screenshot](/readme-documentation/screenshots/compatibility/firefox/trolley.png) | ![screenshot](/readme-documentation/screenshots/compatibility/opera/trolley.png) | Works as expected |
| Checkout | ![screenshot](/readme-documentation/screenshots/features/checkout-details.png) | ![screenshot](/readme-documentation/screenshots/compatibility/firefox/checkout.png) | ![screenshot](/readme-documentation/screenshots/compatibility/opera/checkout.png) | Works as expected |
| Checkout Success | ![screenshot](/readme-documentation/screenshots/features/order-confirmation.png) | ![screenshot](/readme-documentation/screenshots/compatibility/firefox/checkout-success.png) | ![screenshot](/readme-documentation/screenshots/compatibility/opera/checkout-success.png) | Works as expected |
| Add Product | ![screenshot](/readme-documentation/screenshots/responsiveness/desktop/add-product.png) | ![screenshot](/readme-documentation/screenshots/compatibility/firefox/add-product.png) | ![screenshot](/readme-documentation/screenshots/compatibility/opera/add-product.png) | Works as expected |
| Edit Product | ![screenshot](/readme-documentation/screenshots/responsiveness/desktop/edit-product.png) | ![screenshot](/readme-documentation/screenshots/compatibility/firefox/edit-product.png) | ![screenshot](/readme-documentation/screenshots/compatibility/opera/edit-product.png) | Works as expected |
| Newsletter | ![screenshot](/readme-documentation/screenshots/features/newsletter.png) | ![screenshot](/readme-documentation/screenshots/compatibility/firefox/newsletter.png) | ![screenshot](/readme-documentation/screenshots/compatibility/opera/newsletter.png) | Works as expected |
| 404 | ![screenshot](/readme-documentation/screenshots/features/404.png) | ![screenshot](/readme-documentation/screenshots/compatibility/firefox/404.png) | ![screenshot](/readme-documentation/screenshots/compatibility/opera/404.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. Some warnings are outside of my control, my laptop is very old so performance may be skewed, and mobile results tend to be lower than desktop.

All the images on the site were compressed in TinyPNG, I used minimal moving parts and the lighthouse audit was run on a chrome incognito window, so I don't know what more can be done to improve scores.

| Page | Mobile | Desktop |
| --- | --- | --- |
| Register | ![screenshot](/readme-documentation/screenshots/lighthouse/mobile/register.png) | ![screenshot](/readme-documentation/screenshots/lighthouse/desktop/register.png) |
| Login | ![screenshot](/readme-documentation/screenshots/lighthouse/mobile/login.png) | ![screenshot](/readme-documentation/screenshots/lighthouse/desktop/login.png) |
| Profile | ![screenshot](/readme-documentation/screenshots/lighthouse/mobile/profile.png) | ![screenshot](/readme-documentation/screenshots/lighthouse/desktop/profile.png) |
| Home/Products | ![screenshot](/readme-documentation/screenshots/lighthouse/mobile/home.png) | ![screenshot](/readme-documentation/screenshots/lighthouse/desktop/home.png) |
| Product Details | ![screenshot](/readme-documentation/screenshots/lighthouse/mobile/product-details.png) | ![screenshot](/readme-documentation/screenshots/lighthouse/desktop/product-details.png) |
| Trolley | ![screenshot](/readme-documentation/screenshots/lighthouse/mobile/trolley.png) | ![screenshot](/readme-documentation/screenshots/lighthouse/desktop/trolley.png) |
| Checkout | ![screenshot](/readme-documentation/screenshots/lighthouse/mobile/checkout.png) | ![screenshot](/readme-documentation/screenshots/lighthouse/desktop/checkout.png) |
| Checkout Success | ![screenshot](/readme-documentation/screenshots/lighthouse/mobile/checkout-success.png) | ![screenshot](/readme-documentation/screenshots/lighthouse/desktop/checkout-success.png) |
| Add Product | ![screenshot](/readme-documentation/screenshots/lighthouse/mobile/add-product.png) | ![screenshot](/readme-documentation/screenshots/lighthouse/desktop/add-product.png) |
| Edit Product | ![screenshot](/readme-documentation/screenshots/lighthouse/mobile/edit-product.png) | ![screenshot](/readme-documentation/screenshots/lighthouse/desktop/edit-product.png) |
| 404 | ![screenshot](/readme-documentation/screenshots/lighthouse/mobile/404.png) | ![screenshot](/readme-documentation/screenshots/lighthouse/desktop/404.png) |

## WAVE Testing

I used the [WAVE](https://wave.webaim.org/) browser extension in Chrome to give my site a once over. The errors that I have remaining are considered acceptable errors and were by design. No contrast issues detected.

| Page | Screenshot | Notes |
| --- | --- | --- |
| Home | ![screenshot](/readme-documentation/screenshots/wave/home.png) | Link errors in the footer for the github icon and the link that appears on the smaller breakpoints. Acceptable. |
| Product Detail | ![screenshot](/readme-documentation/screenshots/wave/product-details.png) | Link errors in the footer for the github icon and the link that appears on the smaller breakpoints. Acceptable. |
| Trolley | ![screenshot](/readme-documentation/screenshots/wave/trolley.png) | Acceptable errors, label not needed as there's a heading above it, table header left blank is intentional and the aria label error is because it's on a model. |
| Checkout | ![screenshot](/readme-documentation/screenshots/wave/checkout.png) | Used placeholders instead of labels and the fieldsets have labels. |
| Checkout Success | ![screenshot](/readme-documentation/screenshots/wave/checkout-success.png) | Link errors in the footer for the github icon and the link that appears on the smaller breakpoints. Acceptable. |
| Add/Edit Product | ![screenshot](/readme-documentation/screenshots/wave/add-product.png) | Link errors in the footer for the github icon and the link that appears on the smaller breakpoints. Acceptable. |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- | --- |
| Products | Feature is expected to allow users to browse products without registration. | Opened product pages as a guest user. | Products were fully accessible without requiring registration. | ![screenshot](/readme-documentation/screenshots/features/products.png) |
| | Feature is expected to sort products by category. | Tested sorting categories. | Sorting worked correctly for all options. | ![screenshot](/readme-documentation/screenshots/defensive/categories.png) ![screenshot of clothing only](/readme-documentation/screenshots/defensive/sorted-by-clothing.png) |
| Product Detail | Feature is expected to show detailed product information. | Clicked on individual products to view details. | Product details (description, price, image) were displayed correctly. | ![screenshot](/readme-documentation/screenshots/responsiveness/tablet/product-detail.png) |
| | User should not be able to add an item that has a size without choosing a size | Tested by attempting to add sized item without selecting a size | Didn't allow me to add to trolley and instead popped up a boxing asking me to choose a size. Success. | ![screenshot of please select size](/readme-documentation/screenshots/defensive/choose-size.png) |
| Trolley | Feature is expected to allow customers to add items to the trolley. | Added products to the cart. | Items were added successfully, with quantities as expected. | ![screenshot](/readme-documentation/screenshots/features/add-notification.png) | 
| | Feature is expected to allow customers to view and manage their trolley. | Opened the cart page and edited trolley contents. | Cart contents were displayed and removed correctly. | ![screenshot of hoodie in trolley](/readme-documentation/screenshots/features/trolley.png) |
| Checkout | Feature is expected to display cart items, grand total, and input fields for checkout. | Proceeded to checkout with items in the cart. | Checkout page displayed cart items, total, and input fields as expected. | ![screenshot](/readme-documentation/screenshots/features/checkout.png) ![screenshot of checkout input](/readme-documentation/screenshots/features/checkout-details.png) |
| | Feature is expected to allow secure payment via Stripe. | Entered valid card details using Stripe at checkout. | Payment was processed securely, and an order confirmation page was displayed. | ![screenshot](/readme-documentation/screenshots/user-stories/notification-of-order-number.png) |
| | Feature is expected to send a confirmation email after purchase. | Completed a purchase and checked email inbox. | Confirmation email was received with order details. | ![screenshot](/readme-documentation/screenshots/defensive/email-received.png) |
| | Feature is expected to display an order confirmation page with an order number. | Completed a purchase. | Order confirmation page displayed successfully with an order number. | ![screenshot](/readme-documentation/screenshots/user-stories/order-confirmation.png) |
| |  User shouldn't be able to buy an item without inputting necessary details | Attempted to purchase something without inputting any details. | Order didn't go through and put my cursor on the field(s) that needed filling | ![screenshot of empty order details](/readme-documentation/screenshots/defensive/pay-without-details.png) |
| Account Management | Feature is expected to allow returning customers to log in and view past orders. | Logged in as a returning customer and accessed order history. | Past orders were displayed correctly in the account section. | ![screenshot](/readme-documentation/screenshots/defensive/past-orders.png) |
| Admin Features | Feature is expected to allow the site owner to create new products. | Created new products with valid data (name, price, description, image, category). | Products were added successfully and displayed on the site. | ![screenshot](/readme-documentation/screenshots/defensive/add-test.png) ![screenshot of notification](/readme-documentation/screenshots/defensive/add-notification.png) ![screenshot of added item](/readme-documentation/screenshots/defensive/add-success.png)  |
| | Feature is expected to allow the site owner to update product details. | Edited product details as an admin user. | Product updates were saved and displayed correctly. | ![screenshot](/readme-documentation/screenshots/defensive/edit-test.png) ![screenshot of edit notification](/readme-documentation/screenshots/defensive/edit-notification.png) ![screenshot of edit success](/readme-documentation/screenshots/defensive/edit-success.png) ![screenshot of edited product](/readme-documentation/screenshots/defensive/edit-product.png) |
| | Feature is expected to allow the site owner to delete products. | Deleted a product from the inventory. | Product was removed successfully from the site, after being prompted to confirm first. | ![screenshot](/readme-documentation/screenshots/defensive/delete-modal.png) ![screenshot of delete success notification](/readme-documentation/screenshots/defensive/delete-success.png) |
| Newsletter | Feature was added as custom model to allow an input and get a response. | Submitted email addresses for newsletter registration. | Response from site was received | ![screenshot](/readme-documentation/screenshots/defensive/newsletter-notification.png) |
| 404 Error Page | Feature is expected to display a 404 error page for non-existent pages. | Navigated to an invalid URL (e.g., `/test`). | A custom 404 error page was displayed as expected. | ![screenshot](/readme-documentation/screenshots/defensive/404.png) |

## User Story Testing

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a guest user | I would like to browse products without needing to register | so that I can shop freely before deciding to create an account. | ![screenshot](/readme-documentation/screenshots/features/products.png) |
| As a guest user | I would like to be prompted to create an account or log in at checkout | so that I can complete my purchase and track my order history. | ![screenshot](/readme-documentation/screenshots/user-stories/create-account-prompt.png) |
| As a user | I would like to sign up to the site's newsletter | so that I can stay up to date with any upcoming sales or promotions. | ![screenshot](/readme-documentation/screenshots/defensive/newsletter-notification.png) |
| As a customer | I would like to browse various product categories | so that I can easily find what I'm looking for. | ![screenshot](/readme-documentation/screenshots/defensive/categories.png) |
| As a customer | I would like to filter products by category | so that I can narrow down the products to the types I am most interested in. | ![screenshot](/readme-documentation/screenshots/defensive/sorted-by-clothing.png) |
| As a customer | I would like to click on individual products to view more details (description, price, image, etc.) | so that I can make an informed decision about my purchase. | ![screenshot](/readme-documentation/screenshots/features/profile-details.png) |
| As a customer | I would like to view and manage my items added to trolley | so that I can review or remove items before proceeding to checkout. | ![screenshot](/readme-documentation/screenshots/features/trolley.png) |
| As a customer | I would like to remove items from my cart | so that I can remove products I no longer wish to buy. | ![screenshot](/readme-documentation/screenshots/user-stories/remove-from-trolley.png) |
| As a customer | I would like to proceed to checkout where I see my cart items, grand total, and input my name, email, shipping address, and card details | so that I can complete my purchase. | ![screenshot](/readme-documentation/screenshots/features/checkout.png) ![screenshot of checkout details](/readme-documentation/screenshots/features/checkout-details.png) |
| As a customer | I would like to receive a confirmation email after my purchase | so that I can have a record of my transaction and order details. | ![screenshot](/readme-documentation/screenshots/defensive/email-received.png) |
| As a customer | I would like to see an order confirmation page with a checkout order number after completing my purchase | so that I know my order has been successfully placed. | ![screenshot](/readme-documentation/screenshots/user-stories/order-confirmation.png) |
| As a customer | I would like to securely enter my card details using Stripe at checkout | so that I can feel confident my payment information is protected. | ![screenshot](/readme-documentation/screenshots/user-stories/card-details-input.png) |
| As a returning customer | I would like to be able to log in and view my past orders | so that I can track my previous purchases and order history. | ![screenshot](/readme-documentation/screenshots/defensive/past-orders.png) |
| As a site owner | I would like to create new products with a name, description, price, images, and category | so that I can add additional items to the store inventory. | ![screenshot](/readme-documentation/screenshots/defensive/add-test.png) ![screenshot](/readme-documentation/screenshots/defensive/add-notification.png) ![screenshot](/readme-documentation/screenshots/defensive/add-success.png) |
| As a site owner | I would like to update product details (name, price, description, image, category) at any time | so that I can keep my product listings accurate and up to date. | ![screenshot](/readme-documentation/screenshots/defensive/edit-test.png) ![screenshot](/readme-documentation/screenshots/defensive/edit-notification.png) ![screenshot](/readme-documentation/screenshots/defensive/edit-success.png) ![screenshot](/readme-documentation/screenshots/defensive/edit-product.png) |
| As a site owner | I would like to delete products that are no longer available or relevant | so that I can maintain a clean and accurate inventory. | ![screenshot](/readme-documentation/screenshots/defensive/delete-modal.png) ![screenshot](/readme-documentation/screenshots/defensive/delete-success.png) |
| As a site owner | I would like to manage product categories | so that I can ensure items are correctly organized and easy for customers to find. | ![screenshot](/readme-documentation/screenshots/user-stories/edit-category.png |
| As a user | I would like to see a 404 error page if I get lost | so that it's obvious that I've stumbled upon a page that doesn't exist. | ![screenshot](/readme-documentation/screenshots/features/404.png) |

## Bugs/Issues

* The X button on my toasts didn't close the toast, despite the data-dismiss being linked to the .toast class in my toasts.
    * The fix for this was simple, Bootstrap 5 attributes use data-bs and the example project was made before Bootstrap 5 so I just had to update the data-dismiss to data-bs-dismiss.

* I have been unable to get any images to display. I'm not sure if it's because I've done something wrong with the MEDIA_URL in settings.
    * I was getting this error message in the console: `ValueError: Field 'id' expected a number but got 'default-image.jpg'.` So I assume it's an issue with my model somewhere.
        * FIXED: The issue was due to the MEDIA_URL not being read correctly. I had scoured the internet but the solutions I found I had already implimented. So I replaced the {{ MEDIA_URL }} bit in my image if statements with the hard code that Django would expect to see as the MEDIA_URL is really only going to be used for the placeholder image.
        Instead of `<img src="{{ MEDIA_URL }}default-image.jpg" alt="{{ product.name }}" class="card-img-top card-img-bottom">`, I'm using `<img src="/media/default-image.jpg" alt="{{ product.name }}" class="card-img-top card-img-bottom">`.

* The checkout page wasn't loading when I was trying to render the template and the context like this `return render(request, context, template)`
    * FIX: I didn't explictly find a solution but noticed when trawling through stackonline posts and other examples that context was always the last argument rendered, so I tried this and it seemed to work.

* Stripe threw this error: ![unknown parameter surname](/readme-documentation/screenshots/bugs-and-issues/checkout/unknown-parameter-surname.png)
    * FIX: I eventually found out that surname is actually just not an accepted parameter for the stripe billing details. I wasn't aware they had to be preset because the walkthrough said nothing about it.
        * Furthermore, other fields needed changing. Nothing about Stripe requiring specific fields was mentioned in the walkthroughs.

* I encountered an error when trying to impliment delete product logic. Which was `"Page not found at /"` after deleting a product. ![error after deleting](/readme-documentation/screenshots/bugs-and-issues/general/after-delete-issue.png)
    * At the moment I cannot do anything on my site, all I get is a 404 saying not found: /. Nothing I have tried has helped so it looks like I'm stuffed.
        * FIX!: Turns out I had deleted a product that still existed in a trolley session, the site was trying to find something that didn't exist. Found here using the django debug toolbar. ![found deleted item in session data](/readme-documentation/screenshots/bugs-and-issues/general/deleted-item-in-trolley.png)

* MAJOR ISSUE: When attempting to set up my AWS bucket to handle static files, I could not for life of me get it to work. When pushing to github and therefore heroku, it was scraping the static files correctly but then saving them in a tmp folder. ![static files in tmp folder](/readme-documentation/screenshots/bugs-and-issues/deployment/heroku-tmp-static-files.png)
    * FIX: I reached out to student support and learned that the Django commands in the video that I had used, `STATICFILES_STORAGE` and `DEFAULT_FILE_STORAGE`, were actually depreciated in the current version of Django. When replaced with the correct django setting under the STORAGES setting in settings.py, my static files populated the bucket successfully.

* I wasn't able to style the allauth forms to the extent I'd like. In particular the log in form, I don't want the "forgot your password" to be in a span next to the password input but as I can't access the form there's nothing I can do about that. 

* When attempting to display item sizes in the user's trolley, I would get an error stating that I was trying to increment a string or something like that: ![+= string error](/readme-documentation/screenshots/bugs-and-issues/trolley/type-error-plus-equals.png)
![+= type error callback](/readme-documentation/screenshots/bugs-and-issues/trolley/type-error-plus-equals-traceback.png)
    * FIX: I had to turn to chatgpt to suggest a fix for my piece of code in trolley/views.py. I had to make sure I was only incrementing the trolley item generally if there was no dictionary in the particular trolley item, which would indicate a size. I don't think I'd have worked out the exact code on my own.

* EMAIL ISSUE: When writing the view for the email, I used a long form link of something like `checkout/template/checkout/confirmation_emails/confirmation_email_subject`. This meant it didn't work. The fix was to change it to `checkout/confirmation_emails/confirmation_email_subject`. I asked chatgpt about how to link to the confirmation emails and it corrected my structure.

### Current Bugs/Issues

* DEVELOPMENT BUG: In the developer server for Django, updating the Css files and then clearing cache doesn't actually update the css for me since I migrated to the PostgreSQL database. Instead I have to run manually `python manage.py collectstatic --noinput` if I wanted to update anything done in a css file in the development server. While this isn't the end of the world and has a workaround, it did probably influence the limited custom css that I used. I tended to use bootstrap classes to do most of the styling.

* DISPLAY BUG: It appears as though there is a very small amount of horizontal scrolling on the site, possibly caused by the header or footer as it's on all pages that those are on. But I hadn't adjusted them in a while and haven't yet found out the cause. It's not site breaking.

* NOTIFICATION BUG: When buying an item with a size for the 2nd time, I got a double notification pop up with the size incrementing code not completely working. I'm not sure what went wrong there but I was out of time to debug this. The site still works. ![screenshot of double notification](/readme-documentation/screenshots/bugs-and-issues/trolley/trolley-notification-duplication-bug.png)