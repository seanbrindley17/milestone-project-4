# Testing

Return to [README](README.md)

## Code Validation

### HTML

| File | Screenshot | Notes |
| :---: | :---: | :---: |

### CSS

| File | Screenshot | Notes |
| :---: | :---: | :---: |

### Javascript

| File | Screenshot | Notes |
| :---: | :---: | :---: |

### Python

| File | Screenshot | Notes |
| :---: | :---: | :---: |

## Browser Compatibility

## Responsiveness

## Accessibility

| Page | Summary | Details | Contrast | Notes |
| :---: | :---: | :---: | :---: | :---: |

## Lighthouse Audit

### Desktop

| Page | Screenshot | Notes |
| :---: | :---: | :---: |

### Mobile

| Page | Screenshot | Notes |
| :---: | :---: | :---: |

## User Story Testing

| User Story | Screenshot |
| :---: | :---: |

## Defensive Programming

| Page | Expectation | Test | Result | Fix | Screenshot |
| :---: | :---: | :---: | :---: | :---: | :---: |

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