# Testing

> [!NOTE]
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
| home | [add_product.html](https://github.com/seanbrindley17/milestone-project-4/blob/main/home/templates/home/add_product.html) | Link (if applicable) | ![screenshot](/readme-documentation/screenshots/validation/html/add-product-success.png) | No errors |
| home | [edit_product.html](https://github.com/seanbrindley17/milestone-project-4/blob/main/home/templates/home/edit_product.html) | Link (if applicable) | ![screenshot](/readme-documentation/screenshots/validation/html/edit-product-success.png) | No errors |
| home | [product_display.html](https://github.com/seanbrindley17/milestone-project-4/blob/main/home/templates/home/product_display.html) | Link (if applicable) | ![screenshot](/readme-documentation/screenshots/validation/html/index-errors.png) | Two errors, repeated. The duplicate class error was because on the confirm delete button in the model, there were two class attributes, one blank. This was removed. The other was an aria label error because I hadn't referenced what was being labelled. This was corrected by putting the id in the title and using the jinja templating to generate the correct ID  |
| home | [index.html](https://github.com/seanbrindley17/milestone-project-4/blob/main/home/templates/home/index.html) | [Link](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmilestone-project-4-sb-1448d349aa27.herokuapp.com%2F) | ![screenshot](/readme-documentation/screenshots/validation/html/index-success.png) | No errors |
| home | [product_detail.html](https://github.com/seanbrindley17/milestone-project-4/blob/main/home/templates/home/product_detail.html) | Link (if applicable) | ![screenshot](/readme-documentation/screenshots/validation/html/product_detail-errors.png) | Repeat class attribute, removed extra one. aria-label error, no link to the delete element, fixed by correctly linking. Warning for using type=text/javascript. Didn't know this wasn't necessary as my walkthrough used it. |
| home | [product_detail.html](https://github.com/seanbrindley17/milestone-project-4/blob/main/home/templates/home/product_detail.html) | [Link](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmilestone-project-4-sb-1448d349aa27.herokuapp.com%2F6%2F) | ![screenshot](/readme-documentation/screenshots/validation/html/product_detail-success.png) | No errors. |
| profiles | [profile.html](https://github.com/seanbrindley17/milestone-project-4/blob/main/profiles/templates/profiles/profile.html) | [Link](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmilestone-project-4-sb-1448d349aa27.herokuapp.com%2Fprofile%2F) | ![screenshot of errors](/readme-documentation/screenshots/validation/html/profile-errors.png) | Unsure about this. The errors say there are missing closing tags but looking at the source code I see the open tags here and then corresponding close tags here: ![screenshot of open tags](/readme-documentation/screenshots/validation/html/profile-open-tags.png), ![screenshot of close tags](/readme-documentation/screenshots/validation/html/profile-close-tags.png). I am completely unsure what to do about this. |
| templates | [404.html](https://github.com/seanbrindley17/milestone-project-4/blob/main/templates/404.html) | Link (if applicable) | ![screenshot](/readme-documentation/screenshots/validation/html/404-success.png) | No errors |
| trolley | [trolley.html](https://github.com/seanbrindley17/milestone-project-4/blob/main/trolley/templates/trolley/trolley.html) | [Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmilestone-project-4-sb-1448d349aa27.herokuapp.com%2Ftrolley%2F) | ![screenshot](/readme-documentation/screenshots/validation/html/trolley-success.png) | No errors |


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| profiles | [profiles.css](https://github.com/seanbrindley17/milestone-project-4/blob/main/profiles/static/profiles/css/profiles.css) | Link (if applicable) | ![screenshot](/readme-documentation/screenshots/validation/css/profiles.css-success.png) | No errors |
| static | [base.css](https://github.com/seanbrindley17/milestone-project-4/blob/main/static/css/base.css) | [Link](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fmilestone-project-4-sb-1448d349aa27.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#warnings) | ![screenshot](/readme-documentation/screenshots/validation/css/base.css-success.png) | No errors |


### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| checkout | [stripe_elements.js](https://github.com/seanbrindley17/milestone-project-4/blob/main/checkout/static/checkout/js/stripe_elements.js) | N/A | ![screenshot](/readme-documentation/screenshots/validation/js/checkout-stripe-js-success.png) | No errors |


### Python

⚠️ INSTRUCTIONS ⚠️

The [CI Python Linter](https://pep8ci.herokuapp.com) can be used two different ways.

- Copy/Paste your Python code directly into the linter.
- As an API, using the "raw" URL appended to the linter URL.
    - To find the "raw" URL, navigate to your file directly on the GitHub repo.
    - On that page, GitHub provides a button on the right called "Raw" that you can click.
    - From that new page, copy the full URL, and paste it after the CI Python Linter URL (with a `/` separator).

It's recommended to validate each file using the API URL. This will give you a custom URL which you can use on your testing documentation. It makes it easier to return back to a file for validating it again in the future. Use the steps above to generate your own custom URLs for each Python file.

**IMPORTANT**: `E501 line too long` errors

You must strive to fix all Python lines that are too long (>80 characters). In rare cases where you cannot break the lines [*without breaking the functionality*], adding "`  # noqa`" (*NO Quality Assurance*) to the end of those lines will ignore linting validation. Do not use "`  # noqa`" all over your project just to clear down validation errors! This can still cause a project to fail, for failing to fix actual PEP8 validation errors.

Sometimes variables can get too long, or excessive `if/else` conditional statements. These are acceptable instances to use the "`  # noqa`" comment.

When trying to fix "line too long" errors, try to avoid using `/` to split lines. A better approach would be to use any type of opening bracket, and hit `<Enter>` just after that. Any opening bracket type will work: `(`, `[`, `{`. By using an opening bracket, Python knows where to appropriately indent the next line of code, without having to *guess* for yourself and attempt to "tab" to the correct indentation level.

⚠️ --- END --- ⚠️

🛑 IMPORTANT 🛑

**IMPORTANT**: Django settings

The Django `settings.py` file comes with 4 lines that are quite long, and will throw the `E501 line too long` error. This is default behavior, but can be fixed by adding the "`  # noqa`" comment at the end of those lines.

```python
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa
    },
]
```

**IMPORTANT**: *migration* and *pycache* files

You do not have to validate files from the `migrations/` or `pycache/` folders! Ignore these `.py` files, and validate just the files that you've created or modified.

🛑 --- END --- 🛑

I used autopep8 to force my lines to be 79 maximum as designated by the CI Linter. God knows why you can't just stick with 88 as it was before but let's just hope everything still works.

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files. 

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| checkout | [admin.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/checkout/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/checkout/admin.py) | ![screenshot](/readme-documentation/screenshots/validation/python/checkout/admin.png) | No errors |
| checkout | [forms.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/checkout/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/checkout/forms.py) | ![screenshot](/readme-documentation/screenshots/validation/python/checkout/forms.png) | No errors |
| checkout | [models.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/checkout/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/checkout/models.py) | ![screenshot](/readme-documentation/screenshots/validation/python/checkout/models.png) | Had to use `#noqa`, as some of the lines were too long for the CI Linter, yet when I tried shortening them at brackets and saving, the automatic linter would put them back where they were originally. Using `#noqa` made the auto linter put brackets around some of the problem lines. |
| checkout | [signals.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/checkout/signals.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/checkout/signals.py) | ![screenshot](/readme-documentation/screenshots/validation/python/checkout/signals.png) | No erros |
| checkout | [urls.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/checkout/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/checkout/urls.py) | ![screenshot](/readme-documentation/screenshots/validation/python/checkout/urls.py.png) | No errors |
| checkout | [views.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/checkout/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/checkout/views.py) | ![screenshot](/readme-documentation/screenshots/validation/python/checkout/views.py.png) | Had to #noqa a couple of lines |
| checkout | [webhook_handler.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/checkout/webhook_handler.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/checkout/webhook_handler.py) | ![screenshot](/readme-documentation/screenshots/validation/python/checkout/webhook_handlers.py.png) | Notes (if applicable) |
| checkout | [webhooks.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/checkout/webhooks.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/checkout/webhooks.py) | ![screenshot](/readme-documentation/screenshots/validation/python/checkout/webhooks.py.png) | Notes (if applicable) |
|  | [custom_storages.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/custom_storages.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/custom_storages.py) | ![screenshot](/readme-documentation/screenshots/validation/python/root-level/custom-storages.py.png) | Notes (if applicable) |
| home | [admin.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/home/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/home/admin.py) | ![screenshot](/readme-documentation/screenshots/validation/python/home/admin.py.png) | Notes (if applicable) |
| home | [forms.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/home/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/home/forms.py) | ![screenshot](/readme-documentation/screenshots/validation/python/home/forms.py.png) | Notes (if applicable) |
| home | [models.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/home/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/home/models.py) | ![screenshot](/readme-documentation/screenshots/validation/python/home/models.py.png) | Notes (if applicable) |
| home | [urls.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/home/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/home/urls.py) | ![screenshot](documentation/validation/py-home-urls.png) | Notes (if applicable) |
| home | [views.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/home/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/home/views.py) | ![screenshot](/readme-documentation/screenshots/validation/python/home/views.py.png) | Notes (if applicable) |
|  | [manage.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/manage.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/manage.py) | ![screenshot](/readme-documentation/screenshots/validation/python/root-level/manage.py.png) | Notes (if applicable) |
| profiles | [forms.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/profiles/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/profiles/forms.py) | ![screenshot](/readme-documentation/screenshots/validation/python/profiles/forms.py.png) | Notes (if applicable) |
| profiles | [models.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/profiles/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/profiles/models.py) | ![screenshot](/readme-documentation/screenshots/validation/python/profiles/models.py.png) | Notes (if applicable) |
| profiles | [urls.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/profiles/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/profiles/urls.py) | ![screenshot](/readme-documentation/screenshots/validation/python/profiles/urls.py.png) | Notes (if applicable) |
| profiles | [views.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/profiles/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/profiles/views.py) | ![screenshot](/readme-documentation/screenshots/validation/python/profiles/views.py.png) | Notes (if applicable) |
| trolley | [admin.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/trolley/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/trolley/admin.py) | ![screenshot](documentation/validation/py-trolley-admin.png) | Notes (if applicable) |
| trolley | [contexts.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/trolley/contexts.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/trolley/contexts.py) | ![screenshot](documentation/validation/py-trolley-contexts.png) | Notes (if applicable) |
| trolley | [models.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/trolley/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/trolley/models.py) | ![screenshot](documentation/validation/py-trolley-models.png) | Notes (if applicable) |
| trolley | [tests.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/trolley/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/trolley/tests.py) | ![screenshot](documentation/validation/py-trolley-tests.png) | Notes (if applicable) |
| trolley | [urls.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/trolley/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/trolley/urls.py) | ![screenshot](documentation/validation/py-trolley-urls.png) | Notes (if applicable) |
| trolley | [views.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/trolley/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/trolley/views.py) | ![screenshot](documentation/validation/py-trolley-views.png) | Notes (if applicable) |
| wnsc_shop | [settings.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/wnsc_shop/settings.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/wnsc_shop/settings.py) | ![screenshot](documentation/validation/py-wnsc_shop-settings.png) | Notes (if applicable) |
| wnsc_shop | [urls.py](https://github.com/seanbrindley17/milestone-project-4/blob/main/wnsc_shop/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/seanbrindley17/milestone-project-4/main/wnsc_shop/urls.py) | ![screenshot](documentation/validation/py-wnsc_shop-urls.png) | Notes (if applicable) |


## Responsiveness

⚠️ INSTRUCTIONS ⚠️

Use this space to discuss testing the live/deployed site on various device sizes.

The minimum requirement is to test the following 3 sizes:

- Mobile
- Tablet
- Desktop

**IMPORTANT**: You must provide screenshots of your results, to "prove" that you've actually tested them.

Using the [amiresponsive](http://ami.responsivedesign.is) mockup images (*or similar*) does not meet the requirements. Consider using some of the built-in device sizes from the Developer Tools.

If you have tested the project on your actual mobile phone or tablet, consider also including screenshots of these as well. It showcases a higher level of manual tests, and can be seen as a positive inclusion!

⚠️ --- END --- ⚠️

I've tested my deployed project to check for responsiveness issues.

| Page | Mobile | Tablet | Desktop | Notes |
| --- | --- | --- | --- | --- |
| Register | ![screenshot](documentation/responsiveness/mobile-register.png) | ![screenshot](documentation/responsiveness/tablet-register.png) | ![screenshot](documentation/responsiveness/desktop-register.png) | Works as expected |
| Login | ![screenshot](documentation/responsiveness/mobile-login.png) | ![screenshot](documentation/responsiveness/tablet-login.png) | ![screenshot](documentation/responsiveness/desktop-login.png) | Works as expected |
| Profile | ![screenshot](documentation/responsiveness/mobile-profile.png) | ![screenshot](documentation/responsiveness/tablet-profile.png) | ![screenshot](documentation/responsiveness/desktop-profile.png) | Works as expected |
| Home | ![screenshot](documentation/responsiveness/mobile-home.png) | ![screenshot](documentation/responsiveness/tablet-home.png) | ![screenshot](documentation/responsiveness/desktop-home.png) | Works as expected |
| Products | ![screenshot](documentation/responsiveness/mobile-products.png) | ![screenshot](documentation/responsiveness/tablet-products.png) | ![screenshot](documentation/responsiveness/desktop-products.png) | Works as expected |
| Product Details | ![screenshot](documentation/responsiveness/mobile-product-details.png) | ![screenshot](documentation/responsiveness/tablet-product-details.png) | ![screenshot](documentation/responsiveness/desktop-product-details.png) | Works as expected |
| Bag | ![screenshot](documentation/responsiveness/mobile-bag.png) | ![screenshot](documentation/responsiveness/tablet-bag.png) | ![screenshot](documentation/responsiveness/desktop-bag.png) | Works as expected |
| Checkout | ![screenshot](documentation/responsiveness/mobile-checkout.png) | ![screenshot](documentation/responsiveness/tablet-checkout.png) | ![screenshot](documentation/responsiveness/desktop-checkout.png) | Works as expected |
| Checkout Success | ![screenshot](documentation/responsiveness/mobile-checkout-success.png) | ![screenshot](documentation/responsiveness/tablet-checkout-success.png) | ![screenshot](documentation/responsiveness/desktop-checkout-success.png) | Works as expected |
| Add Product | ![screenshot](documentation/responsiveness/mobile-add-product.png) | ![screenshot](documentation/responsiveness/tablet-add-product.png) | ![screenshot](documentation/responsiveness/desktop-add-product.png) | Works as expected |
| Edit Product | ![screenshot](documentation/responsiveness/mobile-edit-product.png) | ![screenshot](documentation/responsiveness/tablet-edit-product.png) | ![screenshot](documentation/responsiveness/desktop-edit-product.png) | Works as expected |
| Newsletter | ![screenshot](documentation/responsiveness/mobile-newsletter.png) | ![screenshot](documentation/responsiveness/tablet-newsletter.png) | ![screenshot](documentation/responsiveness/desktop-newsletter.png) | Works as expected |
| Contact | ![screenshot](documentation/responsiveness/mobile-contact.png) | ![screenshot](documentation/responsiveness/tablet-contact.png) | ![screenshot](documentation/responsiveness/desktop-contact.png) | Works as expected |
| 404 | ![screenshot](documentation/responsiveness/mobile-404.png) | ![screenshot](documentation/responsiveness/tablet-404.png) | ![screenshot](documentation/responsiveness/desktop-404.png) | Works as expected |

## Browser Compatibility

⚠️ INSTRUCTIONS ⚠️

Use this space to discuss testing the live/deployed site on various browsers. Consider testing at least 3 different browsers, if available on your system. You DO NOT need to use all of the browsers below, just pick any 3 (minimum).

Recommended browsers to consider:
- [Chrome](https://www.google.com/chrome)
- [Firefox (Developer Edition)](https://www.mozilla.org/firefox/developer)
- [Edge](https://www.microsoft.com/edge)
- [Safari](https://support.apple.com/downloads/safari)
- [Brave](https://brave.com/download)
- [Opera](https://www.opera.com/download)

**IMPORTANT**: You must provide screenshots of the browsers you've tested, to "prove" that you've actually tested them.

Please note, there are services out there that can test multiple browser compatibilities at the same time. Some of these are paid services, but some are free. If you use these, you must provide a link to the source used for attribution, and multiple screenshots of the results.

⚠️ --- END --- ⚠️

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Page | Chrome | Firefox | Safari | Notes |
| --- | --- | --- | --- | --- |
| Register | ![screenshot](documentation/browsers/chrome-register.png) | ![screenshot](documentation/browsers/firefox-register.png) | ![screenshot](documentation/browsers/safari-register.png) | Works as expected |
| Login | ![screenshot](documentation/browsers/chrome-login.png) | ![screenshot](documentation/browsers/firefox-login.png) | ![screenshot](documentation/browsers/safari-login.png) | Works as expected |
| Profile | ![screenshot](documentation/browsers/chrome-profile.png) | ![screenshot](documentation/browsers/firefox-profile.png) | ![screenshot](documentation/browsers/safari-profile.png) | Works as expected |
| Home | ![screenshot](documentation/browsers/chrome-home.png) | ![screenshot](documentation/browsers/firefox-home.png) | ![screenshot](documentation/browsers/safari-home.png) | Works as expected |
| Products | ![screenshot](documentation/browsers/chrome-products.png) | ![screenshot](documentation/browsers/firefox-products.png) | ![screenshot](documentation/browsers/safari-products.png) | Works as expected |
| Product Details | ![screenshot](documentation/browsers/chrome-product-details.png) | ![screenshot](documentation/browsers/firefox-product-details.png) | ![screenshot](documentation/browsers/safari-product-details.png) | Works as expected |
| Bag | ![screenshot](documentation/browsers/chrome-bag.png) | ![screenshot](documentation/browsers/firefox-bag.png) | ![screenshot](documentation/browsers/safari-bag.png) | Works as expected |
| Checkout | ![screenshot](documentation/browsers/chrome-checkout.png) | ![screenshot](documentation/browsers/firefox-checkout.png) | ![screenshot](documentation/browsers/safari-checkout.png) | Works as expected |
| Checkout Success | ![screenshot](documentation/browsers/chrome-checkout-success.png) | ![screenshot](documentation/browsers/firefox-checkout-success.png) | ![screenshot](documentation/browsers/safari-checkout-success.png) | Works as expected |
| Add Product | ![screenshot](documentation/browsers/chrome-add-product.png) | ![screenshot](documentation/browsers/firefox-add-product.png) | ![screenshot](documentation/browsers/safari-add-product.png) | Works as expected |
| Edit Product | ![screenshot](documentation/browsers/chrome-edit-product.png) | ![screenshot](documentation/browsers/firefox-edit-product.png) | ![screenshot](documentation/browsers/safari-edit-product.png) | Works as expected |
| Newsletter | ![screenshot](documentation/browsers/chrome-newsletter.png) | ![screenshot](documentation/browsers/firefox-newsletter.png) | ![screenshot](documentation/browsers/safari-newsletter.png) | Works as expected |
| Contact | ![screenshot](documentation/browsers/chrome-contact.png) | ![screenshot](documentation/browsers/firefox-contact.png) | ![screenshot](documentation/browsers/safari-contact.png) | Works as expected |
| 404 | ![screenshot](documentation/browsers/chrome-404.png) | ![screenshot](documentation/browsers/firefox-404.png) | ![screenshot](documentation/browsers/safari-404.png) | Works as expected |

## Lighthouse Audit

⚠️ INSTRUCTIONS ⚠️

Use this space to discuss testing the live/deployed site's Lighthouse Audit reports. Avoid testing the local version (Gitpod/VSCode/etc.), as this can have knock-on effects for performance. If you don't have "Lighthouse" in your Developer Tools, it can be added as an [extension](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk).

Unless your project is a single-page application (SPA), you should test Lighthouse Audit results for all of your pages, for both *mobile* and *desktop*.

**IMPORTANT**: You must provide screenshots of the results, to "prove" that you've actually tested them.

⚠️ --- END --- ⚠️

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. Some warnings are outside of my control, and mobile results tend to be lower than desktop.

| Page | Mobile | Desktop |
| --- | --- | --- |
| Register | ![screenshot](documentation/lighthouse/mobile-register.png) | ![screenshot](documentation/lighthouse/desktop-register.png) |
| Login | ![screenshot](documentation/lighthouse/mobile-login.png) | ![screenshot](documentation/lighthouse/desktop-login.png) |
| Profile | ![screenshot](documentation/lighthouse/mobile-profile.png) | ![screenshot](documentation/lighthouse/desktop-profile.png) |
| Home | ![screenshot](documentation/lighthouse/mobile-home.png) | ![screenshot](documentation/lighthouse/desktop-home.png) |
| Products | ![screenshot](documentation/lighthouse/mobile-products.png) | ![screenshot](documentation/lighthouse/desktop-products.png) |
| Product Details | ![screenshot](documentation/lighthouse/mobile-product-details.png) | ![screenshot](documentation/lighthouse/desktop-product-details.png) |
| Bag | ![screenshot](documentation/lighthouse/mobile-bag.png) | ![screenshot](documentation/lighthouse/desktop-bag.png) |
| Checkout | ![screenshot](documentation/lighthouse/mobile-checkout.png) | ![screenshot](documentation/lighthouse/desktop-checkout.png) |
| Checkout Success | ![screenshot](documentation/lighthouse/mobile-checkout-success.png) | ![screenshot](documentation/lighthouse/desktop-checkout-success.png) |
| Add Product | ![screenshot](documentation/lighthouse/mobile-add-product.png) | ![screenshot](documentation/lighthouse/desktop-add-product.png) |
| Edit Product | ![screenshot](documentation/lighthouse/mobile-edit-product.png) | ![screenshot](documentation/lighthouse/desktop-edit-product.png) |
| Newsletter | ![screenshot](documentation/lighthouse/mobile-newsletter.png) | ![screenshot](documentation/lighthouse/desktop-newsletter.png) |
| Contact | ![screenshot](documentation/lighthouse/mobile-contact.png) | ![screenshot](documentation/lighthouse/desktop-contact.png) |
| 404 | ![screenshot](documentation/lighthouse/mobile-404.png) | ![screenshot](documentation/lighthouse/desktop-404.png) |

## Defensive Programming

⚠️ INSTRUCTIONS ⚠️

Defensive programming (defensive design) is extremely important! When building projects that accept user inputs or forms, you should always test the level of security for each form field. Examples of this could include (but not limited to):

All Projects:

- Users cannot submit an empty form (add the `required` attribute)
- Users must enter valid field types (ensure the correct input `type=""` is used)
- Users cannot brute-force a URL to navigate to a restricted pages

Python Projects:

- Users cannot perform CRUD functionality if not authenticated (if login functionality exists)
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication
- Standard users should not be able to access pages intended for superusers/admins

You'll want to test all functionality on your application, whether it's a standard form, or CRUD functionality, for data manipulation on a database. Try to access various pages on your site as different user types (User-A, User-B, guest user, admin, superuser). You should include any manual tests performed, and the expected results/outcome.

Testing should be replicable (can someone else replicate the same outcome?). Ideally, tests cases should focus on each individual section of every page on the website. Each test case should be specific, objective, and step-wise replicable.

Instead of adding a general overview saying that everything works fine, consider documenting tests on each element of the page (eg. button clicks, input box validation, navigation links, etc.) by testing them in their "happy flow", their "bad/exception flow", mentioning the expected and observed results, and drawing a parallel between them where applicable.

Consider using the following format for manual test cases:

- Expected Outcome / Test Performed / Result Received / Fixes Implemented

- **Expected**: "Feature is expected to do X when the user does Y."
- **Testing**: "Tested the feature by doing Y."
- (either) **Result**: "The feature behaved as expected, and it did Y."
- (or) **Result**: "The feature did not respond to A, B, or C."
- **Fix**: "I did Z to the code because something was missing."

Use the table below as a basic start, and expand on it using the logic above.

⚠️ --- END --- ⚠️

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- | --- |
| Products | Feature is expected to allow users to browse products without registration. | Opened product pages as a guest user. | Products were fully accessible without requiring registration. | ![screenshot](documentation/defensive/products.png) |
| | Feature is expected to sort products by price and name. | Tested sorting options for price (low-to-high/high-to-low) and name (alphabetical). | Sorting worked correctly for all options. | ![screenshot](documentation/defensive/sorting.png) |
| | Feature is expected to filter products by category. | Applied category filters while browsing products. | Filters worked as expected, displaying only relevant products. | ![screenshot](documentation/defensive/filtering.png) |
| | Feature is expected to show detailed product information. | Clicked on individual products to view details. | Product details (description, price, image) were displayed correctly. | ![screenshot](documentation/defensive/product-details.png) |
| Shopping Cart | Feature is expected to allow customers to add items to the cart with quantity controls. | Added products to the cart and adjusted quantities. | Items were added successfully, and quantities updated as expected. | ![screenshot](documentation/defensive/add-to-cart.png) |
| | Feature is expected to allow customers to view and manage their cart. | Opened the cart page and edited cart contents. | Cart contents were displayed, updated, and removed correctly. | ![screenshot](documentation/defensive/manage-cart.png) |
| Checkout | Feature is expected to display cart items, grand total, and input fields for checkout. | Proceeded to checkout with items in the cart. | Checkout page displayed cart items, total, and input fields as expected. | ![screenshot](documentation/defensive/checkout.png) |
| | Feature is expected to allow secure payment via Stripe. | Entered valid card details using Stripe at checkout. | Payment was processed securely, and an order confirmation page was displayed. | ![screenshot](documentation/defensive/stripe-payment.png) |
| | Feature is expected to send a confirmation email after purchase. | Completed a purchase and checked email inbox. | Confirmation email was received with order details. | ![screenshot](documentation/defensive/confirmation-email.png) |
| | Feature is expected to display an order confirmation page with an order number. | Completed a purchase. | Order confirmation page displayed successfully with an order number. | ![screenshot](documentation/defensive/order-confirmation.png) |
| Account Management | Feature is expected to allow returning customers to log in and view past orders. | Logged in as a returning customer and accessed order history. | Past orders were displayed correctly in the account section. | ![screenshot](documentation/defensive/order-history.png) |
| | Feature is expected to remember the shipping address for returning customers. | Completed multiple checkouts as a returning customer. | Shipping address was pre-filled on subsequent purchases. | ![screenshot](documentation/defensive/saved-address.png) |
| Admin Features | Feature is expected to allow the site owner to create new products. | Created new products with valid data (name, price, description, image, category). | Products were added successfully and displayed on the site. | ![screenshot](documentation/defensive/create-product.png) |
| | Feature is expected to allow the site owner to update product details. | Edited product details as an admin user. | Product updates were saved and displayed correctly. | ![screenshot](documentation/defensive/update-product.png) |
| | Feature is expected to allow the site owner to delete products. | Deleted a product from the inventory. | Product was removed successfully from the site, after being prompted to confirm first. | ![screenshot](documentation/defensive/delete-product.png) |
| Orders | Feature is expected to allow the site owner to view all orders placed. | Accessed the orders dashboard as an admin user. | All orders were displayed correctly. | ![screenshot](documentation/defensive/view-orders.png) |
| Newsletter | Feature is expected to allow users to sign up for the newsletter. | Submitted valid email addresses for newsletter registration. | Email addresses were successfully added to the newsletter list. | ![screenshot](documentation/defensive/newsletter.png) |
| 404 Error Page | Feature is expected to display a 404 error page for non-existent pages. | Navigated to an invalid URL (e.g., `/test`). | A custom 404 error page was displayed as expected. | ![screenshot](documentation/defensive/404.png) |

## User Story Testing

⚠️ INSTRUCTIONS ⚠️

Testing User Stories is actually quite simple, once you've already got the stories defined on your README.

Most of your project's **Features** should already align with the **User Stories**, so this should be as simple as creating a table with the User Story, matching with the re-used screenshot from the respective Feature.

⚠️ --- END --- ⚠️

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a guest user | I would like to browse products without needing to register | so that I can shop freely before deciding to create an account. | ![screenshot](documentation/features/feature01.png) |
| As a guest user | I would like to be prompted to create an account or log in at checkout | so that I can complete my purchase and track my order history. | ![screenshot](documentation/features/feature02.png) |
| As a user | I would like to sign up to the site's newsletter | so that I can stay up to date with any upcoming sales or promotions. | ![screenshot](documentation/features/feature03.png) |
| As a customer | I would like to browse various product categories (clothing, toys, jewelry, kitchen gadgets, etc.) | so that I can easily find what I'm looking for. | ![screenshot](documentation/features/feature04.png) |
| As a customer | I would like to sort products by price (low-to-high/high-to-low) and name (alphabetical) | so that I can quickly organize items in a way that suits my shopping style. | ![screenshot](documentation/features/feature05.png) |
| As a customer | I would like to filter products by category | so that I can narrow down the products to the types I am most interested in. | ![screenshot](documentation/features/feature06.png) |
| As a customer | I would like to click on individual products to view more details (description, price, image, etc.) | so that I can make an informed decision about my purchase. | ![screenshot](documentation/features/feature07.png) |
| As a customer | I would like to add items to my shopping cart using quantity increment/decrement buttons | so that I can adjust how many units of a product I want before checkout. | ![screenshot](documentation/features/feature08.png) |
| As a customer | I would like to view and manage my shopping cart | so that I can review, add, or remove items before proceeding to checkout. | ![screenshot](documentation/features/feature09.png) |
| As a customer | I would like to adjust the quantity of items in my cart | so that I can modify my purchase preferences without leaving the cart. | ![screenshot](documentation/features/feature10.png) |
| As a customer | I would like to remove items from my cart | so that I can remove products I no longer wish to buy. | ![screenshot](documentation/features/feature11.png) |
| As a customer | I would like to proceed to checkout where I see my cart items, grand total, and input my name, email, shipping address, and card details | so that I can complete my purchase. | ![screenshot](documentation/features/feature12.png) |
| As a customer | I would like to receive a confirmation email after my purchase | so that I can have a record of my transaction and order details. | ![screenshot](documentation/features/feature13.png) |
| As a customer | I would like to see an order confirmation page with a checkout order number after completing my purchase | so that I know my order has been successfully placed. | ![screenshot](documentation/features/feature14.png) |
| As a customer | I would like to securely enter my card details using Stripe at checkout | so that I can feel confident my payment information is protected. | ![screenshot](documentation/features/feature15.png) |
| As a returning customer | I would like to be able to log in and view my past orders | so that I can track my previous purchases and order history. | ![screenshot](documentation/features/feature16.png) |
| As a returning customer | I would like the checkout process to remember my shipping address | so that future purchases are quicker and easier. | ![screenshot](documentation/features/feature17.png) |
| As a site owner | I would like to create new products with a name, description, price, images, and category | so that I can add additional items to the store inventory. | ![screenshot](documentation/features/feature18.png) |
| As a site owner | I would like to update product details (name, price, description, image, category) at any time | so that I can keep my product listings accurate and up to date. | ![screenshot](documentation/features/feature19.png) |
| As a site owner | I would like to delete products that are no longer available or relevant | so that I can maintain a clean and accurate inventory. | ![screenshot](documentation/features/feature20.png) |
| As a site owner | I would like to view all orders placed on the website | so that I can track and manage customer purchases. | ![screenshot](documentation/features/feature21.png) |
| As a site owner | I would like to manage product categories | so that I can ensure items are correctly organized and easy for customers to find. | ![screenshot](documentation/features/feature22.png) |
| As a user | I would like to see a 404 error page if I get lost | so that it's obvious that I've stumbled upon a page that doesn't exist. | ![screenshot](documentation/features/feature23.png) |

## Bugs/Issues

* The X button on my toasts doesn't close the toast, despite the data-dismiss being linked to the .toast class in my toasts.
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