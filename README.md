# Simple-Upload

This website uploads files to Google Drive. Because the conditions of this assignment is limited to hosting via GitHub pages, this will not have a backend facilitating the uploads working or other data manipluation.

## Indended Purpose

My wife is a Ph.D candidate studying how the judiciary impacts a child's health outcome. Little reasearch has been collected to evaluate how judges rule on an individual per judge basis. What is happening in family court is that judges frequently rule against the protective/safe parent. Transparency within the judiciary would open up the judges for greater public scrutiny and a check & balance within our system of government. The judiciary in most states do not open judicial orders to the public. Instead you have to physically go to the courthouse to get documents.

This project is intended to have unadulterated data available to the public to serve as a public good. Users to the website should be able to evaluate judges against knowns (i.e., research, other judges, other court systems, etc). The intent is that this will serve as a source of societal pressure for judges to make better rulings.

### This will be solved in three steps:

### 1. Submission of custody order & data to Google sheets

This section will allow users to (ultimately) drag & drop custody orders (what the judge is telling the parents to do) into a second on the screen. This will upload the PDF to google drive and fill in pre-populated data.

### 2. Validation of custody order within google sheets

Currently, a trained person will open the pdf and validate the submitted data. This will be populated in the Google Sheets and serve as the source data.

### 3. Presentation of data to website

Using plotly or another web display repo the data will be pulled from Google Sheets and displayed to the user. The user will be able to search for specific judge or compare the judges. For instance, you can see if a judge is ruling based on age or gender.

## Phases of Deployment

### Phase 1: This Assignment

- Accomplish the objectives of the assignment.
- Add features that provide actual functionality or demonstrate matestery of the assignment given the constraints of not having a backend web hosting environment

### Phase 2: Basic Functionality & Hosting

- Build out uploads
- Build out ploting functionality
- Find a web deployment service
- Deploy the service

### Phase 3: Additional Functionality

- Clean up HTML, CSS, JS. Take out what is not relevant. Validate comments.
- Build out upload functionality.
- Build out plotting and data display functionality. This may involve a new page.

### Phase 4: Input of Generative AI

- Google Drive was used because you can quickly access generative AI tools such as LLAMA, Gemeni etc. (LLAMA v3 came out this week WOOT WOOT!)
- When files are uploaded, instead of having a human read over it, a generative AI tool can. A human can simply validate what is correct.

## References & Attribution

### Template - Bootstrap.com

### Sales Image - https://thenounproject.com/icon/scales-of-justice-204999/

### Secure File Upload - https://blog.filestack.com/simple-secure-file-uploads-flask/

This is not complete yet. This is the tutorial I am using.

### Tutorial on Google Forms - https://www.youtube.com/watch?v=HLXDiIDI9YU

### Tutorial on Bootstrap Drag & Drop Upload Zone - https://www.youtube.com/watch?v=HrK7RFNDTKA

Not used but it got me thinking in the right direction.
