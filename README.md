# CampusConnect — Campus Event Registration Portal

CampusConnect is a front-end web project that lets students explore sample campus events, register for an event, view their registrations, and cancel a registration.

## Features
- Browse sample technical, cultural, sports, and career events
- Register using student name, USN/student ID, email, and year of study
- View remaining seats and registration summaries
- Search events and filter by category, availability, or personal registrations
- Prevent duplicate registrations for the same event and student ID
- Cancel registrations
- Save registrations in browser `localStorage`

## Technologies
- HTML5 for page structure and forms
- CSS3 for styling and responsive layout
- JavaScript for validation, filtering, event capacity, and registration actions
- Browser localStorage for local persistence
- GitHub for source-code hosting
- GitHub Pages (optional) for publishing the demo

## Run the project
1. Download the ZIP or clone the repository.
2. Open `index.html` in a modern browser.
3. Fill in the registration form and select a sample event.
4. Try searching, filtering, registering, and cancelling.
5. Refresh the page to verify that registrations remain saved in that browser.

No server or package installation is required.

## Upload to GitHub
1. Sign in at https://github.com/ and create a public repository named `campusconnect-event-portal`.
2. Open **Add file → Upload files**.
3. Upload `index.html` and `README.md`.
4. Enter a commit message such as `Add CampusConnect event portal`.
5. Click **Commit changes**.

## Optional GitHub Pages deployment
Open repository **Settings → Pages**. Choose **Deploy from a branch**, select `main` and `/(root)`, then save. Wait for GitHub to show the published website URL.

## Suggested report screenshots
1. Event list and summary cards.
2. Successful registration shown under My Registrations.
3. Search or category filter in action.
4. GitHub repository showing `index.html` and `README.md`.

## Limitations
This is a demonstration project. Sample event details are static, registrations are stored only in the current browser, and the form does not send emails or communicate with a college server. Replace sample events and details if your instructor requires institution-specific information.
