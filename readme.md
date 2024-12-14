# BookOps
Cradle to grave publishing tool which currently stops at the marketing step.

## Outline
BookOps is organized along 4 seperate axis. 
- The overarching bookops app which handles user login and registration.
- Slush, aka the Slush Pile, where users can submit manuscripts and editors can accept submissions for editing.
- Manuscript, aka Editing Tools, where editors can markup manuscript text.
- Marketing, the Marketing Suite, where editors can plan how to sell an accepted manuscript.

### BookOps
- Templates and static css/js files are stored here.
- Views and urls are mostly for user registration.
- Defines the User model for the app, which is standard except for an editor flag.

### Slush
- Doesn't currently define any new models.
- Classic GET/POST model for submitting new manuscripts and browsing existing manuscripts.

### Manuscript
- Defines the model for Manuscript
- One page app for selecting manuscripts and editing them

### Marketing
- Defines the model for a Lead, Sale, Buyer generic data point for marketing information.
- Was unable to fully realize this section in the final product.
- Start of a React app, but couldn't get State to function, also not connection to the backend.
- Form page runs a simulation of generating sales and buyers.

#### Requirements
- Using Bootstrap and Bootstrap's Javascript plugins
- We use the Python random library for simulating marketing data
- No other python dependencies

#### Video
Link: https://youtu.be/B66RcDoCQKE

