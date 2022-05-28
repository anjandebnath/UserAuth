# Requirements
1. There will be two roles: USER & ADMIN. 
2. Create a basic sign-up feature.
   1. Profile image
   2. Name
   3. Date of Birth
   4. Email
   5. Attachment(image/pdf/doc/xls)
   6. Password
   7. Confirm Password
3. Develop an admin panel where you'll record all of these registered user information
4. The ADMIN can modify any of these user info as an admin.
5. Create a basic sign-in page from where the pre-registered USERs can sign in using the login creds (Email & Password).
6. USER can see the details(profile) that s/he submitted on the registration process.

#Solution 
1. As per requirements since 2 roles are the concern so select Django as it supports default ADMIN section.
2. Django has good support on authentication mechanism.

### Run the project 
1. Python 3 and Django is mandatory in the system
2. Create virtual environment in the local system 
3. Make sure migrations command have executed

    `python manage.py makemigrations`
    `python manage.py migrate`
4. Run server locally `python manage.py runserver`
5. Create Superuser for ADMIN access
    `python manage.py createsuperuser`

# Output
## USER ROLE
Screen 1             |  Screen 2           |  Screen 3
:-------------------------:|:-------------------------:|:-------------------------:
![Screen1](https://github.com/anjandebnath/UserAuth/blob/main/user_auth/blog/static/output/User_Profile.PNG)  |  ![Screen2](https://github.com/anjandebnath/UserAuth/blob/main/user_auth/blog/static/output/User_Signin.PNG) |  ![Screen3](https://github.com/anjandebnath/UserAuth/blob/main/user_auth/blog/static/output/User_SignUp.PNG)

## ADMIN ROLE
Screen 1             |  Screen 2 
:-------------------------:|:-------------------------:
![Screen1](https://github.com/anjandebnath/UserAuth/blob/main/user_auth/blog/static/output/admin_1.PNG)  |  ![Screen2](https://github.com/anjandebnath/UserAuth/blob/main/user_auth/blog/static/output/admin_2.PNG)