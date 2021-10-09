# Use Case Model

*This use case model was defined to realize all features of Job Offer Comparison Application.*

**Author**: \<Team 161\>

## 1 Use Case Diagram

![](/Images/UseCaseDiagram.png)

## 2 Use Case Descriptions

### Use Case #1 Enter or Edit Current Job Details:

#### Requirements

    This use case must allow user to enter or edit all of the details of their current job, including: 
    * Title
    * Company
    * Location (entered as city and state)
    * Cost of living in the location 
    * Yearly salary
    * Yearly bonus
    * Allowed weekly telework days 
    * Leave time 
    * Gym membership allowance

### Pre-conditions

* The user must open the application and select `Enter Current Job Details` in the main menu
* Input in `Allowed weekly telework days` must be integer and be includsively between 0 and 5
* Input in `Gym membership allowance` must be in range of $0 - $500 annually

### Post-conditions

* Changes on details of current job are saved

### Scenarios

#### Normal: User Save Current Job Details

* The user opens Job Offer Comparision application and is presented with the main menu 
* The user select `Enter Current Job Details` in the main menu
* The user input or edit details of current job
* The user save job details
* The user return to the main menu

#### Alternate: User Cancel and Exit Without Saving

* The user opens Job Offer Comparision application and is presented with the main menu 
* The user select `Enter Current Job Details` in the main menu
* The user input or edit details of current job
* The user cancel and exit without saving
* The user return to the main menu

### Use Case #2 Enter Job Offers:

#### Requirements

* This use case must allow user to enter all of the details of the job offer. Details are the same listed above for the current job. 

### Pre-conditions

* The user must open the application and select `Enter Job Offer Details` in the main menu
* Input in `Allowed weekly telework days` must be integer and be includsively between 0 and 5
* Input in `Gym membership allowance` must be in range of $0 - $500 annually

### Post-conditions

* The changes on details of job offers are saved

### Scenarios

#### Normal: Enter Job Offer and Return to Main Menu

* The user opens Job Offer Comparision application and is presented with the main menu 
* The user select `Enter Job Offer Details` in the main menu
* The user input details of job offer
* The user save or cancel job details
* The user return to the main menu

#### Alternate: Enter Another Offer

* The user opens Job Offer Comparision application and is presented with the main menu 
* The user select `Enter Job Offer Details` in the main menu
* The user input details of job offer
* The user save or cancel job details
* The user enter another offer

#### Alternate: Compare the Offer with the Current Job Details 

* The user opens Job Offer Comparision application and is presented with the main menu 
* The user select `Enter Job Offer Details` in the main menu
* The user input details of job offer
* The user save job details
* The user compare the offer with the current job details (if present)

### Use Case #3 Compare Job Offers:

#### Requirements

    This use case must allow user to asign integer weights to:
    * Yearly salary
    * Yearly bonus
    * Allowed weekly telework days
    * Leave time
    * Gym membership allowance


### Pre-conditions

* The user must open the application and select `Adjust Comparison Settings` in the main menu
* All weights are set at 1 as default 
* All inputs should be integer
* Either leave empty for all factors, or have input value for all factors

### Post-conditions

* The current settings are stored and used on the next round of comparison 

### Scenarios

#### Normal: User Adjust the Comparison Settings

* The user opens Job Offer Comparision application and is presented with the main menu 
* The user select `Adjust Comparison Settings` in the main menu
* The user input weight for each factor
* The user save details
* The user return to the main menu

#### Alternate: No Weights Are Assigned (Defaults Used)

* The user opens Job Offer Comparision application and is presented with the main menu 
* The user select `Adjust Comparison Settings` in the main menu
* The user leave all inputs empty
* All weights set to 1
* The user return to the main menu

### Use Case #4 Adjust Comparison Settings:

#### Requirements

* This use case must allow user to select two jobs to compare

### Pre-conditions

* The user must open the application and select `Compare Job Offers` in the main menu
* Title and Company of all job offers are displayed to user, ranked from best to worst, and including the current job (if present)

### Post-conditions

* A table comparing the two jobs is displayed to user, including:
1. Title
2. Company
3. Location 
4. Yearly salary adjusted for cost of living
5. Yearly bonus adjusted for cost of living
6. Allowed weekly telework days
7. Leave time
8. Gym Membership Allowance

### Scenarios

#### Normal: Compare Two Offers and Return to Main Menu

* The user opens Job Offer Comparision application and is presented with the main menu 
* The user select `Compare Job Offers` in the main menu
* The user select two jobs from given job offer table to compare 
* Comparison result is shown to user as a table 
* The user return to the main menu

#### Alternate: Perform Another Comparison 

* The user opens Job Offer Comparision application and is presented with the main menu 
* The user select `Compare Job Offers` in the main menu
* The user select two jobs from given job offer table to compare 
* Comparison result is shown to user as a table 
* The user choose to perform another comparison 

