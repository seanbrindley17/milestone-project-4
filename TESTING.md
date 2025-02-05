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